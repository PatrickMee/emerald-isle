# Version 0.1 Release Test Matrix

**Status:** Release matrix passed with explicit C4 waiver
**Feature set:** FS-001 Oats, FS-002 Dry-Stone Wall, FS-003 Hand Quern,
FS-004 Milled Oats, and FS-005 Oat Foods (per the
[v0.1 release checklist](../release/v0.1-release-checklist.md))
**Policy:** [Supported platforms](../engineering/supported-platforms.md) — test
Core-only plus the all-supported-DLC configuration at minimum; no v0.1 feature
requires or enhances a specific DLC, so per-DLC solo runs are risk-based only.

## Environment

Record before executing. All runs use the exact archive produced by
`tools/stage-mod.sh` from the frozen release commit, not the working tree.

| Input | Value |
|---|---|
| RimWorld build | 1.6.4871 rev597 |
| Release commit | `fad78944a45b3285da5888c8c232995b7075d80d` (`v0.1.0`); human-tested runtime candidate `999990dbdf16579620c75488a3871455e7044926` is byte-identical |
| Archive | Published `EmeraldIsle-v0.1.0.zip`; 26 files; SHA-256 `94de4d0a05eddc111a645c517c9d4647115b215b947e910e467c50ed2f7f5b16` |
| Platform | macOS |
| Tester | Patrick Mee |
| Date | 2026-07-11 |

## Configuration Runs

| ID | Configuration | Save state | Result | Evidence |
|---|---|---|---|---|
| C1 | Core + Emerald Isle only | New colony | Pass | Maintainer confirmation, 2026-07-11: clean load and complete feature paths looked good |
| C2 | Core + Emerald Isle only | Existing vanilla save, mod added | Pass | Maintainer confirmation, 2026-07-11: existing-save addition and reload worked |
| C3 | All supported DLC + Emerald Isle | New colony | Pass | Maintainer confirmation, 2026-07-11: requested DLC configuration and feature smoke tests were good |
| C4 | Core + Emerald Isle, then mod removed | Save with planted oats, stored oats/milled oats/oat foods, built walls, placed quern, and active bills | Waived | Explicitly waived by Patrick Mee, 2026-07-11; rationale below |

### C4 Waiver

Patrick Mee explicitly waived the destructive removal test on 2026-07-11. The
accepted risk is low because Version 0.1 is XML-only, introduces no C# assembly,
Harmony patch, custom serialized state, world component, map component, or
migration code, and uses ordinary RimWorld definitions and persistence. Removal
is still documented as unsupported for content preservation: missing-definition
warnings and loss of Emerald Isle plants, items, buildings, bills, filters, and
policy references are expected. The waiver is not recorded as a test pass.

## Per-Configuration Checks

Run in C1 and C3; C2 checks load and player path only; C4 checks documented
degradation (missing-Def warnings, content loss) matches release notes.

### Load and Logs

- [x] Clean load with no Emerald Isle errors or warnings in the log
- [x] Core + Emerald Isle only clean-log certification
      (deferred from FS-002 Gate 2 evidence — this is the closing check)
- [x] Mod list order has no load-order warnings

Evidence: Patrick Mee confirmed the requested C1 and C3 load, log, and feature
checks on 2026-07-11. The package declares only Core ordering and no DLC or mod
dependency.

### FS-001 Oats

- [x] Sow, grow, harvest oats through the full cycle
- [x] Raw oats usable in meals, nutrient paste, and animal feed; tradeable
- [x] Oats rot at the specified shelf life; no hydroponics sowing allowed
- [x] Save/load mid-growth and with stored oats preserves state

Evidence: current C1–C3 confirmations close the release configurations; detailed
crop, item, inheritance, save/load, rot-timer, Ground-only sowing, and integration
evidence is recorded in
[FS-001 Oats Test Evidence](evidence/FS-001-oats-test-matrix.md).

### FS-002 Dry-Stone Wall

- [x] Buildable in all five Core stone types with correct tinting
- [x] Linked rendering, room formation, and roof support behave as specified
- [x] Save/load with built and blueprinted walls preserves state

Evidence: current C1–C3 confirmations close the release configurations; five-stone,
linked-rendering, room/roof, and save/reload evidence is recorded in
[FS-002 Dry-Stone Wall Test Evidence](evidence/FS-002-dry-stone-wall-test-matrix.md).

### FS-003 / FS-004 Hand Quern and Milled Oats

- [x] Quern buildable; milling bill converts raw oats to milled oats as specified
- [x] Milled oats usable per specification; whole-chain labor and value hold
- [x] Save/load with an active bill, work in progress, and stored milled oats

