# Version 0.1 Package and Build Contract

**Status:** Approved<br>
**Owner:** Patrick Mee<br>
**Created:** 2026-07-05<br>
**Approved by/date:** Patrick Mee, 2026-07-05<br>
**Decision:** [ADR-0002](../adr/0002-version-0.1-package-build-contract.md)<br>
**Gameplay content:** None<br>
**Implementation authorization:** None

## Stable Metadata

| Field | Value |
|---|---|
| Mod name | Emerald Isle |
| Author | Patrick Mee |
| Package ID | `patrickmee.emeraldisle` |
| Supported RimWorld version | `1.6` |
| Required content | RimWorld Core |
| Required DLC | None |
| Project URL | `https://github.com/PatrickMee/emerald-isle` |

`About/About.xml` is the canonical runtime metadata source. The package ID must not
change after acceptance without migration, load-order, distribution, and save-impact
review.

## Source and Staged Layout

```text
About/
  About.xml
Defs/
Languages/
  English/
    DefInjected/
      ThingDef/
Textures/
```

The initial staged package contains only `About/About.xml`; the other directories are
empty readiness boundaries. Source-control `.gitkeep` files are never staged.

The following are deliberately absent:

- `LoadFolders.xml`: no multiple-version or conditional load contract exists.
- `Assemblies/` and `Source/`: no C# is required.
- `Patches/`: no vanilla, DLC, or external-mod patch exists.
- `Defs/*.xml`: no gameplay definition is authorized.
- textures, localization entries, sounds, preview art, or placeholder objects.

## Staging Requirements

- Bash on macOS or Linux.
- `xmllint` from libxml2 available on `PATH`.
- A dedicated output directory that may be safely replaced by the staging script.

Stage and verify the infrastructure-only package:

```bash
./tools/stage-mod.sh --verify-empty
```

Default output:

```text
build/EmeraldIsle
```

Stage directly into the local macOS RimWorld Mods directory:

```bash
./tools/stage-mod.sh --verify-empty "/Users/patrickmee/Library/Application Support/Steam/steamapps/common/RimWorld/RimWorldMac.app/Mods/EmeraldIsle"
```

The destination is replaced on each run. Use only the dedicated `EmeraldIsle`
subdirectory, never the parent `Mods` directory.

After gameplay implementation is explicitly authorized, omit `--verify-empty`; the
same allowlisted staging process will copy approved runtime files while continuing to
exclude docs, tests, source art, source code, Git files, and editor metadata.

## Static Acceptance Check

The empty-package command must report:

```text
packageId: patrickmee.emeraldisle
supported RimWorld version: 1.6
empty package verification: passed
```

The staged package must contain no files under `Defs`, `Textures`, `Languages`,
`Patches`, `Sounds`, or `Assemblies`.

## Manual RimWorld 1.6 Verification

1. Close RimWorld.
2. Stage the package into the dedicated local Mods path shown above.
3. Launch RimWorld 1.6.
4. Open **Mods** and confirm `Emerald Isle` appears with author `Patrick Mee` and no
   unsupported-version warning.
5. Enable only Core and Emerald Isle, then allow RimWorld to restart.
6. Confirm the main menu loads without a red configuration or XML error.
7. Open the development-mode log and confirm Emerald Isle caused no error or warning.
8. Quit and inspect:
   `~/Library/Logs/Ludeon Studios/RimWorld by Ludeon Studios/Player.log`.
9. Record the exact RimWorld build, mod list, screenshot, log result, date, and tester
   in the package review.

Patrick Mee completed steps 3–9 against RimWorld 1.6.4871 rev597 on 2026-07-05.
Repeat the manual check whenever package metadata, staging, or supported-version
behavior changes.

## Empty-Package Review Record

| Check | Status | Evidence |
|---|---|---|
| Metadata XML parses | Pass | `xmllint --noout About/About.xml`, 2026-07-05 |
| Package ID is stable | Pass | Staging and RimWorld reported `patrickmee.emeraldisle` |
| Supported version is 1.6 | Pass | Staging reported `1.6` |
| No gameplay definitions | Pass | Empty-package verification, 2026-07-05 |
| No textures or localization content | Pass | Empty-package verification, 2026-07-05 |
| No C# assembly or Harmony | Pass | Empty-package verification, 2026-07-05 |
| Appears in Mods list | Pass | Verified by Patrick Mee, RimWorld 1.6.4871 rev597, 2026-07-05; mod shows correct name and author, no unsupported-version warning |
| Core-only restart is clean | Pass | Player.log 2026-07-05: `patrickmee.emeraldisle` loaded, `Mod Emerald Isle did not load any content` (expected for empty package), no Emerald Isle errors or warnings |

## Change Control

Changes to package ID, supported versions, load-folder routing, runtime-directory
allowlist, code/toolchain policy, or staging output contract require ADR review.
Ordinary script fixes that preserve the contract require tests and documentation but
do not require a new ADR.
