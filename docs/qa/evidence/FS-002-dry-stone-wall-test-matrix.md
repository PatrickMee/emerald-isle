# FS-002 Dry-Stone Wall Test Evidence

**Status:** Working/art checkpoint approved; broader verification pending<br>
**Feature:** [FS-002 — Dry-Stone Wall](../../specifications/FS-002-dry-stone-wall.md)<br>
**Test date:** 2026-07-06<br>
**Tester:** Codex; human in-game reviewer Patrick Mee

## Environment

| Input | Value |
|---|---|
| Installed RimWorld data | `1.6.4871 rev595` |
| Platform | macOS |
| Package ID | `patrickmee.emeraldisle` |
| Source branch | `004-dry-stone-wall-specification` |
| Staging command | `./tools/stage-mod.sh` |

## Checkpoint 1 — First Working Wall

| Check | Result | Evidence |
|---|---|---|
| XML well formed | Pass | `xmllint --noout` on metadata, definition, and localization |
| Public identifier | Pass | Exactly one project definition: `EI_DryStoneWall` |
| No Core/DLC collision | Pass | Identifier absent from installed RimWorld 1.6 Core/DLC XML |
| Linked atlas contract | Pass | Verified 4×4/16-state CornerFiller order; matches AR-002 |
| Texture files | Pass | 256×256 atlas and 64×64 icon are case-correct RGBA PNGs with alpha |
| Frozen values | Pass | Cost 4, base HP 240, base work 200; no tuning |
| Material scope | Pass (static) | Inherited material list replaced with `Stony` only; in-game options pending |
| Prohibited implementation | Pass | No C#, Harmony, patch, resource, gate, variant, research, or ticker |
| Clean package staging | Pass | Existing staging contract copied source-identical runtime files |
| Structure menu | Pass | User-provided in-game screenshot shows Dry-Stone Wall in Architect → Structure |
| Menu icon and text | Pass | Screenshot shows the custom icon, localized description, Granite blocks selection, and cost of 4 |
| Five Core materials | Pending in-game | Human verification required |
| Linked rendering | Pass (human art review) | Patrick Mee reported the linked atlas and normal-zoom readability working well and approved release-candidate revision 4 |
| Feature-specific load log | Pass with environment caveat | RimWorld 1.6.4871 rev597 loaded the active Emerald Isle package with no `EI_DryStoneWall`, XML-reference, or missing-texture error |
| Overall clean log | Not established | The session used the owner's full mod list and reported one unattributed English translation-data error plus unrelated third-party warnings; repeat Core + Emerald Isle only |

### First Launch Environment Note

The installed package was launched on 2026-07-06 and `patrickmee.emeraldisle` was
present in the active mod configuration. The log contained no Dry-Stone Wall, XML,
reference, or missing-texture failure. A user-provided in-game screenshot confirms
that the wall appears in Architect → Structure with its custom icon and localized
description, and that Granite blocks cost 4. It was not a clean isolation run: the active
configuration also contained many Workshop mods, and the log reported unrelated or
unattributed warnings. Human art review subsequently approved the linked rendering
and normal-zoom readability. Five-material availability and a Core-only clean log
still require confirmation.

No balance tuning is permitted during this checkpoint. Any broken atlas topology or
tint is an art defect; any mismatch in cost, HP, or work returns to implementation
without changing FS-002 values.
