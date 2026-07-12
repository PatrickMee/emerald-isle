# Testing Strategy

Testing follows changed behavior and credible failure risk. Test volume is not a
quality metric; useful evidence is evidence that would catch the defect being
guarded against.

## Baseline for Every Gameplay Change

1. Run relevant static/build validation.
2. Exercise one complete in-game path through the changed behavior.
3. Review the log for new errors or recurring warnings caused by the change.
4. Obtain human gameplay or visual review.

Routine non-gameplay work verifies only its affected surface.

## Risk-Triggered Checks

- **Save/load:** new or changed persistent state, public defs, bills, policies, or
  migrations.
- **DLC/mod combinations:** behavior or availability actually branches by
  configuration.
- **Regression automation:** a defect can be reproduced with a stable automated
  assertion or the same failure is likely to recur.
- **Performance:** code runs frequently, scales with map entities, allocates in a
  hot path, or introduces a measurable loading/runtime concern.
- **Long playtest:** balance, pacing, economy, storyteller interaction, or delayed
  state matters more than immediate function.
- **Compatibility/removal:** the change modifies public IDs, shared systems,
  patches, serialized state, or dependency boundaries.

Do not run a broad matrix merely because one exists. Do not waive a check when its
trigger is present.

## Release Evidence

Release candidates are tested from the exact staged package, not the developer
tree. Always verify package metadata, XML/load safety, texture paths, exclusion of
developer assets, clean load, and representative smoke paths. Recheck individual
features only when they or a shared dependency changed.

Record ordinary evidence once in the issue, PR, or feature record. Use a separate
matrix only for cross-feature, configuration, migration, or release-level work.
