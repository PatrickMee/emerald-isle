# FS-003 — Hand Quern

**Status:** Review<br>
**Gate 1 status:** Pending maintainer approval<br>
**Milestone:** Version 0.1 — The First Holding<br>
**Catalog feature:** PR-01<br>
**Feature branch:** `codex/fs-003-hand-quern-specification`<br>
**Owner:** Patrick Mee<br>
**Created:** 2026-07-07<br>
**Vanilla balance baseline:** RimWorld 1.6.4871 rev595<br>
**Research:** [RSC-004 Hand Quern](../research/version-0.1/hand-quern.md),
[RSC-005 Milled Oats](../research/version-0.1/milled-oats.md),
[RSC-006 Oat Foods](../research/version-0.1/oat-foods.md)<br>
**Implementation authorized:** No

## Authority and Boundaries

This specification defines the approved design target for the Version 0.1 hand
quern candidate. It conforms to the
[Version 0.1 approved scope](../product/version-0.1-approved-scope.md),
[Version 1.0 Vision](../product/version-1.0-vision.md), the
[Design Bible](../design/design-bible.md), and the approved Version 0.1 research
briefs.

The hand quern is conditional. Historical evidence supports it, but that does not
make it automatically worthwhile. It remains in Version 0.1 only if the complete
oat chain creates a meaningful player decision:

```text
Oats
  ↓
Hand Quern
  ↓
Milled Oats
  ↓
Oat Porridge or Oat Flatbread
```

A standalone player-facing quern with no useful milling recipe is not acceptable.
Gate 2 for this feature must not pass unless the quern has an actual milling use in
the same release path, or the implementation deliberately keeps it non-player-facing
until FS-004 supplies that use.

This document contains no XML, C#, Harmony patch, file layout, texture path,
public `defName`, or implementation sequence. Public identifiers and file paths are
implementation contracts and must be selected deliberately during implementation.

## Overview

The hand quern is a compact, unpowered household production station for turning raw
oats into milled oats through ordinary RimWorld bills. It represents domestic
rotary-quern grain processing at the scale of one holding. Its gameplay purpose is
to let the player schedule grain preparation separately from final cooking, not to
simulate every historical processing step.

The feature must feel like a small vanilla worktable: familiar placement,
construction, bills, hauling, reservations, work priorities, save behavior, and
failure states. It must not introduce a new milling framework, powered mill,
resource family, or custom code.

## Historical Research

The approved Hand Quern research brief supports one small rotary hand quern as an
ordinary domestic grain-processing tool in early medieval Ireland, approximately
AD 400–1100. Archaeological syntheses identify quernstones across secular,
ecclesiastical, cashel, rath, and crannog contexts. The evidence supports domestic
grain processing but does not prove universal ownership, one standardized quern
shape, or oat-exclusive use.

The research also records that watermills existed in early medieval Ireland. The
Version 0.1 hand quern therefore represents low-infrastructure household
processing, not technological isolation. A later mill could become a throughput
upgrade, but Version 0.1 must not implement or pre-build that system.

The milled-oats and oat-food research briefs provide the gameplay dependency:
raw oats remain useful, milled oats can support a processed-food choice, and the
chain must be simplified if playtesting shows that milling is compulsory busywork.

## Cultural Significance

The quern reinforces the first holding as a place of daily work. It connects the
oat field, stored grain, household labor, and food preparation without invoking
monumental, elite, mythic, or romantic imagery.

The feature must avoid these claims and presentations:

- hand querns were uniquely Irish;
- early medieval Irish communities lacked water-powered technology;
- every household used the same quern in the same way;
- milling was exclusively assigned by pawn gender, status, ethnicity, ideology, or
  culture;
- repetitive food labor is valuable merely because it is historically attested;
- decorated or deposited quern fragments justify ritual, mood, or supernatural
  effects.

The player-facing English name is `hand quern`. Irish terms such as `bró` remain
research notes unless future qualified language review approves localization use.

## Gameplay Purpose

The hand quern exists to create a scheduling and allocation decision:

