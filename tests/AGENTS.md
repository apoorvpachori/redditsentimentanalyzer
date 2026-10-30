# Offline tests instructions

Follow the root AGENTS.md and read this directory’s README.md.

Keep default tests offline and independent of `.env` credentials. Mock the
dependency where the route uses it (`app.api.routes`). Test observable behavior
and contracts when changing functionality. Keep retrieval checks separate from
HTTP tests; explicitly label any future live-provider integration tests.
