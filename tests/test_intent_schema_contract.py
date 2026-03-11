import pytest

from planner.intent.schemas import SUPPORTED_SCHEMA_VERSION, IntentArtifact, IntentSpec


def test_intent_artifact_uses_supported_schema_version_by_default():
    artifact = IntentArtifact(
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

    assert artifact.schema_version == SUPPORTED_SCHEMA_VERSION


def test_intent_artifact_rejects_unsupported_schema_version():
    with pytest.raises(ValueError):
        IntentArtifact(
            intent_id="intent_001",
            schema_version="2.0.0",
            kind="ForexPredictionModel",
            spec=IntentSpec(
                dataset="eurusd_hourly",
                instrument="EURUSD",
                prediction_target="volatility",
                retrain_frequency="weekly",
                evaluation_metric="sharpe_ratio",
            ),
        )
