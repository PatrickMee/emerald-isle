# AR-002 — Dry-Stone Wall Architecture Review

**Status:** Draft — Human architecture review required<br>
**Feature:** [FS-002 — Dry-Stone Wall](../specifications/FS-002-dry-stone-wall.md)<br>
**Milestone:** Version 0.1 — The First Holding<br>
**Owner:** Patrick Mee<br>
**Prepared:** 2026-07-06<br>
**Vanilla reference build:** RimWorld 1.6.4871 rev595<br>
**Implementation plan:** [Spec Kit plan](../../specs/003-dry-stone-wall/plan.md)<br>
**Definition of Ready:** Not evaluated<br>
**Implementation authorized:** No

## Decision Summary

FS-002 will be represented by one public, Stuff-based building definition named
`EI_DryStoneWall`. It will inherit RimWorld Core's named `Wall` definition and
override only identity, the stone-only material filter, frozen cost/HP/work values,
UI ordering/hotkey behavior, and original linked graphics.

Inheritance preserves the normal wall contracts required by the approved
specification: construction, impassability, light/wind blocking, rooms, temperature,
roof support, wall attachments, doors, paint, replacement, damage, repair,
deconstruction, save/load, and eligible stone airtightness. No vanilla or DLC
definition is patched.

The architecture adds no C# assembly, Harmony patch, runtime component, ticker,
custom save state, research, resource, gate, compatibility adapter, or shared wall
framework.

## Feature Boundaries

### Implemented by FS-002

- One start-available buildable named `Dry-Stone Wall`.
- Four eligible stone blocks per tile.
- Base 240 HP and base 200 construction work before Stuff modifiers.
- The five Core stone blocks as the supported balance and visual set.
- Full normal wall structural behavior and bidirectional vanilla-wall replacement.
- Original linked wall atlas and construction-menu icon.
- English def-injected label and description.
- Static, in-game, persistence, Core/Odyssey, visual, performance, balance, and
  playtest evidence proportional to the specification.

### Explicitly Not Implemented

- Gates, doors, fences, barricades, curves, diagonals, corner objects, towers, or a
  wall family.
- Fieldstone, rubble, mortar, mixed-stone, new stone types, or gathering systems.
- Ringfort/cashel generation, named monuments, map generation, or settlement logic.
- Collapse, restacking, maintenance, erosion, weathering, moss, or deterioration.
- Combat bonuses, cover bonuses, beauty/mood auras, styles, rituals, or ideology.
- Custom blueprint gameplay, UI, work type, research, category, stat, or alert.
- Global patches or automatic interoperability with other wall/material mods.
- C#, Harmony, assemblies, custom serialization, or custom runtime behavior.
- Version 0.1 release packaging changes unrelated to adding the four runtime files.

## RimWorld Architecture

### Public Definition

| Public definition | Core parent | Responsibility | Runtime dependencies |
|---|---|---|---|
| `EI_DryStoneWall` | named Core `Wall` | Identity, material boundary, frozen balance values, custom art, and localization | Core wall, `Stony` Stuff, construction, linked graphics, rooms/roofs, attachments, replacement, paint, damage, save/load |

Core itself declares `Wall` as a named child of `BuildingBase`. Official Odyssey and
Anomaly content inherit `Wall`, so this is a verified supported inheritance seam in
the target build rather than an inferred convention.

No abstract Emerald Isle parent will be created. One wall does not demonstrate a
reusable project abstraction.

### Frozen Value Mapping

| FS-002 contract | Definition-level target | Expected Core result |
|---|---:|---|
| Stone cost | 4 Stuff units | 20% fewer blocks than vanilla wall's 5 |
| Durability | 240 base HP | 80% of same-material vanilla wall HP |
| Construction labor | 200 base work | `(200 + 140) / (135 + 140)` = approximately 123.6% of vanilla for current Core stone modifiers |
| Skill gate | None added | Same accessibility as ordinary wall |
| Research gate | None added | Available from the start |
| Material category | `Stony` only | Core sandstone, granite, limestone, slate, and marble are supported |
| Passability/rooms/roofs | Inherited | Normal full wall behavior |
| Airtightness | Inherited | Normal eligible Stuff-based wall behavior |
| Damage response | Inherited | Normal bomb/thump multipliers; lower HP supplies the weakness |
| Beauty/meditation | Inherited baseline | No feature-specific bonus |

Architecture may not tune these values. Any mismatch with actual in-game results is
an implementation defect or a specification issue requiring human review.

### Inherited Wall Contracts

