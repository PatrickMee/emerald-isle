# Feature Specification: Dry-Stone Wall

**Feature Branch:** `004-dry-stone-wall-specification`
**Created:** 2026-07-05
**Status:** Approved — Frozen
**Milestone:** Version 0.1 — The First Holding
**Input:** "Create FS-002 for the approved single Dry-Stone Wall feature; do not implement gameplay."

**Design Bible:** `docs/design/design-bible.md`
**Canonical detailed specification:** `docs/specifications/FS-002-dry-stone-wall.md`

## Player Value and Scenarios

### Player Story 1 - Enclose a Holding with Scarce Stone (P1)

A player wants to complete a meaningful perimeter before the colony has enough stone
blocks for ordinary walls. The Dry-Stone Wall saves material but takes longer to
construct and is easier to breach.

**Why now:** Version 0.1 needs one visible architectural feature that defines the
first holding and establishes a reusable building pattern.
**Independent test:** A 100-tile designation consumes 400 stone blocks, has 80% of
the same-material vanilla wall HP, and requires approximately 124% of its work.

1. **Given** a colony has 400 eligible stone blocks, **when** the player designates a
   100-tile Dry-Stone Wall perimeter, **then** the complete perimeter can be supplied
   while its lower durability and higher labor remain visible.

### Player Story 2 - Use Familiar Wall Behavior (P1)

A player uses the wall as part of a compound and expects standard RimWorld walls,
doors, rooms, roofs, temperature, attachments, and replacement to keep working.

**Why now:** Hidden structural exceptions would undermine vanilla fit and make one
small feature disproportionately difficult to understand and maintain.
**Independent test:** A completed mixed enclosure behaves like an ordinary stone wall
for rooms, roofs, doors, attachments, movement, light, wind, and eligible airtightness.

1. **Given** a completed enclosure includes Dry-Stone Wall tiles and supported doors,
   **when** the player roofs, heats, cools, attaches fixtures, damages, repairs, saves,
   reloads, or replaces sections, **then** normal wall behavior is preserved.

### Player Story 3 - Choose Vanilla Strength When It Matters (P2)

A player with adequate blocks wants a fast, durable defensive line and should prefer
an ordinary wall instead of treating the new feature as an upgrade.

**Why now:** Emerald Isle requires consequential tradeoffs, not cosmetic power creep.
**Independent test:** Under matched conditions, a same-material vanilla wall has 25%
more HP per tile and completes with about 19% less work.

1. **Given** block supply is sufficient, **when** defense or completion speed is the
   priority, **then** the vanilla wall remains the rational choice.

### Edge and Failure Cases

- Insufficient blocks leave ordinary blueprints and frames, not special partial walls.
- Mixed Core stone types preserve their own colors and material-derived statistics.
- All linked junctions, doors, ordinary walls, natural rock, and non-linking fences
  remain visually legible.
- Damage, breach, fire, repair, deconstruction, and replacement use normal wall rules.
- Save/load preserves construction, material, damage, attachments, paint, rooms, and roofs.
- Core-only play is complete and supported DLC presence does not change balance.
- Untested modded stony materials and wall overhauls receive best-effort behavior only.

## Requirements

- **FR-001:** The feature MUST add exactly one player-buildable wall named
  `Dry-Stone Wall`.
- **FR-002:** The wall MUST be available without research or a minimum Construction skill.
- **FR-003:** Each tile MUST cost exactly four eligible stone blocks and MUST reject
  wood and metal.
- **FR-004:** All five Core stone-block types MUST be officially supported.
- **FR-005:** The wall MUST have 240 base HP, preserving each Core stone's normal
  material factor and producing 20% less HP than a same-material vanilla wall.
- **FR-006:** The wall MUST require approximately 23.6% more displayed construction
  work than a same-material vanilla wall under the supported baseline.
- **FR-007:** The wall MUST be impassable and use normal full-height wall behavior.
- **FR-008:** The wall MUST block movement, line of sight, light, and wind normally.
- **FR-009:** The wall MUST enclose rooms, retain temperature, and support roofs normally.
- **FR-010:** Eligible stone versions MUST follow normal airtight-wall behavior.
- **FR-011:** Supported ordinary doors and wall attachments MUST remain functional.
- **FR-012:** Direct replacement with ordinary walls MUST work in both directions
  without duplication, false room boundaries, or unexpected roof loss.
- **FR-013:** Normal wall damage, breach, fire, repair, destruction, and
  deconstruction rules MUST apply without a defensive bonus.
- **FR-014:** Isolated, end, straight, corner, T, and cross visual states MUST render
  without gaps and preserve Core stone colors.
- **FR-015:** Joins with ordinary walls, natural rock, and supported doors MUST be
  intentional; fences MUST NOT appear to form the same continuous structure.
- **FR-016:** The feature MUST use original, provenance-recorded wall art and a
  readable construction icon.
