# ADR 0005: Shared Stone Construction Language

**Status:** Accepted<br>
**Date:** 2026-07-13<br>
**Decision owner:** Patrick Mee<br>
**Related:** Design Bible 1.1.0, Art Guide, FS-002 Dry-Stone Wall, FU-01 Central Hearth

## Context

Emerald Isle will include multiple stone assets made by the same early medieval
Irish-inspired community. Without a common visual vocabulary, individually strong
assets can imply unrelated builders, materials, or construction techniques. Making
them near-copies would solve consistency at the cost of silhouette, function, and
gameplay readability.

The released FS-002 Dry-Stone Wall already establishes a mortarless, stacked-stone
treatment. The FS-007 Central Hearth completed art review on its feature branch at
commit `3fc6cf7974068d2cc0c95814970e2e6ed54452b9`. Wells, kilns, ovens, mills,
bridges, boundary walls, ruins, and other stone buildings may follow in later
approved scope. A durable principle is needed before those assets accumulate
conflicting conventions.

## Decision Drivers

- Make buildings by one culture read as products of shared knowledge and labor.
- Preserve clear silhouettes and gameplay identities for different structures.
- Maintain RimWorld-scale readability, outline discipline, and texture restraint.
- Avoid visible mortar, cut-masonry logic, or brick-like regularity where the
  intended construction tradition is dry stone.
- Protect approved art from unnecessary redesign and repeated polish cycles.

## Options Considered

### Let each feature define stone independently

- Benefits: Maximum freedom for each asset and no shared review criteria.
- Costs and risks: Visual drift would make one settlement look assembled from
  unrelated cultures and construction traditions.

### Reuse one near-identical stone pattern across every asset

- Benefits: Immediate visual consistency and efficient production reuse.
- Costs and risks: Repetition would weaken silhouettes, obscure function, and make
  structures feel stamped from one texture rather than built for different uses.

### Share a construction language while preserving asset identity

- Benefits: Establishes cultural coherence through proportions, joints, wear,
  rendering, and stacking logic while leaving room for functional forms and wear.
- Costs and risks: Art review must distinguish meaningful functional variation
  from accidental style drift.

## Decision

Adopt the Design Bible's
[Stone Construction Language](../design/design-bible.md#stone-construction-language)
as the project-wide authority for stone assets made by this culture.

Such assets share comparable stone proportions, dry-stone construction without
visible mortar, edge wear, outline weight, painterly texture density, highlight
and shadow treatment, controlled irregularity, and stacked-stone construction
logic. They do not share a mandatory silhouette, footprint, stone arrangement, or
set of functional details.

The frozen FS-002 Dry-Stone Wall is the first approved visual reference, not a
tileable texture source or exact template. This decision does not reopen its
Version 0.1 art approval.

The paired review of the Wall and Central Hearth found their differences acceptable.
The Wall uses flatter, smaller stones in denser horizontal courses because it is a
full-height linked barrier. The Hearth uses larger, rounder rim stones and stronger
local highlights because it is a low, two-tile fire surround that must separate
clearly from its fuel bed and the floor. Both retain mortarless fieldstone, dark
joint separation, controlled hand-built irregularity, compatible outlines,
painterly rendering, and the same broad light direction.

Freeze both assets. Do not continue iteration merely to make their individual stone
shapes or course density more alike. No consistency adjustment is recommended.

## Consequences

**Positive:** Future stone assets will accumulate as a coherent architectural set,
and briefs have concrete criteria for shared cultural authorship.

**Negative:** A future asset may need a limited polish pass if its stone scale,
joint treatment, outline, or rendering density diverges visibly at gameplay zoom.

**Neutral/follow-up:** Functional evidence may justify soot, heat damage, water
staining, heavier structural mass, collapse, or other local variation. Those
differences preserve identity without changing the underlying construction
language.

## Compatibility and Migration

This is an art-direction and documentation change. It changes no Def, translation
key, save contract, runtime path, balance value, or released texture. Approved
Version 0.1 assets require no immediate redesign. Future asset records and art
briefs should link the Design Bible section rather than duplicate its full rules.

## Validation

Review each future stone asset beside the Dry-Stone Wall at normal gameplay zoom,
in representative Stuff colors and lighting where applicable. Confirm:

- fieldstone proportions belong to the same broad size family;
- stones read as stacked and mortarless rather than cut and mortared;
- edge wear, outlines, painterly density, highlights, and joint shadows feel
  related;
- irregularity appears hand-built without becoming noisy or brick-like; and
- silhouette and functional details still identify the asset immediately.

The Central Hearth comparison was completed on 2026-07-13 against FS-007 commit
`3fc6cf7974068d2cc0c95814970e2e6ed54452b9`. Its larger rounded rim stones, deeper
pit contrast, and stronger highlights are accepted functional variation. The
FS-007 art record also shows that a constrained refinement increased capstone scale,
surface density, and ring regularity without improving gameplay readability. That
result supports freezing the approved baseline rather than adding another polish
pass.

## Revisit When

- A feature intentionally represents a different culture, period, material, or
  construction tradition.
- Historical or gameplay evidence requires mortared or cut-stone construction.
- Shared rendering rules reduce normal-zoom readability or functional identity.
- Repeated approved exceptions show that the language is too broad or too narrow.
