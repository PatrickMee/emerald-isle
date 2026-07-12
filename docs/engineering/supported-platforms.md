# Supported RimWorld and DLC Policy

**Baseline:** v0.0.0  
**Effective:** Version 0.1 planning

## Required Platform

- RimWorld 1.6
- Core game content

Older RimWorld versions are unsupported unless a future roadmap and release record
explicitly add them. Support claims apply to tested 1.6 builds; game updates may
require revalidation before a project release is declared compatible.

## Officially Supported DLC

- Royalty
- Ideology
- Biotech
- Anomaly
- Odyssey

Core functionality must remain coherent with none of these DLCs enabled unless a
feature record explicitly declares a DLC as required and product governance
accepts that dependency. DLC integrations must be isolated and fail safely.

## Mandatory Feature Fields

Every gameplay feature record must state, concisely:

- **Required DLC:** DLC without which the feature is unavailable
- **Optional DLC enhancements:** additional behavior enabled by each supported DLC
- **Behavior without DLC:** fallback, omission, or safe degradation
- **Save compatibility:** state, migration, add/remove DLC, and removal implications

High-Risk work maps relevant statements to load folders, conditional patches,
guarded code, tests, migration, and release notes. A standalone implementation
plan is not required when the feature record or PR is sufficient.

## Test Matrix

Test Core-only for ordinary shared content. Add every DLC the feature requires or
enhances, alone or in combinations only where behavior meaningfully differs.
Version-level release smoke may cover the all-supported-DLC configuration. Record
the exact configuration once in the PR, feature record, or release evidence.
