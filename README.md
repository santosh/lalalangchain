# lalalangchain

A step-by-step tutorial building a LangChain agent from scratch — starting with a simple weather lookup and growing toward a fully-featured conversational AI application.

Each stage lives on its own branch so you can check out any point in the journey independently.

## Tutorial Stages

| Stage | Branch | What's covered |
|---|---|---|
| 1 | [stage-1](../../tree/stage-1) | Basic weather agent — custom tool, Ollama LLM, Open-Meteo API |
| 2 | [stage-2](../../tree/stage-2) | Context-aware agent — runtime context, structured output, conversation memory |

## Quickstart (latest stage)

**Requirements:** Python 3.12+, [Ollama](https://ollama.com) with `qwen3:14b`, [uv](https://docs.astral.sh/uv/)

```bash
ollama pull qwen3:14b
uv sync
uv run main.py
```

## Following the tutorial

To explore a specific stage:

```bash
git checkout stage-1   # or stage-2, stage-3, …
```

Each branch has its own README explaining what was added and why.
