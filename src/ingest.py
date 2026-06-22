"""
Ingest — build the index. Run this ONCE (re-run when you change the corpus or model).

Pipeline:
    CSV rows  ->  recipe documents  ->  embeddings  ->  saved vector store on disk

"Vector store" here is deliberately humble: a numpy matrix of embeddings plus a JSON
list of recipe metadata. For a few hundred (or few thousand) recipes, brute-force
cosine search over that matrix is instant, needs no database, and keeps the whole
retrieval mechanism visible — which is the entire point of Phase 1.

Run from the project root:
    python -m src.ingest
"""

from __future__ import annotations

import ast
import csv
import json
import sys

import numpy as np

from . import config, embed


def parse_list_field(raw: str) -> list[str]:
    """RecipeNLG stores `ingredients`/`directions` as stringified Python lists, e.g.
    "['1 cup sugar', '2 eggs']". Parse them safely with ast.literal_eval (NOT eval,
    which would execute arbitrary code). Fall back to the raw string if parsing fails.
    """
    raw = (raw or "").strip()
    if not raw:
        return []
    try:
        value = ast.literal_eval(raw)
        if isinstance(value, list):
            return [str(item) for item in value]
        return [str(value)]
    except (ValueError, SyntaxError):
        return [raw]


def build_document_text(title: str, ingredients: list[str], directions: list[str]) -> str:
    """The text we actually embed for a recipe.

    We fold the title, ingredients, and directions into one block so the embedding
    captures all three. (One recipe = one document; recipes are short and
    self-contained, so there is no need to split them into chunks.)
    """
    return (
        f"{title}\n"
        f"Ingredients: {'; '.join(ingredients)}\n"
        f"Directions: {' '.join(directions)}"
    )


def load_recipes(csv_path, limit: int) -> list[dict]:
    """Read up to `limit` rows from the CSV into structured recipe records.

    Uses csv.DictReader so we address columns by name and tolerate the extra columns
    RecipeNLG carries (a leading index column and a trailing `NER` column).
    """
    if not csv_path.exists():
        sys.exit(
            f"CSV not found: {csv_path}\n"
            f"  - For a quick test, the committed data/sample_recipes.csv should exist.\n"
            f"  - For the real corpus, download RecipeNLG from Kaggle and set\n"
            f"    RAGCHEF_CSV to its full_dataset.csv path (see README)."
        )

    recipes: list[dict] = []
    with open(csv_path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            if i >= limit:
                break
            title = (row.get("title") or "").strip()
            ingredients = parse_list_field(row.get("ingredients", ""))
            directions = parse_list_field(row.get("directions", ""))
            recipes.append(
                {
                    "id": i,  # stable position-based id; the eval phase matches on this
                    "title": title,
                    "ingredients": ingredients,
                    "directions": directions,
                    "link": (row.get("link") or "").strip(),
                    "source": (row.get("source") or "").strip(),
                    "text": build_document_text(title, ingredients, directions),
                }
            )
    return recipes


def main() -> None:
    print(f"Reading up to {config.CORPUS_SIZE} recipes from {config.CSV_PATH} ...")
    recipes = load_recipes(config.CSV_PATH, config.CORPUS_SIZE)
    if not recipes:
        sys.exit("No recipes loaded — is the CSV empty or malformed?")
    print(f"Loaded {len(recipes)} recipes.")

    print(f"Embedding via {config.EMBEDDING_MODEL} at {config.OPENAI_BASE_URL} ...")
    texts = [r["text"] for r in recipes]
    embeddings = embed.embed_texts(texts)  # (N, dim) unit vectors
    print(f"Got embeddings of shape {embeddings.shape}.")

    # Persist the index: embeddings as a .npy matrix, metadata as JSON.
    config.INDEX_DIR.mkdir(parents=True, exist_ok=True)
    np.save(config.EMBEDDINGS_PATH, embeddings)
    with open(config.METADATA_PATH, "w", encoding="utf-8") as f:
        json.dump(recipes, f, ensure_ascii=False)

    print(
        f"Saved index:\n"
        f"  {config.EMBEDDINGS_PATH}\n"
        f"  {config.METADATA_PATH}\n"
        f"Done. You can now ask questions:  python ask.py \"how do I keep cookies soft?\""
    )


if __name__ == "__main__":
    main()
