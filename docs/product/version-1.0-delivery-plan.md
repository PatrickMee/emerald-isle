# Version 1.0 Delivery Plan: The Ringfort

**Status:** Approved delivery plan; individual gameplay slices still require their own approval<br>
**Owner:** Patrick Mee<br>
**Planning baseline:** [`v0.6.3`](../release/v0.6.3.md)<br>
**Target:** Version 1.0 — Emerald Isle<br>
**Created:** 2026-08-23<br>
**Review trigger:** Approval, rejection, or material change to the Version 1.0
scope, release sequence, marquee feature, or conditional round-tower decision

## Authority and Use

This document defines the approved delivery path from the published Version 0.6.3
baseline to Version 1.0. It operates beneath the
[Constitution](../../.specify/memory/constitution.md),
[Design Bible](../design/design-bible.md),
[Version 1.0 vision](version-1.0-vision.md), and
[roadmap](../roadmap.md).

The roadmap continues to own milestone status. This plan does not approve a
gameplay feature, close Version 0.5, or authorize implementation. Each gameplay
slice receives its own proportionate feature record and maintainer approval when
it enters implementation. The implementation PR owns Done evidence, and the
release PR owns publication approval.

## Release Promise

**Build, provision, and defend a mature ringfort holding on the Rim.**

Version 1.0 should make the existing Emerald Isle content feel like one complete
colony path rather than a collection of additions. A player can establish a first
holding, develop a recognizable fortified settlement, provision it through
ordinary work, and defend it without leaving RimWorld's normal systems.

The ringfort is the marquee feature because it is visually legible, changes base
layout and defensive planning, builds on the released dry-stone construction
language, and gives the existing crops, animals, food, apparel, hearth, and
wolfhound a coherent place to live.

## Planning Principles

- Version 1.0 is judged by cohesion and reliability, not item count.
- The ringfort must create a settlement choice, not a strictly better wall tier.
- Existing released content remains useful independently and in mixed vanilla
  colonies.
- Core RimWorld remains sufficient; optional DLC behavior must remain isolated.
- XML and verified vanilla patterns remain the default. C# requires a named
  behavioral need. Harmony requires an ADR and compatibility plan.
- No new major gameplay system enters scope after the Version 0.9 checkpoint.
- Failed prototypes narrow or reject scope; they do not automatically create a
  larger framework.

## Version 1.0 Scope

### Required: Existing Foundation

Version 1.0 includes and preserves the released Version 0.6.3 foundation:

- oats, raw oats, hand-quern milling, milled oats, porridge, and flatbread;
- dry-stone walls and the central hearth;
- flax, linen, the linen tunic, the brat cloak, and linen recipe alternatives;
- Kerry cattle and farmhouse cheese;
- the wolfhound; and
- the released bulk-production bills and compatibility contracts.

These systems are not reopened merely because they become part of Version 1.0.
Changes require observed balance, usability, compatibility, or integration need.

### Required: Ringfort Settlement Kit

The ringfort is the marquee Version 1.0 feature. Its smallest coherent form must
let a player construct a recognizable fortified holding through modular,
RimWorld-native placement.

The feature record must resolve:

- whether the kit reuses, extends, or sits beside `EI_DryStoneWall`;
- the minimum wall, entrance, and gate pieces required for a coherent enclosure;
- construction material, work, wealth, durability, cover, pathing, and repair
  tradeoffs against vanilla walls and the released dry-stone wall;
- how square-grid placement produces readable circular, oval, or irregular
  enclosures without a custom drawing interface;
- pen, room, fire, temperature, raid, breach, and ordinary pawn-path behavior;
- original art scope and the relationship to the established stone-construction
  language; and
- stable definitions, save behavior, removal, rollback, and mod compatibility.

Explicitly excluded from the first ringfort slice:

- procedural world generation or automatic fort placement;
- multi-level maps, simulated elevation, or custom vertical combat;
- special raid AI, killbox automation, or global defense bonuses;
- a complete faction, governance, hospitality, or ritual system; and
- an oversized architecture set not required to construct the enclosure.

### Required: Hearth, Larder, and Hospitality

Version 1.0 should include one bounded hearth-and-larder feature that makes daily
life inside the mature holding matter. The approved Version 0.7 slice is the
Hearth/Larder/Hospitality checkpoint: improve the released central hearth, add a
hearth-only smoked-meat reserve food, and add an alternate hearth route to
vanilla wort and vanilla beer using oats and hops.

The accepted slice must:

- create clear labor, ingredient, shelf-life, storage, scheduling, or hospitality
  decisions;
- use existing food, hearth, stove, bill, storage, policy, research, barrel, and
  caravan behavior;
- remain materially worse than pemmican and packaged survival meals in their
  specialist roles;
- preserve vanilla wort, fermenting-barrel, and beer contracts rather than adding
  a new drink, alcohol effect, barrel, fermentation system, or research project;
- avoid a new storage framework, preservation manager, custom UI, or resource
  extraction system; and
