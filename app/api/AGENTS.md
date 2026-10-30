# HTTP API instructions

Follow the root AGENTS.md and read this directory’s README.md.

Keep validation and response models in `schemas.py`, endpoint handling in
`routes.py`. Do not expose provider exceptions or secrets in HTTP errors.
Preserve async invocation, timeout handling, and per-request conversation state.
When moving route dependencies, update monkeypatch targets in API tests.
