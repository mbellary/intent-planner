Below is a **fully merged, production-grade `intent_planner_architecture.md`**.
This is **not an MVP doc**—it is written as a **long-lived system spec** with strict boundaries, no ambiguity, and no handwaving.

---

# `intent_planner_architecture.md`

## 1. Purpose, Scope and Rules

### 1.1 Purpose

The **Intent-Planner** is a deterministic, auditable subsystem responsible for transforming **user intent** into a **fully resolved, executable plan** under strict governance constraints.

It acts as the **compiler layer of the platform**, converting human intent into infrastructure-aligned execution plans.

---

### 1.2 Scope

Intent-Planner owns:

* Request ingestion for planning workflows
* Conversation and clarification handling (planning context only)
* Intent extraction and normalization
* Intent Language (IL) generation and validation
* Deterministic planning using capabilities and policies
* Plan generation and validation
* Plan explainability and diagnostics
* Artifact lineage and identity for planning outputs

---

### 1.3 Non-Scope

Intent-Planner does **NOT** own:

* Runtime execution
* Controllers or reconciliation loops
* Infrastructure provisioning
* Execution adapters
* Event orchestration

These belong to:

* **Control Plane** (execution)
* **Platform SDK** (contracts)
* **Adapters / Domain Services** (implementation)

### 1.4 Non-negotiable rules

#### Rule 1

`domain/` may define **business invariants**, but never canonical schema structure.

#### Rule 2

`intent_language/validation/` may define:

* semantic validation
* compatibility guards
* business completeness checks

It may not define canonical schema validation logic.

#### Rule 3

`planning/packaging/` may assemble identity inputs, but may not compute final identity rules independently.

#### Rule 4

Any file with names like:

* `schema`
* `canonicalization_rules`
* `hash_builder`
* `identity_rules`

should be treated as suspicious unless it is clearly an SDK adapter.

#### Rule 5

All contract compatibility CI must validate against SDK, not local copies.

---

## 2. Architectural Principles

### 2.1 Determinism

For a given input:

```text
ResolvedPlan = f(IntentLanguage, CapabilitySnapshot, PolicyBundle, PlannerVersion)
```

Must satisfy:

* Same inputs → identical output (bitwise)
* No runtime randomness
* No LLM involvement in planning

---

### 2.2 Separation of Concerns

Intent-Planner enforces **three hard internal phases**:

1. **Interpretation (non-deterministic allowed)**
2. **Formalization (Intent Language)**
3. **Planning (strictly deterministic)**

---

### 2.3 Intent Language as Boundary

> **Intent Language (IL) is the ONLY valid input to the planner.**

* Natural language is never used directly in planning
* LLM outputs are treated as **proposals**, not truth
* IL is the **canonical, typed, validated representation**

---

### 2.4 Policy Supremacy

* Users cannot override infrastructure decisions
* All plans must satisfy policy constraints
* Policy evaluation is mandatory and blocking

---

### 2.5 Snapshot-Based Planning

Planning uses:

* **Capability Snapshot (versioned)**
* **Policy Bundle (versioned)**

Never live mutable state.

---

### 2.6 Full Auditability

Every plan must trace back to:

* Intent fields
* Policy rules
* Capability sources
* Template selections

---

## 3. System Positioning

```text
User / API / CLI
   ↓
Intent-Planner
   ↓
Control Plane
   ↓
Execution Layer
```

---

## 4. External Dependencies

### 4.1 Platform SDK (REQUIRED)

Provides:

* Canonical schemas
* Validation rules
* Hashing/canonicalization policy
* Contract definitions

**Intent-Planner MUST NOT redefine these.**

> **Intent-Planner MUST NOT redefine canonical schemas, validation rules, hashing/canonicalization policy, or contract definitions from Platform SDK.**

It is now acting as a **strict consumer of SDK contracts** rather than a co-owner.

---

### 4.2 Capability Registry

Consumed as:

* Versioned snapshots only
* Immutable within planning lifecycle

---

### 4.3 Policy System

Provides:

* Governance rules
* Constraints
* Defaults
* Tenant overlays

---

### 4.4 Artifact Registry

Stores:

* IL artifacts
* Resolved plans
* Lineage graphs

---

## 5. Internal Subsystems

### 5.1 Request & Interaction Subsystem

Handles:

* Request ingestion
* Authentication context
* Idempotency
* Conversation state

---

### 5.2 Intent Interpretation Subsystem

Handles:

* Extraction
* Schema mapping
* Normalization
* Completion
* Clarification loop
* Validation

---

### 5.3 Intent Language Subsystem

Handles:

* IL construction
* Canonicalization
* Validation
* Versioning

---

### 5.4 Planning Subsystem

Handles:

* Capability resolution
* Policy evaluation
* Constraint solving
* Plan generation
* Dependency graph construction
* Plan validation

---

### 5.5 Diagnostics & Explainability Subsystem

Handles:

* Decision tracing
* Policy explanations
* Warning generation
* Failure mapping

---

