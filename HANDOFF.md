# RAG Project — Handoff / Restart Context

Context for a fresh Claude session. The previous build ("RAGChef") worked but grew
too large too fast, so we're restarting clean in a new folder. This file carries the
**plan** and the **key design decisions** worth keeping. Fine implementation details
are intentionally omitted — rebuild lean.

**This time: everything runs locally.** Generation and the eval judge use a **local
LLM** (e.g. Ollama / llama.cpp / vLLM / a `transformers` model). Embeddings and the
reranker were already local. There is no hosted-API dependency to design around.

---

## The domain

A retrieval-augmented **cooking advisor** over the **RecipeNLG** dataset (~2.2M recipes;
Kaggle: `paultimothymooney/recipenlg`). Ask a cooking question (or paste a recipe) → the
system retrieves similar recipes from a local store → a local LLM gives grounded advice.

Data quirks worth knowing up front:
- CSV columns: `title`, `ingredients`, `directions`, `link`, `source`.
- `ingredients` / `directions` are **stringified Python lists** in the CSV — parse with
  `ast.literal_eval`, not `eval`.
- **Don't index all 2.2M.** Last time we took the first **N rows** (a config knob) to keep
  ingest fast. Start *small* (a few hundred) and only scale up once the loop works.

---

## The 5-phase plan

1. **Naive RAG baseline.** Simplest end-to-end loop: load → embed → store in a local
   vector DB → retrieve top-k → stuff into a local-LLM prompt → return answer. Tiny CLI.
   Minimal stack, no framework. Goal is *understanding the loop*, not quality.

2. **Make retrieval good (hybrid + rerank).** Add BM25 keyword search alongside dense
   vector search and fuse them; then a cross-encoder reranker narrows the shortlist. This
   is where most of the real quality gain lives. Add metadata filtering. The lesson this
   phase demonstrates: *retrieval quality, not model choice, makes or breaks RAG.*

