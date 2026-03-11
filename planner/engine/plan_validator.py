class PlanValidator:

    def validate(self, plan):

        if "dataset" not in plan:
            raise ValueError("dataset missing")

        if "training" not in plan:
            raise ValueError("training config missing")

        return True
