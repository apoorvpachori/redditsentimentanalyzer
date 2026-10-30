# HTTP API

`routes.py` serves `GET /health` and `POST /analyze`. `schemas.py` defines
`AnalyzeRequest` (a nonblank query up to 2,000 characters) and `AnalyzeResponse`
(answer and elapsed seconds).

The route invokes the agent asynchronously with a total timeout and graph limit.
Timeouts become 504; other analysis failures become generic 503 responses.
Health reports process availability only. See [API tests](../../tests/test_api.py).
