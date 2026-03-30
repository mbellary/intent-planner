# Package Layout Conventions

## Source layout

All Python code is organized using a `src/` layout.

Expected import roots:
- `platform_sdk`
- `intent_planner`
- `control_plane`

## Bootstrap conventions

### Package roots
Each package root must:
- expose a stable import surface
- be side-effect free on import
- expose version metadata
- avoid runtime initialization during module import

### Infrastructure bootstrap
Runtime initialization must happen through explicit factories, not import-time side effects.

Examples:
- database engine factories
- session factories
- settings loaders
- startup hooks

## Configuration conventions

Configuration is environment-driven and typed using `pydantic-settings`.

Rules:
- settings classes must be explicit and typed
- environment variable prefixes must be repo-specific
- settings access should be cached behind an explicit accessor where appropriate
- tests must be able to override configuration without patching module globals irreversibly

## Alembic conventions

For `control-plane`:
- repo root contains `alembic.ini`
- repo root contains `alembic/env.py`
- migration versions live under `src/control_plane/infrastructure/db/migrations/versions/`

Alembic bootstrap must be functional even before business tables are introduced.