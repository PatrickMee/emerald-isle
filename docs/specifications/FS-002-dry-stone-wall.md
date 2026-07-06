# FS-002 — Dry-Stone Wall

**Status:** Approved — Frozen<br>
**Specification gate:** Approved by Patrick Mee, 2026-07-05<br>
**Milestone:** Version 0.1 — The First Holding<br>
**Catalog feature:** BL-01<br>
**Feature branch:** `004-dry-stone-wall-specification`<br>
**Owner:** Patrick Mee<br>
**Created:** 2026-07-05<br>
**Vanilla balance baseline:** RimWorld 1.6.4871 rev595<br>
**Specification QA:** [Passed](../../specs/003-dry-stone-wall/checklists/requirements.md)<br>
**Feature Acceptance:** [Accept for planning](checklists/FS-002-dry-stone-wall-feature-acceptance.md)<br>
**Architecture gate:** [AR-002 approved by Patrick Mee, 2026-07-06](../architecture/AR-002-dry-stone-wall.md)<br>
**Definition of Ready:** Passed by Patrick Mee, 2026-07-06<br>
**Implementation authorized:** Yes — Patrick Mee, 2026-07-06<br>
**Implementation status:** Checkpoint 1 and release-candidate art approved by Patrick Mee, 2026-07-06; broader verification pending

## Authority and Boundaries

This specification defines what the Dry-Stone Wall feature must do. It conforms to
the [Version 0.1 approved scope](../product/version-0.1-approved-scope.md),
[Version 1.0 Vision](../product/version-1.0-vision.md), and approved
[Dry-Stone Wall research brief](../research/version-0.1/dry-stone-wall.md).

It deliberately contains no source markup, code, Harmony patch, public runtime
identifier, file layout, inheritance choice, texture path, or implementation
sequence. Those decisions belong to architecture review after human approval.

## Purpose

### Historical Purpose

The wall gives Version 0.1 an architectural anchor drawn from dry-built stone
enclosures associated with early medieval Irish cashels and ordinary holdings.
It represents the use of local stone and skilled labor to define and protect a
domestic enclosure, not a reconstruction of one named monument or a claim that all
Irish settlements used the same wall form.

The feature must not conflate early medieval cashel enclosures with the extensive
nineteenth-century field-wall landscapes visible in modern Ireland. It also must not
present cashels as purpose-built castles or mortarless construction as primitive.

### Gameplay Purpose

The Dry-Stone Wall lets a colony enclose more perimeter with a limited supply of
stone blocks, but each tile is less durable and takes more labor to build than a
vanilla wall made from the same stone. The player decides whether conserving blocks
is worth slower construction and a weaker defensive line.

This is a perimeter-planning choice, not a stronger wall tier. Vanilla walls remain
better when construction speed, breach resistance, and long-term defense matter
more than initial block supply.

### Intended Player Experience

The player should understand the tradeoff from normal RimWorld information before
placing the wall. A new holding can stretch its first batches of stone blocks around
a yard, field, or compound. That enclosure takes longer to complete and is more
likely to require repair or fail during a raid. As resources become plentiful and
threats intensify, replacing vulnerable sections with vanilla walls is a rational
choice.

The feature should feel like a familiar wall with a distinct visual identity and a
clear economic role. It must not require historical knowledge, a new construction
system, a special resource, or custom controls.

### Why This Feature Exists

Oats establish the agricultural identity of the first holding; the Dry-Stone Wall
establishes its visible built identity. It also proves the project's first
Stuff-based linked building pattern while remaining a single, XML-only construction
choice.

## Gameplay Design

### Availability and Construction

1. The Dry-Stone Wall is available from the start wherever the ordinary wall build
   command is available. It requires no research and no minimum Construction skill.
2. Each tile requires four units of an eligible stone-block material.
3. The five Core stone-block types are officially supported. Other materials that
   identify themselves to RimWorld as ordinary stony construction material may be
   selectable, but their balance and visuals are best-effort unless separately
   tested.
4. Pawns construct, repair, deconstruct, damage, claim, and replace the wall through
   normal building work and designation rules.
5. The wall uses the same terrain support requirement as a vanilla stone wall.
6. The wall is a full-height, impassable wall. It is not a fence, barricade, low
   boundary, gate, or passable obstacle.

### Structural Behavior

The wall deliberately retains normal wall behavior rather than creating an exterior
only exception:

