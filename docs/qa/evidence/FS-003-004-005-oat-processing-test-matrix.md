# FS-003/FS-004/FS-005 Oat Processing Test Evidence

**Release:** Version 0.1 — The First Holding
**Features:** FS-003 Hand Quern, FS-004 Milled Oats, FS-005 Oat Foods
**Review date:** 2026-07-08
**Final smoke date:** 2026-07-10
**Source state:** `main`, synced with `origin/main` at `8d7ae3e`
**Status:** Gate 2 Done

This evidence record covers the bundled oat-processing vertical slice:

```text
raw oats
  ↓
hand quern
  ↓
milled oats
  ↓
oat porridge / oat flatbread
```

The slice is intentionally reviewed together because FS-003 and FS-004 are not
player-complete unless FS-005 provides finished food consumers.

## Implementation Contract Reviewed

| Area | Runtime contract |
|---|---|
| Hand quern | `EI_HandQuern`, `Building_WorkTable`, `BenchBase`, 1x1, Production designation, Bills tab |
| Quern labor | `EI_DoBillsMillOats`, `WorkGiver_DoBill`, Crafting work type, fixed to `EI_HandQuern` |
| Milling recipe | `EI_MillOats`, 10 `EI_RawOats` -> 10 `EI_MilledOats`, 180 work, Crafting, `GeneralLaborSpeed` |
| Milled oats | `EI_MilledOats`, manufactured intermediate, non-ingestible, 30-day rot timer |
| Porridge recipe | `EI_CookOatPorridge`, 10 `EI_MilledOats` -> 1 `EI_OatPorridge`, campfire/fueled stove/electric stove |
| Flatbread recipe | `EI_CookOatFlatbread`, 10 `EI_MilledOats` -> 1 `EI_OatFlatbread`, campfire/fueled stove/electric stove |
| Porridge food | `EI_OatPorridge`, simple-meal preferability, 0.9 nutrition, 2-day rot timer |
| Flatbread food | `EI_OatFlatbread`, simple-meal preferability, 0.8 nutrition, 14-day rot timer |
| Code policy | XML-only; no C#, Harmony, assembly, or custom framework |

## Automated and Static Validation

| Check | Result | Evidence |
|---|---:|---|
| Repository state before review | Pass | `git status --short --branch` reported clean `main...origin/main` |
| XML well-formedness | Pass | `find About Defs Languages Dev/Mod -type f -name '*.xml' -print0 \| xargs -0 xmllint --noout` |
| Production package staging | Pass | `./tools/stage-mod.sh` staged `build/EmeraldIsle` |
| Local RimWorld package staging | Pass | `./tools/stage-mod.sh "/Users/patrickmee/Library/Application Support/Steam/steamapps/common/RimWorld/RimWorldMac.app/Mods/EmeraldIsle"` |
| Developer mod staging | Pass | `./tools/stage-dev-mod.sh` staged `build/EmeraldIsleDevTools` |
| Release-safety guard | Pass | `./tools/validate-release-safety.sh build/EmeraldIsle` |
| Developer files excluded from production package | Pass | No `Dev`, `TestPacks`, or developer package files found in `build/EmeraldIsle` |
| Production staged file count | Pass | `build/EmeraldIsle` contains 26 files |
| Duplicate defName scan — production package | Pass | 11 unique defs, no duplicates |
| Duplicate defName scan — developer package | Pass | 7 unique defs, no duplicates |
| Runtime texture path resolution | Pass | All referenced production texture paths resolve in `Textures/` |
| Runtime texture dimensions | Pass | Quern 128x128, quern menu icon 64x64, milled oats 128x128, porridge 128x128, flatbread 128x128 |

## In-Game Evidence

Maintainer-provided in-game review during implementation confirmed:

- the hand quern is placeable and built successfully;
- the `mill oats` bill appears on the hand quern;
- pawns can produce milled oats from raw oats after the dedicated work giver fix;
- oat porridge and oat flatbread are produced at vanilla cooking stations;
- oat porridge and oat flatbread runtime art is readable in game;
- final oat food artwork was approved for Version 0.1.

The maintainer completed the final smoke test on 2026-07-10 and reported that
the complete slice works correctly in game.

## Runtime Art Provenance

The hand-quern, milled-oats, oat-porridge, and oat-flatbread runtime assets were
created specifically for Emerald Isle with OpenAI image-generation and editing
tools under Patrick Mee's art direction, iterative in-game review, and final
human approval. Historical and vanilla imagery informed the written direction
only; no third-party game texture or reference image was incorporated into the
runtime exports. In-game screenshots supplied during review were used to assess
readability and tinting, not as source pixels.

The exports were refined for transparent backgrounds, vanilla-scale readability,
Stuff tint behavior where applicable, palette, silhouette, and food identity.
They are governed by [`CREATIVE_ASSETS_LICENSE.md`](../../../CREATIVE_ASSETS_LICENSE.md).
No third-party attribution is required for these four assets.

## Defects Found and Resolved

| ID | Defect | Cause | Resolution | Status |
|---|---|---|---|---|
| WG-001 | Quern bill existed but no milling job was generated | `EI_HandQuern` had a bill recipe but no compatible `WorkGiver_DoBill` fixed to the custom work table | Added `EI_DoBillsMillOats` for Crafting bills at `EI_HandQuern` | Fixed |
| ART-001 | Hand quern material coloring and visibility were weak | Initial art/tint setup did not read clearly across stone materials | Reworked quern runtime art for stronger readability and stuff tint behavior | Fixed |
| ART-002 | Oat flatbread read too much like a generic baked item | Initial food art was too bright/saturated and insufficiently oat-like | Reworked food art toward rustic oatcake/flatbread identity | Fixed and approved |

## Design Review

| Review area | Result | Notes |
|---|---:|---|
| Gameplay value | Pass | The chain creates a simple processing choice without adding a new system: raw crop -> optional work investment -> food choice. |
| Vanilla fit | Pass | Uses vanilla work tables, bills, recipes, cooking stations, meal preferability, rotting, storage, and work types. |
| Historical authenticity | Pass | Domestic hand quern and simple oat foods remain consistent with the approved research direction. |
| Scope discipline | Pass | No powered mill, Harmony, C#, extra buildings, extra grains, or unapproved production systems were added. |
| Technical quality | Pass | XML-only, narrow public contracts, and release safeguards pass static validation. |
| Balance | Preliminary pass | Values match approved specs. Longer colony balance remains a Version 0.1 release-test concern. |
| Art and readability | Pass | Maintainer approved final oat food art; hand quern remains functional and readable enough for the current slice. |
| Compatibility | Pass | Static package and release-safety checks pass. Maintainer final smoke confirmed the exact staged package works in game. |

## Final Gate 2 Smoke Evidence

Patrick Mee reported on 2026-07-10 that the final staged package works correctly
in RimWorld. This confirms the required Gate 2 smoke path:

- clean RimWorld 1.6 Core load log with Emerald Isle enabled;
- save/load smoke test containing placed quern, bills, milled oats, oat porridge,
  and oat flatbread;
- no new red errors caused by Emerald Isle;
- confirmation that the package staged by `tools/stage-mod.sh` matches the
  package being tested.

## Gate 2 Recommendation

**Recommendation:** Done.
**Decision:** Done
**Approved by/date:** Patrick Mee, 2026-07-10