Evidence: current C1–C3 confirmations close the release configurations. The
complete quern path and a save/load smoke with quern bills and stored products are
recorded in
[Oat Processing Test Evidence](evidence/FS-003-004-005-oat-processing-test-matrix.md).
Active-bill and work-progress persistence use the unchanged Core bill contract;
the feature adds no custom state or serialization.

### FS-005 Oat Foods

- [x] Cook oat porridge and oat flatbread from milled oats at the supported Core
      cooking buildings
- [x] Food policies, storage, caravans, traders, animals, prisoners, babies, and
      nutrient paste do not select the foods outside their specified roles
- [x] Porridge and flatbread nutrition, work, mass, value, and spoilage preserve
      the intended fresh-food versus portable-food tradeoff
- [x] Save/load with stored foods, active cooking bills, stockpile settings, and
      food policies preserves state

Evidence: production of both foods and save/load were confirmed in the current
configuration runs and prior Gate 2 smoke. Policy, storage, caravan, trader,
feeding, and persistence behavior is inherited from Core `MealBase`, narrow recipe
filters, and standard definitions; no custom selector, comp, or serialized state
exists.

### Whole-Chain Balance (release-blocking, deferred from FS-001)

- [x] Oats occupy a rational niche against rice, potatoes, and corn in at least
      one colony plan without dominating all plans
- [x] Milling earns its labor against eating raw oats; neither mandatory nor empty

### Static Balance Verification

Installed RimWorld 1.6.4871 Core definitions and the exact Version 0.1 XML produce
the following comparison before pawn, health, biome, weather, and difficulty
modifiers:

| Path | Output / advantage | Cost / constraint | Result |
|---|---|---|---|
| Rice | 0.10000 nutrition per tile per grow-day | 3-day cycle; 1.0 fertility sensitivity | Highest base rate and most field cycles |
| Potatoes | 0.09483 nutrition per tile per grow-day | 5.8-day cycle; 0.4 fertility sensitivity | Best marginal-soil option |
| Oats | 0.09375 nutrition per tile per grow-day | 8-day cycle; Ground-only; 45-day shelf life | Intermediate timing and labor; lowest base nutrition rate |
| Corn | 0.09735 nutrition per tile per grow-day | 11.3-day exposure; Ground-only | Best field-work efficiency and longest storage |
| Raw → milled oats | Count, value, and mass remain 10 → 10, 11 → 11, and 0.30 → 0.30 | 180 Crafting work; shelf life falls 45 → 30 days; input loses flexibility | No nutrition, value, mass, or preservation upgrade |
| Oat porridge | 0.9 nutrition; 120 final Cooking work | 180 prior milling work; total 300; 2-day shelf life; narrow input and extra logistics | Matches simple-meal total work but is less flexible and keeps half as long |
| Oat flatbread | Plant-only ready food; 14-day shelf life | 0.8 nutrition; total 600 work; narrow input; 0.44 mass | Moderate reserve, materially below pemmican's 70 days and survival meals' indefinite storage |
| Dry-stone wall | 20% fewer blocks | 20% lower base HP and 48.15% higher base work before ordinary material modifiers | Material coverage trades defense and labor |

The implemented values exactly match the frozen specifications. Patrick Mee's
Gate 2 and C1–C3 smoke confirmations found the paths usable. For this first preview,
the balance hypotheses pass with the explicit expectation that post-release colony
feedback may justify tuning without changing feature identity.

### Performance

- [x] No observable stutter or log spam in a colony using all v0.1 content at
      representative scale

Evidence: C1 and C3 completed without reported stutter or Emerald Isle log spam.
The package contains only declarative definitions and vanilla behavior: no C#,
Harmony, custom tickers, scans, map/world components, or custom serialization.

## Sign-Off

| Check | Result | Date |
|---|---|---|
| Required configuration outcomes | Pass with explicit C4 waiver | 2026-07-11 |
| Matrix blockers resolved or explicitly waived with rationale | Pass | 2026-07-12 |
| Evidence linked from the v0.1 release checklist | Pass | 2026-07-11 |

## Published Artifact Verification

The GitHub release artifact was downloaded after publication on 2026-07-12. Its
SHA-256 matched the pre-publication archive, extraction produced exactly 26 files,
all XML parsed, release-safety validation passed, package metadata reported
`patrickmee.emeraldisle` and RimWorld 1.6, and `diff -qr` found no difference from
the staged package that passed human in-game testing.