- it blocks movement, light, and wind;
- it encloses rooms and participates in temperature control;
- it supports roofs;
- when made from eligible stone, it follows normal airtight-wall behavior;
- it supports ordinary wall attachments such as vents and coolers;
- ordinary doors and other supported wall-adjacent structures work with it; and
- it may replace, and be replaced by, an ordinary wall through normal replacement
  behavior.

These capabilities are retained because silently failing to seal a room, hold a
roof, or support a standard attachment would create disproportionate player friction
and DLC risk. The feature pays for material efficiency through durability and labor,
not hidden structural exceptions.

### Visual and Adjacency Behavior

- Connected tiles form one continuous, irregular dry-laid stone boundary.
- Ends, straight runs, corners, T-junctions, and cross-junctions must read correctly.
- The wall must meet ordinary walls, natural rock, and supported doors without a
  conspicuous visual gap.
- It does not visually merge with fences as though they were the same structure.
- Core stone materials remain distinguishable through their normal material colors.
- Damage, selection, blueprints, placement warnings, snow, rain, darkness, and paint
  remain readable through normal RimWorld presentation.

### Gameplay Niche

The niche is **material-efficient perimeter construction**:

- a 100-tile perimeter saves 100 stone blocks compared with vanilla walls;
- the same perimeter has 20% less hit-point capacity before material modifiers;
- the same perimeter requires approximately 24% more construction work with each
  Core stone type; and
- the completed wall provides normal structural utility, so the tradeoff remains
  visible in cost, build time, damage, repair, and breach outcomes.

The wall is strongest as an early or material-constrained enclosure. It is weaker as
an emergency barrier because it takes longer to build, and weaker as a permanent
defensive line because each tile fails sooner.

### Player Decisions

- **Coverage versus strength:** enclose a larger area with current blocks, or build a
  shorter but tougher vanilla wall.
- **Materials versus labor:** conserve stone at the cost of more pawn time.
- **Early enclosure versus future replacement:** establish the holding now, knowing
  exposed sections may later warrant upgrading.
- **Repair versus upgrade:** restack a damaged section, or spend additional blocks
  replacing it with a vanilla wall.
- **Aesthetic identity versus combat optimization:** use the distinctive wall where
  its tradeoff fits rather than treating it as the universal best wall.

### Player Scenarios

#### P1 — Enclose a Holding with Limited Blocks

**Given** a colony has enough stone blocks for a 100-tile Dry-Stone Wall perimeter
but not a 100-tile vanilla wall perimeter, **when** the player chooses the dry-stone
option, **then** the full boundary can be designated with 20% fewer blocks while its
longer build time and lower durability remain visible before construction.

#### P1 — Preserve Normal Wall Expectations

**Given** the player uses Dry-Stone Walls for part of a room or enclosure, **when**
the boundary is completed, **then** rooms, roofs, temperature, doors, wall
attachments, pathing, and supported airtight behavior operate as they do for an
ordinary stone wall.

#### P2 — Prefer a Vanilla Wall for Defense

**Given** stone supply is adequate and breach resistance or rapid construction is
the priority, **when** the player compares the two walls in the same material, **then**
the vanilla wall offers 25% more hit points per tile and completes with about 19%
less work than the Dry-Stone Wall.

#### P2 — Replace a Vulnerable Section

**Given** a Dry-Stone Wall section now protects a high-risk approach, **when** the
player replaces it with a vanilla wall, **then** normal replacement rules preserve
the intended room and roof boundary without requiring a new gate or wall system.

#### Edge and Failure Scenarios

- A pawn lacks enough blocks to finish a long perimeter; completed and unfinished
  sections remain normal buildings and blueprints without a special partial-wall
  state.
- Different Core stone types meet within one run; each tile retains its own material
  color and material-derived statistics.
- Fire, explosions, melee attacks, breaching, repair, deconstruction, roof changes,
  and wall replacement use normal wall rules with the specified lower durability.
- A save containing completed, damaged, under-construction, roof-supporting,
  attached, painted, or replacing wall tiles restores those states after reload.
- Core-only play is complete. Adding or removing a supported DLC does not remove or
  duplicate the wall.
- Another mod changes wall textures or adds stony materials; Emerald Isle does not
  overwrite that mod's definitions or claim universal visual compatibility.

## Balance Targets

Targets apply per tile before material-specific modifiers unless stated otherwise.
The baseline comparison is the ordinary RimWorld 1.6 wall made from the same Core
stone blocks.

