"""
Central configuration — every tunable lives here, nothing is hard-coded elsewhere.

This is the single most important file in the project: other modules import their
settings from here, so changing corpus size, top-k, or which local model to call is a
one-line edit (or an environment-variable override) instead of a hunt through the code.

Why environment-variable overrides? The three things that genuinely vary from machine
to machine are the LM Studio URL and the two model ids (whatever you happen to have
loaded). Those read from the environment with sensible defaults; everything else is a
plain constant you can edit directly.
"""

from __future__ import annotations

import os
from pathlib import Path

# --------------------------------------------------------------------------------------
# Paths
# --------------------------------------------------------------------------------------
# PROJECT_ROOT is this file's grandparent:  <root>/src/config.py -> <root>
PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"
INDEX_DIR = PROJECT_ROOT / "index"  # built by ingest.py; gitignored

# The recipe corpus. Defaults to the tiny committed sample so the pipeline runs out of
# the box. Point CSV_PATH at the full RecipeNLG `full_dataset.csv` once you've
# downloaded it from Kaggle (paultimothymooney/recipenlg).
CSV_PATH = Path(os.getenv("RAGCHEF_CSV", DATA_DIR / "sample_recipes.csv"))

# Where ingest.py writes the index (the "vector store"). Two small files:
EMBEDDINGS_PATH = INDEX_DIR / "embeddings.npy"   # float32 matrix, shape (N, dim)
METADATA_PATH = INDEX_DIR / "metadata.json"      # list of N recipe records

# --------------------------------------------------------------------------------------
# Corpus / retrieval knobs
# --------------------------------------------------------------------------------------
# How many CSV rows to index. Start SMALL — a few hundred — so ingest is fast and the
# artifacts stay tiny. Scale up only once the end-to-end loop works.
CORPUS_SIZE = int(os.getenv("RAGCHEF_CORPUS_SIZE", "200"))

# How many recipes to retrieve and feed to the LLM per question.
TOP_K = int(os.getenv("RAGCHEF_TOP_K", "4"))

# --------------------------------------------------------------------------------------
# Local LLM server (LM Studio, or any OpenAI-compatible server)
# --------------------------------------------------------------------------------------
# LM Studio's local server speaks the OpenAI API. Start it from the "Developer" /
# "Local Server" tab; the default address is http://localhost:1234/v1.
OPENAI_BASE_URL = os.getenv("RAGCHEF_BASE_URL", "http://localhost:1234/v1")

# LM Studio ignores the key, but the OpenAI client requires a non-empty string.
OPENAI_API_KEY = os.getenv("RAGCHEF_API_KEY", "lm-studio")

# The chat model id — must match a model loaded in LM Studio. Set RAGCHEF_CHAT_MODEL to
# whatever id LM Studio shows for your Gemma model.
CHAT_MODEL = os.getenv("RAGCHEF_CHAT_MODEL", "google/gemma-4-e4b")

# The embedding model id — LM Studio can serve an embedding model alongside the chat
# model. Load a small one (e.g. nomic-embed-text) and set RAGCHEF_EMBED_MODEL to its id.
# IMPORTANT: the *same* embedding model must be used for ingest and for querying, or the
# vectors live in different spaces and retrieval is meaningless.
EMBEDDING_MODEL = os.getenv(
    "RAGCHEF_EMBED_MODEL", "text-embedding-nomic-embed-text-v1.5"
)

# --------------------------------------------------------------------------------------
# Generation knobs
# --------------------------------------------------------------------------------------
# Low temperature -> more grounded, less inventive answers. We want the model to lean on
# the retrieved recipes, not improvise.
TEMPERATURE = float(os.getenv("RAGCHEF_TEMPERATURE", "0.2"))
MAX_TOKENS = int(os.getenv("RAGCHEF_MAX_TOKENS", "600"))
