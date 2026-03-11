from __future__ import annotations

from fastapi import APIRouter, Header, Request

from planner.artifacts.artifact_models import IntentArtifact
from planner.engine.planner_engine import PlannerEngine

router = APIRouter()
engine = PlannerEngine()


@router.get("/health")
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


@router.post("/v1/plan")
async def generate_plan(
    request: Request,
    intent: IntentArtifact,
    x_idempotency_key: str | None = Header(default=None),
):
    plan = engine.plan(intent)
    return {
        "api_version": "v1",
        "request_id": request.state.request_id,
        "idempotency_key": x_idempotency_key,
        "data": plan,
        "error": None,
    }
