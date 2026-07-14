# FS-008 Feature Record: Brat Cloak

**Status:** Approved<br>
**Milestone:** Version 0.5 — Living Culture<br>
**Risk class:** Standard<br>
**Owner:** Patrick Mee<br>
**Created:** 2026-07-14<br>
**Catalog candidate:** AP-01

## Decision

**Player value:** Give colonies one practical outer garment that completes the
everyday dress pair started by the linen tunic: a léine under a brat. The brat is
a cheap, quick-to-make cloak that keeps early and mid colonies warm without
competing with armor, so players choose between warmth now and protection later.
Together with the tunic it makes an Emerald Isle colony visually recognizable at
normal zoom.

**In scope:**

- one shell-layer, brat-inspired cloak with the player-facing name **brat cloak**;
- stuffable from vanilla Fabric textiles, with insulation-focused stats so wool
  stuffs are the rational default;
- craftable at existing vanilla apparel benches with no new building, recipe
  chain, or resource;
- English localization and original runtime art (item icon plus worn graphics for
  the standard body types and directions, following the FS-006 apparel pipeline).

**Out of scope:** New textile resources or stuff categories, patches to vanilla
wool definitions, sheep or other animals, dyes, status or rank variants, gifting
or hospitality mechanics, Irish-language player text, research projects, ideology
behavior, C#, Harmony, and DLC-specific behavior.

**Vanilla comparison and tradeoff:** Closest alternatives are the duster and
parka. The brat must be cheaper in material and work than both and warmer than
the duster, while offering clearly weaker armor contribution and no heat-tolerance
advantage. Intended niche: the best low-cost cold-weather outer layer before the
colony can afford dusters, parkas, or armor that occupy the same layer; a
situational choice, never a strict upgrade. Exact values are implementation
decisions bounded by the acceptance checks below.

**Material decision:** The brat is historically a woollen cloak. A wool-only
material restriction was considered and rejected: vanilla wools do not form their
own stuff category, so enforcement would require patching vanilla wool
definitions, adding compatibility surface for a restriction the fiction does not
need. Instead the cloak accepts vanilla Fabric stuffs and its stat multipliers
make wool the optimal and default presentation, mirroring how FS-006 keeps linen
inside vanilla Fabric recipes. The RimWorld wiki (accessed 2026-07-14) confirms
the Fabric category contains all wools alongside cloth, devilstrand, hyperweave,
and synthread, with no wool-specific category; the implementation still confirms
this against installed RimWorld 1.6 data before freezing the choice. RimWorld
wools are also notably flammable, which the balance pass may use as part of the
wool brat's tradeoff.

## Basis

FS-006 research (accessed 2026-07-12) already establishes the garment category:
the Early Medieval Archaeology Project economic synthesis describes the brat
specifically as a woollen cloak worn over the léine, and Wincott Heckett reports
the archaeological basis for linen tunics paired with woollen cloaks in early
Irish display. See the source list in
[FS-006 — Linen Household](FS-006-linen-household.md). No new research is
required: the feature transforms a well-attested everyday garment category and
claims no specific cut, color, fastening, or social meaning.

**ADR-0006 relationship:** craft and material, plus dress as social identity. The
cloak-over-tunic pairing is a durable relationship that later features may carry
into quality, status, or exchange contexts without freezing the mod at one era.

## Implementation Boundary

- XML only; no C#, Harmony, or patches to vanilla definitions.
- Public IDs: `EI_BratCloak` plus its localization keys become compatibility
  contracts at release; no save-serialized state beyond the apparel item itself.
- No DLC requirement; no DLC-conditional behavior.
- Art: original textures following the FS-006 worn-apparel pipeline; provenance
  recorded in `docs/art/assets/FS-008-brat-cloak.md` at implementation.
- Localization: English DefInjected keys; functional English name; log in the
  cultural review register (low risk, no Irish-language text).

## Acceptance Checks

- [ ] A colonist can craft the brat cloak at an existing vanilla apparel bench
      from stocked vanilla textiles and wear it over the linen tunic; both render
      correctly at normal zoom in all body types and directions.
- [ ] With identical stuff, the brat is cheaper in material and work than the
      duster and parka, insulates against cold better than the duster, and
      contributes less armor than both; a wool brat outperforms a cloth brat for
      warmth. The brat is selected in at least one rational early-colony loadout
      without displacing dusters, parkas, or armor in every loadout.
- [ ] Textile categorization verified against installed RimWorld 1.6 data; the
      material decision above is confirmed or revised at implementation review.
- [ ] Clean load with no Emerald Isle errors or warnings; save/load preserves
      worn and stockpiled cloaks; the staged package passes CI validation.

## Approval

**Decision:** Approved<br>
**Maintainer/date:** Patrick Mee, 2026-07-14<br>
**Conditions:** none

## Done Evidence

[Recorded at implementation: static/build result, in-game player path, log
review, maintainer visual and gameplay review.]

**Decision:** Done | Not Done<br>
**Maintainer/date:** [name, YYYY-MM-DD]