- keep farmhouse cheese, oat flatbread, pemmican, survival meals, and
  refrigeration as understandable alternatives.

### Required: Cohesion and Release Quality

Version 1.0 must include the integration work needed to present a finished mod:

- understandable build-menu organization and feature discovery;
- full-colony balance from first holding through mature settlement;
- clean Core and supported-DLC loading;
- affected save/load, removal, rollback, and compatibility checks;
- normal-zoom art and UI readability beside vanilla content;
- concise installation, upgrade, support, and contributor guidance;
- release-quality Workshop presentation; and
- exact-artifact GitHub and Steam publication verification.

### Conditional: Round Tower Refuge

The round tower is a desired supporting landmark, not a guaranteed Version 1.0
requirement. It enters scope only after a prototype proves a meaningful RimWorld
role.

Acceptable directions may include a costly refuge, last-resort shelter, or another
bounded settlement-defense function that remains understandable through normal
RimWorld behavior. The tower must not claim simulated height, sight, ranged-combat,
or multi-floor advantages that the implementation does not actually provide.

Stop, defer to Version 1.1 or later, or reject the tower if:

- its value is primarily decorative;
- its role is only "a stronger wall" or generic defensive stat block;
- useful behavior requires invasive combat, pathing, map, or AI patches;
- the building becomes an automatic best defense at comparable access; or
- its art and implementation burden threatens completion of the ringfort and
  required 1.0 quality work.

## Deferred Beyond Version 1.0

The following do not enter Version 1.0 without explicit plan revision and a clear
displacement decision:

- peat extraction and a new fuel-resource chain;
- generic festivals, fairs, or feast systems;
- a new brewing or distilling subsystem, new alcohol, new barrel, or new
  fermentation behavior. The approved oat-wort bill is an alternate route to
  existing vanilla `Wort`, vanilla fermenting barrels, and vanilla `Beer`; it is
  not a new alcohol subsystem;
- factions, governance, law, or large hospitality systems;
- mythology, Sidhe-inspired encounters, or omen chains;
- monastic enclaves, quests, ruins, or world-map expeditions;
- biome or settlement world generation;
- procedural ringfort placement; and
- a general height, tower, fortification, or settlement framework.

Deferral is not rejection. It protects the Version 1.0 promise and leaves later
roadmap milestones coherent.

## Delivery Sequence

Version numbers below are planning checkpoints, not authorized scope or promises.
A checkpoint becomes a public release only after its included feature is Done and
the exact candidate receives release approval.

### Discovery Checkpoint — Ringfort Decision

Before the Version 0.8 ringfort implementation branch begins:

1. Research the ringfort as a settlement relationship rather than an exact
   archaeological reconstruction.
2. Verify relevant RimWorld 1.6 building, linking, gate, pathing, room, pen,
   cover, and combat behavior against the installed source/build.
3. Compare a minimal kit against vanilla walls, gates, barricades, and the
   released dry-stone wall.
4. Produce a small layout and art proof at normal zoom.
5. Approve, revise, or reject the smallest coherent feature record.

No public compatibility contract should be created during failed discovery.

### Version 0.7 — Hearth, Larder, and Hospitality

Target outcome: make the central hearth a stronger household anchor and add a
bounded, vanilla-compatible reserve-food and hospitality route.

Exit conditions:

- hearth speed, fuel, ejection, glow, heat, gather, and Flame meditation match
  the approved balance and verified vanilla contracts;
- smoked meat creates a meaningful 30-day reserve-food choice without replacing
  pemmican, packaged survival meals, farmhouse cheese, or fresh meals;
- oat wort consumes 20 raw oats and 5 hops for 5 vanilla Wort only after Brewing,
  and the resulting vanilla barrel-to-Beer path remains unchanged;
- ingredients, provenance, food thoughts, poisoning, diet/Ideology behavior,
  recipe order, save/load, and Core/DLC loading pass affected-path checks; and
- the one original smoked-meat icon is readable at normal zoom and has recorded
  provenance.

### Version 0.8 — Ringfort Foundations

Target outcome: ship the smallest complete, playable ringfort settlement kit.

Exit conditions:

- the enclosure and entrance path work through normal construction and pawn jobs;
- the player can understand why and when to build it;
- vanilla or mixed-material settlements remain viable alternatives;
- defense, wealth, work, footprint, and material costs pass targeted playtesting;
- normal rooms, pens, temperature, fire, raids, breaches, repair, and save/load
  behavior remain coherent; and
- final art reads as one settlement language with existing dry-stone construction.

If this outcome cannot be achieved without a custom placement framework, invasive
patching, or automatic-best defense, stop and return the marquee feature for
product review.

### Version 0.9 — Integration and Release Hardening

Target outcome: freeze major gameplay scope and prove the complete colony arc and
release artifact.

Work includes:

- a go/no-go decision on the round tower after a bounded technical and gameplay
  prototype;
