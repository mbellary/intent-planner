from planner.intent.schemas import IntentArtifact


class IntentNormalizer:
    """Apply deterministic canonicalization to incoming intents."""

    @staticmethod
    def _normalize_feature_name(feature: str) -> str:
        normalized = "_".join(feature.strip().lower().split())
        return normalized

    def normalize(self, intent: IntentArtifact) -> IntentArtifact:
        normalized_features = sorted(
            {
                self._normalize_feature_name(feature)
                for feature in intent.spec.required_features
                if feature and feature.strip()
            }
        )

        return intent.model_copy(
            deep=True,
            update={
                "intent_id": intent.intent_id.strip(),
                "spec": intent.spec.model_copy(
                    update={
                        "dataset": intent.spec.dataset.strip().lower(),
                        "instrument": intent.spec.instrument.strip().upper(),
                        "required_features": normalized_features,
                    }
                ),
            },
        )
