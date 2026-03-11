from __future__ import annotations

from planner.engine.errors import PlannerErrorDetail, PlanValidationError


class PlanValidator:
    REQUIRED_TOP_LEVEL_FIELDS = (
        "api_version",
        "intent_id",
        "dataset",
        "feature_pipeline",
        "training",
        "compute",
        "evaluation",
        "policy_trace",
        "provenance",
        "plan_hash",
    )

    def validate(self, plan: dict) -> bool:
        missing = [
            field for field in self.REQUIRED_TOP_LEVEL_FIELDS if field not in plan
        ]
        if missing:
            raise PlanValidationError(
                PlannerErrorDetail(
                    code="missing_required_fields",
                    message="Plan is missing required fields",
                    context={"missing": missing},
                )
            )

        if not isinstance(plan["feature_pipeline"], list):
            raise PlanValidationError(
                PlannerErrorDetail(
                    code="invalid_feature_pipeline",
                    message="feature_pipeline must be a list",
                    context={"actual_type": type(plan['feature_pipeline']).__name__},
                )
            )

        return True
