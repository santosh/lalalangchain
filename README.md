# lalalangchain

My notes and code from working through a [LangChain tutorial](https://www.youtube.com/watch?v=J7j5tCB_y4w), starting from a small weather agent.

Each lesson explores a **different** LangChain concept rather than building on top of the previous one. So every lesson lives on its own branch and stands alone — the numbers just suggest an order to follow them in, not a dependency chain. `main` holds this overview plus a runnable copy of the latest lesson's code.

## Lessons

| # | Branch | Concept |
|---|---|---|
| 01 | [01-basic-weather-agent](../../tree/01-basic-weather-agent) | Custom `@tool`, `create_agent`, a local Ollama LLM, and calling the Open-Meteo API |
| 02 | [02-context-and-memory](../../tree/02-context-and-memory) | Runtime context (`context_schema`), structured output (`response_format`), and conversation memory (checkpointer) |
| 03 | [03-multimodal-input](../../tree/03-multimodal-input) | Multimodal input — sending text + an image to a vision-capable model (`gemma3`) |

Each branch has its own README explaining what that lesson covers.

## Running a lesson

**Requirements:** Python 3.12+, [Ollama](https://ollama.com), [uv](https://docs.astral.sh/uv/)

```bash
git checkout 01-basic-weather-agent   # or any lesson branch
uv sync                               # install that lesson's deps
ollama pull qwen3:14b                 # check the branch README for the model it uses
uv run main.py
```

The model each lesson uses is noted in its README (lesson 01 uses `llama3.1:8b`, lesson 02 uses `qwen3:14b`, lesson 03 uses `gemma3:12b`).