3. **Prove it works (evaluation harness).** A fixed test set + measured metrics so every
   change gets a number. This is the phase that makes the project stand out. (Details below
   — this is what we'd just finished.)

4. **Adaptive / agentic routing.** A query classifier routes simple factual questions to
   the fast Phase-2 retriever and complex multi-step questions to an agentic loop
   (decompose → multi-hop retrieve → synthesize). The Phase-3 eval then *proves* the
   adaptive version beats the simple one. (LangGraph is the usual orchestrator.)

5. **Ship it.** Clean repo (retrieval/indexing separated from app code), Dockerfile, a
   runnable demo, and a short architecture/tradeoffs writeup. Optional stretch: a small
   GraphRAG or multimodal component over a data subset.

---

## Key design decisions (carry these forward)

**Architecture**
- **Plain Python, no RAG framework** (no LangChain/LlamaIndex) — keeps the retrieval→generation
  loop fully visible. Good for learning; revisit only if a framework clearly earns its weight.
- **One recipe = one document; no chunking.** Recipes are short and self-contained, so chunk-
  splitting added nothing. (Chunking matters for long docs — not here.)
- **One central `config.py`** holding every tunable (corpus size, top-k, the k's for each
  retrieval stage, model names). Other modules import from it; nothing is hard-coded. This was
  the single best decision — it's what lets the eval sweep configs.
- Clean module split: `config` / `ingest` (build indexes, run once) / `retrieve` / `generate`
  / a shared tokenizer / a thin CLI.

**Retrieval (Phase 2)**
- **Two-stage funnel:** (1) *recall* — dense (vector) + sparse (BM25) each return ~20
  candidates; (2) *precision* — fuse, then cross-encoder rerank down to the final top-k.
- **Reciprocal Rank Fusion (RRF)** to combine dense + sparse. Chosen because vector distances
  and BM25 scores live on totally different scales; RRF uses *rank only*, sidestepping that.
- Metadata filter (e.g. by `source`) applied in the vector DB and re-enforced for BM25 hits.

**Local models**
- Embeddings: a small sentence-transformers bi-encoder (e.g. `all-MiniLM-L6-v2`, 384-dim).
  The **same model must be used for indexing and querying.**
- Reranker: a cross-encoder (e.g. `ms-marco-MiniLM-L-6-v2`) — scores (query, doc) jointly;
  far sharper than the bi-encoder but too slow for the whole corpus, so it only sees the shortlist.
- Generation + eval judge: a **local LLM**.

**Evaluation (Phase 3) — the important part**
- **Two metric tiers:**
  1. *Retrieval metrics* — `hit@k`, `recall@k`, `MRR`. Deterministic, no LLM, instant, free.
     The fast inner loop for tuning.
  2. *Generation metrics* (RAGAS) — `faithfulness`, `answer_relevancy`, `context_precision`,
     `context_recall`. LLM-judged. **Hallucination rate = 1 − faithfulness** is the headline number.
- **Recipe-grounded, LLM-generated test set.** Sample *real indexed* recipes, have the LLM
  write a specific question + a reference answer for each, and record that recipe's id as the
  **gold doc**. This is what enables the deterministic retrieval metrics *and* gives RAGAS its
  reference answers. Generate ~80–100 candidates, then **curate by hand** to a frozen ~50–100
  and commit it — frozen so numbers stay comparable across runs.
- **Before/after is the centerpiece:** run the same test set against the Phase-1 config
  (dense, no rerank) vs the Phase-2 config (hybrid + rerank) and show the deltas.
- **Two tiny pipeline hooks the eval needs:** the retriever must **expose the doc id** of each
  result (to match against gold ids), and generation needs a way to **run quietly in a loop**
  (no streaming to stdout for 100 questions).
- **Known limitation:** RecipeNLG has near-duplicate recipes, so a single gold id can
  undercount retrieval hits (a valid sibling recipe scores as a "miss"). Treat retrieval
  metrics as *directional*; the RAGAS context metrics don't need exact gold-id matching and are
  the duplicate-robust complement. Allow a *list* of gold ids.
- RAGAS needs a **judge LLM + an embeddings model**; point both at your local stack. Use a
  *different/stronger* model for judging than for generation when you can, so the system isn't
  grading its own homework.
- CI was deliberately deferred (local-only). Easy to add later since the harness is config-driven.

---

## Lessons — keep it lean this time

These are *why* the last build felt too heavy:
- **Start with a few hundred recipes, not 15k.** Big ingest = slow iteration and large local
  artifacts early, for no learning benefit.
- **Pin a mainstream Python (3.11 or 3.12), not the bleeding edge.** The eval stack (RAGAS +
  LangChain) fought hard on a brand-new interpreter — missing wheels, version conflicts, and an
  `asyncio`/`nest_asyncio` incompatibility that silently turned every metric into `NaN`. A
  boring interpreter avoids almost all of it.
- **RAGAS pulls in a large LangChain dependency tree and is version-sensitive** — pin it (and
  the LangChain packages) the moment it works, or consider a lighter eval (even hand-rolled
  faithfulness/relevance prompts) if it becomes the tail wagging the dog.
- **Build phases as thin vertical slices.** Get Phase 1 answering end-to-end before adding
  hybrid/rerank; get a 10-question eval running before scaling the test set. Resist adding
  config knobs and stages until a metric says you need them.
- **Never commit the dataset or the generated indexes** (gitignore them). Commit the frozen
  test set and the eval report.

---

## Suggested minimal starting layout

```
src/config.py      # all tunables + paths
src/ingest.py      # CSV subset -> documents -> embeddings -> vector store (run once)
src/retrieve.py    # dense (+ later sparse + rerank) -> ranked docs (exposes doc id)
src/generate.py    # docs -> local-LLM prompt -> grounded answer (quiet mode for eval)
ask.py             # tiny CLI
eval/              # added in Phase 3: test set, retrieval metrics, RAGAS runner, report
```

Build Phase 1 only. Add the rest one slice at a time.
