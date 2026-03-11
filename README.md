# intent-planner

Intent Planning Engine for deterministic plan generation.

This repository transforms human intent into deterministic resolved plans.
It does not execute workloads.

## Development (uv)

- Install dependencies: `uv sync --dev`
- Run API: `uv run uvicorn planner.api.app:app --reload`
- Run tests: `uv run pytest -q`
- Run linting: `uv run ruff check .`

## Project layout

- `src/planner/`: application package
- `tests/`: pytest test suite
