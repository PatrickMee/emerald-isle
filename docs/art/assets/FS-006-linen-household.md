# FS-006 Linen Household Asset Record

**Status:** Maintainer playtest accepted, 2026-07-13<br>
**Feature:** [FS-006 — Linen Household](../../specifications/FS-006-linen-household.md)<br>
**Production date:** 2026-07-12<br>
**Human acceptance owner:** Patrick Mee

## Provenance and License

OpenAI image generation created one original six-panel production source under
Emerald Isle art direction, without input images or third-party assets. It
contained two mature flax clusters, one immature cluster, harvested flax, folded
linen, and a plain early-medieval-inspired tunic. Codex removed the flat magenta
chroma key, resized the source art to 128×128 runtime sprites, derived stack-count
and immature variants, converted Stuff-tinted exports to neutral grayscale, and
created the five vanilla adult body-type sets for north, east, and south views.

The generated source sheet and conversion helper are ignored local production
intermediates, not runtime dependencies or committed source art. Runtime exports
are creative assets governed by
[`CREATIVE_ASSETS_LICENSE.md`](../../../CREATIVE_ASSETS_LICENSE.md), not the MIT
source-code license.

## Runtime Contract

| Asset group | Runtime path contract | Exports |
|---|---|---:|
| Mature flax | `Things/Plant/Flax/EI_Plant_Flax/EI_Plant_Flax_{a,b}` | 2 |
| Immature flax | `Things/Plant/Flax/EI_Plant_Flax_Immature/EI_Plant_Flax_Immature_{a,b}` | 2 |
| Raw flax stacks | `Things/Item/Resource/Textile/EI_RawFlax/EI_RawFlax_{a,b,c}` | 3 |
| Linen stacks | `Things/Item/Resource/Textile/EI_Linen/EI_Linen_{a,b,c}` | 3 |
| Tunic ground icon | `Things/Pawn/Humanlike/Apparel/LinenTunic/EI_LinenTunic` | 1 |
| Tunic worn art | `.../EI_LinenTunic_{Male,Female,Thin,Hulk,Fat}_{north,east,south}` | 15 |

All 26 exports are 128×128 RGBA PNGs. East-facing worn art is mirrored by the
vanilla renderer for west-facing pawns. Linen stacks and tunic art use neutral
grayscale so RimWorld's Stuff tint supplies the linen color.

## Production Controls

- The source prompt required distinct flax botany, practical undyed fiber and
  cloth, plain construction, no modern tailoring, no decoration, and no copied
  game assets.
- The crop variants preserve transparent separation and readable silhouettes at
  normal zoom. Stack-count variants use vanilla `_a`, `_b`, and `_c` suffixes.
- Worn art follows the verified legacy apparel contract: five adult body types,
  three stored directions, and the XML `wornGraphicPath` stem.
- Automated inspection confirms dimensions, alpha channels, filename case, and
  all XML-referenced texture stems. Maintainer playtesting confirmed normal-zoom
  readability and the complete player-facing slice in RimWorld 1.6.

## Review Disposition

Patrick Mee accepted the FS-006 playtest on 2026-07-13. The runtime exports are
accepted for this feature branch; future changes require a rendering defect,
gameplay-readability issue, or a later project-wide art-direction decision.
