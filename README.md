# MCP-Based Developer Assistant

<!-- project-guide:start -->
## Project guide

[Project architecture](PROJECT_ARCHITECTURE.md) · [Interview questions and answers](INTERVIEW_QA.md)

Use the architecture document for the component diagram, implementation boundaries, and verification entry points. The interview guide includes source-backed answers and project walkthroughs.

### Implementation map

| Component | Responsibility |
| --- | --- |
| [`src/mcpdev/main.py`](src/mcpdev/main.py) | HTTP handlers: `GET /healthz`, `GET /tools`, `POST /call` |
| [`src/mcpdev/mcp.py`](src/mcpdev/mcp.py) | Functions: `list_tools`, `call` |
| [`requirements.txt`](requirements.txt) | Implementation or supporting configuration |
| [`src/mcpdev/__init__.py`](src/mcpdev/__init__.py) | Implementation or supporting configuration |
| [`tests/test_mcp.py`](tests/test_mcp.py) | Executable checks and regression examples |
| [`.github/workflows/ci.yml`](.github/workflows/ci.yml) | GitHub Actions job definitions |
| [`README.md`](README.md) | Project explanations or operating notes |

### Local setup and verification

From the repository root (the commands follow the checked-in manifests):

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -q
```

To serve the FastAPI application locally, install the server separately if it is not already available:

```bash
python -m pip install uvicorn
PYTHONPATH=src python -m uvicorn mcpdev.main:app --reload
```

<!-- project-guide:end -->

Level: 10 — MCP & Tool-Using Agents

Skills: Python, tool schema, no apply

Tools: read_file, list_tests, run_tests. Apply is refused.

```bash
pip install -r requirements.txt
pytest -q
```

This is a local laptop proof. It does not call a hosted model and it does not apply production changes.

## Ops plane

Workspaces, tenant isolation, job approval, and audit live under `/v1`. Production apply is refused. See `docs/ARCHITECTURE.md`.
