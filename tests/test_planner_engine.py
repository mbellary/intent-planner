from planner.engine.planner_engine import PlannerEngine
from planner.intent.schemas import IntentArtifact, IntentSpec


def test_planner_engine_returns_deterministic_plan():
    engine = PlannerEngine()
    intent = IntentArtifact(
        intent_id="intent_001",
        kind="ForexPredictionModel",
        spec=IntentSpec(
            dataset="eurusd_hourly",
            instrument="EURUSD",
            prediction_target="volatility",
            retrain_frequency="weekly",
            evaluation_metric="sharpe_ratio",
        ),
    )

    plan = engine.plan(intent)

    assert plan["dataset"] == "eurusd_hourly"
    assert plan["feature_pipeline"] == ["realized_volatility", "rolling_std"]
    assert "plan_hash" in plan
    assert isinstance(plan["policy_trace"], list)
