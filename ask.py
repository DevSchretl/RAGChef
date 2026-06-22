"""
ask.py — the tiny CLI that runs the whole naive-RAG loop for one question.

    retrieve(question)  ->  generate_answer(question, recipes)  ->  print

Usage (from the project root, with the venv active):
    python ask.py "how do I keep chocolate chip cookies chewy?"
    python ask.py --top-k 6 "what can I make with chicken and rice?"
    python ask.py --show-context "substitute for buttermilk?"

Prerequisites:
    1. LM Studio running with a chat model AND an embedding model loaded
       (see README for the one-time setup).
    2. The index built once:  python -m src.ingest
"""

from __future__ import annotations

import argparse

from src import config, generate, retrieve


def main() -> None:
    parser = argparse.ArgumentParser(description="Ask the local RAG cooking advisor a question.")
    parser.add_argument("question", help="your cooking question (wrap it in quotes)")
    parser.add_argument(
        "--top-k",
        type=int,
        default=config.TOP_K,
        help=f"how many recipes to retrieve (default: {config.TOP_K})",
    )
    parser.add_argument(
        "--show-context",
        action="store_true",
        help="also print the full text of the recipes sent to the model",
    )
    args = parser.parse_args()

    # 1. RETRIEVE — find the most relevant recipes.
    results = retrieve.retrieve(args.question, top_k=args.top_k)

    # Show which recipes grounded the answer (titles + similarity scores). This makes
    # the retrieval step visible, which is the whole point of the learning exercise.
    print("\nRetrieved recipes:")
    for r in results:
        print(f"  [{r.score:.3f}] (id={r.id}) {r.recipe['title']}")

    if args.show_context:
        print("\n--- context sent to the model ---")
        print(generate.format_context(results))
        print("--- end context ---")

    # 2. GENERATE — have the local LLM answer, grounded in those recipes.
    print("\nThinking ...\n")
    answer = generate.generate_answer(args.question, results)

    print("Answer:")
    print(answer)


if __name__ == "__main__":
    main()
