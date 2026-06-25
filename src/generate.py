"""
Generate — the "G" in RAG. Turn retrieved recipes + a question into a grounded answer.

The whole idea of RAG: instead of asking the LLM to answer from memory (where it may
hallucinate), we hand it real recipes as context and instruct it to answer *from that
context*. The model becomes a reader/synthesizer over retrieved facts.

`generate_answer` returns a string and never prints. That keeps it usable both from the
CLI (which prints the return value) and, later, from the Phase 3 eval loop (which runs
100 questions and must not spew to stdout).

We call LM Studio's OpenAI-compatible `/v1/chat/completions`, so any OpenAI-compatible
local server (LM Studio, llama.cpp server, vLLM, Ollama's OpenAI shim) works unchanged.
"""

from __future__ import annotations

from openai import OpenAI

from . import config
from .retrieve import Result

# System prompt: defines the assistant's role and the grounding rule.
SYSTEM_PROMPT = (
    "You are a helpful cooking advisor. Answer the user's question using ONLY the "
    "recipes provided as context. Ground your advice in those recipes and refer to "
    "them by title. If the context does not contain enough information to answer, say "
    "so plainly rather than inventing details."
)

# Closed-book prompt: the "no-RAG" baseline for the ablation. The model answers from its
# own parametric memory with no retrieved context. We push it to commit to one concrete
# recipe (rather than refuse) so its answer makes measurable claims to score for
# hallucination against the gold recipe.
CLOSED_BOOK_SYSTEM = (
    "You are a helpful cooking advisor. Answer the user's question from your own culinary "
    "knowledge with concrete, specific steps and ingredients. Give your single best recipe "
    "or answer; do not refuse or say you lack a specific recipe."
)

_client: OpenAI | None = None


def _get_client() -> OpenAI:
    global _client
    if _client is None:
        _client = OpenAI(
            base_url=config.OPENAI_BASE_URL,
            api_key=config.OPENAI_API_KEY,
        )
    return _client


def format_context(results: list[Result]) -> str:
    """Render retrieved recipes into a readable, numbered context block for the prompt."""
    blocks = []
    for n, r in enumerate(results, start=1):
        recipe = r.recipe
        ingredients = "\n".join(f"  - {item}" for item in recipe["ingredients"])
        directions = "\n".join(
            f"  {i}. {step}" for i, step in enumerate(recipe["directions"], start=1)
        )
        blocks.append(
            f"[Recipe {n}] {recipe['title']}\n"
            f"Ingredients:\n{ingredients}\n"
            f"Directions:\n{directions}"
        )
    return "\n\n".join(blocks)


def build_messages(query: str, results: list[Result]) -> list[dict]:
    """Assemble the chat messages: a system instruction + the grounded user turn."""
    context = format_context(results)
    user_content = (
        f"Here are some recipes that may be relevant:\n\n{context}\n\n"
        f"Question: {query}"
    )
    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_content},
    ]


def generate_answer(query: str, results: list[Result]) -> str:
    """Send the grounded prompt to the local LLM and return its answer as a string."""
    client = _get_client()
    response = client.chat.completions.create(
        model=config.CHAT_MODEL,
        messages=build_messages(query, results),
        temperature=config.TEMPERATURE,
        max_tokens=config.MAX_TOKENS,
    )
    return (response.choices[0].message.content or "").strip()


def generate_answer_closed_book(query: str) -> str:
    """Answer with NO retrieved context — the no-RAG baseline for the ablation harness."""
    client = _get_client()
    response = client.chat.completions.create(
        model=config.CHAT_MODEL,
        messages=[
            {"role": "system", "content": CLOSED_BOOK_SYSTEM},
            {"role": "user", "content": query},
        ],
        temperature=config.TEMPERATURE,
        max_tokens=config.MAX_TOKENS,
    )
    return (response.choices[0].message.content or "").strip()
