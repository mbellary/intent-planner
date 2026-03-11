from planner.intent.normalizer import IntentNormalizer
from planner.intent.schemas import IntentArtifact, IntentSpec


def test_intent_normalizer_returns_intent_unchanged():
    normalizer = IntentNormalizer()
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

    result = normalizer.normalize(intent)

    assert result == intent