### 5.6 Artifact & Lineage Subsystem

Handles:

* Artifact persistence
* Hashing
* Lineage tracking
* Registration

---

### 5.7 External Interface Subsystem

Provides:

* Planning API
* Validation API
* Explanation API
* Approval API

---

## 6. End-to-End Lifecycle

```text
Request
 → Ingestion
 → Conversation Resolution
 → Intent Extraction
 → Schema Mapping
 → Normalization
 → Completion
 → Clarification
 → Validation
 → Intent Language Generation
 → IL Canonicalization
 → IL Validation
 → Capability Snapshot Load
 → Policy Bundle Load
 → Planning Intent Normalization
 → Constraint Evaluation
 → Template Selection
 → Candidate Plan Generation
 → Dependency Resolution
 → Plan Validation
 → Plan Canonicalization
 → Hashing
 → Summary Generation
 → Artifact Registration
 → Output
```

---

## 7. Artifact Model

### 7.1 Request Artifact

* request_id
* actor / tenant
* raw_input
* timestamp
* correlation_ids

---

### 7.2 Conversation Artifact

* conversation_id
* message history
* clarification state
* resolved parameters

---

### 7.3 Draft Intent Artifact

* partially structured intent
* unresolved fields

---

### 7.4 Intent Language Artifact (CRITICAL)

Must be:

* typed
* schema-compliant
* canonicalizable
* versioned
* hashable

---

### 7.5 Capability Snapshot Artifact

* datasets
* compute engines
* frameworks
* adapters
* versions

---

### 7.6 Policy Bundle Artifact

* governance rules
* security constraints
* tenant overlays

---

### 7.7 Resolved Plan Artifact

The primary output.

Contains:

* intent_projection
* task_plan
* compute_plan
* cloud_plan
* operators_plan
* analysis_plan
* observability_plan
* explainability_plan
* compiler_directives
* dependency_graph
* lineage
* diagnostics
* summary

---

### 7.8 Plan Summary Artifact

Human-readable explanation.

---

### 7.9 Diagnostics Artifact

* warnings
* rejected options
* policy decisions
* reasoning traces

---

## 8. Intent Language Specification Role

IL ensures:

* elimination of ambiguity
* enforcement of schema
* deterministic planning input

### Properties

* strongly typed
* declarative
* domain-aware
* extensible via versioning

---

## 9. Deterministic Planning Model

### Inputs

* IL
* Capability Snapshot
* Policy Bundle

### Steps

1. Normalize intent for planning
2. Apply defaults
3. Apply constraints
4. Select templates
5. Generate candidate plans
6. Resolve dependencies
7. Validate plan
8. Canonicalize output

---

## 10. Capability Snapshot Model

### Requirements

* Immutable
* Versioned
* Fully self-contained

### Includes

* data sources
* compute engines
* execution frameworks
* adapters

---

## 11. Policy Evaluation Model

Policy enforces:

* security constraints
* compliance rules
* resource limits
* architecture standards

### Enforcement Points

* IL validation
* constraint evaluation
* plan validation

---

## 12. Resolved Plan Package Model

A structured output containing:

* logical execution steps
* infrastructure mapping
* dependency graph
* execution directives

---

## 13. Human Review Model

Three modes:

### 13.1 Auto-Approve

Low-risk plans

### 13.2 Review Required

High-cost or sensitive plans

### 13.3 Clarification Required

Incomplete or ambiguous intent

---

## 14. Diagnostics & Explainability

Each plan must answer:

* Why this compute?
* Why this dataset?
* Why this pipeline?
* Why not alternatives?

---

## 15. Security & Multi-Tenancy

* strict tenant isolation
* policy overlays per tenant
* no user-driven infra injection
* validated input boundaries

---

## 16. Performance & Scalability

* low latency planning (bounded)
* horizontal scaling
* caching of snapshots
* stateless planning core

---

## 17. Failure Taxonomy

### Categories

* ingestion failure
* auth failure
* incomplete intent
* IL violation
* capability mismatch
* policy violation
* dependency resolution failure
* plan validation failure
* artifact persistence failure

Each failure must include:

* error code
* explanation
* remediation hint

---

## 18. Repository Structure

