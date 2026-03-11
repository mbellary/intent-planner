from planner.intent.schemas import IntentArtifact


class ConstraintSolver:
    """Apply governance-driven constraints in deterministic order."""

    GOVERNANCE_FEATURES = {
        "volatility": ["realized_volatility", "rolling_std"],
    }

    def apply(self, intent: IntentArtifact, capabilities: dict) -> IntentArtifact:
        required_by_policy = self.GOVERNANCE_FEATURES.get(
            intent.spec.prediction_target, []
        )

        constrained_features = sorted(
            set(intent.spec.required_features + required_by_policy)
        )

        return intent.model_copy(
            deep=True,
            update={
                "spec": intent.spec.model_copy(
                    update={"required_features": constrained_features}
                )
            },
        )
