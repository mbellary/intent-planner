from fastapi import APIRouter

from planner.artifacts.artifact_models import IntentArtifact
from planner.engine.planner_engine import PlannerEngine

router = APIRouter()
engine = PlannerEngine()


@router.post("/plan")
async def generate_plan(intent: IntentArtifact):
    plan = engine.plan(intent)
    return plan
