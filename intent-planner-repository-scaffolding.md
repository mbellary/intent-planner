Below is a **production-grade scaffold for the `intent-planner` repository**, aligned with the architecture we defined:

* Intent Planning Engine (merged **Intent Compiler + Planner Engine**)
* Deterministic planning
* Capability Registry integration
* Governance validation
* Plan generation
* Plan hashing
* Artifact emission

The goal of this repository is to implement:

```text
Human Intent → Deterministic Resolved Plan
```

This repository **does not execute workloads**.
It only **interprets intent and generates plans**.

Ownership boundaries:

* `intent-planner` owns `planner/` and planner-facing APIs.
* Runtime controllers and runtime APIs are owned by `control-plane`.
* Kernel contracts and deterministic primitives are owned by `platform-sdk`.

---

# intent-planner Repository

```text
intent-planner/
│
├── README.md
├── pyproject.toml
├── Makefile
├── Dockerfile
├── .env.example
│
├── planner/
│   ├── __init__.py
│   │
│   ├── api/
│   │   ├── app.py
│   │   ├── routes.py
│   │   └── dependencies.py
│   │
│   ├── engine/
│   │   ├── planner_engine.py
│   │   ├── constraint_solver.py
│   │   ├── capability_resolver.py
│   │   ├── plan_generator.py
│   │   └── plan_validator.py
│   │
│   ├── intent/
│   │   ├── extractor.py
│   │   ├── normalizer.py
│   │   ├── completion.py
│   │   ├── clarification.py
│   │   └── schemas.py
│   │
│   ├── registry/
│   │   ├── client.py
│   │   └── capability_graph.py
│   │
│   ├── artifacts/
│   │   ├── hashing.py
│   │   ├── artifact_models.py
│   │   └── serializer.py
│   │
│   ├── policies/
│   │   ├── governance_rules.py
│   │   └── policy_engine.py
│   │
│   ├── templates/
│   │   └── forex_model_template.yaml
│   │
│   ├── utils/
│   │   ├── logging.py
│   │   └── config.py
│   │
│   └── tests/
│       ├── test_planner_engine.py
│       ├── test_intent_normalization.py
│       └── test_plan_generation.py
│
└── examples/
    └── forex_intent.yaml
```

---

# 1️⃣ pyproject.toml

```toml
[project]
name = "intent-planner"
version = "0.1.0"
description = "Intent Planning Engine for Deterministic AI Governance Platform"
requires-python = ">=3.10"

dependencies = [
    "fastapi",
    "pydantic",
    "uvicorn",
    "pyyaml",
    "networkx",
    "httpx"
]

[tool.black]
line-length = 88
```

---

# 2️⃣ planner/api/app.py

```python
from fastapi import FastAPI
from planner.api.routes import router

app = FastAPI(
    title="Intent Planner",
    version="1.0.0"
)

app.include_router(router)
```

---

# 3️⃣ planner/api/routes.py

```python
from fastapi import APIRouter
from planner.engine.planner_engine import PlannerEngine
from planner.artifacts.artifact_models import IntentArtifact

router = APIRouter()
engine = PlannerEngine()


@router.post("/plan")
async def generate_plan(intent: IntentArtifact):
    plan = engine.plan(intent)
    return plan
```

---

# 4️⃣ planner/engine/planner_engine.py

```python
from planner.intent.normalizer import IntentNormalizer
from planner.intent.completion import IntentCompletion
from planner.engine.capability_resolver import CapabilityResolver
from planner.engine.constraint_solver import ConstraintSolver
from planner.engine.plan_generator import PlanGenerator
from planner.engine.plan_validator import PlanValidator


class PlannerEngine:

    def __init__(self):

        self.normalizer = IntentNormalizer()
        self.completion = IntentCompletion()
        self.capability_resolver = CapabilityResolver()
        self.constraint_solver = ConstraintSolver()
        self.generator = PlanGenerator()
        self.validator = PlanValidator()

    def plan(self, intent):

        intent = self.normalizer.normalize(intent)

        intent = self.completion.complete(intent)

        capabilities = self.capability_resolver.resolve(intent)

        constrained_intent = self.constraint_solver.apply(intent, capabilities)

        plan = self.generator.generate(constrained_intent, capabilities)

        self.validator.validate(plan)

        return plan
```

