## `platform-sdk/`

```text
platform-sdk/
├── .github/
│   └── workflows/
│       ├── ci.yaml
│       ├── compatibility.yaml
│       ├── contract-check.yaml
│       ├── determinism.yaml
│       ├── lint.yaml
│       ├── release.yaml
│       └── test.yaml
├── docker/
│   ├── Dockerfile
│   └── Dockerfile.dev
├── docs/
│   ├── adr/
│   │   ├── ADR-001-contract-first-layering.md
│   │   ├── ADR-002-sdk-owns-artifact-contracts.md
│   │   ├── ADR-003-sdk-owns-state-machine-contracts.md
│   │   ├── ADR-004-canonicalization-policy.md
│   │   ├── ADR-005-hashing-policy.md
│   │   └── ADR-006-error-taxonomy-and-compatibility.md
│   ├── architecture/
│   │   ├── artifact_system_contract.md
│   │   ├── canonicalization_and_hashing.md
│   │   ├── compatibility_policy.md
│   │   ├── contract_layering.md
│   │   ├── repository_boundaries.md
│   │   ├── state_machine_contract.md
│   │   └── validation_profiles.md
│   └── testing/
│       ├── compatibility_strategy.md
│       ├── contract_strategy.md
│       ├── cross_language_hash_vectors.md
│       └── determinism_strategy.md
├── schemas/
│   ├── intent/
│   |    ├── intent.schema.json
│   |    └── intent.validation_error.schema.json
│   ├── plan/
│   ├── artifact/
│   ├── execution/
│   ├── policy/
│   ├── event/
│   ├── api/
│   └── state_machine/
├── scripts/
│   ├── export_hash_vectors.py
│   ├── run_contract_checks.py
│   └── verify_compatibility.py
├── src/
│   └── platform_sdk/
│       ├── canonicalization/
│       │   ├── __init__.py
│       │   ├── normalizer.py
│       │   ├── policy.py
│       │   ├── serializers.py
│       │   └── stable_json.py
│       ├── catalogs/
│       │   ├── artifacts/
│       │   │   ├── __init__.py
│       │   │   ├── catalog.py
│       │   │   ├── enums.py
│       │   │   ├── identity_participation.py
│       │   │   ├── lineage_rules.py
│       │   │   ├── producer_consumer_matrix.py
│       │   │   ├── publication_policy.py
│       │   │   ├── shared_contracts.py
│       │   │   ├── taxonomy.py
│       │   │   └── types.py
│       │   ├── machines/
│       │   │   ├── __init__.py
│       │   │   ├── admissibility.py
│       │   │   ├── artifact_bindings.py
│       │   │   ├── catalog.py
│       │   │   ├── enums.py
│       │   │   ├── guards.py
│       │   │   ├── snapshot_policy.py
│       │   │   ├── state_sets.py
│       │   │   ├── state_transition_validator.py
│       │   │   ├── taxonomy.py
│       │   │   ├── transitions.py
│       │   │   └── types.py
│       │   ├── validators/
│       │   │   ├── __init__.py
│       │   │   ├── catalog_consistency.py
│       │   │   ├── freeze_gate.py
│       │   │   ├── freeze_manifest.py
│       │   │   └── machine_snapshot_policy.py
│       │   └── __init__.py
│       ├── compatibility/
│       │   ├── __init__.py
│       │   ├── deprecations.py
│       │   ├── migrations.py
│       │   ├── rules.py
│       │   ├── semver.py
│       │   └── snapshots.py
│       ├── contracts/
│       │   ├── api/
│       │   │   ├── __init__.py
│       │   │   ├── request_models.py
│       │   │   └── response_models.py
│       │   ├── artifacts/
│       │   │   ├── __init__.py
│       │   │   ├── base.py
│       │   │   ├── catalog_adapter.py
│       │   │   ├── families.py
│       │   │   ├── graph.py
│       │   │   ├── identity.py
│       │   │   ├── integrity.py
│       │   │   ├── lifecycle.py
│       │   │   ├── lineage.py
│       │   │   ├── publication.py
│       │   │   └── registration.py
│       │   ├── common/
│       │   │   ├── __init__.py
│       │   │   ├── enums.py
│       │   │   ├── envelope.py
│       │   │   ├── metadata.py
│       │   │   ├── references.py
│       │   │   └── versioning.py
│       │   ├── errors/
│       │   │   ├── __init__.py
│       │   │   ├── artifact.py
│       │   │   ├── base.py
│       │   │   ├── codes.py
│       │   │   ├── payloads.py
│       │   │   ├── state_machine.py
│       │   │   └── validation.py
│       │   ├── event/
│       │   │   ├── __init__.py
│       │   │   ├── event_envelope.py
│       │   │   └── event_refs.py
│       │   ├── execution/
│       │   │   ├── __init__.py
│       │   │   ├── execution_record.py
│       │   │   ├── execution_status.py
│       │   │   └── run_manifest.py
│       │   ├── intent/
│       │   │   ├── __init__.py
│       │   │   ├── intent.py
│       │   │   ├── intent_language.py
│       │   │   ├── request.py
│       │   │   └── review_packet.py
│       │   ├── plan/
│       │   │   ├── __init__.py
│       │   │   ├── diagnostics.py
│       │   │   ├── plan_summary.py
│       │   │   └── resolved_plan.py
│       │   ├── policy/
│       │   │   ├── __init__.py
│       │   │   ├── policy_bundle.py
│       │   │   └── policy_result.py
│       │   ├── state_machines/
│       │   │   ├── __init__.py
│       │   │   ├── audit.py
│       │   │   ├── base.py
│       │   │   ├── catalogs.py
│       │   │   ├── events.py
│       │   │   ├── guards.py
│       │   │   ├── rejects.py
│       │   │   ├── replay.py
│       │   │   ├── states.py
│       │   │   └── transitions.py
│       │   └── __init__.py
│       ├── hashing/
│       │   ├── __init__.py
│       │   ├── engine.py
│       │   ├── fingerprints.py
│       │   ├── policy.py
│       │   └── vectors.py
│       ├── interfaces/
│       │   ├── __init__.py
│       │   ├── artifact_store.py
│       │   ├── machine_catalog.py
│       │   ├── result_types.py
│       │   └── schema_registry.py
│       ├── public/
│       │   ├── __init__.py
│       │   ├── canonicalization.py
│       │   ├── compatibility.py
│       │   ├── contracts.py
│       │   ├── errors.py
│       │   ├── hashing.py
│       │   ├── state_machines.py
│       │   └── validation.py
│       ├── registries/
│       │   ├── __init__.py
│       │   ├── artifact_family_catalog.py
│       │   ├── machine_catalog.py
│       │   └── schema_registry.py
│       ├── shared/
│       │   ├── __init__.py
│       │   ├── clocks.py
│       │   ├── ids.py
│       │   ├── result.py
│       │   └── typing.py
│       ├── tooling/
│       │   ├── __init__.py
│       │   ├── compatibility_check.py
│       │   ├── contract_lint.py
│       │   ├── hash_vector_export.py
│       │   └── ownership_check.py
│       ├── validation/
│       │   ├── profiles/
│       │   │   ├── __init__.py
│       │   │   ├── artifact.py
│       │   │   ├── base.py
│       │   │   ├── execution.py
│       │   │   ├── intent.py
│       │   │   └── plan.py
│       │   ├── __init__.py
│       │   ├── artifact_graph.py
│       │   ├── engine.py
│       │   ├── governance.py
│       │   ├── schema.py
│       │   ├── semantic.py
│       │   └── state_machine.py
│       ├── __init__.py
│       └── py.typed
├── tests/
│   ├── fixtures/
│   │   ├── __init__.py
│   │   ├── artifacts.py
│   │   ├── helpers.py
│   │   ├── machines.py
│   │   └── payloads.py
│   ├── golden/
│   │   ├── __init__.py
│   │   ├── canonical_draft_intent_payload.json
│   │   ├── canonical_intent_language_payload.json
│   │   ├── canonical_request_payload.json
│   │   ├── expected_draft_intent_identity.json
│   │   ├── expected_intent_language_identity.json
│   │   └── expected_request_identity.json
│   ├── integration/
│   │   ├── artifact_flow/
│   │   │   ├── __init__.py
│   │   │   ├── test_draft_intent_to_intent_language_flow.py
│   │   │   ├── test_intent_to_resolved_plan_flow.py
│   │   │   ├── test_lineage_rule_reconstructable_paths.py
│   │   │   ├── test_request_to_draft_intent_flow.py
│   │   │   └── test_review_and_approval_flow.py
│   │   ├── cross_catalog/
│   │   │   ├── __init__.py
│   │   │   ├── test_artifact_machine_alignment.py
│   │   │   ├── test_artifact_machine_binding_consistency.py
│   │   │   ├── test_identity_vs_progressive_artifact_consistency.py
│   │   │   ├── test_lineage_vs_machine_consistency.py
│   │   │   └── test_publication_vs_lifecycle_consistency.py
│   │   ├── machine_flow/
│   │   │   ├── __init__.py
│   │   │   ├── test_execution_lifecycle_machine_flow.py
│   │   │   ├── test_intent_lifecycle_machine_flow.py
│   │   │   ├── test_request_lifecycle_machine_flow.py
│   │   │   ├── test_resolved_plan_lifecycle_machine_flow.py
│   │   │   └── test_runtime_failure_and_retry_flow.py
│   │   └── __init__.py
│   ├── invariants/
│   │   ├── admissibility/
│   │   │   ├── __init__.py
│   │   │   ├── test_artifact_lineage_admissibility_surface.py
│   │   │   ├── test_artifact_machine_binding_surface_is_closed_world.py
│   │   │   ├── test_guard_catalog_is_closed_world.py
│   │   │   ├── test_guard_violations_are_rejected.py
│   │   │   ├── test_invalid_lineage_is_rejected.py
│   │   │   ├── test_invalid_transition_is_rejected.py
│   │   │   ├── test_orphan_lifecycle_artifacts_are_rejected.py
│   │   │   └── test_transition_admissibility_surface_is_closed_world.py
│   │   ├── closed_world/
│   │   │   ├── __init__.py
│   │   │   ├── test_all_artifacts_are_cataloged.py
│   │   │   ├── test_all_artifacts_have_identity_participation.py
│   │   │   ├── test_all_artifacts_have_lineage_rules.py
│   │   │   ├── test_all_artifacts_have_publication_policy.py
│   │   │   ├── test_all_machines_are_cataloged.py
│   │   │   ├── test_machine_snapshot_policy_surface_is_closed_world.py
│   │   │   ├── test_no_unknown_artifact_families.py
│   │   │   ├── test_no_unknown_machine_families.py
│   │   │   └── test_root_artifact_types_are_well_formed.py
│   │   ├── determinism/
│   │   │   ├── __init__.py
│   │   │   ├── test_identity_inputs_are_stable.py
│   │   │   ├── test_identity_projection_contract.py
│   │   │   ├── test_machine_snapshot_policy_contract.py
│   │   │   ├── test_non_semantic_fields_do_not_affect_identity.py
│   │   │   └── test_snapshot_artifacts_are_immutable_by_contract.py
│   │   └── __init__.py
│   ├── property/
│   │   ├── __init__.py
│   │   ├── test_lineage_properties.py
│   │   └── test_transition_properties.py
│   ├── unit/
│   │   ├── artifacts/
│   │   │   ├── __init__.py
│   │   │   ├── test_artifact_graph.py
│   │   │   ├── test_artifact_identity_contract.py
│   │   │   ├── test_artifact_lineage_contract.py
│   │   │   ├── test_artifact_publication.py
│   │   │   ├── test_artifact_registration.py
│   │   │   └── test_base_artifact.py
│   │   ├── catalogs/
│   │   │   ├── __init__.py
│   │   │   ├── test_artifact_catalog.py
│   │   │   ├── test_artifact_enums.py
│   │   │   ├── test_artifact_identity_participation.py
│   │   │   ├── test_artifact_lineage_rules.py
│   │   │   ├── test_artifact_machine_bindings.py
│   │   │   ├── test_artifact_publication_policy.py
│   │   │   ├── test_artifact_taxonomy.py
│   │   │   ├── test_catalog_consistency.py
│   │   │   ├── test_identity_participation_determinism_alignment.py
│   │   │   ├── test_machine_admissibility.py
│   │   │   ├── test_machine_catalog.py
│   │   │   ├── test_machine_guards.py
│   │   │   ├── test_machine_snapshot_policy.py
│   │   │   ├── test_machine_state_sets.py
│   │   │   └── test_machine_transitions.py
│   │   ├── state_machines/
│   │   │   ├── __init__.py
│   │   │   ├── test_state_machine_base.py
│   │   │   ├── test_state_machine_executor.py
│   │   │   ├── test_state_machine_guards.py
│   │   │   ├── test_state_machine_registry_adapter.py
│   │   │   └── test_state_machine_serialization.py
│   │   ├── validation/
│   │   │   ├── __init__.py
│   │   │   ├── test_schema_validator.py
│   │   │   └── test_semantic_validator.py
│   │   ├── __init__.py
│   │   ├── test_fixture_imports.py
│   │   ├── test_sdk_import_surface.py
│   │   └── test_test_infrastructure.py
│   ├── __init__.py
│   └── conftest.py
├── .editorconfig
├── .env.example
├── .gitignore
├── .pre-commit-config.yaml
├── .python-version
├── Makefile
├── README.md
├── REPOSITORY_SCAFFOLD_L4.md
├── coverage.ini
├── mypy.ini
├── phase_3_0_engineering_plan.md
├── pyproject.toml
├── pytest.ini
├── ruff.toml
├── test-repo-scaffolding.md
└── uv.lock
```

