# RAGChef — Phase 1: Naive RAG over recipes

A retrieval-augmented **cooking advisor**. Ask a cooking question → the system retrieves
similar recipes from a local store → a **local LLM** (Gemma in LM Studio) gives a grounded
answer. Everything runs on your machine; nothing is sent to a hosted API.

This is **Phase 1** of the [5-phase plan](HANDOFF.md): the simplest possible end-to-end
loop. The goal is to *understand the RAG loop*, not to maximize quality — hybrid search,
reranking, and evaluation come in later phases.

```
                      ┌─────────────────────────── run once ───────────────────────────┐
   data/*.csv  ──►  ingest.py  ──►  embeddings (LM Studio)  ──►  index/  (numpy + json)
                      └────────────────────────────────────────────────────────────────┘

   "how do I keep cookies chewy?"
            │
            ▼
        retrieve.py  ──►  embed the query (LM Studio)  ──►  cosine search over index/
            │                                                        │
            │                                  top-k most similar recipes
            ▼                                                        │
        generate.py  ──►  build a grounded prompt  ──►  LM Studio chat (Gemma)  ──►  answer
```

---

## How it works (the whole loop in four steps)

1. **Embed** — Every recipe (title + ingredients + directions) is turned into a vector by
   an embedding model. A vector is just a list of numbers that captures meaning, so
   recipes about similar things end up close together. This happens once, during ingest.
2. **Store** — The vectors are saved as a numpy matrix (`index/embeddings.npy`) and the
   recipe text/metadata as JSON (`index/metadata.json`). That pair *is* our "vector
   store" — no database needed for a few hundred recipes.
3. **Retrieve** — Your question is embedded with the **same** model, then compared against
   every recipe vector by cosine similarity. Because all vectors are unit-length, this is
   one fast matrix multiply. We keep the top-k closest recipes.
4. **Generate** — Those recipes are pasted into a prompt with an instruction to "answer
   using only these recipes," and the local LLM writes the grounded answer.

Each step is one small, readable module — see [The code](#the-code) below.

---

## Setup

### 1. Python deps

Python 3.11–3.14 all work (this build was verified on 3.14). From the project root:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. LM Studio (the local OpenAI-compatible server)

This project talks to LM Studio's built-in server, which speaks the OpenAI API. Any
OpenAI-compatible server (llama.cpp, vLLM, Ollama's OpenAI shim) works too.

1. In LM Studio, download **two** models and **load both**:
   - a **chat model** — your Gemma model (e.g. `google/gemma-3-4b`)
   - an **embedding model** — a small one, e.g. `nomic-embed-text-v1.5`
2. Open the **Developer / Local Server** tab and **Start Server**. The default address is
   `http://localhost:1234/v1`.
3. Note the exact **model ids** LM Studio lists for each — you'll set them below.

### 3. Point the config at your models

The two model ids vary per machine, so set them via environment variables (or edit the
defaults in [src/config.py](src/config.py)):

```powershell
$env:RAGCHEF_CHAT_MODEL  = "google/gemma-3-4b"                 # your chat model id
$env:RAGCHEF_EMBED_MODEL = "text-embedding-nomic-embed-text-v1.5"  # your embedding model id
```

> The embedding model used to **build** the index and the one used to **query** it must be
> the same, or retrieval is meaningless. Re-run ingest if you ever change it.

---

## Run it

```powershell
# 1. Build the index (once). Uses the tiny committed sample by default.
python -m src.ingest

# 2. Ask questions.
python ask.py "how do I keep chocolate chip cookies chewy?"
python ask.py --top-k 6 "what can I make with chicken and rice?"
python ask.py --show-context "what is a substitute for buttermilk in pancakes?"
```

Example output:

```
Retrieved recipes:
  [0.612] (id=0) Chewy Chocolate Chip Cookies
  [0.341] (id=4) Simple Banana Bread
  ...

Answer:
For chewy cookies, the "Chewy Chocolate Chip Cookies" recipe uses brown sugar and a
shorter 9–11 minute bake ...
```

---

## Using the real RecipeNLG dataset

The committed `data/sample_recipes.csv` has just 8 recipes so the loop runs immediately.
For the real thing:

1. Download **RecipeNLG** from Kaggle (`paultimothymooney/recipenlg`) and unzip
   `full_dataset.csv` into `data/` (it's gitignored — never committed).
2. Point the config at it and choose how many rows to index (start small!):

   ```powershell
   $env:RAGCHEF_CSV         = "data/full_dataset.csv"
   $env:RAGCHEF_CORPUS_SIZE = "300"
   python -m src.ingest
   ```

Indexing all 2.2M recipes is unnecessary and slow — a few hundred to a few thousand is
plenty for learning and iterating.

---

## The code

| File | Role |
|------|------|
| [src/config.py](src/config.py)   | Every tunable + path. Edit one place to change anything. |
| [src/embed.py](src/embed.py)     | Shared embedding function (same model for index & query). |
| [src/ingest.py](src/ingest.py)   | CSV → recipe docs → embeddings → saved index. Run once. |
| [src/retrieve.py](src/retrieve.py) | Embed query → cosine search → top-k recipes (with ids). |
| [src/generate.py](src/generate.py) | Recipes + question → grounded prompt → local-LLM answer. |
| [ask.py](ask.py)                 | The CLI that wires retrieve → generate together. |

---

## Design notes (Phase 1)

- **No RAG framework** (no LangChain/LlamaIndex) — the retrieval→generation loop stays
  fully visible. That's the point of Phase 1.
- **One recipe = one document, no chunking.** Recipes are short and self-contained.
- **Brute-force cosine search**, not a vector DB. For a few hundred vectors it's instant
  and keeps the mechanism transparent. (A real DB earns its place only at larger scale.)
- **Embeddings + generation both via LM Studio**, so there's no torch dependency and the
  code is OpenAI-compatible out of the box.
- **`retrieve()` exposes each recipe's `id`** — unused in Phase 1, but it's the hook the
  Phase 3 evaluation harness needs to score retrieval against gold recipe ids.

## What's next (not built yet)

Phase 2 adds BM25 keyword search + cross-encoder reranking; Phase 3 adds an evaluation
harness. See [HANDOFF.md](HANDOFF.md) for the full plan.
