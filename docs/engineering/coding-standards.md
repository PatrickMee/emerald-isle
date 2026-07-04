# Engineering Standards

**Status:** Stable baseline at v0.0.0. Material changes normally require an ADR.

## General

- Prefer the smallest supported RimWorld extension point.
- Keep domain behavior together and dependencies explicit.
- Validate inputs at load boundaries and fail optional integrations safely.
- Comments explain intent, invariants, compatibility hazards, or source reasoning.
- Treat warnings, unresolved references, and repeated log errors as defects.

## XML Conventions

- Prefix public def names with `EI_`; use stable, descriptive PascalCase suffixes.
- Group defs by gameplay domain, not by contributor or release.
- Use inheritance only when it expresses a real shared contract.
- Keep player-facing strings in localization; XML labels are not a substitute.
- Use patch operations for external content. Never replace an entire external def
  when a narrow operation works.
- Document load-order assumptions and test missing optional targets.
- Preserve public def names after release or supply a migration strategy.

## C# Conventions

- Use the repository SDK and language version once selected; do not rely on a
  developer machine's implicit configuration.
- Root namespace is `EmeraldIsle`; public API surface stays minimal.
- Nullable analysis and analyzers should be enabled when the initial project is
  created. New warnings are not accepted without rationale.
- Separate pure decision logic from RimWorld state access so it can be tested.
- Avoid per-tick work; cache only with explicit invalidation and lifecycle rules.
- Serialization fields are compatibility contracts. Test new, old, and missing
  values and document migrations.
- Harmony patches require an ADR, the narrowest viable target, a guarded prepare
  path, conflict analysis, and behavior tests.

## Logging and Errors

Prefix messages with `[Emerald Isle]`, include actionable context, avoid secrets
or personal paths, and prevent recurring spam. Recover only when the resulting
state remains valid; otherwise fail clearly at the earliest safe boundary.