---

## `intent-planner/`

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
│   │   ├── repository_structure.md
│   │   ├── artifact_production_model.md
│   │   ├── planner_state_machines.md
│   │   └── determinism_model.md
│   ├── adr/
│   │   ├── ADR-001-il-boundary.md
│   │   ├── ADR-002-resolved-plan-contract-consumption.md
│   │   ├── ADR-003-capability-snapshot-planning.md
│   │   ├── ADR-004-policy-evaluation-stages.md
│   │   ├── ADR-005-human-review-gate.md
│   │   ├── ADR-006-sdk-owned-hashing-and-canonicalization.md
│   │   └── ADR-007-no-runtime-execution-in-planner.md
│   ├── operations/
│   │   ├── runbook.md
│   │   ├── slos.md
│   │   └── alerting.md
│   ├── security/
│   │   ├── threat_model.md
│   │   ├── tenant_isolation.md
│   │   └── authz_model.md
│   └── testing/
│       ├── determinism_strategy.md
│       ├── golden_tests.md
│       ├── contract_tests.md
│       └── fixture_strategy.md
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
|
|
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
│       ├── api/
│       │   ├── app.py
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
│       │   ├── response_models/
│       │   |   ├── planning_responses.py
│       │   |   ├── validation_responses.py
│       │   |   ├── explanation_responses.py
│       │   |   ├── approval_responses.py
│       │   |   └── error_responses.py
│       │   └── dependencies.py
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
|       |
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
|       |
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
│       │   ├── builders/
│       │   │   ├── il_builder.py
│       │   │   ├── field_projector.py
│       │   │   └── il_factory.py
│       │   ├── normalization/
│       │   │   ├── pre_sdk_normalizer.py
│       │   │   ├── default_projection.py
│       │   │   └── field_preprocessor.py
|       |   |
│       │   ├── validation/
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
|       |
|       |
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
│       │   │   └── policy_post_validator.py
│       │   ├── packaging/
│       │   │   ├── resolved_plan_builder.py
│       │   │   ├── package_assembler.py
│       │   │   └── resolved_plan_sdk_projection.py
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
│       │   ├── buiders/
│       │   │   ├── request_builder.py
│       │   │   ├── conversation_builder.py
│       │   │   ├── draft_intent_builder.py
│       │   │   ├── intent_language_builder.py
│       │   │   ├── capability_snapshot_builder.py
│       │   │   ├── policy_bundle_builder.py
│       │   │   ├── resolved_plan_builder.py
│       │   │   ├── summary_builder.py
│       │   │   └── diagnostics_builder.py
│       │   ├── persistence/
│       │   │   ├── artifact_store.py
│       │   │   ├── object_store_layout.py
│       │   │   ├── manifest_store.py
│       │   │   └── retention_policies.py
│       │   ├── lineage/
│       │   │   ├── lineage_graph_builder.py
│       │   │   ├── parent_child_links.py
│       │   │   ├── provenance_recorder.py
│       │   │   └── lineage_queries.py
│       │   ├── projections/
│       │   │   ├── sdk_artifact_projection.py
│       │   │   ├── summary_projection.py
|       |   |   ├── review_projection.py
│       │   │   └── diagnostics_projection.py
│       │   ├── records/
│       │   │   ├── artifact_manifest_record.py
│       │   │   ├── artifact_write_record.py
│       │   │   └── lineage_record.py
│       │   └── serialization/
│       │       ├── serializer.py
│       │       ├── deserializer.py
│       │       └── manifest_serializer.py
│       │
│       ├── state_machines/
|       |    ├── runtime/
|       |    │   ├── machine_runtime.py
|       |    │   ├── transition_executor.py
|       |    │   └── replay_runtime.py
|       |    ├── reducers/
|       |    │   ├── intent_reducer.py
|       |    │   ├── plan_reducer.py
|       |    │   └── review_reducer.py
|       |    ├── guards/
|       |    │   ├── planner_context_guards.py
|       |    │   └── review_guards.py
|       |    ├── projections/
|       |    │   ├── state_view.py
|       |    │   └── audit_projection.py
|       |    └── bindings/
|       |        ├── sdk_machine_catalog_binding.py
|       |        └── sdk_transition_binding.py
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
|       |
│       │
│       ├── integrations/
│       │   ├── sdk/
|       │   │    ├── __init__.py
|       │   │    ├── contracts.py
|       │   │    ├── validation.py
|       │   │    ├── canonicalization.py
|       │   │    ├── hashing.py
|       │   │    ├── compatibility.py
|       │   │    ├── state_machines.py
|       │   │    ├── sdk_canonicalization_adapter.py
|       │   │    ├── resolved_plan_sdk_contract_guard.py
|       │   │    ├── resolved_plan_sdk_validator_adapter.py
|       │   │    ├── sdk_validator_adapter.py
|       │   │    ├── mappers.py
|       |   |    ├── adapters/
│       |   |    |     ├── artifact_adapter.py
│       |   |    |     ├── capability_adapter.py
│       |   |    |     ├── policy_adapter.py
│       |   |    |     └── machine_adapter.py
│       |   |    ├── facade.py
│       |   |    └── types.py
|       |   │
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
│       ├── bootstrap/
│       │   ├── container.py
│       │   ├── settings.py
│       │   ├── dependency_graph.py
│       │   ├── feature_flags.py
│       │   └── startup_checks.py
│       │
│       └── shared/
│       │   ├── enums.py
│       │   ├── constants.py
│       │   ├── clock.py
│       │   ├── ids.py
│       │   ├── canonical_representation.py
│       │   ├── pagination.py
│       │   ├── types.py
│       │   └── versioning.py
|       |
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
│       ├── governance/
|       |   ├── import_rules.py
|       |   ├── ownership_rules.py
|       |   └── public_api_manifest.py
|       |   
│       ├── workers/
│       │   ├── clarification_dispatcher.py
│       │   ├── artifact_compactor.py
│       │   ├── cache_warmer.py
│       │   ├── snapshot_prefetcher.py
│       │   └── review_escalation_worker.py
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
│   │   ├── application/
│   │   ├── domain/
│   │   ├── intent_language/
│   │   ├── planning/
│   │   ├── artifacts/
│   │   ├── state_machines/
│   │   └── diagnostics/
│   ├── contract/
│   │   ├── sdk_schemas/
│   │   ├── sdk_validation/
│   │   └── sdk_machine_catalogs/
│   ├── integration/
│   │   ├── api/
│   │   ├── persistence/
│   │   ├── planner_flow/
│   │   └── approvals/
│   ├── determinism/
│   │   ├── golden_plans/
│   │   ├── replay/
│   │   └── artifact_identity/
│   ├── golden/
│   │   ├── fixtures/
│   │   ├── inputs/
│   │   ├── expected_il/
│   │   ├── expected_plans/
│   │   └── test_golden_outputs.py
│   ├── security/
│   ├── performance/
│   │   ├── load/
│   │   ├── latency/
│   │   └── cache_effectiveness/
│   └── fixtures/
│       ├── requests/
│       ├── conversations/
│       ├── snapshots/
│       ├── policies/
│       └── plans/
│
├── scripts/
│   ├── bootstrap.sh
│   ├── run_local.sh
│   ├── seed_templates.sh
│   ├── lint.sh
│   ├── test.sh
│   ├── generate_openapi.py
│   ├── generate_mermaid.py
│   ├── backfill_artifacts.py
│   └── replay_plans.py
│
└── .github/
    └── workflows/
        ├── ci.yaml
        ├── lint.yaml
        ├── test.yaml
        ├── contract-check.yaml
        ├── determinism.yaml
        ├── golden-tests.yaml
        ├── security-scan.yaml
        └── release.yaml
