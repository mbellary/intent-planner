from planner.intent.normalizer import IntentNormalizer
from planner.intent.schemas import IntentArtifact, IntentSpec


def test_intent_normalizer_canonicalizes_fields_and_features():
    normalizer = IntentNormalizer()
    intent = IntentArtifact(
        intent_id=" intent_001 ",
        kind="ForexPredictionModel",
        spec=IntentSpec(
            dataset=" EURUSD_Hourly ",
            instrument=" eurusd ",
            prediction_target="volatility",
            retrain_frequency="weekly",
            evaluation_metric="sharpe_ratio",
            required_features=["Rolling Std", "realized_volatility", "rolling std"],
        ),
    )

    result = normalizer.normalize(intent)

    assert result.intent_id == "intent_001"
    assert result.spec.dataset == "eurusd_hourly"
    assert result.spec.instrument == "EURUSD"
    assert result.spec.required_features == ["realized_volatility", "rolling_std"]
