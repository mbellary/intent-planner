from planner.artifacts.hashing import compute_hash


class PlanGenerator:

    def generate(self, intent, capabilities):

        plan = {

            "dataset": intent.spec.dataset,

            "feature_pipeline": intent.spec.required_features,

            "training": {
                "engine": "xgboost"
            },

            "compute": {
                "engine": "spark"
            },

            "evaluation": {
                "metric": intent.spec.evaluation_metric
            }
        }

        plan["plan_hash"] = compute_hash(plan)

        return plan