```text
intent-planner/
├── README.md
├── pyproject.toml
├── poetry.lock
├── Makefile
├── .env.example
├── .gitignore
├── .editorconfig
├── .pre-commit-config.yaml
├── mypy.ini
├── pytest.ini
├── coverage.ini
├── ruff.toml
│
├── docker/
│   ├── Dockerfile
│   ├── Dockerfile.dev
│   └── entrypoint.sh
│
├── deploy/
│   ├── helm/
│   │   └── intent-planner/
│   ├── k8s/
│   │   ├── deployment.yaml
│   │   ├── service.yaml
│   │   ├── configmap.yaml
│   │   ├── secret.template.yaml
│   │   ├── hpa.yaml
│   │   └── networkpolicy.yaml
│   └── terraform/
│       ├── main.tf
│       ├── variables.tf
│       ├── outputs.tf
│       └── modules/
│
├── docs/
│   ├── architecture/
│   │   ├── intent_planner_architecture.md
│   │   ├── system_context.md
│   │   ├── execution_boundaries.md
│   │   ├── artifact_model.md
│   │   ├── lifecycle.md
│   │   ├── repository_structure.md
│   │   └── sequence_diagrams.md
│   ├── adr/
│   │   ├── ADR-001-intent-language-boundary.md
│   │   ├── ADR-002-resolved-plan-contract-consumption.md
│   │   ├── ADR-003-capability-snapshot-planning.md
│   │   ├── ADR-004-policy-evaluation-stages.md
│   │   ├── ADR-005-human-review-gate.md
│   │   ├── ADR-006-sdk-owned-hashing-and-canonicalization.md
│   │   └── ADR-007-no-runtime-execution-in-planner.md
│   ├── operations/
│   │   ├── runbook.md
│   │   ├── oncall.md
│   │   ├── slos.md
│   │   ├── alerting.md
│   │   └── disaster_recovery.md
│   ├── security/
│   │   ├── threat_model.md
│   │   ├── tenant_isolation.md
│   │   ├── authz_model.md
│   │   └── data_classification.md
│   └── testing/
│       ├── determinism_strategy.md
│       ├── golden_tests.md
│       ├── contract_tests.md
│       └── fixture_strategy.md
│
├── scripts/
│   ├── bootstrap.sh
│   ├── run_local.sh
│   ├── lint.sh
│   ├── test.sh
│   ├── generate_openapi.py
│   ├── generate_mermaid.py
│   ├── backfill_artifacts.py
│   └── replay_plans.py
│
├── config/
│   ├── base.yaml
│   ├── local.yaml
│   ├── dev.yaml
│   ├── staging.yaml
│   ├── prod.yaml
│   ├── logging.yaml
│   ├── templates.yaml
│   ├── review_gates.yaml
│   └── feature_flags.yaml
│
├── templates/
│   ├── quant/
│   │   ├── forecasting/
│   │   ├── training/
│   │   └── evaluation/
│   ├── compute/
│   │   ├── batch/
│   │   ├── streaming/
│   │   └── on_demand/
│   ├── cloud/
│   │   ├── aws/
│   │   ├── local/
│   │   └── hybrid/
│   ├── observability/
│   ├── explainability/
│   ├── operators/
│   └── task/
│
├── src/
│   └── intent_planner/
│       ├── __init__.py
│       │
│       ├── bootstrap/
│       │   ├── container.py
│       │   ├── settings.py
│       │   ├── dependency_graph.py
│       │   ├── feature_flags.py
│       │   └── startup_checks.py
│       │
│       ├── shared/
│       │   ├── enums.py
│       │   ├── constants.py
│       │   ├── clock.py
│       │   ├── ids.py
│       │   ├── canonical_representation.py
│       │   ├── pagination.py
│       │   ├── types.py
│       │   └── versioning.py
│       │
│       ├── api/
│       │   ├── __init__.py
│       │   ├── app.py
│       │   ├── dependencies.py
│       │   ├── middleware/
│       │   │   ├── auth.py
│       │   │   ├── logging.py
│       │   │   ├── tracing.py
│       │   │   ├── idempotency.py
│       │   │   ├── tenant_context.py
│       │   │   ├── request_limits.py
│       │   │   └── exception_mapping.py
│       │   ├── routes/
│       │   │   ├── health.py
│       │   │   ├── readiness.py
│       │   │   ├── planning.py
│       │   │   ├── validation.py
│       │   │   ├── explanation.py
│       │   │   ├── approvals.py
│       │   │   ├── artifacts.py
│       │   │   ├── clarification.py
│       │   │   └── admin.py
│       │   ├── request_models/
│       │   │   ├── planning_requests.py
│       │   │   ├── validation_requests.py
│       │   │   ├── explanation_requests.py
│       │   │   └── approval_requests.py
│       │   └── response_models/
│       │       ├── planning_responses.py
│       │       ├── validation_responses.py
│       │       ├── explanation_responses.py
│       │       ├── approval_responses.py
│       │       └── error_responses.py
│       │
│       ├── application/
│       │   ├── commands/
│       │   │   ├── create_plan.py
│       │   │   ├── validate_intent_language.py
│       │   │   ├── explain_plan.py
│       │   │   ├── request_approval.py
│       │   │   ├── approve_plan.py
│       │   │   ├── reject_plan.py
│       │   │   └── replay_plan.py
│       │   ├── queries/
│       │   │   ├── get_plan.py
│       │   │   ├── get_plan_summary.py
│       │   │   ├── get_diagnostics.py
│       │   │   ├── get_artifact_lineage.py
│       │   │   └── get_review_state.py
│       │   ├── services/
│       │   │   ├── planning_service.py
│       │   │   ├── validation_service.py
│       │   │   ├── explanation_service.py
│       │   │   ├── approval_service.py
│       │   │   ├── diagnostics_service.py
│       │   │   ├── artifact_service.py
│       │   │   └── lineage_service.py
│       │   ├── orchestration/
│       │   │   ├── planning_workflow.py
│       │   │   ├── clarification_workflow.py
│       │   │   ├── approval_workflow.py
│       │   │   └── replay_workflow.py
│       │   └── ports/
│       │       ├── sdk_contracts_port.py
│       │       ├── capability_snapshot_port.py
│       │       ├── policy_bundle_port.py
│       │       ├── artifact_store_port.py
│       │       ├── review_store_port.py
│       │       ├── conversation_store_port.py
│       │       └── template_registry_port.py
│       │
│       ├── domain/
│       │   ├── requests/
│       │   │   ├── entities.py
│       │   │   ├── value_objects.py
│       │   │   └── invariants.py
│       │   ├── conversations/
│       │   │   ├── entities.py
│       │   │   ├── value_objects.py
│       │   │   ├── policies.py
│       │   │   └── services.py
│       │   ├── intent_draft/
│       │   │   ├── entities.py
│       │   │   ├── value_objects.py
│       │   │   └── invariants.py
│       │   ├── intent_language/
│       │   │   ├── adapters.py
│       │   │   ├── invariants.py
│       │   │   └── business_rules.py
│       │   ├── capabilities/
│       │   │   ├── entities.py
│       │   │   ├── value_objects.py
│       │   │   └── selection_rules.py
│       │   ├── policies/
│       │   │   ├── entities.py
│       │   │   ├── value_objects.py
│       │   │   ├── evaluation_results.py
│       │   │   └── rule_types.py
│       │   ├── plans/
│       │   │   ├── adapters.py
│       │   │   ├── invariants.py
│       │   │   ├── dependency_graph_rules.py
│       │   │   ├── compiler_directive_rules.py
│       │   │   └── summary_rules.py
│       │   ├── diagnostics/
│       │   │   ├── entities.py
│       │   │   ├── warnings.py
│       │   │   ├── decision_trace.py
│       │   │   └── failure_taxonomy.py
│       │   └── artifacts/
│       │       ├── entities.py
│       │       ├── manifests.py
│       │       ├── lineage.py
│       │       └── provenance_rules.py
│       │
│       ├── ingestion/
│       │   ├── request_ingestor.py
│       │   ├── request_classifier.py
│       │   ├── auth_context_resolver.py
│       │   ├── tenant_context_resolver.py
│       │   ├── idempotency_key_resolver.py
│       │   ├── correlation_context.py
│       │   └── payload_sanitizer.py
│       │
│       ├── conversation/
│       │   ├── session_manager.py
│       │   ├── conversation_manager.py
│       │   ├── context_assembler.py
│       │   ├── clarification_state_machine.py
│       │   ├── turn_resolution.py
│       │   └── unresolved_slot_tracker.py
│       │
│       ├── interpretation/
│       │   ├── extractor/
│       │   │   ├── llm_extractor.py
│       │   │   ├── heuristic_extractor.py
│       │   │   ├── hybrid_extractor.py
│       │   │   └── extraction_result.py
│       │   ├── mapping/
│       │   │   ├── schema_mapper.py
│       │   │   ├── ontology_mapper.py
│       │   │   ├── synonym_registry.py
│       │   │   └── domain_aliases.py
│       │   ├── normalization/
│       │   │   ├── normalizer.py
│       │   │   ├── units_normalizer.py
│       │   │   ├── defaults_expander.py
│       │   │   └── conflict_resolver.py
│       │   ├── completion/
│       │   │   ├── completion_engine.py
│       │   │   ├── inference_rules.py
│       │   │   └── missing_field_detector.py
│       │   ├── clarification/
│       │   │   ├── clarification_engine.py
│       │   │   ├── question_generator.py
│       │   │   ├── ambiguity_detector.py
│       │   │   └── clarification_policies.py
│       │   ├── validation/
│       │   │   ├── draft_intent_validator.py
│       │   │   ├── semantic_validator.py
│       │   │   ├── safety_validator.py
│       │   │   └── completeness_validator.py
│       │   └── assembly/
│       │       ├── draft_intent_builder.py
│       │       └── interpretation_report_builder.py
│       │
│       ├── intent_language/
│       │   ├── adapters/
│       │   │   ├── sdk_contract_adapter.py
│       │   │   ├── sdk_schema_projection.py
│       │   │   └── sdk_version_projection.py
│       │   ├── builders/
│       │   │   ├── il_builder.py
│       │   │   ├── field_projector.py
│       │   │   └── il_factory.py
│       │   ├── normalization/
│       │   │   ├── pre_sdk_normalizer.py
│       │   │   ├── default_projection.py
│       │   │   └── field_preprocessor.py
│       │   ├── canonicalization/
│       │   │   └── sdk_canonicalization_adapter.py
│       │   ├── validation/
│       │   │   ├── sdk_validator_adapter.py
│       │   │   ├── semantic_validator.py
│       │   │   └── compatibility_guard.py
│       │   ├── versions/
│       │   │   ├── router.py
│       │   │   ├── upgrade_adapter.py
│       │   │   ├── downgrade_adapter.py
│       │   │   └── migration_orchestrator.py
│       │   └── serialization/
│       │       ├── serializer.py
│       │       ├── deserializer.py
│       │       └── sdk_schema_bindings.py
│       │
│       ├── planning/
│       │   ├── engine/
│       │   │   ├── planner_engine.py
│       │   │   ├── planning_context.py
│       │   │   ├── planning_input_assembler.py
│       │   │   └── planning_result.py
│       │   ├── normalization/
│       │   │   ├── planning_intent_normalizer.py
│       │   │   ├── planner_defaults.py
│       │   │   └── planner_alias_resolution.py
│       │   ├── capabilities/
│       │   │   ├── capability_snapshot_loader.py
│       │   │   ├── capability_filter.py
│       │   │   ├── capability_ranker.py
│       │   │   ├── capability_matcher.py
│       │   │   └── capability_explanations.py
│       │   ├── policy/
│       │   │   ├── policy_bundle_loader.py
│       │   │   ├── policy_evaluator.py
│       │   │   ├── policy_overlay_resolver.py
│       │   │   ├── policy_decision_log.py
│       │   │   └── policy_enforcement_points.py
│       │   ├── constraints/
│       │   │   ├── constraint_engine.py
│       │   │   ├── resource_constraints.py
│       │   │   ├── compliance_constraints.py
│       │   │   ├── topology_constraints.py
│       │   │   └── incompatibility_rules.py
│       │   ├── templates/
│       │   │   ├── template_registry.py
│       │   │   ├── template_selector.py
│       │   │   ├── template_resolver.py
│       │   │   ├── template_models.py
│       │   │   └── template_versioning.py
│       │   ├── synthesis/
│       │   │   ├── candidate_plan_generator.py
│       │   │   ├── operators_plan_builder.py
│       │   │   ├── task_plan_builder.py
│       │   │   ├── compute_plan_builder.py
│       │   │   ├── cloud_plan_builder.py
│       │   │   ├── analysis_plan_builder.py
│       │   │   ├── observability_plan_builder.py
│       │   │   ├── explainability_plan_builder.py
│       │   │   └── compiler_directives_builder.py
│       │   ├── dependencies/
│       │   │   ├── dependency_graph_builder.py
│       │   │   ├── topological_sort.py
│       │   │   ├── cycle_detector.py
│       │   │   └── dependency_validator.py
│       │   ├── validation/
│       │   │   ├── resolved_plan_semantic_validator.py
│       │   │   ├── resolved_plan_business_invariants.py
│       │   │   ├── resolved_plan_sdk_contract_guard.py
│       │   │   ├── resolved_plan_sdk_validator_adapter.py
│       │   │   └── policy_post_validator.py
│       │   ├── packaging/
│       │   │   ├── resolved_plan_builder.py
│       │   │   ├── package_assembler.py
│       │   │   ├── sdk_canonicalization_adapter.py
│       │   │   ├── resolved_plan_sdk_projection.py
│       │   │   └── sdk_identity_adapter.py
│       │   └── summary/
│       │       ├── summary_generator.py
│       │       ├── human_review_projection.py
│       │       ├── rationale_builder.py
│       │       └── alternative_rejections.py
│       │
│       ├── diagnostics/
│       │   ├── explainability/
│       │   │   ├── decision_trace_builder.py
│       │   │   ├── intent_to_plan_mapping.py
│       │   │   ├── policy_trace_builder.py
│       │   │   └── capability_trace_builder.py
│       │   ├── warnings/
│       │   │   ├── warning_emitter.py
│       │   │   ├── ambiguity_warnings.py
│       │   │   ├── risk_warnings.py
│       │   │   └── drift_warnings.py
│       │   ├── failures/
│       │   │   ├── error_codes.py
│       │   │   ├── exceptions.py
│       │   │   ├── error_mapper.py
│       │   │   └── remediation_hints.py
│       │   └── reports/
│       │       ├── diagnostics_report_builder.py
│       │       ├── validation_report_builder.py
│       │       └── review_packet_builder.py
│       │
│       ├── artifacts/
│       │   ├── models/
│       │   │   ├── request_artifact.py
│       │   │   ├── conversation_artifact.py
│       │   │   ├── draft_intent_artifact.py
│       │   │   ├── intent_language_artifact.py
│       │   │   ├── capability_snapshot_artifact.py
│       │   │   ├── policy_bundle_artifact.py
│       │   │   ├── resolved_plan_artifact.py
│       │   │   ├── summary_artifact.py
│       │   │   └── diagnostics_artifact.py
│       │   ├── storage/
│       │   │   ├── artifact_store.py
│       │   │   ├── object_store_layout.py
│       │   │   ├── manifest_store.py
│       │   │   └── retention_policies.py
│       │   ├── lineage/
│       │   │   ├── lineage_graph_builder.py
│       │   │   ├── parent_child_links.py
│       │   │   ├── provenance_recorder.py
│       │   │   └── lineage_queries.py
│       │   ├── identity/
│       │   │   ├── sdk_identity_adapter.py
│       │   │   ├── artifact_identity_projection.py
│       │   │   └── identity_input_assembler.py
│       │   ├── registration/
│       │   │   ├── artifact_registry_client.py
│       │   │   ├── registration_service.py
│       │   │   └── status_reconciler.py
│       │   └── serialization/
│       │       ├── serializer.py
│       │       ├── deserializer.py
│       │       └── manifest_serializer.py
│       │
│       ├── approvals/
│       │   ├── models/
│       │   │   ├── review_request.py
│       │   │   ├── review_state.py
│       │   │   ├── approval_decision.py
│       │   │   └── rejection_reason.py
│       │   ├── policy/
│       │   │   ├── review_gate_policy.py
│       │   │   ├── risk_classifier.py
│       │   │   └── mandatory_review_rules.py
│       │   ├── services/
│       │   │   ├── approval_router.py
│       │   │   ├── approval_state_machine.py
│       │   │   ├── reviewer_notification_service.py
│       │   │   └── escalation_service.py
│       │   └── persistence/
│       │       ├── review_store.py
│       │       └── review_history_store.py
│       │
│       ├── integrations/
│       │   ├── sdk/
│       │   │   ├── contract_loader.py
│       │   │   ├── schema_validator_adapter.py
│       │   │   ├── compatibility_adapter.py
│       │   │   ├── canonicalization_policy_adapter.py
│       │   │   ├── identity_policy_adapter.py
│       │   │   └── version_policy_adapter.py
│       │   ├── capability_registry/
│       │   │   ├── client.py
│       │   │   ├── snapshot_resolver.py
│       │   │   └── mappers.py
│       │   ├── policy_source/
│       │   │   ├── client.py
│       │   │   ├── bundle_fetcher.py
│       │   │   └── overlay_fetcher.py
│       │   ├── artifact_registry/
│       │   │   ├── client.py
│       │   │   ├── publisher.py
│       │   │   └── query_adapter.py
│       │   └── eventing/
│       │       ├── publisher.py
│       │       ├── topics.py
│       │       └── event_models.py
│       │
│       ├── persistence/
│       │   ├── postgres/
│       │   │   ├── models.py
│       │   │   ├── repositories/
│       │   │   │   ├── request_repository.py
│       │   │   │   ├── conversation_repository.py
│       │   │   │   ├── review_repository.py
│       │   │   │   └── diagnostics_repository.py
│       │   │   ├── migrations/
│       │   │   └── unit_of_work.py
│       │   ├── redis/
│       │   │   ├── caches.py
│       │   │   ├── keys.py
│       │   │   └── ttl_policies.py
│       │   └── object_store/
│       │       ├── client.py
│       │       ├── paths.py
│       │       └── object_metadata.py
│       │
│       ├── observability/
│       │   ├── logging.py
│       │   ├── tracing.py
│       │   ├── metrics.py
│       │   ├── audit.py
│       │   ├── business_metrics.py
│       │   └── dashboards.md
│       │
│       ├── security/
│       │   ├── authz.py
│       │   ├── tenant_scope.py
│       │   ├── pii_redaction.py
│       │   ├── input_validation.py
│       │   ├── secrets_handling.py
│       │   └── injection_protection.py
│       │
│       ├── workers/
│       │   ├── clarification_dispatcher.py
│       │   ├── artifact_compactor.py
│       │   ├── cache_warmer.py
│       │   ├── snapshot_prefetcher.py
│       │   └── review_escalation_worker.py
│       │
│       └── cli/
│           ├── main.py
│           ├── plan.py
│           ├── validate.py
│           ├── explain.py
│           ├── replay.py
│           └── export.py
│
├── tests/
│   ├── unit/
│   │   ├── api/
│   │   ├── application/
│   │   ├── domain/
│   │   ├── interpretation/
│   │   ├── intent_language/
│   │   ├── planning/
│   │   ├── diagnostics/
│   │   ├── artifacts/
│   │   └── approvals/
│   ├── integration/
│   │   ├── api/
│   │   ├── sdk_contracts/
│   │   ├── capability_registry/
│   │   ├── policy_source/
│   │   ├── artifact_registry/
│   │   └── persistence/
│   ├── contract/
│   │   ├── sdk_schema_consumption/
│   │   ├── resolved_plan_compatibility/
│   │   └── version_compatibility/
│   ├── determinism/
│   │   ├── same_input_same_plan_test.py
│   │   ├── snapshot_change_effects_test.py
│   │   ├── policy_change_effects_test.py
│   │   └── canonicalization_stability_test.py
│   ├── golden/
│   │   ├── fixtures/
│   │   ├── inputs/
│   │   ├── expected_il/
│   │   ├── expected_plans/
│   │   └── test_golden_outputs.py
│   ├── performance/
│   │   ├── load/
│   │   ├── latency/
│   │   └── cache_effectiveness/
│   ├── security/
│   │   ├── authz/
│   │   ├── tenant_isolation/
│   │   └── injection/
│   └── fixtures/
│       ├── requests/
│       ├── conversations/
│       ├── snapshots/
│       ├── policies/
│       └── plans/
│
└── .github/
    └── workflows/
        ├── ci.yaml
        ├── lint.yaml
        ├── test.yaml
        ├── contract-check.yaml
        ├── determinism.yaml
        ├── security-scan.yaml
        └── release.yaml
```

