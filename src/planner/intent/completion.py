from planner.intent.schemas import IntentArtifact


class IntentCompletion:
    """Fill deterministic defaults for partially specified intents."""

    DEFAULT_FEATURES_BY_TARGET = {
        "volatility": ["realized_volatility", "rolling_std"],
    }

    def complete(self, intent: IntentArtifact) -> IntentArtifact:
        baseline_features = self.DEFAULT_FEATURES_BY_TARGET.get(
            intent.spec.prediction_target, []
        )

        merged_features = sorted(set(intent.spec.required_features + baseline_features))

        return intent.model_copy(
            deep=True,
            update={
                "spec": intent.spec.model_copy(
                    update={"required_features": merged_features}
                )
            },
        )
