# lalalangchain

My notes and code from working through a [LangChain tutorial](https://www.youtube.com/watch?v=J7j5tCB_y4w), starting from a small weather agent.

Each lesson explores a **different** LangChain concept rather than building on top of the previous one. So every lesson lives on its own branch and stands alone — the numbers just suggest an order to follow them in, not a dependency chain. `main` holds this overview plus a runnable copy of the latest lesson's code.

## Lessons

| # | Branch | Concept |
|---|---|---|
| 01 | [01-basic-weather-agent](../../tree/01-basic-weather-agent) | Custom `@tool`, `create_agent`, a local Ollama LLM, and calling the Open-Meteo API |
| 02 | [02-context-and-memory](../../tree/02-context-and-memory) | Runtime context (`context_schema`), structured output (`response_format`), and conversation memory (checkpointer) |
| 03 | [03-multimodal-input](../../tree/03-multimodal-input) | Multimodal input — sending text + an image to a vision-capable model (`gemma3`) |
| 04 | [04-similarity-search](../../tree/04-similarity-search) | Similarity search — embeddings, a FAISS vector store, and retrieval by meaning (the retrieval step of RAG) |
| 05 | [05-retriever-tool-agent](../../tree/05-retriever-tool-agent) | Retriever-tool agent — wrapping a vector store as a tool with `create_retriever_tool` and letting an agent decide when to retrieve (closing the RAG loop) |
| 06 | [06-dynamic-prompt-middleware](../../tree/06-dynamic-prompt-middleware) | Dynamic prompt middleware — reshaping the system prompt at runtime from `context_schema` via `@dynamic_prompt`, and disabling `qwen3` reasoning mode |
| 07 | [07-dynamic-model-selection](../../tree/07-dynamic-model-selection) | Dynamic model selection — routing a single agent across multiple local models at runtime with `@wrap_model_call` |

Each branch has its own README explaining what that lesson covers.

## Running a lesson

**Requirements:** Python 3.12+, [Ollama](https://ollama.com), [uv](https://docs.astral.sh/uv/)

```bash
git checkout 01-basic-weather-agent   # or any lesson branch
uv sync                               # install that lesson's deps
ollama pull qwen3:14b                 # check the branch README for the model it uses
uv run main.py
```

The model each lesson uses is noted in its README (lesson 01 uses `llama3.1:8b`, lesson 02 uses `qwen3:14b`, lesson 03 uses `gemma3:12b`, lesson 04 uses the `qwen3-embedding` embedding model, lesson 05 uses `qwen3-embedding` for retrieval and `qwen3:14b` as the agent's chat model, lesson 06 uses `qwen3:14b` with reasoning disabled, lesson 07 routes across `llama3.1:8b`, `qwen3:14b`, and `gemma3:12b`).