- keep oats raw for flexible ordinary food, feed, trade, storage, or emergency use;
- or spend pawn labor at an unpowered station to create a prepared ingredient for
  the oat-food chain.

The quern solves a limited gameplay problem: it decouples grain preparation from
final cooking without requiring power, fuel, research, or a large bench. It gives a
small holding a visible place where crop surplus becomes food infrastructure.

It does not exist to add a mandatory step before eating oats. If the player always
mills every oat and always uses the same downstream recipe, the feature has failed
its gameplay purpose.

## Vanilla Comparison

The closest vanilla patterns are ordinary Core worktables and production
intermediates:

- **Crafting spot:** proves that low-infrastructure manual production can be
  readable, but the hand quern must not be a free disposable spot.
- **Hand tailor bench and stonecutter's table:** prove that unpowered bill-driven
  production can communicate manual work through existing RimWorld systems.
- **Fueled and electric stoves:** define the cooking bottleneck that milling should
  prepare for, not duplicate.
- **Wort:** proves that a passive intermediate can carry storage, hauling, and
  production-chain costs, but does not justify copying fermentation behavior.

The quern should be familiar to players who understand bills. It should not require
new UI, special job controls, or a custom production category.

## Gameplay Design

### Availability

The hand quern is available from the start of a colony. It requires no research, no
DLC, no electricity, no fuel, and no minimum skill gate. Material access and pawn
labor are the intended constraints.

If implemented before the milled-oats recipe is also ready, it must not ship as a
player-facing dead worktable. The preferred delivery path is to implement and
verify the quern together with its first milling recipe, or keep it unavailable to
players until that recipe exists.

### Physical Role

The quern is a compact domestic production object:

- it occupies one tile;
- it must not function as a wall, barricade, cover system, or defensive blocker;
- it should be movable and maintainable through normal vanilla building behavior
  where practical;
- it should read as a practical household tool, not as a sculpture, shrine,
  powered mill, grindstone for weapons, table, or loose rock chunk.

### Materials and Construction

Construction uses only existing vanilla materials. The target material identity is:

- mostly stone blocks, representing the upper and lower stones;
- a small wood component, representing the handle or simple support;
- no metal, cloth, components, new quernstone item, fieldstone resource, mortar, or
  special regional stone family.

The construction target is 25 stone blocks and 10 wood, with no minimum skill and
no research prerequisite. This is intentionally low enough for an early holding,
but high enough that parallel querns are not free disposable spots. Capital cost is
secondary; pawn labor and processing choice are the main tradeoff.

### Work and Labor

Milling should use ordinary RimWorld production labor through the bill system. It
must not require a custom work type, custom skill, custom job driver, or custom UI.
The design target is non-Cooking production labor so milling can be scheduled
separately from final meal preparation. If the supported RimWorld 1.6 XML contract
cannot express that without code, implementation must stop for review rather than
silently moving milling into the cook bottleneck.

Design intent:

- the work should be manually scheduled and interruptible like vanilla bills;
- a player should be able to maintain a target amount of milled oats;
- milling should not require the colony's best cook if a simpler production labor
  channel can express the work cleanly;
- the work must be meaningful enough to matter, but not so large that the
  downstream foods become obvious traps;
- the quern itself must not grant nutrition, preservation, quality, beauty, mood,
  medical, ideology, or cultural bonuses.

The recipe work amount belongs to FS-004, but it must satisfy this gameplay
requirement: milling is independently schedulable preparation, not hidden extra
stove work.

### Player Decisions

- **Raw flexibility versus processed commitment:** keep oats useful in ordinary
  systems, or commit part of the reserve to the processed-food chain.
- **Labor timing:** mill during quiet periods so final cooking can later be faster
  or more specialized.
- **Throughput versus footprint:** build one quern for modest household throughput,
  or spend more space and materials to let multiple pawns process at once.
- **Low-tech resilience:** continue grain preparation during power shortages or in
  low-infrastructure settlements.
- **Simplification fallback:** ignore the chain if its payoff is not worth the
  labor; raw oats must remain viable.

## Balance Analysis

### Balance Hypothesis