| Dimension | Dry-Stone Wall target | Vanilla comparison | Design intent |
|---|---:|---:|---|
| Material cost | 4 stone blocks | 5 stone blocks | 20% less material per perimeter tile |
| Base hit points | 240 | 300 | 20% less durability per tile |
| Base construction work | 200 | 135 | Produces about 23.6% more displayed work after current Core stone modifiers |
| Construction skill | No minimum | No minimum | Accessible vernacular construction; labor, not a skill gate, pays the cost |
| Research | None | None | A starting construction alternative, not progression content |
| Passability | Impassable | Impassable | Full wall behavior, not a fence |
| Roof and room behavior | Normal wall behavior | Normal wall behavior | Avoid hidden structural exceptions |
| Airtight behavior | Normal eligible stone-wall behavior | Normal eligible stone-wall behavior | No Odyssey-specific exploit or surprise |
| Beauty | No feature bonus | Material-derived | Cultural identity is not a free mood bonus |
| Flammability | Material-derived; Core stone is nonflammable | Material-derived | No special resistance beyond the selected stone |
| Explosion and thump response | Same damage rules as vanilla wall | Baseline | Lower HP already creates the defensive penalty |
| Market value and colony wealth | Normal engine-derived value; no feature override | Normal engine-derived value | No cultural price premium or hidden wealth adjustment |

### Core Stone Durability Targets

| Material | Dry-Stone Wall HP | Vanilla wall HP | Difference |
|---|---:|---:|---:|
| Sandstone | 336 | 420 | -20% |
| Marble | 288 | 360 | -20% |
| Slate | 312 | 390 | -20% |
| Limestone | 372 | 465 | -20% |
| Granite | 408 | 510 | -20% |

Displayed values may use normal whole-number rounding. Material differences remain
meaningful; the feature does not flatten all stone into one generic durability.

### Construction-Work Targets

Against a vanilla wall made from the same Core stone, each Dry-Stone Wall tile must
require approximately 23.6% more displayed construction work under the supported
1.6 baseline. For example, the current Core data produces targets near 1,700 work
for sandstone, 1,870 for marble, and 2,040 for granite, limestone, and slate before
pawn speed and other runtime factors.

The player-facing requirement is the relative tradeoff. If the supported RimWorld
build changes stone modifiers, architecture review must preserve approximately 24%
more work without silently changing the frozen gameplay design.

### Complete-Perimeter Comparison

For a 100-tile run in one material:

- Dry-Stone Wall: 400 blocks, 80% of vanilla total hit points, approximately 124% of
  vanilla construction work.
- Vanilla wall: 500 blocks, full baseline hit points, baseline construction work.

The Dry-Stone Wall therefore buys coverage, not superior efficiency in every metric.
It must never combine lower material cost with equal durability, equal-or-lower work,
or an additional defensive bonus.

## Integration

### Construction and Work

The wall appears with ordinary structure construction and uses normal hauling,
blueprint, reservation, Construction work, quality-independent building, repair,
deconstruction, claim, forbid, and home-area behavior. It adds no work type, research
project, recipe, specialist role, or construction minigame.

### Rooms, Roofs, and Temperature

Completed wall tiles participate in room detection, roof support, light blocking,
wind blocking, temperature containment, and fire behavior as ordinary stone walls
do. Blueprints, frames, destroyed sections, and incomplete perimeters must expose
rooms through normal rules rather than a feature-specific exception.

### Combat and Threats

The wall blocks movement and line of sight as an ordinary wall. It receives the same
categories of melee, projectile, explosion, thump, breach, fire, and environmental
damage; its lower HP causes earlier failure. It grants no bonus against sappers,
breachers, siege weapons, insects, anomalies, or mechanoids.

### Doors, Attachments, and Replacement

No new gate or door is included. Supported vanilla doors may be used within a
Dry-Stone Wall run. Ordinary supported wall attachments may be installed. Direct
replacement between the Dry-Stone Wall and ordinary walls must follow normal
replacement behavior without duplicating materials, deleting unrelated structures,
or leaving a false room boundary.

### Materials, Paint, and Styles

Core stone-block colors and material-derived statistics remain visible. The wall is
paintable wherever the ordinary wall painting system is available. It adds no custom
paint, Ideology style, material, stone type, beauty effect, or meditation category.

### DLC

**Required DLC:** None. RimWorld 1.6 Core is sufficient.

**Optional DLC enhancements:** None in FS-002.