---

### What each top-level area owns

#### 1. `docs/`

This is not optional. For a compiler-grade planning repository, architecture and decision records must live with the codebase.

It should hold:

* the merged architecture spec,
* ADRs for non-negotiable decisions,
* operational docs,
* determinism and test strategy,
* security model.

This is important because your current docs define critical stage boundaries that must not be lost during implementation.

#### 2. `src/intent_planner/api/`

Public ingress only.
This layer should:

* authenticate,
* authorize,
* validate request envelopes,
* enforce idempotency,
* map external request/response models,
* never contain planning logic.

#### 3. `src/intent_planner/application/`

This is the orchestration layer for use cases:

* create a plan,
* validate IL,
* explain a plan,
* route review,
* replay deterministic planning.

It coordinates subsystems, but does not hold domain rules.

#### 4. `src/intent_planner/domain/`

This is the core business model and invariants layer.

It should define:

* request entities,
* IL invariants,
* resolved plan invariants,
* policy decision result models,
* diagnostics taxonomy,
* artifact identity models.

This is where “compiler-grade” correctness lives.

#### 5. `src/intent_planner/interpretation/`

Everything before IL becomes canonical.

This layer can contain controlled non-determinism and LLM-assisted extraction, but its output is still not planning truth. That matches the architectural separation from the intent compiler and intent language docs.

