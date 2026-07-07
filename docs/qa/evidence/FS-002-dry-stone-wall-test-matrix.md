# FS-002 Dry-Stone Wall Test Evidence

**Status:** Gate 2 Done passed; ready to merge<br>
**Feature:** [FS-002 — Dry-Stone Wall](../../specifications/FS-002-dry-stone-wall.md)<br>
**Test date:** 2026-07-06 to 2026-07-07<br>
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
| Proportional verification decision | Patrick Mee confirmed the five reduced smoke tests passed on 2026-07-07 |
| Gate 2 Design Review | Approved by Patrick Mee on 2026-07-07 |

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
| Material scope | Pass | Inherited material list replaced with `Stony` only; human smoke test confirmed the five Core materials are available and tint correctly |
| Prohibited implementation | Pass | No C#, Harmony, patch, resource, gate, variant, research, or ticker |
| Clean package staging | Pass | Existing staging contract copied source-identical runtime files |
| Structure menu | Pass | User-provided in-game screenshot shows Dry-Stone Wall in Architect → Structure |
| Menu icon and text | Pass | Screenshot shows the custom icon, localized description, Granite blocks selection, and cost of 4 |
| Five Core materials | Pass | Human smoke test confirmed granite, limestone, sandstone, slate, and marble are selectable/tint correctly |
| Linked rendering | Pass | Human reviewer reported the wall looks good. Preserved screenshot shows uninterrupted straight runs, readable T/cross-style connections, selection/room-overlay readability, and rock-adjacent context. Exhaustive atlas-cell screenshots are not blocking for this XML-only inherited wall. |
| Feature-specific load log | Pass with environment caveat | `Player.log` from RimWorld 1.6.4871 rev597 loaded `patrickmee.emeraldisle` and contained no `Emerald`, `EI_DryStoneWall`, XML-reference, missing-texture, or feature-specific error. |
| Overall clean log | Deferred to release integration | The session used the owner's full mod list and reported one unattributed English translation-data error plus unrelated third-party warnings. No Emerald Isle or Dry-Stone Wall failure was found. Core + Emerald Isle only clean-log certification is deferred to Version 0.1 release integration. |

## Checkpoint 2 — Proportional FS-002 Smoke Verification

Patrick Mee confirmed on 2026-07-07 that the reduced five-test verification set
passed. This reduced gate is accepted because FS-002 is a low-risk XML-only
definition that inherits vanilla `Wall` behavior, adds no C#, Harmony, custom comp,
ticker, custom save state, or global patch, and has already passed static staging,
art, and feature-specific log checks.

| Check | Result | Evidence |
|---|---|---|
| Load/log check | Pass | Current full-mod-list `Player.log` includes `patrickmee.emeraldisle` and contains no Emerald Isle, `EI_DryStoneWall`, XML-reference, or missing-texture failure. Overall clean-log certification is deferred to release integration. |
| Five material check | Pass | Human tester confirmed granite, limestone, sandstone, slate, and marble are selectable and tint correctly. |
| Visual linked-wall check | Pass | Human tester confirmed the wall looks good in game; screenshots preserve straight runs, room overlay, rock-adjacent context, and visible junction behavior. |
| Structural smoke test | Pass | Human tester confirmed a small enclosed room built with the wall forms the expected room/roof boundary. |
| Save/reload smoke test | Pass | Human tester confirmed a save containing the Dry-Stone Wall reloads with the wall present and rendering correctly. |

## Gate 2 Done and Design Review

FS-002 passed Gate 2 on 2026-07-07. The review applies the Constitution 3.0.0
three-gate lifecycle after the feature's earlier seven-gate planning records. The
older specification, architecture review, and implementation plan remain valid
historical decision records; they are not required as a pattern for later small
features.