| Core wall contract | FS-002 use | Reason to inherit |
|---|---|---|
| Building class and static ticker | Normal wall lifecycle with no recurring work | Satisfies XML-only and performance constraints |
| `Wall` replacement tag | Direct replacement with ordinary wall/fence-family structures where Core permits | Preserves normal construction workflow |
| Wall/Rock link flags and corner-filler linking | Links to walls and natural rock | Matches approved visual adjacency |
| Impassability, fill, light and wind blocking | Full-height perimeter and room boundary | Required by FS-002 |
| Heavy terrain and Stuff terrain affordance | Stone construction support | Matches same-material vanilla wall |
| Roof support and zone overlap rules | Normal roof/room behavior | Avoids hidden exterior-only exception |
| Paint, wall identity, and wall attachments | Standard paint, cooler, vent, and attachment integration | Required vanilla fit |
| Stuff-based airtight flag | Odyssey parity for eligible stone walls | Prevents vacuum exploit or surprise |
| Related door/cooler/vent commands | Normal adjacent-build workflow | No custom gate or UI needed |
| Minimal meditation component | Same baseline as vanilla wall | No new or stronger cultural benefit |
| Bomb and thump damage multipliers | Normal wall threat behavior | Lower HP is the only defensive change |
| Blueprint and damage presentation | Standard wall construction/damage readability | Avoids extra assets unless evidence rejects reuse |

### Required Overrides

| Concern | Architecture decision | Failure prevented |
|---|---|---|
| Identity | Stable `EI_DryStoneWall` public name and localized English text | Save/reference collisions and hard-coded UI text |
| Material list | Replace inherited Metallic/Woody/Stony list with Stony only | Wood or metal violating approved scope |
| Cost and stats | Override cost 4, base HP 240, base work 200 | Balance drift from vanilla wall |
| Graphic | Use `Graphic_Single` with one original neutral-grayscale atlas while inheriting `CornerFiller` and Wall/Rock link flags | Cosmetic clone and broken junctions |
| Menu icon | Use a dedicated original icon | Player cannot distinguish build commands |
| Stuff-specific icon list | Clear inherited Wall icon mappings | Core `Bricks` appearance silently displays vanilla wall icon |
| UI order | Use `2001`, immediately after ordinary wall's `2000` in Structure ordering | Feature is hard to discover or appears unrelated |
| Hotkey | Clear the inherited wall hotkey | Two Structure commands compete for one shortcut |

The implementation must use explicit list replacement where XML inheritance would
otherwise merge material or icon entries. It must not rely on accidental loader
behavior.

### Vanilla Systems Used

| System | Use | Change to vanilla content |
|---|---|---|
| Definition database and inheritance | Load one child of Core `Wall` | None |
| Stuff and stone blocks | Material selection, tint, HP/work/value modifiers, sounds, terrain affordance | None |
| Construction | Designation, hauling, frames, builders, work, completion, failure | None |
| Linked graphics/map mesh | Ends, runs, corners, junctions, wall/rock adjacency | None |
| Structure designator | Player discovery and material selection | None |
| Rooms and temperature | Boundary, light/wind block, heating/cooling | None |
| Roof system | Support, collapse rules after destruction/removal | None |
| Doors and attachments | Vanilla doors, vents, coolers, and supported attachments | None |
| Paint and style presentation | Normal inherited paint and material color | None; no custom style |
| Combat/damage | Projectiles, melee, explosions, thump/breach, fire, repair | None |
| Replacement/deconstruction | Wall conversion and resource handling | None |
| Localization | Def-injected English label and description | None |
| Save/load | Definition reference plus vanilla building state | None |
| Odyssey atmosphere | Inherited Stuff-based airtight wall behavior | None |

## Required Assets

### Game-Ready Art

| Asset ID | Planned file | Runtime path | Purpose |
|---|---|---|---|
| `EI_DryStoneWall_Atlas` | `Textures/Things/Building/Linked/DryStoneWall/EI_DryStoneWall_Atlas.png` | `Things/Building/Linked/DryStoneWall/EI_DryStoneWall_Atlas` | All linked map states through the inherited corner-filler contract |
| `EI_DryStoneWall_MenuIcon` | `Textures/Things/Building/Linked/DryStoneWall/EI_DryStoneWall_MenuIcon.png` | `Things/Building/Linked/DryStoneWall/EI_DryStoneWall_MenuIcon` | Structure menu and material-selection command |

The atlas target is a 256×256 transparent RGBA PNG using RimWorld's 4×4 linked-wall
layout with 64×64 cells. The icon target is a 64×64 transparent RGBA PNG. Both use
neutral grayscale values so normal Stuff tint preserves the five Core stone colors.
No color mask, animation, rotation set, source photograph, or copied mod art is
planned.

The first art checkpoint must verify the atlas layout, Stuff tint, alpha edges,
normal-zoom silhouette, every junction, and the icon in game. If the target build
proves a different export contract, implementation stops and AR-002 is corrected
before additional assets are created.

### Reused Core Presentation

