from planner.engine.plan_generator import PlanGenerator
from planner.intent.schemas import IntentArtifact, IntentSpec


def test_plan_generation_includes_hash_and_metric():
    generator = PlanGenerator()
    intent = IntentArtifact(
        intent_id="intent_001",
        kind="ForexPredictionModel",
        spec=IntentSpec(
            dataset="eurusd_hourly",
            instrument="EURUSD",
            prediction_target="volatility",
            retrain_frequency="weekly",
            evaluation_metric="sharpe_ratio",
            required_features=["realized_volatility", "rolling_std"],
        ),
    )

    plan = generator.generate(intent, capabilities={})

    assert plan["evaluation"]["metric"] == "sharpe_ratio"
    assert len(plan["plan_hash"]) == 64