#### 6. `src/intent_planner/intent_language/`

This is the formal compiler boundary.

It owns:

* IL building,
* canonicalization,
* version routing,
* semantic and schema validation,
* deterministic serialization for hashing.

The planner must only consume artifacts from here.

#### 7. `src/intent_planner/planning/`

This is the deterministic engine.

It owns:

* capability snapshot loading,
* policy bundle loading,
* constraint evaluation,
* template selection,
* candidate synthesis,
* dependency graph construction,
* resolved plan packaging,
* plan summary generation.

This directly corresponds to the planner engine responsibility from your architecture.

#### 8. `src/intent_planner/diagnostics/`

This must be first-class, not bolted on.

It should produce:

* decision traces,
* policy traces,
* capability selection explanations,
* rejection reasons,
* remediation hints,
* review packets.

That is required for explainability and for human approval flow.

#### 9. `src/intent_planner/artifacts/`

This area owns immutable planning outputs and lineage:

* request artifact,
* conversation artifact,
* IL artifact,
* capability snapshot artifact,
* policy bundle artifact,
* resolved plan artifact,
* summary artifact,
* diagnostics artifact.

This is also where deterministic identity and provenance are enforced.

#### 10. `src/intent_planner/approvals/`

Human review should not be hidden in generic services.

This bounded area should own:

