"""
make_testset — generate a corpus-grounded test set from the indexed recipes.

A test set is only meaningful if its gold ids point at recipes that are actually in the
index. So instead of hand-writing questions, we sample real indexed recipes and ask the
local LLM to write, for each one, a specific question that recipe answers plus a concise
reference answer grounded in it. The recipe's own id becomes the gold id — which is what
makes the deterministic retrieval metrics (hit@k etc.) work.

This produces *candidates*. The intended workflow is to then CURATE by hand — delete vague
or wrong questions, fix wording, and (for near-duplicate recipes) add sibling ids to
gold_ids — and commit the frozen result. Start small and grow.

Run (needs LM Studio + a built index):
    python -m eval.make_testset --num 15 --out eval/testset.json
"""

from __future__ import annotations

import argparse
import json
import random

from openai import OpenAI

from src import config, retrieve
from eval.judge import _extract_json, JudgeParseError  # reuse robust JSON parsing

_SYSTEM = (
    "You write evaluation data for a recipe question-answering system. "
    "Respond with ONLY valid JSON — no prose, no markdown, no code fences."
)


def _prompt(recipe: dict) -> str:
    ingredients = "; ".join(recipe["ingredients"])
    directions = " ".join(recipe["directions"])
    return (
        "Given the RECIPE below, write ONE specific cooking question that a home cook "
        "might ask and that THIS recipe answers well, plus a concise reference answer "
        "grounded only in the recipe. The question should be specific to this dish (not "
        "generic) and answerable from the recipe.\n\n"
        f"RECIPE TITLE: {recipe['title']}\n"
        f"INGREDIENTS: {ingredients}\n"
        f"DIRECTIONS: {directions}\n\n"
        'Return JSON: {"question": "<question>", "reference_answer": "<answer>"}'
    )


def generate(num: int, seed: int) -> list[dict]:
    """Sample `num` indexed recipes and turn each into a test item."""
    _, recipes = retrieve._load_index()  # the indexed corpus (id-aligned metadata)
    if num > len(recipes):
        num = len(recipes)
    sampled = random.Random(seed).sample(recipes, num)

    client = OpenAI(base_url=config.OPENAI_BASE_URL, api_key=config.OPENAI_API_KEY)
    items: list[dict] = []
    for recipe in sampled:
        response = client.chat.completions.create(
            model=config.CHAT_MODEL,
            messages=[
                {"role": "system", "content": _SYSTEM},
                {"role": "user", "content": _prompt(recipe)},
            ],
            temperature=0.3,
            max_tokens=400,
        )
        try:
            parsed = _extract_json(response.choices[0].message.content or "")
            question = parsed["question"].strip()
            reference_answer = parsed["reference_answer"].strip()
        except (JudgeParseError, KeyError, AttributeError, TypeError):
            print(f"  skipped recipe {recipe['id']} ({recipe['title']!r}): bad JSON")
            continue

        items.append(
            {
                "id": f"q{len(items) + 1:03d}",
                "question": question,
                "reference_answer": reference_answer,
                "gold_ids": [recipe["id"]],
                "source_recipe_id": recipe["id"],
            }
        )
        print(f"  [{len(items)}] id={recipe['id']:<3} {recipe['title']}")
    return items


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a corpus-grounded eval test set.")
    parser.add_argument("--num", type=int, default=15, help="how many questions to generate")
    parser.add_argument("--seed", type=int, default=42, help="sampling seed (reproducible)")
    parser.add_argument("--out", default=str(config.TESTSET_PATH), help="output JSON path")
    args = parser.parse_args()

    print(f"Generating {args.num} questions from the indexed corpus "
          f"(model={config.CHAT_MODEL}) ...")
    items = generate(args.num, args.seed)

    payload = {
        "description": (
            "Auto-generated, corpus-grounded test set (eval/make_testset.py). Each gold id "
            "points at an indexed recipe. REVIEW AND CURATE before trusting the numbers: "
            "delete vague/wrong items, fix wording, add sibling ids to gold_ids for "
            "near-duplicate recipes."
        ),
        "items": items,
    }
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"\nWrote {len(items)} questions to {args.out}")


if __name__ == "__main__":
    main()
