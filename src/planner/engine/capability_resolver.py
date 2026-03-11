from __future__ import annotations

from planner.engine.errors import CapabilityResolutionError, PlannerErrorDetail
from planner.intent.schemas import IntentArtifact
from planner.registry.client import CapabilityRegistryClient


class CapabilityResolver:
    def __init__(self, registry: CapabilityRegistryClient | None = None):
        self.registry = registry or CapabilityRegistryClient()

    def resolve(self, intent: IntentArtifact) -> dict[str, list[str]]:
        snapshot = self.registry.get_snapshot()
        if intent.spec.dataset not in snapshot.datasets:
            raise CapabilityResolutionError(
                PlannerErrorDetail(
                    code="dataset_not_available",
                    message="Requested dataset is not available in capability registry",
                    context={
                        "dataset": intent.spec.dataset,
                        "available": list(snapshot.datasets),
                    },
                )
            )

        return {
            "datasets": list(snapshot.datasets),
            "training_engines": list(snapshot.training_engines),
            "compute": list(snapshot.compute_engines),
        }
