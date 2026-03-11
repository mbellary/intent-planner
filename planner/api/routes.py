from fastapi import APIRouter
from planner.engine.planner_engine import PlannerEngine
from planner.artifacts.artifact_models import IntentArtifact

router = APIRouter()
engine = PlannerEngine()


@router.post("/plan")
async def generate_plan(intent: IntentArtifact):
    plan = engine.plan(intent)
    return plan