---

# 5️⃣ planner/engine/capability_resolver.py

```python
from planner.registry.client import CapabilityRegistryClient


class CapabilityResolver:

    def __init__(self):
        self.registry = CapabilityRegistryClient()

    def resolve(self, intent):

        datasets = self.registry.get_datasets()

        engines = self.registry.get_training_engines()

        compute = self.registry.get_compute_engines()

        return {
            "datasets": datasets,
            "training_engines": engines,
            "compute": compute
        }
```

---

# 6️⃣ planner/engine/constraint_solver.py

```python
class ConstraintSolver:

    def apply(self, intent, capabilities):

        # Example governance rule

        if intent.spec.prediction_target == "volatility":

            intent.spec.required_features = [
                "realized_volatility",
                "rolling_std"
            ]

        return intent
```

---

# 7️⃣ planner/engine/plan_generator.py

```python
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
```

---

# 8️⃣ planner/engine/plan_validator.py

```python
class PlanValidator:

    def validate(self, plan):

        if "dataset" not in plan:
            raise ValueError("dataset missing")

        if "training" not in plan:
            raise ValueError("training config missing")

        return True
```

---

# 9️⃣ planner/intent/schemas.py

```python
from pydantic import BaseModel


class IntentSpec(BaseModel):

    dataset: str

    instrument: str

    prediction_target: str

    retrain_frequency: str

    evaluation_metric: str


class IntentArtifact(BaseModel):

    intent_id: str

    kind: str

    spec: IntentSpec
```

---

# 🔟 planner/artifacts/hashing.py

```python
import hashlib
import json


def compute_hash(data):

    canonical = json.dumps(data, sort_keys=True)

    return hashlib.sha256(canonical.encode()).hexdigest()
```

---

# 11️⃣ planner/registry/client.py

Example registry client.

```python
class CapabilityRegistryClient:

    def get_datasets(self):

        return [
            "eurusd_hourly",
            "eurusd_daily"
        ]

    def get_training_engines(self):

        return [
            "xgboost",
            "pytorch"
        ]

    def get_compute_engines(self):

        return [
            "spark",
            "ray"
        ]
```

---

# 12️⃣ examples/forex_intent.yaml

```yaml
intent_id: intent_001

kind: ForexPredictionModel

spec:

  dataset: eurusd_hourly

  instrument: EURUSD

  prediction_target: volatility

  retrain_frequency: weekly

  evaluation_metric: sharpe_ratio
```

---

# 13️⃣ Example Execution

Call planner:

```bash
curl -X POST http://localhost:8000/plan \
-H "Content-Type: application/json" \
-d @examples/forex_intent.yaml
```

Output:

```json
{
  "dataset": "eurusd_hourly",
  "feature_pipeline": [
    "realized_volatility",
    "rolling_std"
  ],
  "training": {
    "engine": "xgboost"
  },
  "compute": {
    "engine": "spark"
  },
  "evaluation": {
    "metric": "sharpe_ratio"
  },
  "plan_hash": "ab123..."
}
```

---

# 14️⃣ Responsibilities of intent-planner

The repository is responsible for:

```text
Intent normalization
Capability discovery
Constraint solving
Plan generation
Plan validation
Deterministic hashing
```

It is **NOT responsible for execution**.

Execution happens in:

```text
platform-sdk
execution runtime
```

---

# 15️⃣ How This Fits the Full Platform

```text
User
 ↓
User Interaction Layer
 ↓
intent-planner
 ↓
Compiler
 ↓
Platform SDK
 ↓
Execution Runtime
```

---

If you'd like, I can also provide a **much more advanced production implementation** next — the **real enterprise version** of this repository including:

* **LLM-driven intent extraction**
* **capability graph solver**
* **policy engine**
* **deterministic planning algorithm**
* **plan optimization**
* **plan diffing**
