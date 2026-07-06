# FS-002 Dry-Stone Wall Test Evidence

**Status:** Working checkpoint, Version 0.1 artwork approved, and full-mod-list log reviewed; broader verification pending<br>
**Feature:** [FS-002 — Dry-Stone Wall](../../specifications/FS-002-dry-stone-wall.md)<br>
**Test date:** 2026-07-06<br>
**Tester:** Codex; human in-game reviewer Patrick Mee

## Environment

| Input | Value |
|---|---|
| Installed RimWorld data | `1.6.4871 rev595` |
| Observed runtime log | `RimWorld 1.6.4871 rev597` |
| Platform | macOS |
| Package ID | `patrickmee.emeraldisle` |
| Source branch | `004-dry-stone-wall-specification` |
| Staging command | `./tools/stage-mod.sh` |

## Evidence Artifacts

| Artifact | Purpose |
|---|---|
| [`screenshots/FS-002/2026-07-06-dry-stone-wall-junctions-and-room-overlay.png`](screenshots/FS-002/2026-07-06-dry-stone-wall-junctions-and-room-overlay.png) | Human-provided normal-zoom visual review showing dry-stone wall runs, junctions, selected/room overlays, and rock adjacency context |
| [`screenshots/FS-002/2026-07-06-debug-log-full-mod-list.png`](screenshots/FS-002/2026-07-06-debug-log-full-mod-list.png) | Human-provided debug-log screenshot showing active full mod list context and visible warnings |

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
| Linked rendering | Pass for visual checkpoint | Human reviewer reported the wall looks good. Preserved screenshot shows uninterrupted straight runs, readable T/cross-style connections, selection/room-overlay readability, and rock-adjacent context. Full material/junction matrix still pending. |
| Feature-specific load log | Pass with environment caveat | `Player.log` from RimWorld 1.6.4871 rev597 loaded `patrickmee.emeraldisle` and contained no `Emerald`, `EI_DryStoneWall`, XML-reference, missing-texture, or feature-specific error. |
| Overall clean log | Not established | The session used the owner's full mod list and reported one unattributed English translation-data error plus unrelated third-party warnings; repeat Core + Emerald Isle only |

### First Launch Environment Note

The installed package was launched on 2026-07-06 and `patrickmee.emeraldisle` was
present in the active mod configuration. The log contained no Dry-Stone Wall, XML,
reference, or missing-texture failure. A user-provided in-game screenshot confirms
that the wall appears in Architect → Structure with its custom icon and localized
description, and that Granite blocks cost 4. It was not a clean isolation run: the active
configuration also contained many Workshop mods, and the log reported unrelated or
unattributed warnings. Human art review approved the preceding linked rendering, then
requested RC2 and final polish to improve individual-stone readability. The supplied
normal-zoom screenshots support the final art freeze and visual checkpoint. Five-material
availability, full junction coverage, and a Core-only clean log still require confirmation.

### 2026-07-06 Player.log Review

The current macOS RimWorld log was read from the active Ludeon/Unity log location
after the human in-game checkpoint. The relevant findings are:

- RimWorld runtime reported `1.6.4871 rev597`.
- The active save loaded with `patrickmee.emeraldisle` present in the mod list.
- Search terms for `Emerald`, `emeraldisle`, `EI_DryStoneWall`, `DryStone`,
  `Dry-Stone`, XML failures, missing textures, and feature-specific errors found no
  Emerald Isle or Dry-Stone Wall failure.
- The visible warnings were not attributed to Emerald Isle: keybinding conflicts,
  one generic English translation-data error, a `HeatMapHelper` warning, hidden
  ritual precept additions, and several third-party mod messages.
- Emerald Isle English DefInjected localization was separately parsed with
  `xmllint --noout` for source and staged files. No XML parse error was found in
  `EI_DryStoneWall` or existing oats localization.

This is enough to support a feature-specific log pass in the owner's normal modded
environment. It is not enough to certify the overall clean-log requirement, because
the run was not Core + Emerald Isle only and the generic translation warning remains
unattributed without a generated RimWorld translation report.

No balance tuning is permitted during this checkpoint. Any broken atlas topology or
tint is an art defect; any mismatch in cost, HP, or work returns to implementation
without changing FS-002 values.