- **FR-017:** The feature MUST use normal stone audio and MUST NOT add audio assets.
- **FR-018:** Player-facing language MUST be localization-ready and MUST NOT use an
  unreviewed Irish term.
- **FR-019:** RimWorld 1.6 Core MUST be the only required content.
- **FR-020:** Royalty, Ideology, Biotech, Anomaly, and Odyssey MUST remain optional
  and MUST NOT alter core balance.
- **FR-021:** Adding the feature to an existing save MUST modify no existing structure.
- **FR-022:** Save/load MUST preserve all wall state normally persisted by RimWorld.
- **FR-023:** The feature MUST add no custom serialized state or recurring behavior.
- **FR-024:** The feature MUST NOT alter vanilla or other mods' definitions globally.
- **FR-025:** The feature MUST contain no gate, wall family, new stone resource,
  research, generation, C#, Harmony patch, custom UI, or special gameplay system.

## Research and Cultural Transformation

The approved `docs/research/version-0.1/dry-stone-wall.md` establishes early medieval
Irish cashel enclosures as the primary inspiration. It distinguishes those enclosures
from later field-wall networks, rejects the claim that cashels were simply castles,
and records regional, chronological, reconstruction, and material uncertainty.

Emerald Isle transforms that evidence into one RimWorld perimeter choice: local stone
coverage gained through patient labor at the cost of per-tile strength. It does not
reconstruct a monument, simulate a historical technique, or claim unique Irish
ownership of dry-stone construction.

## Vanilla Comparison and Balance

The ordinary vanilla wall is the primary comparator; the fence is rejected because
the approved feature is full-height and impassable. Against the same Core stone wall,
the new wall uses 20% fewer blocks, has 20% less HP, and takes approximately 24% more
work. It retains normal structural behavior so the tradeoff is clear and discoverable
rather than hidden in room or roof exceptions.

Abuse cases include cheap universal room walls, lower-wealth defense, modded stone
with extreme factors, and replacement exploits. The specification requires matched
perimeter tests, normal material-derived value, lower breach resistance, ordinary
replacement rules, and best-effort status for untested modded materials.

## Scope

**In scope:** One cashel-inspired, connected, Stuff-based, full-height Dry-Stone Wall;
five Core stone types; normal wall integration; original art; localization; save,
DLC, compatibility, performance, balance, and playtest requirements.
**Out of scope:** Gates, wall families, fences, curves, diagonals, generation, new
resources, named monuments, cultural bonuses, special damage rules, Irish UI terms,
custom code, Harmony, runtime state, and implementation planning.

## Cross-Discipline Requirements

**Technical:** XML-only, static wall behavior, no global changes, no custom state.
**Art/audio:** Original connected wall set and UI icon; standard stone audio.
**Localization:** English source name `Dry-Stone Wall`; functional description;
no unreviewed Irish.
**Required DLC:** None.
**Optional DLC enhancements:** None.
**Behavior without DLC:** Full Core feature.
**Save compatibility:** Existing-save addition and same-version persistence required;
removal while built walls exist is not promised safe.

## Success Criteria

- **SC-001:** A 100-tile perimeter consumes exactly 400 Core stone blocks.
- **SC-002:** Each Core stone version has 80% of same-material vanilla wall HP,
  subject only to normal whole-number display rounding.
- **SC-003:** Each Core stone version requires approximately 123.6% of same-material
  vanilla wall construction work under the supported baseline.
- **SC-004:** All functional, link, room, roof, attachment, replacement, save, Core,
  Odyssey, and all-supported-DLC acceptance scenarios pass without recurring errors.
- **SC-005:** In human design review, the reviewer identifies the material advantage
  and one meaningful disadvantage from normal game information.
- **SC-006:** Representative play produces at least one rational dry-stone choice and
  one rational vanilla-wall choice.
- **SC-007:** A 250-tile perimeter introduces no feature-specific recurring work or
  sustained, reproducible slowdown.

## Dependencies, Assumptions, and Risks

- Depends on RimWorld 1.6 Core wall, construction, Stuff, linked-graphic, room, roof,
  temperature, attachment, paint, damage, replacement, and save behavior.
- Assumes the five current Core stone types remain the official balance set.
- Assumes normal wall structural behavior is preferable to an exterior-only exception.
- Major risks are universal adoption, no rational adoption, linked-art failure,
  replacement or airtight defects, unsafe removal, modded-material extremes, and
  historical overstatement.
- No existing ADR conflicts. ADR-0002 supplies the package contract only.

## Review Gates

- [x] Feature Acceptance Checklist approved by Patrick Mee on 2026-07-05
- [x] Historical/cultural research approved
- [x] Gameplay and vanilla fit approved
- [x] Balance approved
- [ ] Architecture review recorded after specification approval
- [x] Art/audio requirements approved
- [ ] QA/release evidence completed after implementation
