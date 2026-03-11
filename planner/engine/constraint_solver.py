class ConstraintSolver:

    def apply(self, intent, capabilities):

        # Example governance rule

        if intent.spec.prediction_target == "volatility":

            intent.spec.required_features = [
                "realized_volatility",
                "rolling_std"
            ]

        return intent
