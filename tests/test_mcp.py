from fastapi.testclient import TestClient
from mcpdev.main import app

client = TestClient(app)


def test_lists_and_refuses_apply():
    assert "read_file" in client.get("/tools").json()["tools"]
    ok = client.post("/call", json={"name": "read_file", "arguments": {"q": "status"}}).json()
    assert ok["ok"] is True
    assert ok["applied"] is False
    refused = client.post("/call", json={"name": "read_file", "arguments": {"cmd": "kubectl apply"}}).json()
    assert refused["ok"] is False
