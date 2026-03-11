import pytest

from planner.engine.capability_resolver import CapabilityResolver
from planner.engine.errors import CapabilityResolutionError
from planner.intent.schemas import IntentArtifact, IntentSpec


def test_capability_resolver_rejects_unknown_dataset():
    resolver = CapabilityResolver()
    intent = IntentArtifact(
        intent_id="intent_001",
        kind="ForexPredictionModel",
        spec=IntentSpec(
            dataset="unknown",
            instrument="EURUSD",
            prediction_target="volatility",
            retrain_frequency="weekly",
            evaluation_metric="sharpe_ratio",
        ),
    )

    with pytest.raises(CapabilityResolutionError):
        resolver.resolve(intent)
