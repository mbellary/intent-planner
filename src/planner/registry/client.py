from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CapabilitySnapshot:
    datasets: tuple[str, ...]
    training_engines: tuple[str, ...]
    compute_engines: tuple[str, ...]


class CapabilityRegistryClient:
    """Deterministic registry client contract.

    Network calls are represented by local constants for this scaffold while keeping
    timeout/retry posture explicit in interface.
    """

    DEFAULT_TIMEOUT_SECONDS = 1.0
    DEFAULT_RETRIES = 2

    def __init__(
        self,
        timeout_seconds: float = DEFAULT_TIMEOUT_SECONDS,
        retries: int = DEFAULT_RETRIES,
    ):
        self.timeout_seconds = timeout_seconds
        self.retries = retries

    def get_snapshot(self) -> CapabilitySnapshot:
        datasets = tuple(sorted(["eurusd_hourly", "eurusd_daily"]))
        training_engines = tuple(sorted(["xgboost", "pytorch"]))
        compute_engines = tuple(sorted(["spark", "ray"]))
        return CapabilitySnapshot(
            datasets=datasets,
            training_engines=training_engines,
            compute_engines=compute_engines,
        )
