# FS-001 Oats Asset Record

**Status:** Initial in-game art review passed; release-context comparison deferred<br>
**Feature:** [FS-001 — Oats](../../specifications/FS-001-oats.md)<br>
**Production date:** 2026-07-05<br>
**Human acceptance owner:** Patrick Mee

## Provenance and License

The five exports were generated with OpenAI image generation under project art
direction, without input images or third-party assets. Codex removed a flat magenta
chroma key, downscaled the results to 128×128, and retained transparency. The
generated source images are local production intermediates and are not runtime
dependencies or committed source art.

The exports are creative assets governed by
[`CREATIVE_ASSETS_LICENSE.md`](../../../CREATIVE_ASSETS_LICENSE.md), not the MIT
source-code license. No additional permission to copy, modify, or redistribute is
granted unless the project records one later.

## Runtime Exports

| Asset | Runtime path | SHA-256 |
|---|---|---|
| Mature A | `Things/Plant/Oats/EI_Plant_Oats_a` | `5918782d38a76093942b946064af629ec95acb3ae765a7ed907ad6b26d846498` |
| Mature B | `Things/Plant/Oats/EI_Plant_Oats_b` | `27ae038215b889d6fa4ca9b5ceac084c177b297e507ef5e4281ead217c8b2ec9` |
| Immature A | `Things/Plant/Oats/EI_Plant_Oats_Immature_a` | `a5483e6f43f5321a5def633c46b0d1c09a8d2d95d65b6e8577e877fb657038ce` |
| Immature B | `Things/Plant/Oats/EI_Plant_Oats_Immature_b` | `d4e5468ed0a4f88c33782a487e7adf38530d2803e06236d8c3e6634a2f79db5d` |
| Harvested oats | `Things/Item/Resource/PlantFoodRaw/EI_RawOats` | `a65661f773ad43a64388f2ac9b762fc1f1c1ca942cf34f7ba39bec5f66bc9d55` |

All exports are RGBA PNGs at 128×128 pixels. Mature plants use loose branching
panicles and muted gold grain; immature plants omit seed heads and use shorter,
sparser silhouettes. The harvested item uses a compact oval grain pile.

## Production Controls

- Original prompts required an oat-specific silhouette, a grounded palette, no
  scenery or text, and no copying of existing RimWorld textures.
- The background-removal key was sampled from the image border and converted to
  alpha with soft matte and despill processing.
- Exact filename case and runtime texture stems match AR-001.
- Automated inspection confirmed 128×128 dimensions and an alpha channel for every
  export.

## Review Disposition

Patrick Mee confirmed the selector icon, mature and immature plants, and harvested
item render correctly in RimWorld at normal play scale. Broader weather, snow,
stockpile, shelf, trade, caravan, and inventory comparisons are release-context
checks and do not block the XML crop implementation.
