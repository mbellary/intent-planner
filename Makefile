.PHONY: run test lint

run:
	uv run uvicorn planner.api.app:app --reload

test:
	uv run pytest -q

lint:
	uv run ruff check .
