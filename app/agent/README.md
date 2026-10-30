# ReAct agent

`service.py` builds and caches the OpenAI-compatible chat model and LangChain
agent running on LangGraph. `prompts.py` holds `SYSTEM_PROMPT`.

The model calls the Reddit search tool and receives its results before producing
a final answer. Provider credentials and model settings come from `core/config.py`.
The HTTP route supplies the user message, graph limit, and overall timeout.