- Inherited wall blueprint atlas.
- Inherited damage overlays.
- Inherited stone construction, impact, repair, and destruction sounds.
- Normal selection, placement, paint, snow, rain, night, and damage presentation.

### Localization

English def-injected localization supplies:

- `EI_DryStoneWall.label`: `dry-stone wall`
- `EI_DryStoneWall.description`: `An impassable wall of carefully stacked stone,
  built without mortar. It uses fewer stone blocks than a standard wall, but takes
  longer to build and is less durable.`

No Irish term is player-facing. Translator context belongs in the localization file
or adjacent project convention, and no text may be embedded in art.

## File Plan

### Files created during implementation

| File | Purpose |
|---|---|
| `Defs/ThingDefs_Buildings/EI_DryStoneWall.xml` | One public wall definition |
| `Languages/English/DefInjected/ThingDef/EI_DryStoneWall.xml` | English label and description |
| `Textures/Things/Building/Linked/DryStoneWall/EI_DryStoneWall_Atlas.png` | Linked wall art |
| `Textures/Things/Building/Linked/DryStoneWall/EI_DryStoneWall_MenuIcon.png` | Build-menu icon |
| `docs/art/assets/FS-002-dry-stone-wall.md` | Asset provenance and acceptance evidence |
| `docs/qa/evidence/FS-002-dry-stone-wall-test-matrix.md` | Current technical and playtest evidence |

### Files modified as state changes

| File | Purpose |
|---|---|
| `docs/specifications/FS-002-dry-stone-wall.md` | Architecture, Ready, implementation, verification, and review status only |
| `docs/product/feature-catalog.md` | BL-01 lifecycle state |
| `docs/roadmap.md` | Current Version 0.1 state |
| `README.md` and `docs/README.md` | User/contributor status and document map |
| `CHANGELOG.md` | Player-visible unreleased feature entry |

### No planned change

`About/About.xml`, `LoadFolders.xml`, `tools/stage-mod.sh`, `Patches/`, `Assemblies/`,
and `Source/` remain unchanged. If the four runtime files cannot stage through the
existing package contract, implementation stops because that contradicts ADR-0002.

## Compatibility

### RimWorld 1.6 Core

Core owns every required runtime system. The feature must load with Core and Emerald
Isle only. The build menu, five Core stones, construction path, rooms, roofs, doors,
attachments, paint, damage, replacement, and save/load are mandatory feature checks.

### Supported DLC

| DLC | Architecture behavior |
|---|---|
| Royalty | Inherited minimal wall meditation behavior only; no new benefit |
| Ideology | Normal wall/paint presentation; no Emerald Isle style, precept, or preference |
| Biotech | Normal construction and threat behavior; no integration |
| Anomaly | Inherited related security-door command where Core's conditional reference permits; no containment bonus |
| Odyssey | Inherited Stuff-based airtight and wall-adjacent behavior; explicit vacuum comparison required |

No DLC definition is referenced directly by Emerald Isle. Conditional related-build
commands are inherited from Core's wall definition, which already guards DLC absence.

### External Mods

- Wall texture replacements may not alter the project-owned atlas; compatibility is
  best-effort and tested against one current representative.
- Broad architecture mods coexist through unique public IDs; no automatic unification
  or load-order rule is added.
- Modded materials declaring the Stony Stuff category may appear as options. Their
  declared tint and stat factors apply normally, but only Core stones are balanced
  and supported.
- No external definition is patched or overwritten.

### Vanilla Expanded Philosophy

The feature follows the relevant philosophy—familiar vanilla verbs, readable stats,
and restrained scope—but has no dependency, integration, copied asset, or claim of
formal compatibility with Vanilla Expanded. A targeted sample may be tested only if
it materially touches walls or stony Stuff.

### Existing Saves and Removal

Adding the Def is low risk: existing maps and structures are unchanged, and the new
build command becomes available. Same-version save/load is required once walls exist.

Removing Emerald Isle from a save containing `EI_DryStoneWall` is unsupported. Missing
walls can expose rooms, temperature, roofs, defenses, or Odyssey vacuum. This cannot
be made removal-safe without scope and migration machinery disproportionate to
Version 0.1.

## Save and Public Contracts

These identifiers become durable when a public build containing FS-002 is released:

| Contract | Identifier or path | Consequence of change |
|---|---|---|
| Wall definition | `EI_DryStoneWall` | Existing walls, frames, blueprints, bills/designations, and references can break or disappear |
| Label key | `EI_DryStoneWall.label` | Existing translations become orphaned |
| Description key | `EI_DryStoneWall.description` | Existing translations become orphaned |
| Linked atlas path | `Things/Building/Linked/DryStoneWall/EI_DryStoneWall_Atlas` | Map rendering and replacement art break |
| Menu icon path | `Things/Building/Linked/DryStoneWall/EI_DryStoneWall_MenuIcon` | Build command icon breaks |
| Package ID | `patrickmee.emeraldisle` | Existing package/load-order identity breaks; governed by ADR-0002 |