| Review area | Result | Evidence |
|---|---|---|
| Gameplay | Pass | The wall creates a clear material-coverage versus durability/labor decision. It is useful when stone blocks are constrained and does not replace vanilla walls for speed or defense. |
| Historical integrity | Pass | The implementation remains a restrained cashel-inspired dry-stone perimeter wall. It does not add monuments, field-wall networks, gates, Irish UI terminology, or broader historical claims. |
| Vanilla fit | Pass | The feature uses one normal Structure command and inherits vanilla `Wall` behavior for construction, rooms, roofs, damage, repair, replacement, and save/load. |
| Technical quality | Pass | XML-only definition, no C#, no Harmony, no custom comp, no ticker, no custom save state, stable `EI_DryStoneWall` DefName, and source-identical staged package files. |
| Balance | Pass | Frozen values preserve the approved tradeoff: 4 stone blocks, base 240 HP, base 200 work, `Stony` materials only. No gameplay tuning was made during art or verification. |
| Art and presentation | Pass | Runtime atlas and menu icon are frozen for Version 0.1; human art review approved the wall and screenshots preserve normal-zoom evidence. |
| Scope discipline | Pass | One wall variant only. No new resources, gates, wall family, research, styles, rituals, generation, C#, Harmony, or extra wall systems. |
| Maintainability | Pass | Vanilla inheritance and project-owned assets keep the maintenance surface narrow. Deferred checks are release/regression concerns, not feature-blocking defects. |
| Compatibility | Pass with release deferrals | Feature-specific log review found no Emerald Isle or Dry-Stone Wall failure in the owner's modded environment. Core-only clean-log, Odyssey airtight, large-run, and external-mod samples are deferred to Gate 3 release integration. |

### Gate 2 Evidence Checklist

| Item | Result | Evidence or rationale |
|---|---|---|
| Acceptance, edge, failure, and safe-degradation scenarios | Pass, proportional | Static validation, in-game smoke checks, and human visual review cover the low-risk XML-only wall path. Exhaustive edge matrices are deferred to release/regression testing. |
| Static validation and useful automated checks | Pass | `./tools/stage-mod.sh` passes; package ID and supported RimWorld version are correct; XML parses with `xmllint --noout`. |
| Complete in-game player path | Pass | Human tester confirmed build-menu access, material selection, rendering, room/roof boundary behavior, and save/reload. |
| Save/load where state persists | Pass | Human tester confirmed the wall persists and renders correctly after reload. |
| Applicable compatibility and performance checks | Pass with bounded deferrals | No feature-specific log failures. No custom ticker or runtime code exists. Broader compatibility/performance matrix is deferred to Gate 3 because the implementation is declarative and inherited. |
| Logs contain no new unresolved feature errors | Pass | Current full-mod-list `Player.log` includes `patrickmee.emeraldisle` and no Emerald Isle, `EI_DryStoneWall`, XML-reference, or missing-texture failure. |
| Gameplay purpose and tradeoffs survive playtest | Pass | Maintainer accepted the material-efficient perimeter niche and proportional smoke test result. |
| Specification and Design Bible review | Pass | Feature remains within the frozen FS-002 scope, Version 0.1 approved scope, XML-first constraint, and Design Bible requirements. |
| Art/audio presentation | Pass | Art approved and frozen. No custom audio required; inherited wall sounds are sufficient. |
| Player text and terminology | Pass | English DefInjected label/description parse cleanly; no Irish-language player-facing term is introduced. |
| Project memory updates | Pass | Specification status, feature catalog, roadmap, README, changelog, and this evidence record are updated. |

**Decision:** Done
**Approved by/date:** Patrick Mee, 2026-07-07

### Deferred Non-Blocking Checks

The following checks remain useful for release integration or future regression
testing, but they are not blocking FS-002 Design Review under the proportional
testing decision:

- Core + Emerald Isle only clean-log certification.
- Exhaustive damage, repair, attachment, and replacement matrices.
- Every possible linked-atlas cell captured as separate screenshots.
- 250-tile mixed-material performance case.
- Odyssey airtight/vacuum parity.
- Broad external-mod compatibility samples.

### First Launch Environment Note

The installed package was launched on 2026-07-06 and `patrickmee.emeraldisle` was
present in the active mod configuration. The log contained no Dry-Stone Wall, XML,
reference, or missing-texture failure. A user-provided in-game screenshot confirms
that the wall appears in Architect → Structure with its custom icon and localized
description, and that Granite blocks cost 4. It was not a clean isolation run: the active
configuration also contained many Workshop mods, and the log reported unrelated or
unattributed warnings. Human art review approved the preceding linked rendering, then
requested RC2 and final polish to improve individual-stone readability. The supplied
normal-zoom screenshots support the final art freeze and visual checkpoint. The
five-material check, small-room structural smoke test, and save/reload smoke test
were later confirmed as passed by the human tester. Full release-matrix coverage is
deferred to Version 0.1 release integration.

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
unattributed without a generated RimWorld translation report. That broader clean-log
certification is deferred to Version 0.1 release integration.

No balance tuning is permitted during this checkpoint. Any broken atlas topology or
tint is an art defect; any mismatch in cost, HP, or work returns to implementation
without changing FS-002 values.