The hand quern is balanced if it makes oat processing a controlled labor choice.
It should be attractive when a colony has oats, spare production labor, and a
reason to prepare milled oats for porridge or flatbread. It should be unattractive
when the colony needs immediate food, has severe labor shortages, or can use raw
oats more flexibly.

The quern must never make the complete oat chain a strict upgrade over vanilla
food paths. Its value is scheduling, low infrastructure, and identity; its cost is
extra labor, hauling, storage, and an additional production object.

### Required Tradeoffs

The implemented feature must preserve all of these tradeoffs:

| Strength | Required cost or constraint |
|---|---|
| No power or fuel | Slow manual throughput and pawn labor |
| Early availability | Low output ceiling; no research-tier advantage |
| Compact footprint | Limited simultaneous work per building |
| Enables milled-oat foods | Raw oats remain useful and processing is not mandatory |
| Low material cost | Parallel querns still cost space, materials, bills, and pawn time |

### Abuse and Failure Cases

The design fails if any of these become true:

- the optimal policy is always to mill every oat immediately;
- raw oats are made useless to manufacture demand for the quern;
- milling increases nutrition, value, shelf life, or market profit by itself;
- the quern becomes a cheap defensive object or room-shaping exploit;
- broad ingredient filters consume unintended grains or modded resources;
- the work type competes so badly with essential labor that the building is a trap;
- the building ships with no bill and confuses players;
- multiple querns remove the intended labor constraint too cheaply;
- the art reads as a generic stone slab, ruined monument, ritual object, or modern
  mechanical mill.

## Player Scenarios and Acceptance

1. **Given** a Core-only colony has the required vanilla materials, **when** the
   player builds a hand quern, **then** it behaves as a normal small production
   building with no power, fuel, research, DLC, or custom UI requirement.

2. **Given** raw oats and a valid milled-oats recipe exist, **when** the player
   creates a milling bill at the hand quern, **then** pawns process oats through
   ordinary RimWorld bill, hauling, reservation, interruption, and output behavior.

3. **Given** the colony has no power or fuel, **when** a milling bill is available,
   **then** the hand quern can still operate because its throughput cost is pawn
   labor rather than infrastructure.

4. **Given** the player chooses not to mill oats, **when** raw oats are stored,
   cooked through ordinary Core paths, fed, traded, or carried, **then** the crop
   remains useful and the quern is not a compulsory gateway.

5. **Given** a save contains a built hand quern and active or suspended bills,
   **when** the game is saved and reloaded, **then** ordinary building and bill
   state persists without custom serialized data.

6. **Given** official DLC are absent or present, **when** the hand quern is loaded,
   placed, operated, saved, and reloaded, **then** no DLC is required and no
   optional DLC creates a hard dependency or duplicate behavior.

7. **Given** the milled-oats recipe is not available in the same playable release
   path, **when** the feature is reviewed for Gate 2, **then** the quern cannot be
   accepted as Done as a player-facing feature.

8. **Given** a player compares the quern chain with direct raw-oat cooking,
   **when** the complete labor and hauling path is evaluated, **then** the quern
   must demonstrate a real scheduling or food-choice benefit or be removed from
   Version 0.1.

## Scope

### In

- One compact, unpowered hand quern production building.
- Standard RimWorld placement, construction, designation, hauling, bills, work,
  save/load, deconstruction, minification or movement behavior where supported by
  the chosen vanilla pattern.
- Existing vanilla construction materials only.
- Compatibility with the later FS-004 milled-oats recipe.
- Original, restrained runtime art sufficient to read as a rotary hand quern at
  normal RimWorld zoom.
- English localization-ready label and description.

### Out

- Milled oats item definition and conversion recipe values.
- Oat porridge, oat flatbread, or any other food.
- A generic milling, flour, grain, baking, drying, dehulling, sifting, or water
  system.
- Watermills, windmills, animal mills, powered automation, upgrades, quality
  grades, byproducts, waste, bran, hulls, straw, or flour variants.
