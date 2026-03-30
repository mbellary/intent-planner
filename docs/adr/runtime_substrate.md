# ADR: Runtime Substrate for Phase 5 First Cut

## Status
Accepted

## Context

The first-cut platform runtime must establish one canonical persistence substrate before
planner and control-plane implementation proceed.

This first cut is intentionally limited to:
- RequestArtifact
- IntentArtifact

The runtime must support:
- canonical artifact persistence
- canonical event logging
- relational lineage edges
- deterministic replay from persisted truth

## Decision

The runtime substrate for the first cut is:

- **Postgres** as the canonical system of record
- **canonical event log** stored in Postgres
- **outbox projection** stored in Postgres as a derived transport-facing projection
- **relational lineage edges** stored in Postgres
- **Kafka compatibility** documented but not introduced as runtime truth in XS-00
- **Neo4j compatibility** documented but not introduced as runtime truth in XS-00

## Rationale

This preserves a single source of truth while allowing Kafka and Neo4j integration
to be introduced later without redefining canonical semantics.

The key rule is:

> semantic truth is resolved from canonical storage, not inferred from transport payloads.

## Consequences

### Positive
- Deterministic replay has a clear source of truth.
- Planner persistence and control-plane intake can be designed against one canonical model.
- Runtime semantics are stable before distributed transport complexity is introduced.

### Negative
- Kafka and Neo4j integration are deferred from the runnable bootstrap slice.
- Some future adaptation work will still be needed for transport and lineage graph projections.

## Non-negotiable rules
1. SDK freezes first; downstream repos consume, never redefine.
2. Canonical event log is runtime truth.
3. Outbox is a derived projection, not semantic truth.
4. Lineage is stored relationally in canonical storage.
5. Replay and restart correctness are promotion gates.