| Configuration | Required behavior |
|---|---|
| Core only | Full feature is available |
| Royalty present or absent | No feature-specific change; no new meditation benefit |
| Ideology present or absent | No style, precept, ritual, or cultural preference is added |
| Biotech present or absent | Normal construction and threat interactions; no mech or pollution exception |
| Anomaly present or absent | Normal wall and breach interactions; no containment or security bonus |
| Odyssey present or absent | Eligible stone walls follow normal airtight, vacuum, attachment, and gravship restrictions |
| All supported DLC | Core balance targets and wall behavior remain unchanged |

## Technical Constraints

### Implementation Boundary

- The complete feature must be expressible with RimWorld 1.6 Core declarative data.
- Custom C# and Harmony patches are prohibited.
- No new runtime system, custom save state, recurring scan, collapse simulation, or
  bespoke interface is permitted.
- The implementation must not modify ordinary walls, stone blocks, construction,
  rooms, roofs, pathing, combat, or DLC behavior globally.
- One buildable wall variant is permitted. A family, gate, corner object, or material
  resource is not.
- Public identifiers selected during architecture review become compatibility
  contracts and must use the project namespace.

### Required Art Assets

The feature requires original, provenance-recorded art for:

- one connected dry-stone wall set covering isolated, end, straight, corner,
  T-junction, and cross-junction presentation;
- one construction-menu icon that remains readable at normal UI scale; and
- any feature-specific blueprint or placement presentation proven necessary during
  architecture review.

Normal engine damage overlays may be used if they remain readable. The wall must look
irregular and dry-laid rather than like dressed brick, retain Core stone-material
recognition, avoid excessive visual noise, and remain distinct from natural rock,
vanilla walls, fences, and rubble at normal zoom. No audio asset is required; ordinary
stone construction, impact, repair, and destruction sounds are sufficient.

### Localization Requirements

- The English player-facing name is `Dry-Stone Wall`.
- The description must identify a carefully stacked, mortarless stone wall and state
  the material, labor, and durability tradeoff in plain language.
- Documentation may use `cashel-inspired`; the UI must not call a single tile a
  `cashel`.
- No Irish term is player-facing in FS-002. `caiseal` and `balla fuar` remain research
  notes pending competent language review.
- All player-facing text must be localization-ready and include translator context.
- Text must not be embedded in art.

### Save Compatibility

- Adding the feature to an existing RimWorld 1.6 save must load without an Emerald
  Isle error and make the wall available for future construction. Existing walls,
  rooms, roofs, maps, and settlements are not changed retroactively.
- Save and load must preserve material, hit points, damage, construction progress,
  ownership, forbidden state, paint, attachments, room boundary, roof support, and
  replacement state wherever vanilla persists those states.
- The feature adds no custom serialized state.
- Adding or removing any supported DLC must not alter, remove, or duplicate the wall.
- Removing Emerald Isle while Dry-Stone Walls exist is not promised to be safe. It
  may remove defenses, expose rooms or vacuum, and destabilize supported roofs.
  Release documentation must warn users and state the tested compatibility level.
- Public identifiers and asset paths must not change after release without migration
  analysis and a documented compatibility decision.

### Compatibility and Performance

- Coexistence with wall-texture replacements, broad architecture mods, and modded
  stony materials is best-effort until specific versions are tested.
- The feature must not overwrite another mod's definitions or assets, add load-order
  metadata without evidence, or promise universal compatibility.
- The wall must add no recurring errors or warnings in Core-only or supported-DLC
  configurations.
- Large mixed-material perimeters must use normal static building and map-mesh
  behavior. No feature-specific ticking or scanning is allowed.

## Acceptance Criteria

- **AC-001 — Availability:** In a new Core-only colony, Dry-Stone Wall is visible as
  a normal structure without research or a minimum Construction skill.
- **AC-002 — Material boundary:** Each tile accepts eligible stone blocks, costs
  exactly four units, and does not accept wood or metal.
- **AC-003 — Core materials:** Sandstone, marble, slate, limestone, and granite blocks
  are all selectable and preserve their normal material color and relative stats.
- **AC-004 — Work:** With each Core stone under the supported baseline, displayed
  construction work is approximately 23.6% higher than the same-material vanilla wall.
- **AC-005 — Durability:** Base HP is 240 and each Core stone result is 20% below the
  same-material vanilla wall, subject only to normal display rounding.
- **AC-006 — Perimeter economy:** A 100-tile designation requires 400 blocks rather
  than the vanilla wall's 500 and exposes the complete work and HP tradeoff before or
  during construction through normal information views.