* review state machine,
* mandatory review rules,
* approval/rejection persistence,
* reviewer notifications/escalations.

#### 11. `src/intent_planner/integrations/`

All external system interaction is adapted here:

* `platform-sdk`
* capability registry
* policy source
* artifact registry
* event publishing

This avoids leaking external client details into domain or planning logic.

#### 12. `src/intent_planner/persistence/`

Persistence details should be isolated here:

* PostgreSQL for workflow/review/diagnostic metadata
* Redis for cache and idempotency
* object store for immutable artifacts

#### 13. `templates/`

Keep planning templates outside the Python package root as governed assets.

These are not just config files. They are versioned planning assets and should be reviewed like code, because template changes can change resolved plans. That follows from the planner engine’s template-driven plan generation model.

#### 14. `tests/`

This repo needs more than standard unit tests. It must have:

* determinism tests,
* golden tests,
* contract tests against SDK schemas,
* policy change tests,
* snapshot change tests,
* security boundary tests.

---

### Internal ownership rules

These rules should be enforced in code review and CI.

#### Rule 1: `platform-sdk` owns canonical schemas

Therefore:

* do not define canonical IL or resolved plan contracts independently in this repo,
* only bind or adapt them here.

#### Rule 2: `interpretation/` must not emit final plans

It may emit:

* extracted structures,
* draft intent,
* clarification prompts,
* interpretation reports.

It must never bypass IL.

#### Rule 3: `planning/` must not consume raw natural language

Planning input must be:

* validated IL
* versioned capability snapshot
* versioned policy bundle.

#### Rule 4: `api/` must not contain business rules

No planning logic, no policy logic, no snapshot logic.

#### Rule 5: `integrations/` must not contain domain decisions

It only adapts external services to internal ports.

#### Rule 6: `artifacts/` is immutable-by-default

Artifacts are append-only and version-addressed.

#### Rule 7: no runtime execution code

No executors, controllers, reconciliers, or adapter invocations belong here. Those are outside intent-planner scope.

---

### Recommended package layering

Use this dependency direction:

```text
api -> application -> domain
api -> application -> interpretation
api -> application -> intent_language
api -> application -> planning
application -> ports
integrations -> ports
persistence -> ports
domain -> shared

NEVER:
domain -> api
planning -> api
planning -> persistence concrete classes
domain -> integrations
```

That keeps the planner testable and prevents architectural drift.

---

### Minimal database/storage split

A production deployment should usually separate storage like this:

#### PostgreSQL

Use for:

* requests
* conversations
* review states
* diagnostics metadata
* artifact manifests
* replay indexes