- build-menu and onboarding improvements justified by observed confusion;
- early-, middle-, and mature-colony balance passes;
- mixed vanilla/Emerald Isle settlement testing;
- Core and supported-DLC checks;
- long-save, removal, rollback, performance, localization, and compatibility
  checks triggered by the final feature set; and
- final 1.0 scope freeze.

No new major gameplay system enters scope after this checkpoint. A rejected tower
does not block Version 1.0.

### Version 1.0 — Emerald Isle: The Ringfort

Target outcome: publish the complete, stable core product promise.

Version 1.0 adds no untested headline system after the Version 0.9 scope freeze.
Work is limited to critical fixes, balance corrections, presentation, onboarding,
documentation, compatibility, release evidence, and publication.

## Approval and Stop Gates

### Gate A — Ringfort Worth Building

Approve implementation only when the feature record demonstrates a settlement
decision beyond visual theming and identifies visible costs against vanilla and
released walls.

### Gate B — Ringfort Works in the Real Game

Mark Done only after the complete build, gate, path, room or pen, defense, repair,
damage, save/load, and removal path works in-game with no new recurring errors.

### Gate C — Provisioning Is Distinct

Approve the larder feature only when players can understand its role without
hidden rules and it does not erase an existing food or preservation choice.

### Gate D — Tower Earns Inclusion

Include the tower only after its player value, technical boundary, balance, art,
and affected-path evidence pass independently. Decorative recognizability alone is
insufficient.

### Gate E — Version 1.0 Scope Freeze

Freeze major gameplay after Version 0.9. Later discoveries may fix defects, narrow
scope, or defer content; they may not add a new system without reopening this plan
and identifying what work it displaces.

## Version 1.0 Success Criteria

Version 1.0 is ready when:

- a new player can discover and understand the mod through normal RimWorld UI;
- a colony can establish the released first-holding systems and develop into a
  recognizable ringfort settlement;
- ringfort, vanilla, and mixed settlement patterns remain viable;
- the mature colony still uses or deliberately replaces early content through
  understandable choices rather than forced obsolescence;
- the complete food, craft, animal, apparel, hearth, architecture, and defense
  loop produces recognizable stories without excessive bill or build-menu clutter;
- Core and supported DLC configurations load and play without critical errors;
- credible persistence, performance, compatibility, localization, art, and
  rollback risks have passing evidence;
- no unresolved critical defect or known release blocker remains; and
- the exact GitHub and Steam artifacts match the approved release candidate.

## Announcement Readiness

Do not make a firm Version 1.0 feature announcement until:

- the ringfort's smallest playable form has passed in-game testing;
- its final visual direction is credible at normal zoom;
- the provisioning feature has a distinct approved role;
- the round tower has an explicit include-or-defer decision; and
- Version 0.9 has frozen major gameplay scope.

The proposed public message is:

> Emerald Isle 1.0: build, provision, and defend a mature ringfort holding on the Rim.

The release presentation should show the settlement at a readable gameplay scale,
including its entrance, courtyard life, existing crops and animals, hearth and food
work, and defensive use. The tower appears in public material only if it ships.

## Primary Risks and Responses

| Risk | Response |
|---|---|
| Ringfort is only a visual wall reskin | Require a clear layout, access, cost, and defensive decision before approval |
| Ringfort becomes an automatic defense upgrade | Compare complete construction, wealth, repair, cover, footprint, and breach lifecycles |
| Square-grid art cannot read as a ringfort | Prototype modular curves and irregular layouts at normal zoom before freezing defs |
| Tower requires fictional or invasive height mechanics | Constrain it to verified RimWorld behavior or defer it |
| Provisioning duplicates released or vanilla food | Require one distinct role and reject it if comparison remains subtle |
| Art scope delays the release | Freeze the minimum kit and shared stone language before optional variants |
| Public IDs create premature compatibility burden | Keep failed discovery outside public releases and add only accepted defs |
| Feature accumulation obscures the headline | Freeze major gameplay at Version 0.9 and defer unrelated candidates |
| Process consumes more effort than development | Keep one plan, one feature record per approved slice, and evidence in implementation/release PRs |

## Approved Decisions

The maintainer approved these five decisions as the authoritative Version 1.0
delivery direction:

1. The ringfort is the required marquee feature for Version 1.0.
2. One distinct provisioning/larder feature is required for Version 1.0.
3. The round tower is conditional and may be deferred without blocking Version
   1.0.
4. Version 0.7, 0.8, and 0.9 are planning checkpoints with major gameplay frozen
   after Version 0.9.
5. Peat, generic festivals, brewing, factions, mythology, and world generation
   remain outside Version 1.0 unless this plan is explicitly reopened.

## Approval

**Decision:** Approved as written<br>
**Approved by/date:** Patrick Mee, 2026-08-29<br>
**Conditions:** Each gameplay slice still requires its own proportionate feature
record and maintainer approval. The round tower remains conditional, and failed
ringfort discovery must narrow, revise, or reject implementation rather than
creating a larger framework.
