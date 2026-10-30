# Reddit Product Sentiment Analyzer — Agent

CS410 Text Information Systems, UIUC. Team: Rohit Khorana, Rahul Patel, Apoorv Pachori.

A minimal Python ReAct (reason + act) agent served through FastAPI. LangChain's
`create_agent` runs on LangGraph: the model chooses a search query, calls the
search tool, reads the results, and repeats or produces an answer. This repo
covers the agent/API portion of the project.

## Run locally

Requires Python 3.11+.

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
cp .env.example .env
# Edit .env with your provider credentials, endpoint, and model ID.
uvicorn app.main:app --reload
```

Use an OpenAI-compatible provider that supports tool calling for your chosen
model. Set `LLM_API_KEY`, `LLM_BASE_URL`, and `LLM_MODEL` together. The example
Llama model ID is illustrative: providers use different identifiers, and the
OpenAI endpoint in the example does not host Llama. For OpenAI, select a model
available to your account instead. Keys remain server-side; `.env` is ignored.

Interactive API docs: http://127.0.0.1:8000/docs

```sh
curl -X POST http://127.0.0.1:8000/analyze \
  -H 'Content-Type: application/json' \
  -d '{"query":"What do Reddit users think about the Sony WH-1000XM5?"}'
```

Response: `{"answer":"...", "elapsed_seconds":1.23}`.
`GET /health` checks the API process only, without calling the model.
Each request is independent; there is no chat history or database.

## Connect BM25 later

Replace the body of `search_reddit` in `app/tools/reddit_search.py` with the retrieval call.
Return `SearchResults(status="ok", query=query, comments=[...]).model_dump()`.
Each comment has `id`, `text`, `subreddit`, `url`, and an optional retrieval
`score` (not a sentiment score). Honor `limit`, clamped to 1–50. Preserve actual
Reddit permalinks so the agent can cite its evidence.

The placeholder deliberately returns `not_implemented` and no comments.
Until retrieval is connected, the agent should explain that it cannot establish
Reddit consensus. It does not generate fake reviews. Prompt instructions guide
sentiment reporting but are not an accuracy guarantee; evaluate with labeled
comments and human review once retrieval is connected.

Requests have a total timeout and a bounded graph loop. Errors return generic
503/504 responses; details go to server logs. This is a local development API;
add authentication and deployment controls before exposing it publicly.

## Tests

```sh
pytest -q
```

Tests use a fake agent, without API calls or credentials.

## Repository map

```text
app/
  main.py              FastAPI application assembly and server entry point
  api/
    routes.py          Health and analysis endpoints; timeout/error handling
    schemas.py         HTTP request and response models
  agent/
    service.py         Cached model client and LangGraph agent construction
    prompts.py         Evidence and sentiment instructions
  core/
    config.py          Environment settings and validation
  tools/
    reddit_search.py   Placeholder BM25 tool; retrieval integration point
    schemas.py         Shared search-result and Reddit-comment models
tests/
  test_api.py          API checks using a fake agent
  test_tools.py        Placeholder search contract check
```

Each source directory and the tests directory includes a README for navigation
and an AGENTS.md with scoped contributor instructions. Root AGENTS.md applies
throughout the repository. Environment folders and generated files are excluded.

## Request flow

`POST /analyze` → request validation → configured ReAct agent → Reddit search
tool → agent final answer → response with elapsed time. The agent can repeat
search within its graph step limit. HTTP models live in `api/schemas.py`;
retrieval models live in `tools/schemas.py` so retrieval need not depend on HTTP.

## Configuration

| Variable | Purpose | Default |
| --- | --- | --- |
| `LLM_API_KEY` | Provider secret | Required |
| `LLM_MODEL` | Provider model identifier with tool support | Required |
| `LLM_BASE_URL` | OpenAI-compatible API endpoint | `https://api.openai.com/v1` |
| `REQUEST_TIMEOUT_SECONDS` | Overall invocation and model request timeout | `60` |
| `AGENT_RECURSION_LIMIT` | Maximum graph steps | `12` |

Run commands from the repository root so `.env` is found. Settings and the
agent are cached per process; restart the server after changing configuration.

## Project scope

The proposal targets approximately 500,000 product-related Reddit comments,
PySerini/Lucene BM25 retrieval, and Llama 3.1 8B Instruct sentiment analysis.
Dataset preparation, indexing, evaluation datasets, and the BM25 implementation
are future integrations. This scaffold implements only the agent/API portion.
Evaluate retrieval relevance, labeled sentiment accuracy, human-rated summaries,
and response latency once the full pipeline is connected.
