# FS-008 Brat Cloak Asset Record

**Status:** Candidate exports produced 2026-07-14; maintainer in-game visual
acceptance pending<br>
**Feature:** [FS-008 — Brat Cloak](../../specifications/FS-008-brat-cloak.md)<br>
**Human acceptance owner:** Patrick Mee

## Runtime Contract

| Asset group | Runtime path contract | Exports |
|---|---|---:|
| Cloak ground icon | `Things/Pawn/Humanlike/Apparel/BratCloak/EI_BratCloak` | 1 |
| Cloak worn art | `.../EI_BratCloak_{Male,Female,Thin,Hulk,Fat}_{north,east,south}` | 15 |

All 16 exports are 128×128 RGBA PNGs following the FS-006 apparel pipeline.
East-facing worn art is mirrored by the vanilla renderer for west-facing pawns.
All art uses neutral grayscale so RimWorld's Stuff tint supplies the textile
color; a wool brat reads as wool through the stuff tint, not baked-in color.

## Art Brief

A heavy rectangular cloak draped over the shoulders and pinned at the chest,
covering torso, neck, and shoulders over other clothing. Plain construction:
thick fabric mass, simple folds, no decoration, no modern tailoring, no clasps
beyond a single plain pin, no copied game assets. It must read at normal zoom as
a distinct outer layer over the linen tunic without hiding the pawn silhouette.

## Provenance

The 16 candidate exports were generated programmatically on 2026-07-14 by Claude
(Anthropic) under Emerald Isle art direction, using an original Python/Pillow
drawing script and no input images or third-party assets. The script derives
per-body-type cloak proportions from the accepted FS-006 tunic silhouettes and
reproduces the established flat two-tone style: fill `(205,205,198)` and outline
`(56,56,52)` at the measured alpha levels, so RimWorld's Stuff tint supplies the
textile color. The generation script is a local production intermediate kept out
of the repository. Runtime exports are creative assets governed by
[`CREATIVE_ASSETS_LICENSE.md`](../../../CREATIVE_ASSETS_LICENSE.md).

Candidate status: automated inspection confirms count, dimensions, alpha, and
XML-referenced stems. The exports remain candidates until maintainer visual
acceptance in-game; readability defects reopen the art pass, following the
FS-006 precedent.
