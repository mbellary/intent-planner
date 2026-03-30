# Repo Boundary Conventions

## platform-sdk

### May define
- canonical contracts
- validation
- canonicalization
- hashing
- compatibility policy
- artifact catalogs
- machine catalogs

### Must not define
- runtime infrastructure
- planner business logic
- control-plane orchestration
- transport implementation concerns

## intent-planner

### May define
- planner-local orchestration
- ingestion
- interpretation
- intent derivation
- planner-local persistence adapters
- planner API

### Must not define
- canonical SDK contracts
- canonical hash semantics
- canonical lineage semantics
- control-plane runtime execution logic

## control-plane

### May define
- runtime orchestration
- event intake
- reconciliation
- worker processes
- canonical persistence adapters
- recovery and resilience logic

### Must not define
- alternative artifact contracts
- alternative machine semantics
- alternative lineage semantics owned by SDK

## Cross-repo rules

1. `platform-sdk` is the canonical contract owner.
2. `intent-planner` and `control-plane` consume SDK contracts through explicit boundaries.
3. No repo may silently redefine identifiers, event envelope semantics, or lifecycle semantics
   owned by the SDK.
4. Bootstrap code must remain side-effect free on import.