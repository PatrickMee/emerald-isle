# Mod and Save Compatibility Policy

The official game/DLC baseline is defined in `supported-platforms.md`.

## Support Claims

Support only game versions and DLC combinations explicitly tested in the current
matrix. `About.xml` support declarations must match evidence. External mods are
classified Tested, Best-effort, Known issue, Incompatible, or Unassessed.

Core Emerald Isle must load without optional DLC or integration targets unless a
separately packaged add-on explicitly says otherwise. Integrations are isolated
by load folders, conditional patches, or guarded code as appropriate.

## Defensive Compatibility

- Never overwrite external Defs wholesale or assume an optional target exists.
- Patch the narrowest node and handle already-modified or missing targets.
- Use stable package IDs, not display names, for dependency and load-order rules.
- Add load-before/after metadata only for demonstrated ordering requirements.
- Treat null, removed, destroyed, and unexpected subclass state as normal boundaries.
- Do not promise compatibility with all mods.

## Save Compatibility Levels

- **S0 None:** development build; save survival not promised.
- **S1 Same-version:** saves work across patch releases in one minor line.
- **S2 Forward migration:** supported older saves migrate to the current release.
- **S3 Removal-safe:** documented removal leaves a loadable save where feasible.

Every release declares its level. After 1.0, default is S2 unless release notes
explicitly identify a major breaking change. Never rename public Defs or serialized
types/fields without migration analysis and fixtures.

## Compatibility Matrix

Record game build, platform, DLC set, external mod/version/order, new/existing save,
scenario, expected result, actual result, evidence, date, and tester. Re-test based
on change risk, not an unbounded popularity list.
