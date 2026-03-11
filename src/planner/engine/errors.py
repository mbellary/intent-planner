from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class PlannerErrorDetail:
    code: str
    message: str
    context: dict[str, Any]


class PlannerError(Exception):
    """Base typed planner error with machine-readable detail."""

    def __init__(self, detail: PlannerErrorDetail):
        self.detail = detail
        super().__init__(detail.message)


class CapabilityResolutionError(PlannerError):
    pass


class PlanValidationError(PlannerError):
    pass
