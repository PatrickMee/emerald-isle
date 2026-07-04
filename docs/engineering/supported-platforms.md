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
feature specification explicitly declares a DLC as required and product governance
accepts that dependency. DLC integrations must be isolated and fail safely.

## Mandatory Feature Fields

Every future feature specification must state:

- **Required DLC:** DLC without which the feature is unavailable
- **Optional DLC enhancements:** additional behavior enabled by each supported DLC
- **Behavior without DLC:** fallback, omission, or safe degradation
- **Save compatibility:** state, migration, add/remove DLC, and removal implications

The implementation plan must map these statements to load folders, conditional
patches, guarded code, tests, and release notes as applicable.

## Test Matrix

At minimum, test Core-only plus every DLC the feature requires or enhances, both
alone where meaningful and in the all-supported-DLC configuration. Risk-based
pairwise combinations are added when systems interact. Record the exact RimWorld
build, DLC set, new/existing save, scenario, evidence, and result.
