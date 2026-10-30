from types import SimpleNamespace
from unittest.mock import AsyncMock

from fastapi.testclient import TestClient

from app.main import app


def test_api(monkeypatch):
    agent = SimpleNamespace(ainvoke=AsyncMock(return_value={
        "messages": [SimpleNamespace(text="Insufficient Reddit evidence.")]
    }))
    monkeypatch.setattr("app.api.routes.get_agent", lambda: agent)
    monkeypatch.setattr("app.api.routes.get_settings", lambda: SimpleNamespace(
        request_timeout_seconds=5, agent_recursion_limit=12
    ))
    with TestClient(app) as client:
        assert client.get("/health").status_code == 200
        assert client.post("/analyze", json={"query": " "}).status_code == 422
        response = client.post("/analyze", json={"query": "headphones"})
        assert response.status_code == 200
        assert response.json()["answer"] == "Insufficient Reddit evidence."
