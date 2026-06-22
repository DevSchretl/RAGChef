"""
Retrieve — given a question, return the most similar recipes.

This is the "R" in RAG. Phase 1 uses pure dense retrieval:
    1. Embed the query with the SAME model that embedded the recipes.
    2. Score every recipe by cosine similarity (a single matrix-vector dot product,
       because all vectors are unit-length).
    3. Return the top-k, each carrying its doc id, score, and metadata.

Exposing the doc `id` on every result is deliberate: the Phase 3 evaluation harness
matches retrieved ids against "gold" recipe ids to compute hit@k / recall@k. Phase 1
doesn't need it yet, but it costs nothing to carry it now.
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass

import numpy as np

from . import config, embed


@dataclass
class Result:
    """One retrieved recipe plus its retrieval score."""

    id: int
    score: float
    recipe: dict  # the full metadata record from the index


# The index is loaded once and cached for the process lifetime.
_embeddings: np.ndarray | None = None
_metadata: list[dict] | None = None


def _load_index() -> tuple[np.ndarray, list[dict]]:
    global _embeddings, _metadata
    if _embeddings is None or _metadata is None:
        if not config.EMBEDDINGS_PATH.exists() or not config.METADATA_PATH.exists():
            sys.exit(
                "No index found. Build it first with:  python -m src.ingest"
            )
        _embeddings = np.load(config.EMBEDDINGS_PATH)
        with open(config.METADATA_PATH, "r", encoding="utf-8") as f:
            _metadata = json.load(f)
    return _embeddings, _metadata


def retrieve(query: str, top_k: int | None = None) -> list[Result]:
    """Return the top_k recipes most similar to `query`, best first."""
    top_k = top_k or config.TOP_K
    embeddings, metadata = _load_index()

    # Embed the query (shape (1, dim)) and reduce to a 1-D vector.
    query_vec = embed.embed_texts([query])[0]

    # Cosine similarity == dot product, since every vector is unit-length.
    # scores[i] is the similarity between the query and recipe i.
    scores = embeddings @ query_vec

    # Indices of the top_k highest scores. argpartition finds them without fully
    # sorting the whole array; we then sort just those k by score, descending.
    k = min(top_k, len(metadata))
    top_idx = np.argpartition(scores, -k)[-k:]
    top_idx = top_idx[np.argsort(scores[top_idx])[::-1]]

    return [
        Result(id=int(i), score=float(scores[i]), recipe=metadata[i]) for i in top_idx
    ]


if __name__ == "__main__":
    # Quick manual check:  python -m src.retrieve "chewy chocolate chip cookies"
    question = " ".join(sys.argv[1:]) or "chewy chocolate chip cookies"
    for r in retrieve(question):
        print(f"[{r.score:.3f}] (id={r.id}) {r.recipe['title']}")