The Wall parent, Stony category, Wall replacement tag, link flags, structural
behavior, cost, HP, and work are behavioral contracts even though they are not new
public identifiers. Changes require specification and save/compatibility review.

No research ID, recipe ID, C# type, serialized field, API, Harmony target, or new
package/load-order contract is created.

## Verification Architecture

### Static and Package Checks

- Parse every staged XML file.
- Reject duplicate public IDs and unresolved definition references.
- Verify exact-case texture and localization paths.
- Verify PNG dimensions, RGBA mode, alpha bounds, and required files.
- Stage through `tools/stage-mod.sh` and compare the staged runtime tree with source.
- Confirm no C#, Harmony, patches, unplanned defs, or source/editor files enter the package.

### In-Game Checkpoints

1. Core-only clean load and log review.
2. Structure-menu discovery, custom icon, and five Core materials.
3. Per-material cost, work, HP, tint, construction, damage, repair, and deconstruction.
4. All isolated/end/straight/corner/T/cross links plus walls, rock, doors, and fences.
5. Rooms, roofs, temperature, coolers, vents, attachments, paint, and bidirectional replacement.
6. Save/load of completed, damaged, framed, painted, attached, roof-supporting, and replacement states.
7. Odyssey airtight/vacuum parity with same-material vanilla walls.
8. Development-spawned 250-tile mixed-material visual/performance case.

No unit-test assembly is justified for one declarative definition. Static validation
and observable in-game integration are the regression evidence that can catch the
actual failure modes.

## Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Inherited Stuff-specific icon list shows vanilla icon | High without override | Medium | Explicitly clear the inherited icon list; verify every Core stone command |
| XML list inheritance admits wood/metal or merges stale entries | Medium | High | Replace the material list explicitly and inspect loaded options in game |
| Inherited wall hotkey collides in Structure menu | Medium | Low | Clear the inherited hotkey and verify menu navigation |
| Atlas layout or alpha is wrong | Medium | High | First-slice load test covers every junction before further work |
| Neutral art tints poorly for one Core stone | Medium | Medium | Review all five materials at normal zoom and revise the source asset, not runtime logic |
| Lower cost becomes a universal room-wall choice | Medium | High | Preserve frozen HP/work penalties and execute controlled perimeter/playtest comparisons |
| Replacement loses attachments or destabilizes roofs | Medium | High | Test both replacement directions with attachments and roofs before approval |
| Odyssey airtight behavior diverges from vanilla | Low | High | Inherit `Wall` and compare incomplete, complete, damaged, and destroyed sections in Odyssey |
| Modded Stony Stuff creates extreme values or poor art | Medium | Medium | Officially support Core stone only; document best-effort behavior |
| Public Def or texture path changes after release | Low | High | Freeze contracts here and require migration review for changes |
| Mod removal damages saves | High when removed | High | Declare removal unsupported and publish warnings |
| A future wall pressures a premature framework | Medium | Medium | Generalize only after multiple implemented features demonstrate the same need |

## Constitution Review

| Principle | Result | Evidence |
|---|---|---|
| Gameplay/story first | Pass by approved spec | Material coverage creates a labor and breach-risk decision |
| RimWorld-native fit | Pass | One normal Structure command using familiar wall behavior |
| Research with transformation | Pass | Cashel inspiration becomes an original Rim perimeter choice without monument reconstruction |
| Tradeoffs over power | Pass | 20% material saving pays 20% HP and approximately 24% work penalties |
| Milestone discipline | Pass | Exactly one wall; no gate, resource, generation, code, or later scope |
| XML-first | Pass | One inherited definition and def-injected localization; no code or patch |
| Whole-system verification | Pass for planning | Full build, structure, damage, persistence, Odyssey, art, and playtest paths are defined |
| Modular compatibility | Pass | Unique Def, no external patches, Core-only dependency, no custom state |
| Proportionality | Pass | AR protects linked-art/save/DLC contracts; no IP-002, framework, or test assembly |

## ADR Review and Recommendation

ADR-0001 is specific to Oats and does not apply. AR-002 conforms to ADR-0002's
package ID, RimWorld 1.6 support, no-assembly policy, and existing staging layout.

This review introduces no Harmony patch, assembly, save schema, API, hard dependency,
load-order rule, package change, generated-asset pipeline, or shared framework. No
new ADR is required.

**Recommendation:** Approve AR-002. After approval, evaluate the project Definition
of Ready and obtain explicit implementation authorization. Do not implement FS-002
from this draft architecture review.
