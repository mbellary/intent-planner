from dataclasses import dataclass


@dataclass
class PlannerConfig:
    environment: str = "development"
    log_level: str = "INFO"
