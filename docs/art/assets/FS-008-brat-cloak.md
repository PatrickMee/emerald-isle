# FS-008 Brat Cloak Asset Record

**Status:** Released in `v0.3.0` — maintainer in-game visual acceptance recorded
2026-07-17<br>
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

The initial 16 candidate exports were generated programmatically on 2026-07-14 by
Claude (Anthropic) under Emerald Isle art direction, using an original
Python/Pillow drawing script and no input images or third-party assets. On
2026-07-16, after the first wool in-game review showed that the front silhouette
read as a rigid poncho or apron, the 15 worn exports were revised with OpenAI's
built-in image-generation tool. Each existing body-type and direction export was
used as the edit target, while the accepted revised male directional exports were
used as design references for the other body types. The revision softened the
sides and hem, clarified the shoulder drape, lowered the front fastening, and
added restrained folds. Flat magenta chroma-key backgrounds were removed locally,
and final exports were downsampled to the existing 128x128 RGBA runtime contract.
The first revised wool screenshot still showed the pawn head hiding the fastening
and shoulder construction, so a second front-view pass widened the five south
silhouettes and moved their fastening and central fold into the visible lower
region. Subsequent east- and north-view screenshots showed that the side read as
a narrow hanging panel and the back as a straight tunic; a third pass gave the
five north exports broader shoulders, a lower wrap seam, and a flared hem. An
attempt to solve the side readability problem with an asymmetric rearward drape
was rejected as theatrical and inconsistent with the practical rectangular
garment. A supplied reconstruction photograph became the design authority for
the final five east exports: compact, mostly vertical blanket drapes with modest
side depth, near-level hems, and no train or swept tail. The ground icon was
unchanged. No third-party assets were incorporated into the runtime exports.
Runtime exports are creative assets governed by
[`CREATIVE_ASSETS_LICENSE.md`](../../../CREATIVE_ASSETS_LICENSE.md).

Automated inspection confirms count, dimensions, alpha, and XML-referenced
stems. Patrick Mee accepted the revised exports in-game on 2026-07-17 after
reviewing the front, side, and back views at normal play zoom. The accepted side
view uses the practical compact drape established by the supplied reconstruction
photograph, with no train or swept tail. Any later readability defect reopens the
art pass, following the FS-006 precedent.
