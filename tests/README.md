# Offline tests

`test_api.py` replaces the agent and settings with fakes, then checks health,
validation, and a successful analysis response. `test_tools.py` checks that
the search placeholder returns no evidence.

Run from the repository root:

```sh
.venv/bin/pytest -q
```

These checks do not evaluate model sentiment accuracy or call a live provider.