- Gender, status, ideology, culture, pawn-type, or faction restrictions.
- Ritual, mythological, mood, health, medical, learning, or beauty bonuses.
- Custom C#, Harmony, custom jobs, custom UI, custom ticking behavior, or custom
  serialized state.
- New stone resources, quernstone items, regional material families, or copied
  historical object art.

## Technical Design

Implementation should use vanilla RimWorld declarative production behavior:

- one small production building;
- standard construction and designation systems;
- standard worktable and bill behavior if the supported 1.6 build confirms that is
  the simplest correct contract;
- standard ingredient filters and recipe users supplied by FS-004;
- normal save persistence through vanilla building and bill state;
- ordinary localization keys and original textures;
- no custom runtime assembly.

The public compatibility contracts created at implementation include the building
definition, translation keys, texture paths, recipe-user relationship, player-facing
label, and any saved bill references. These must be stable once released.

If implementation discovery shows that vanilla XML cannot express the accepted
behavior, stop and request review. Do not add code, Harmony, or a broader system
silently.

## XML vs C# Decision

**Decision target:** XML-only.

RimWorld Core already supports the relevant production concepts: buildings,
construction costs, worktables, bills, recipes, hauling, ingredient search, output
products, save persistence, and localization. FS-003 does not require custom
simulation, custom UI, custom serialization, or Harmony.

C# is not approved. Harmony is explicitly out of scope and would require a new ADR
and scope approval.

## Art Requirements

Required art is one original runtime object set sufficient for the chosen vanilla
building presentation. The object must read as:

- two low stacked stones or a compact rotary quern form;
- hand-operated, domestic, and practical;
- early-medieval-inspired without decorative reconstruction;
- distinct from a loose stone chunk, sculpture, table, grindstone, powered mill,
  ritual object, or modern mechanical device.

Art should use restrained vanilla-style readability and neutral material logic.
If Stuff tinting is used, stone surfaces must remain readable and any wooden handle
must not become visually confusing. If Stuff tinting is not used, the building must
still fit beside vanilla stone and wood objects.

No source image is cleared for copying. References from the research brief are
study material only.

## Audio Requirements

No custom audio is required for Version 0.1. Vanilla bill/work sounds may be used if
they fit the selected production pattern. Custom grinding audio is out of scope
unless a later release proves it materially improves player comprehension.

## Localization

English source text must use a functional label:

- player-facing name: `hand quern`;
- description must explain that it is an unpowered tool for milling oats into a
  prepared ingredient;
- description must not claim universality, primitive technology, exclusive Irish
  identity, exact historical reconstruction, or a ritual role.

Irish-language text is not required. The research term `bró` should remain out of
player-facing English unless future competent language review approves a specific
localization use.

## Testing

Gate 2 evidence should be proportional but must cover the complete player path:

- static XML validation for the building and any linked recipe-user contract;
- clean Core-only load with no new unresolved errors or warnings;
- construction from the player menu when the feature is player-facing;
- material availability with the selected vanilla construction resources;
- operation through at least one real milling bill once FS-004 exists;
- no power or fuel requirement;
- job reservation, interruption, suspension, repeat bills, and target-count bills;
- save/load with built quern, blueprints, active bills, suspended bills, and stored
  inputs/outputs where applicable;
- behavior with official DLC absent and present at the release matrix level;
- player comprehension at normal zoom and in the production menu;
- comparison against the direct raw-oat cooking fallback during the complete-chain
  playtest.

A quern with no available milling bill may pass static checks but cannot pass the
complete in-game player-path test.

## Future Expansion

Future releases may consider larger mills, water-powered processing, settlement
throughput upgrades, broader grain processing, or cultural production spaces only
after Version 0.1 proves the small XML chain is worth keeping. FS-003 must not add
extension framework code, generic categories, placeholder recipes, or unused
material abstractions for those possibilities.

## Dependencies

**Required DLC:** None. RimWorld 1.6 Core is required.

**Optional DLC enhancements:** None for Version 0.1.

**Behavior without DLC:** Full behavior through Core building and bill systems.