- **AC-007 — Wall behavior:** Completed tiles are impassable and block light, wind,
  movement, and line of sight through normal wall rules.
- **AC-008 — Structural behavior:** Completed runs enclose rooms, retain temperature,
  support roofs, and use normal eligible-stone airtight behavior.
- **AC-009 — Adjacent structures:** Supported vanilla doors, vents, coolers, and
  other ordinary wall attachments remain placeable and functional.
- **AC-010 — Replacement:** Normal replacement works in both directions between
  Dry-Stone Wall and vanilla wall without duplicated resources, false room boundaries,
  or unexpected roof loss.
- **AC-011 — Damage:** Melee, projectile, explosion, thump, breach, fire, repair, and
  destruction use ordinary wall rules, with lower HP producing the intended weakness.
- **AC-012 — Visual linking:** Isolated tiles, ends, straight runs, corners,
  T-junctions, and crosses render without gaps; joins with walls, rock, and supported
  doors are intentional; fences do not masquerade as one continuous wall.
- **AC-013 — Art readability:** At normal zoom, five of five reviewed Core stone
  versions are distinguishable as dry-laid wall, not dressed brick, fence, natural
  rock, or rubble, in daylight, darkness, rain, snow, selected, painted, and damaged
  views where applicable.
- **AC-014 — Save/load:** The persistence scenarios in this specification restore
  normal wall, construction, attachment, room, roof, material, damage, and paint state
  without recurring errors.
- **AC-015 — Existing save:** Adding the feature to an existing supported save changes
  no existing structure and permits future construction without an Emerald Isle error.
- **AC-016 — DLC absence:** Core-only, Odyssey, and the all-supported-DLC
  configurations load and play with the same core feature; no missing-content error
  occurs. Separate single-DLC runs are required only when a defect or integration
  change makes that DLC relevant.
- **AC-017 — Performance:** A 250-tile mixed-material test perimeter adds no
  feature-specific ticker or recurring log error and does not cause a sustained,
  reproducible simulation slowdown attributable to the feature.
- **AC-018 — Localization:** The player-facing name is `Dry-Stone Wall`; descriptions
  communicate the tradeoff without anachronism, castle claims, or unexplained Irish.
- **AC-019 — Scope:** The package contains one wall variant and no new gate, resource,
  style, research, generation, C#, Harmony patch, or custom runtime state from FS-002.

## Playtesting Strategy

### Functional Testing

Verify availability, resource filtering, designation, hauling, construction,
inspection, material color, connected visuals, doors, attachments, rooms, roofs,
temperature, airtight behavior, damage, fire, repair, deconstruction, replacement,
paint, save/load, and existing-save addition. Exercise straight and mixed-material
runs plus every junction shape. Review the complete log after each run.

### Controlled Balance Testing

Build equal 25-, 100-, and 250-tile runs of Dry-Stone Wall and vanilla wall in each
Core stone material. Use the same builder, Construction skill, manipulation,
lighting, movement distance, hauling distance, and resource location. Record:

- blocks consumed;
- construction work and elapsed completion time;
- displayed and actual hit points;
- repair work and materials after equal damage;
- survival time against repeatable melee, projectile, explosion, and breach tests;
- replacement cost and time; and
- colony wealth contribution.

### Colony Playtesting

In at least one early material-constrained colony and one established raid-capable
colony, build a real perimeter containing doors, rooms or roofed edges, attachments,
and exposed defensive sections. Record when players select the Dry-Stone Wall, when
they choose vanilla walls, which sections they replace, whether the tradeoff is
understood, and whether visual identity remains clear during ordinary play.

### Compatibility Testing

Test Core only and Odyssey during feature verification, then all supported DLC
together during Version 0.1 release integration. Run a separate single-DLC test only
when that DLC changes an affected behavior or a defect is observed. Include Odyssey
airtight/vacuum behavior. Test one current wall-texture replacement, one broad
medieval architecture mod, and one mod that adds stony material as best-effort
compatibility samples rather than universal claims.

### Success Criteria

- AC-001 through AC-019 pass against the packaged feature.
- The 20% material saving, 20% HP reduction, and approximately 24% work increase are
  reproduced for all five Core stone types.
- In human design review, the reviewer can identify both the block-saving advantage
  and at least one consequential disadvantage from normal game information without
  being told the intended answer.
- At least one representative early-colony plan rationally uses Dry-Stone Wall, and
  at least one defense-focused plan rationally uses vanilla wall instead.
- No player in the review sample expects the wall to be a fence, a special gate, a
  stronger fortification, or a source of hidden cultural bonuses.