#### Redis

Use for:

* idempotency keys
* conversation/session hot state
* snapshot cache
* policy bundle cache
* short-lived workflow coordination

#### Object store

Use for:

* immutable IL artifacts
* resolved plan artifacts
* summaries
* diagnostics payloads
* lineage snapshots

This split is cleaner than trying to store full planning artifacts in a relational database.

---

### CI/CD gates that should be mandatory

Every PR should fail unless all of these pass:

* lint
* typing
* unit tests
* integration tests
* contract tests against `platform-sdk`
* determinism tests
* golden tests
* security scan
* template validation
* architecture import boundary checks

The determinism and contract gates are especially important given your requirement that the planner behave as a governed compiler rather than a heuristic service.

---

### Recommended import boundary policy

You should enforce this structurally:

* `api/*` can import `application/*`, `shared/*`
* `application/*` can import `domain/*`, `interpretation/*`, `intent_language/*`, `planning/*`, `ports/*`
* `domain/*` can import only `shared/*`
* `integrations/*` implements `application/ports/*`
* `persistence/*` implements `application/ports/*`

And explicitly ban:

* `planning/* -> api/*`
* `domain/* -> persistence/*`
* `interpretation/* -> planning/*` direct shortcuts that bypass IL
* `api/* -> integrations/*` direct client usage

---

### What is intentionally not in this repo

To avoid future boundary confusion, these should stay out:

* runtime controller
* reconciliation loop
* task executor
* domain operator execution
* adapter runtime
* workflow engine for execution
* control-plane state machine

Those belong in the control-plane / runtime side, not here.

---

### Final recommended condensed shape

If you want the shortest production-safe mental model, it is this:

```text
intent-planner
├── api                 # ingress only
├── application         # use-case orchestration
├── domain              # invariants and core models
├── interpretation      # raw intent -> draft intent
├── intent_language     # draft intent -> canonical IL
├── planning            # IL -> deterministic resolved plan
├── diagnostics         # explainability and failure mapping
├── artifacts           # immutable artifact storage and lineage
├── approvals           # review workflows and gates
├── integrations        # sdk / registry / policy / artifact clients
├── persistence         # db/cache/object store adapters
├── observability       # logging/metrics/tracing/audit
├── security            # tenant/auth/input protection
├── workers             # async internal maintenance tasks
└── tests               # determinism, contract, golden, integration
```


## 19. Testing Strategy

### Required Test Classes

* unit tests
* integration tests
* determinism tests
* contract tests
* policy tests
* golden tests

### Golden Test Guarantees

* same IL → same plan
* policy change → controlled plan change
* snapshot change → deterministic variation

---

## 20. Artifact Identity Model

```text
plan_hash = hash(
  IL_canonical
  + capability_snapshot_version
  + policy_bundle_version
  + planner_version
)
```

---

## 21. Extension Points

* new intent domains
* new planning templates
* new capability types
* new policy modules

---

## 22. Architecture Validation Checklist

### Architectural consistency checks

* Is IL the only boundary between interpretation and planning?
* Is planning fully deterministic and free of LLM/runtime randomness?
* Is compiler meaning clearly defined inside `intent-planner`?
* Are runtime concerns excluded from `intent-planner`?

### Repository consistency checks

* Are all canonical schemas owned by `platform-sdk`?
* Does `intent-planner` only consume SDK contracts?
* Are `control-plane` imports one-way and read-only from planner outputs?
* Are hashing/canonicalization/version policies centralized in SDK?

### MVP consistency checks

* What is the minimal artifact set?
* What exact API responses are returned by planner?
* What is deferred from MVP: clarification loop, human approval, compiler plan, service plan?

## 23. Final Architectural Statement

Intent-Planner is a **compiler-grade subsystem** with:

* strict input boundary (Intent Language)
* deterministic transformation
* governed output (Resolved Plan)
* complete auditability
* zero runtime responsibility

---

## 24. Non-Negotiable Rules

1. Planning NEVER consumes raw natural language
2. LLMs NEVER decide infrastructure
3. All plans MUST pass policy validation
4. All outputs MUST be reproducible
5. All schemas MUST come from Platform SDK
6. All planning MUST use snapshots
7. All artifacts MUST be versioned and hashable

---
