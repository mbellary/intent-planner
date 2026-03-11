from pydantic import BaseModel, Field


class IntentSpec(BaseModel):

    dataset: str

    instrument: str

    prediction_target: str

    retrain_frequency: str

    evaluation_metric: str

    required_features: list[str] = Field(default_factory=list)


class IntentArtifact(BaseModel):

    intent_id: str

    kind: str

    spec: IntentSpec