### Failure Criteria

The feature returns to specification or balance review if any of these occur:

- the wall is equal or better than vanilla in material cost, durability, and work;
- players choose it universally once enough stone is available, or never find a
  rational use for it;
- room, roof, attachment, replacement, or airtight behavior violates ordinary wall
  expectations;
- its art reads primarily as dressed brick, rubble, fence, or a copied monument;
- mixed materials or junctions create broken or misleading links;
- save/load, existing-save addition, DLC absence, or an ordinary damage case causes
  state loss or recurring errors; or
- implementation requires C#, Harmony, a new resource, or scope beyond one wall.

## Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Lower block cost becomes the default room-wall choice | Medium | High | Retain lower HP and higher work; test early, established, and defense-focused colonies |
| Tradeoff is too punitive to justify use | Medium | High | Test full perimeters under real block scarcity; adjust only through human-reviewed spec change |
| Full structural behavior weakens the perimeter identity | Low | Medium | Keep identity in visual form and economic role; avoid artificial room restrictions that create friction |
| Art fails at linked junctions or mixed materials | High | High | Require every link state and all Core stone colors in normal-zoom review |
| Visual design copies a monument or modern field wall | Medium | High | Use multiple link-only references; create original restrained forms; preserve provenance |
| Wall-texture mods conflict with custom links | Medium | Medium | Use project-owned assets and targeted best-effort tests; avoid global patches |
| Odyssey airtight behavior creates an exploit | Medium | High | Require parity with eligible vanilla stone walls and explicit vacuum testing |
| Replacement removes attachments or roofs | Medium | High | Make bidirectional replacement a functional and persistence acceptance test |
| Removal damages rooms, roofs, or vacuum safety | High if removed | High | Declare removal unsupported and warn in release documentation |
| Modded stony materials produce bad stats or colors | Medium | Medium | Officially balance only Core stone; classify untested materials as best-effort |
| Historical description overstates defense or uniformity | Low | High | Keep cashel framing domestic and bounded; retain research uncertainty in wording |

## Out of Scope

FS-002 does not include:

- gates, doors, fence variants, barricades, crenellations, parapets, stairs, towers,
  corners as separate objects, or any wall family;
- curved, diagonal, procedural, circular, or ringfort/cashel generation;
- new stone, fieldstone, rubble, mortar, mixed-stone, or gathered-rock resources;
- quarrying, terrain clearing, wall collapse, restacking, erosion, moss, weathering,
  deterioration, maintenance, or construction minigames;
- special combat resistance, cover bonuses, beauty auras, mood effects, meditation
  bonuses, ideology content, ritual content, or cultural preferences;
- a reconstruction of Caherconnell, Grianan of Aileach, or any named monument;
- nineteenth-century field-wall or famine-wall framing;
- Irish player-facing terminology;
- automatic patches for other wall or material mods;
- custom C#, Harmony, custom UI, runtime systems, or custom serialized state; and
- implementation plans, source files, public identifiers, asset paths, or release
  integration.

## Design Self-Review

| Challenge | Finding | Revision or retained decision |
|---|---|---|
| Unnecessary complexity | Exterior-only room, roof, or airtight exceptions would require players to learn hidden structural rules for one wall. | Retained normal wall behavior; balance is carried by cost, work, and durability. |
| Historical overreach | Cashels varied widely, monumental survivors are unrepresentative, and modern field walls are often later. | Kept one restrained cashel-inspired enclosure wall and prohibited monument reconstruction or timeless-Ireland claims. |
| Gameplay value | A cosmetic wall would not justify scope; a cheaper equal wall would be an upgrade. | Fixed measurable 20% material, 20% durability, and approximately 24% work tradeoffs. |
| Player friction | A skill gate, unique resource, new gate, or special repair loop would slow ordinary construction without adding a proportional decision. | None are included; the wall uses familiar construction and repair verbs. |
| Maintenance burden | Special topology, global patches, DLC adapters, and runtime state would multiply compatibility work. | XML-only static building behavior is mandatory; supported DLC retains Core parity. |
| Future extensibility | A generic architecture framework is not justified by one wall. | The feature establishes only a concrete Stuff-based linked-building pattern; later reuse must follow actual evidence. |

**Self-review result:** Patrick Mee approved and froze this specification on
2026-07-05. It contains no unresolved gameplay decision required for architecture
review. Changes now require explicit human approval and, where appropriate, an ADR.
Specification approval does not authorize implementation.
