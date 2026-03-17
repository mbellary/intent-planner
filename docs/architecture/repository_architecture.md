# Repository Architecture

## Purpose

Defines repository boundaries, one-way dependencies, and cross-repository lifecycle ownership for the platform.

## Canonical Topology

1. `platform-sdk` — shared contracts, schemas, and compatibility policy.
2. `intent-planner` — intent resolution and plan generation.
3. `control-plane` — runtime orchestration and bounded reconciliation.
4. `platform-adapters` — provider/infrastructure adapter implementations.
5. `domain-services` — domain intents, policy overlays, service composition.
6. `platform-cli` — user/operator command interface.
7. `platform-ops` — deployment, observability, release, and incident operations.

## Platform-SDK vs Control-Plane Module Allocation

The platform is intentionally split so `platform-sdk` remains **contract-only** while
`control-plane` owns **runtime orchestration**. The following module map is the
minimum baseline expected in repository-level architecture docs and scaffolding.

### `platform-sdk` (contract, schema, compatibility, and client primitives)

- `docs/contracts/`
  - `intent-contract.md`
  - `plan-contract.md`
  - `capability-contract.md`
  - `execution-contract.md`
- `docs/compatibility/`
  - `compatibility-window-policy.md`
- `schemas/`
  - `intent.schema.json`
  - `resolved-plan.schema.json`
  - `capability.schema.json`
  - `run-manifest.schema.json`
  - `error-envelope.schema.json`
- `sdk/interfaces/`
  - `planner_api.py`
  - `control_plane_api.py`
  - `adapter_registry_api.py`
  - `event_contracts.py`
- `sdk/versions/`
  - `contract_versions.py`
- `sdk/validation/`
  - `schema_validator.py`
  - `compatibility_validator.py`
- `tests/`
  - `test_schema_compatibility.py`
  - `test_version_semantics.py`

### `control-plane` (runtime reconciliation and liveness-bounded execution)

- `api/`
  - `control_plane_server.py`
  - `intent_submission_api.py`
  - `status_query_api.py`
- `controllers/`
  - `intent_controller.py`
  - `plan_controller.py`
  - `drift_controller.py`
- `reconciliation/`
  - `reconciliation_engine.py`
  - `desired_state_builder.py`
  - `actual_state_collector.py`
- `execution/`
  - `action_dispatcher.py`
  - `adapter_coordinator.py`
  - `rollback_orchestrator.py`
- `events/`
  - `event_router.py`
  - `event_store.py`
  - `event_handlers.py`
- `liveness/`
  - `retry_budget_manager.py`
  - `watchdog_supervisor.py`
  - `circuit_breaker.py`
  - `dead_letter_queue_handler.py`
  - `compensation_dispatcher.py`
  - `convergence_incident_controller.py`
- `incidents/`
  - `incident_model.py`
  - `escalation_policy.py`
- `compliance/`
  - `liveness_obligation_map.md`
  - `controller_timeout_matrix.yaml`
- `tests/`
  - `test_retry_budget.py`
  - `test_watchdog_timeouts.py`
  - `test_dead_letter_path.py`
  - `test_convergence_blocked_event.py`
  - `test_circuit_breaker_behavior.py`

## Explicit Non-Ownership Clarification

To avoid accidental architecture drift after the repository split:

- `platform-sdk` MUST NOT own runtime controllers, reconciliation loops, or
  adapter execution dispatch.
- `platform-sdk` MUST NOT implement planner algorithms or compiler pipelines.
- `control-plane` MUST consume `platform-sdk` contracts and compatibility policy
  as read-only inputs.
- Planner internals remain in `intent-planner`; provider implementations remain
  in `platform-adapters`.

If any of these modules appear in the wrong repository architecture document,
the document is non-compliant and must be corrected before implementation.

## Dependency Rules

- Dependencies are contract-first and one-way.
- `platform-sdk` has no dependency on platform repo internals.
- `control-plane` consumes contracts and APIs but remains the only runtime controller implementation owner.
- Direct circular repository dependencies are forbidden.

## Cross-Repository Lifecycle State Machines

### 1) Adapter Capability Lifecycle

`registered -> compatible -> deprecated -> retired`

- Authoritative owner: `platform-adapters`.
- Compatibility validation consumer: `control-plane`.
- Contract publication consumer: `platform-sdk`.
- Incident bridge consumer: `platform-ops`.

### 2) Contract Version Lifecycle

`introduced -> promoted -> deprecated -> removed`

- Authoritative owner: `platform-sdk`.
- Promotion gate inputs: `intent-planner`, `control-plane`, `platform-adapters`, `platform-cli` compatibility reports.
- Policy: each deprecation must include a declared compatibility window before removal.

### 3) Runtime Incident Lifecycle

`detected -> triaged -> mitigated -> resolved -> closed`

- Detection emitter: `control-plane` (liveness and convergence events).
- Triage/mitigation owner: `platform-ops`.
- Status exposure: `platform-cli`.

## Required Governance Artifacts

- `docs/platform/standards/repo-structure-manifest.schema.json`
- `docs/platform/templates/repo-structure-manifest-template.yaml`
- `docs/platform/cross-category/repo-ownership-matrix.yaml`
- `docs/platform/standards/repo-ownership-matrix.schema.json`
