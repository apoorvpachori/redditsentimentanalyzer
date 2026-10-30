# Configuration instructions

Follow the root AGENTS.md and read this directory’s README.md.

Keep configuration centralized in `config.py`. Use secret types for credentials
and validate numeric bounds. Document added variables in `.env.example` and the
root README. Preserve lazy loading so imports and health checks need no secrets.
