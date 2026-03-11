# intent-planner

Intent Planning Engine for deterministic plan generation.

This repository transforms human intent into deterministic resolved plans.
It does not execute workloads.

## Development (uv)

- Install dependencies: `uv sync --dev`
- Run API: `uv run uvicorn planner.api.app:app --reload`
- Run tests: `uv run pytest -q`
- Run linting: `uv run ruff check .`

## API

- `GET /health` liveness endpoint.
- `POST /v1/plan` deterministic plan generation endpoint.
- Responses include `x-request-id` for traceability.
- Planner errors are returned as typed machine-readable envelopes.

## Project layout

- `src/planner/`: application package
- `tests/`: pytest test suite
- `docs/runbook.md`: operations and release checklist
- `.github/workflows/ci.yml`: quality gate workflow
