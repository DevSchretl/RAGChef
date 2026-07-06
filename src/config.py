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

# The recipe corpus. Defaults to the full RecipeNLG dataset that now lives in data/.
# For a quick smoke test without the 2.2 GB file, override with
# RAGCHEF_CSV=data/sample_recipes.csv.
CSV_PATH = Path(os.getenv("RAGCHEF_CSV", DATA_DIR / "full_dataset.csv"))

# Where ingest.py writes the index (the "vector store"). Two small files:
EMBEDDINGS_PATH = INDEX_DIR / "embeddings.npy"   # float32 matrix, shape (N, dim)
METADATA_PATH = INDEX_DIR / "metadata.json"      # list of N recipe records

# --------------------------------------------------------------------------------------
# Corpus / retrieval knobs
# --------------------------------------------------------------------------------------
# How many CSV rows to index (the first N rows). 50k maximizes near-duplicate density so the
# hard eval set (rare-keyword + near-duplicate-disambiguation questions) has real distractor
# pressure for dense retrieval. Ingest is a one-time ~22 min at ~37 docs/sec; index ~150 MB.
# The committed eval test set is grounded in these first rows, so don't lower this below the
# gold ids it references.
CORPUS_SIZE = int(os.getenv("RAGCHEF_CORPUS_SIZE", "50000"))

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
# Enough room for a full recipe answer; 600 was clipping multi-ingredient answers mid-list.
MAX_TOKENS = int(os.getenv("RAGCHEF_MAX_TOKENS", "1024"))

# --------------------------------------------------------------------------------------
# Evaluation (Phase 3)
# --------------------------------------------------------------------------------------
EVAL_DIR = PROJECT_ROOT / "eval"
TESTSET_PATH = EVAL_DIR / "testset.json"     # frozen, curated test questions (committed)
GENERAL_TESTSET_PATH = EVAL_DIR / "testset.general.json"  # general cooking Qs (ablation only)
REPORTS_DIR = EVAL_DIR / "reports"           # eval outputs (committed)
REPORT_PATH = REPORTS_DIR / "report.md"      # single report, overwritten each run (all test data)
ABLATION_REPORT_PATH = REPORTS_DIR / "ablation.md"  # RAG vs no-RAG comparison report
HISTORY_PATH = REPORTS_DIR / "history.csv"   # one row per run — the cross-run ledger

# k used by the retrieval metrics (hit@k / recall@k). Defaults to TOP_K so the eval
# measures the same retrieval depth the app actually uses.
EVAL_K = int(os.getenv("RAGCHEF_EVAL_K", str(TOP_K)))

# The model that *judges* answers in the RAGAS-style metrics (Tier 2, added next slice).
# Defaults to the chat model, but point it at a different/stronger model when you can, so
# the system isn't grading its own homework.
JUDGE_MODEL = os.getenv("RAGCHEF_JUDGE_MODEL", CHAT_MODEL)
