from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator

SUPPORTED_SCHEMA_VERSION = "1.0.0"


class IntentSpec(BaseModel):
    """Canonical user intent contract for plan generation."""

    model_config = ConfigDict(extra="forbid")

    dataset: str = Field(min_length=1)
    instrument: str = Field(min_length=3)
    prediction_target: Literal["volatility"]
    retrain_frequency: Literal["daily", "weekly", "monthly"]
    evaluation_metric: Literal["sharpe_ratio", "rmse", "mae"]
    required_features: list[str] = Field(default_factory=list)

    @field_validator("dataset", "instrument")
    @classmethod
    def validate_non_empty(cls, value: str) -> str:
        stripped = value.strip()
        if not stripped:
            raise ValueError("value must not be blank")
        return stripped

    @field_validator("required_features", mode="before")
    @classmethod
    def default_required_features(cls, value: list[str] | None) -> list[str]:
        if value is None:
            return []
        return value


class IntentArtifact(BaseModel):
    """Versioned and validated planning intent artifact."""

    model_config = ConfigDict(extra="forbid")

    intent_id: str = Field(min_length=1)
    schema_version: Literal[SUPPORTED_SCHEMA_VERSION] = SUPPORTED_SCHEMA_VERSION
    kind: Literal["ForexPredictionModel"]
    spec: IntentSpec

    @field_validator("intent_id")
    @classmethod
    def validate_intent_id(cls, value: str) -> str:
        stripped = value.strip()
        if not stripped:
            raise ValueError("intent_id must not be blank")
        return stripped
