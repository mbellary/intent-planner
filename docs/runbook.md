# Intent Planner Runbook

## Local operations
- Start API: `uv run uvicorn planner.api.app:app --reload`
- Execute checks: `uv run ruff check . && uv run pytest -q`

## Diagnostics
- Use `/health` for liveness checks.
- Capture `x-request-id` from response headers for request tracing.
- Planner failures use a typed error envelope with code/message/context.

## Release checklist
1. CI green on lint and test jobs.
2. Execution plan task statuses updated.
3. Deterministic plan generation verified by tests.
