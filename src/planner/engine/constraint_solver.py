from __future__ import annotations

from planner.intent.schemas import IntentArtifact


class ConstraintSolver:
    """Apply governance-driven constraints in deterministic order."""

    GOVERNANCE_FEATURES = {
        "volatility": ["realized_volatility", "rolling_std"],
    }

    def apply(
        self, intent: IntentArtifact, capabilities: dict
    ) -> tuple[IntentArtifact, list[dict[str, object]]]:
        policy_trace: list[dict[str, object]] = []

        required_by_policy = self.GOVERNANCE_FEATURES.get(
            intent.spec.prediction_target, []
        )
        policy_trace.append(
            {
                "rule": "governance.required_features",
                "target": intent.spec.prediction_target,
                "added": sorted(required_by_policy),
            }
        )

        constrained_features = sorted(
            set(intent.spec.required_features + required_by_policy)
        )

        constrained_intent = intent.model_copy(
            deep=True,
            update={
                "spec": intent.spec.model_copy(
                    update={"required_features": constrained_features}
                )
            },
        )

        policy_trace.append(
            {
                "rule": "capability.dataset_supported",
                "dataset": constrained_intent.spec.dataset,
                "result": constrained_intent.spec.dataset in capabilities["datasets"],
            }
        )

        return constrained_intent, policy_trace
