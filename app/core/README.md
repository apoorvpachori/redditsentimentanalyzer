# Configuration

`config.py` validates settings with pydantic-settings and loads `.env` from
the working directory. `get_settings()` caches settings. See the
[root configuration table](../../README.md#configuration) and `.env.example`.

Settings are loaded lazily; health checks and offline tests need no API key.
Restart the server after changing environment values.
