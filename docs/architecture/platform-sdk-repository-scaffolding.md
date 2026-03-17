# Platform SDK Repository Scaffolding

## Purpose

`platform-sdk` is a **contract-only** repository. It owns shared schemas, protocol interfaces, type-safe client primitives, and compatibility metadata used by other repositories.

## Explicit Non-Goals

`platform-sdk` does **not** implement:

- runtime controllers,
- reconciliation loops,
- event-bus execution,
- planner algorithms,
- infrastructure adapters.

Those concerns are owned by `control-plane`, `intent-planner`, and `platform-adapters`.

## Repository Structure

```text
platform-sdk/
├── README.md
├── pyproject.toml
├── docs/
│   ├── contracts/
│   │   ├── intent-contract.md
│   │   ├── plan-contract.md
│   │   ├── capability-contract.md
│   │   └── execution-contract.md
│   └── compatibility/
│       └── compatibility-window-policy.md
├── schemas/
│   ├── intent.schema.json
│   ├── resolved-plan.schema.json
│   ├── capability.schema.json
│   ├── run-manifest.schema.json
│   └── error-envelope.schema.json
├── sdk/
│   ├── interfaces/
│   │   ├── planner_api.py
│   │   ├── control_plane_api.py
│   │   ├── adapter_registry_api.py
│   │   └── event_contracts.py
│   ├── versions/
│   │   └── contract_versions.py
│   └── validation/
│       ├── schema_validator.py
│       └── compatibility_validator.py
└── tests/
    ├── test_schema_compatibility.py
    └── test_version_semantics.py
```


## Legacy Module Mapping (Pre-Split -> Current Repositories)

The earlier single-repo `platform-sdk` architecture grouped contract and runtime modules
in one tree. After the split, some module names moved to different repositories.

| Legacy module name (old architecture) | Current owner repository | Current location / equivalent |
| --- | --- | --- |
| `artifact_identity` | `platform-sdk` | `schemas/` + `sdk/validation/schema_validator.py` + `sdk/versions/contract_versions.py` (identity rules + versioned contracts) |
| `canonical_json` | `platform-sdk` | schema/contract canonicalization rules in `docs/contracts/` and validation in `sdk/validation/` |
| `artifact_hashing` | `platform-sdk` | contract-level hashing/canonical artifact identity policy published by SDK contracts/schemas |
| `dependency_graph` (contract model) | `platform-sdk` | `resolved-plan.schema.json` and related plan/execution contracts |
| `drift_detection` | `control-plane` | `controllers/drift_controller.py` with liveness controls in `liveness/` |
| `controllers/*` | `control-plane` | `controllers/`, `reconciliation/`, and `execution/` |
| `planner` implementation | `intent-planner` | `intent-planner` repository (not `platform-sdk`) |
| `compiler` implementation | `intent-planner` / compiler repo boundary | outside `platform-sdk`; consumed as contracts by `control-plane` |
| `adapter` implementations | `platform-adapters` | adapter/provider runtime integrations |

### Quick answer to common gap reports

- **`artifact_identity` is not missing**; it is defined as a contract concern in `platform-sdk`
  (schemas, compatibility/version policy, and validation primitives).
- **`drift_detection` is not in `platform-sdk` by design**; it is runtime behavior owned by
  `control-plane` (`drift_controller.py` + bounded liveness mechanisms).

If a module is runtime/reconciliation behavior, it belongs outside `platform-sdk`.
If it is schema/contract/compatibility policy, it belongs in `platform-sdk`.

## Dependencies

Allowed imports:

- language/runtime standard libraries,
- schema and serialization libraries,
- generated protocol dependencies.

Forbidden imports:

- `control-plane` implementation modules,
- `intent-planner` implementation modules,
- `platform-adapters` implementation modules,
- infrastructure/cloud SDKs.

## Lifecycle Responsibilities

`platform-sdk` is the authoritative publisher for:

- contract version lifecycle (`introduced -> promoted -> deprecated -> removed`),
- compatibility windows and deprecation timelines,
- machine-readable change notices consumed by downstream repositories.

## Source Architecture References

- `docs/platform/architecture/platform_sdk_architecture.md`
- `docs/platform/architecture/repository_architecture.md`
- `docs/platform/architecture/control_plane_liveness_spec.md`
