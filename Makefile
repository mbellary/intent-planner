.PHONY: run test

run:
	uvicorn planner.api.app:app --reload

test:
	pytest planner/tests -q
