# Control-Plane Repository Scaffolding

## Purpose

`control-plane` is the runtime orchestration implementation repository. It consumes contracts from `platform-sdk` and plans from `intent-planner`, then drives reconciliation and execution safely under bounded liveness rules.

## Repository Structure

```text
control-plane/
├── README.md
├── pyproject.toml
├── api/
│   ├── control_plane_server.py
│   ├── intent_submission_api.py
│   └── status_query_api.py
├── controllers/
│   ├── intent_controller.py
│   ├── plan_controller.py
│   └── drift_controller.py
├── reconciliation/
│   ├── reconciliation_engine.py
│   ├── desired_state_builder.py
│   └── actual_state_collector.py
├── execution/
│   ├── action_dispatcher.py
│   ├── adapter_coordinator.py
│   └── rollback_orchestrator.py
├── events/
│   ├── event_router.py
│   ├── event_store.py
│   └── event_handlers.py
├── liveness/
│   ├── retry_budget_manager.py
│   ├── watchdog_supervisor.py
│   ├── circuit_breaker.py
│   ├── dead_letter_queue_handler.py
│   ├── compensation_dispatcher.py
│   └── convergence_incident_controller.py
├── incidents/
│   ├── incident_model.py
│   └── escalation_policy.py
├── compliance/
│   ├── liveness_obligation_map.md
│   └── controller_timeout_matrix.yaml
└── tests/
    ├── test_retry_budget.py
    ├── test_watchdog_timeouts.py
    ├── test_dead_letter_path.py
    ├── test_convergence_blocked_event.py
    └── test_circuit_breaker_behavior.py
```

## Liveness Implementation Rules

All control loops must be bounded. The following patterns are required:

- bounded retries with per-event-class budgets,
- explicit stage deadlines and watchdog timeout actions,
- compensation events for missing acknowledgements,
- dead-letter handling for exhausted/poison events,
- convergence incident escalation when loop caps are exceeded.

Unbounded `while True` loops without timeout/backoff/budget controls are forbidden.

## CI Compliance Gates

The repository must fail CI if liveness tests are missing or failing:

- retry budget enforcement tests,
- watchdog timeout enforcement tests,
- dead-letter routing tests,
- convergence incident escalation tests,
- circuit breaker failure-isolation tests.

## Source Architecture References

- `docs/platform/architecture/control_plane_architecture.md`
- `docs/platform/architecture/control_plane_liveness_spec.md`
- `docs/platform/architecture/repository_architecture.md`
