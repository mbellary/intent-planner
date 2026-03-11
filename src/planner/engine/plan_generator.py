from __future__ import annotations

from planner.artifacts.hashing import compute_hash
from planner.intent.schemas import IntentArtifact


class PlanGenerator:
    def generate(
        self,
        intent: IntentArtifact,
        capabilities: dict[str, list[str]],
        policy_trace: list[dict[str, object]],
    ) -> dict:
        training_engine = sorted(capabilities["training_engines"])[0]
        compute_engine = sorted(capabilities["compute"])[0]

        plan = {
            "api_version": "v1",
            "intent_id": intent.intent_id,
            "dataset": intent.spec.dataset,
            "feature_pipeline": sorted(intent.spec.required_features),
            "training": {
                "engine": training_engine,
                "retrain_frequency": intent.spec.retrain_frequency,
            },
            "compute": {
                "engine": compute_engine,
            },
            "evaluation": {
                "metric": intent.spec.evaluation_metric,
            },
            "policy_trace": policy_trace,
            "provenance": {
                "schema_version": intent.schema_version,
                "kind": intent.kind,
            },
        }

        plan["plan_hash"] = compute_hash(plan)
        return plan
