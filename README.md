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

## The dataset

The full **RecipeNLG** dataset (`data/full_dataset.csv`, ~2.2M recipes, 2.2 GB) is the
default corpus — `config.py` points `CSV_PATH` at it and ingests the first
`CORPUS_SIZE` rows (5,000 by default). It's gitignored, so it's never committed. If you
clone fresh, download it from Kaggle (`paultimothymooney/recipenlg`) and drop
`full_dataset.csv` into `data/`.

```powershell
python -m src.ingest          # indexes the first 5,000 rows of full_dataset.csv
```

Only the first `CORPUS_SIZE` rows are read, so the 2.2 GB file size is irrelevant — ingest
cost is linear in `CORPUS_SIZE` (≈2–3 min for 5,000 on a CPU-class machine, far less on a
GPU). Indexing all 2.2M recipes is unnecessary; a few thousand gives the eval enough
distractors to be discriminating. For a quick test without the big file, use the tiny
committed sample instead:

```powershell
$env:RAGCHEF_CSV = "data/sample_recipes.csv"; python -m src.ingest
```

> The eval test set's gold ids reference recipes in the first 5,000 rows, so don't lower
> `CORPUS_SIZE` below that if you want the committed eval to stay valid.

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

## Evaluation (Phase 3)

A two-tier eval turns "is my RAG any good?" into tracked numbers. It runs the frozen test
set ([eval/testset.json](eval/testset.json)) through the same `retrieve` → `generate`
pipeline and scores it. No new dependencies — same `openai` + `numpy`.

| File | Role |
|------|------|
| [eval/testset.json](eval/testset.json) | Frozen, hand-curated questions + gold recipe ids + reference answers. |
| [eval/retrieval_metrics.py](eval/retrieval_metrics.py) | **Tier 1** — `hit@k`, `recall@k`, `MRR`. Deterministic, no LLM. |
| [eval/judge.py](eval/judge.py) | **Tier 2** — RAGAS-style `faithfulness`, `answer_relevancy`, `context_precision`, `context_recall`, judged by the local LLM. |
| [eval/run_eval.py](eval/run_eval.py) | Runs both tiers, writes `report.md` + appends to `history.csv`. |
| [eval/make_testset.py](eval/make_testset.py) | Generates candidate questions from indexed recipes (then curate by hand). |
| [eval/run_ablation.py](eval/run_ablation.py) | **RAG vs no-RAG** ablation — how much retrieval helps. Writes `ablation.md`. |

**Two metric tiers:**
- **Tier 1 (retrieval)** — deterministic, instant, free. Did the retriever surface the
  right recipe? The fast inner loop for tuning. Needs LM Studio only to embed the query.
- **Tier 2 (generation, RAGAS-style)** — the local LLM judges answer quality. The headline
  number is **hallucination rate = 1 − faithfulness**. These follow the RAGAS *definitions*
  via plain prompts (no `ragas`/LangChain, so it runs fine on Python 3.14); the values are
  *directionally* faithful to canonical RAGAS, which is what you want for tracking change.

```powershell
# Fast, deterministic — retrieval metrics only (no chat model needed):
python -m eval.run_eval --retrieval-only --name phase1-dense

# Full eval (retrieval + LLM judge). Needs the chat model loaded in LM Studio:
python -m eval.run_eval --name phase1-dense
python -m eval.run_eval --limit 3          # quick smoke test
```

Each run writes a single self-contained [eval/reports/report.md](eval/reports/report.md)
— summary metrics plus every question's full test data (question, reference answer,
retrieved recipes, generated answer, scores), overwritten each run — and appends one row
to `eval/reports/history.csv`, your **performance ledger over time**. The `--name` flag
tags each run, so when Phase 2 (hybrid + rerank) lands you re-run with `--name
phase2-hybrid` and diff the history rows: that before/after is the project's centerpiece.

> **Judge model:** by default the judge is your chat model (`JUDGE_MODEL` → `CHAT_MODEL`).
> Point `RAGCHEF_JUDGE_MODEL` at a different/stronger model when you can, so the system
> isn't grading its own homework.

**Caveats (by design):** the eval is only meaningful on a real corpus (a few hundred
ingested recipes) — the 8-recipe sample just smoke-tests the harness. Retrieval metrics are
*directional* because RecipeNLG has near-duplicates (a valid sibling recipe can score as a
"miss"), which is why `gold_ids` is a list and the duplicate-robust context metrics
complement them. Regenerate candidate questions for a new corpus with
`python -m eval.make_testset`, then curate the result by hand.

### Ablation: does RAG actually help?

The harness above scores the RAG pipeline, but not how much the *retrieval* is worth. The
ablation answers every question **twice** — once **with RAG** (retrieve → grounded answer)
and once **closed-book** (no context; the model answers from memory) — and scores both with
the same metric: **groundedness** against the question's gold recipe (the fraction of the
answer's claims the true recipe supports; `hallucination = 1 − groundedness`). Judging
against the gold recipe rather than the retrieved context is what makes the no-RAG arm
measurable, so the two are directly comparable. The gap is the value retrieval adds.

```powershell
# Needs the chat model loaded in LM Studio:
python -m eval.run_ablation --name rag-vs-norag
python -m eval.run_ablation --limit 2          # quick smoke test
```

It runs the frozen specific-recipe questions plus a handful of broad general cooking
questions ([eval/testset.general.json](eval/testset.general.json)) and reports
[eval/reports/ablation.md](eval/reports/ablation.md): a RAG-vs-no-RAG summary table broken
down **overall / specific / general**, then every question with both answers side by side.

> **Reading the number:** "hallucination" here means *unsupported by the gold recipe*, so a
> closed-book answer that gives a valid but *different* recipe still counts against it. That's
> the intended test for **specific-source** questions (RAG's job is to reproduce the source);
> on **general** questions a closed-book model can compete, which is why the two are reported
> separately. The per-answer claim counts (`supported/total`) make refusals or empty answers
> visible so a "0/0 → 1.0" can't masquerade as a win.

## What's next (not built yet)

- **Phase 2** — BM25 keyword search + cross-encoder reranking (the same eval then proves
  the before/after).

See [HANDOFF.md](HANDOFF.md) for the full plan.
