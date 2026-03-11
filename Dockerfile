FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml ./
RUN pip install --no-cache-dir fastapi pydantic uvicorn pyyaml networkx httpx pytest

COPY . .

CMD ["uvicorn", "planner.api.app:app", "--host", "0.0.0.0", "--port", "8000"]