**Save compatibility:** The released building definition, translation keys, texture
paths, and saved bill references become compatibility contracts. Adding the feature
to existing saves should be low risk. Removing the mod can remove built querns,
blueprints, bills, and any linked stored products through ordinary missing-def
behavior; this must be documented at release.

**Feature dependencies:**

- FS-001 Oats supplies the raw input crop.
- FS-004 Milled Oats supplies the first actual milling output and recipe contract.
- FS-005 Oat Foods supplies the downstream payoff that ultimately validates the
  processing chain.

FS-003 can be specified independently, but it is not independently valuable as
playable software without FS-004.

## Risks

| Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---:|---|---|
| Quern becomes compulsory busywork | High | High | Preserve raw-oat paths; test direct-cooking fallback; remove/simplify if behavior converges | Maintainer |
| Building ships without a useful bill | Medium | High | Block Gate 2 for player-facing implementation until FS-004 recipe exists | Maintainer |
| Work type competes with skilled cooking and weakens scheduling value | Medium | High | Use non-Cooking production labor or stop for review if XML cannot express it | Implementer |
| Nutrition or value is created by processing | Medium | High | FS-004 must model full conversion and rounding before implementation | Implementer |
| Construction is so cheap that parallel querns erase throughput constraint | Medium | Medium | Test cost, footprint, and pawn-labor scaling together | Implementer |
| Art reads as generic stone slab or ritual object | Medium | Medium | Validate icon and world object at normal zoom beside vanilla content | Maintainer |
| Broad filters consume unintended grains or modded ingredients | Medium | Medium | Use narrow namespaced filters; avoid universal flour/grain compatibility claims | Implementer |
| Save contracts are renamed after release | Low | High | Select stable identifiers deliberately; require migration review for changes | Maintainer |
| Scope grows into a milling framework | Medium | High | Enforce out-of-scope list; require ADR for C#, Harmony, or generic systems | Maintainer |

## Gate 1: Approval Checklist

- [x] Catalog ID, owner, and active milestone are assigned; the feature belongs to
      the current approved Version 0.1 scope.
- [x] Player problem, meaningful decision, story value, and bounded first slice are
      clear; explicit exclusions prevent scope leakage.
- [x] Constitution and Design Bible conformance are reviewed, including tradeoffs
      over power and vanilla-native fit.
- [x] Material historical, cultural, gameplay, and technical uncertainty is
      resolved to specification depth through approved research.
- [x] Vanilla/DLC comparison and balance hypothesis are measurable.
- [x] Irish-language and culturally sensitive content is identified; no early
      qualified review is requested because player-facing English remains
      functional and low-risk.
- [x] XML-first decision is documented; C# and Harmony are rejected; public
      contracts, save impact, and compatibility are stated.
- [x] Acceptance, edge, failure, and persistence scenarios exist; test and playtest
      intent is actionable.
- [x] Art, audio, and localization needs are defined or marked not applicable.
- [x] The FS-004 dependency is explicit and blocks Gate 2, not specification review:
      no player-facing quern is Done without an actual milling use.

**Decision:** Pending maintainer review<br>
**Approved by/date:** Not approved<br>
**Conditions:** Proposed condition: implementation should be coordinated with
FS-004 or kept non-player-facing until FS-004 supplies a milling recipe.

## Gate 2: Evidence

Not started. No implementation is authorized by this document.

Gate 2 must prove the complete player path with a real milling recipe. Static
validation or a placeable empty worktable is insufficient.

**Decision:** Not Done<br>
**Approved by/date:** Not approved

## Open Questions and Decisions

| Question | Owner | Due point | Status |
|---|---|---|---|
| Should FS-003 implementation be bundled with FS-004, or should the quern remain non-player-facing until FS-004 exists? | Patrick Mee | Before FS-003 implementation starts | Human review required |
| Does the exact supported RimWorld 1.6 build allow non-Cooking production labor for the quern without custom code? | Implementer | During implementation discovery | Verify before XML finalization |
| Does playtesting show that direct raw-oat cooking provides equivalent gameplay more simply? | Maintainer | Complete-chain playtest after FS-004/FS-005 | Must simplify if yes |