```
---

## `control-plane/`

```text
control-plane/
├── pyproject.toml
├── src/control_plane/
│   ├── api/
│   │   ├── app.py
│   │   ├── routes/
│   │   │   ├── intents.py
│   │   │   ├── executions.py
│   │   │   ├── admin.py
│   │   │   └── health.py
│   │   └── schemas/
│   ├── application/
│   │   ├── commands/
│   │   ├── handlers/
│   │   ├── queries/
│   │   └── unit_of_work.py
│   ├── domain/
│   │   ├── controllers/
│   │   ├── reconciliation/
│   │   ├── runtime/
│   │   ├── policies/
│   │   ├── events/
│   │   └── incidents/
│   ├── infrastructure/
│   │   ├── db/
│   │   │   ├── models/
│   │   │   ├── repositories/
│   │   │   ├── migrations/
│   │   │   └── session.py
│   │   ├── messaging/
│   │   │   ├── producer.py
│   │   │   ├── consumer.py
│   │   │   ├── outbox_publisher.py
│   │   │   ├── inbox_store.py
│   │   │   └── dlq.py
│   │   ├── adapters/
│   │   ├── observability/
│   │   └── config/
│   ├── workers/
│   │   ├── event_intake.py
│   │   ├── reconcile.py
│   │   ├── dispatch.py
│   │   ├── watchdog.py
│   │   ├── recovery.py
│   │   └── status_collector.py
│   ├── contracts/
│   │   └── imports_from_platform_sdk_only.py
│   └── bootstrap/
│       ├── container.py
│       └── startup.py
├── tests/
│   ├── unit/
│   ├── contract/
│   ├── integration/
│   ├── e2e/
│   └── resilience/
└── docs/
```



---

## Boundary guardrails to enforce in both repos

```text
platform-sdk:
  MAY define contracts, validation, hashing, compatibility, machine catalogs
  MUST NOT contain runtime infrastructure or planner business logic

intent-planner:
  MAY consume sdk contracts, produce planning artifacts, enforce planner-local machines
  MUST NOT redefine canonical contracts from sdk
  MUST NOT contain runtime/control-plane execution code

control-plane:
  consumes both later, but is not part of the Phase 3 scaffolding
```
