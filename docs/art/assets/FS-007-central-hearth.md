# FS-007 Central Hearth Asset Record

**Status:** Approved and frozen for Version 0.5 by Patrick Mee, 2026-07-13<br>
**Feature:** [FS-007 — Central Hearth](../../specifications/FS-007-central-hearth.md)<br>
**Production date:** 2026-07-13<br>
**Human acceptance owner:** Patrick Mee

## Provenance and License

The source image was generated with OpenAI image generation under project art
direction, without input images or third-party assets. Codex removed a flat green
chroma key, cropped the resulting alpha sprite, and downscaled it into the runtime
building texture and menu icon. The generated source image is a local production
intermediate and is not a runtime dependency or committed source-art file.

The exports are creative assets governed by
[`CREATIVE_ASSETS_LICENSE.md`](../../../CREATIVE_ASSETS_LICENSE.md), not the MIT
source-code license.

## Runtime Exports

| Asset | Runtime path | Dimensions | SHA-256 |
|---|---|---:|---|
| Building texture | `Things/Building/Temperature/CentralHearth/EI_CentralHearth` | 256×128 RGBA | `ec5390a9834c92f3499370886358b5fa17d4c4f539c8c86a9a976c9a9f4f63f4` |
| Temperature menu icon | `Things/Building/Temperature/CentralHearth/EI_CentralHearth_MenuIcon` | 64×64 RGBA | `98bccf2d8f0a8f8993e515aa7357ee9eba37a2f9ac5cf53e9cbd5f4374cdabbc` |

## Production Controls

- The generation prompt requested one original horizontal, stone-lined household
  cooking hearth with an unlit fuel bed and iron trivet in a readable top-down game
  silhouette.
- The prompt excluded active flame, smoke, scenery, copied game textures, decorative
  knotwork, text, and watermarks so RimWorld's fueled fire overlay supplies the live
  flame state.
- The standard image-generation chroma helper sampled and removed the flat green
  background with a soft matte and despill pass.
- Deterministic post-processing used the alpha bounds to fit the source into a
  256×128 building texture and a centered 64×64 menu icon, preserving transparency.
- Exact filename case, dimensions, and texture stems match the FS-007 ThingDef.

## Review Disposition

Automated inspection confirmed the recorded RGBA dimensions, alpha, SHA-256 hashes,
and XML path references. Human in-game review confirmed normal-zoom readability,
the centered vanilla fire overlay, dry-stone architectural fit, and clear stuff
tinting across the requested Granite, Limestone, Sandstone, Slate, Marble, and Jade
comparison set.

The maintainer's Pass 2 review approved the current sprite as the baseline design.
It reads immediately as a durable, everyday, early medieval dry-stone cooking hearth;
its silhouette, painterly rendering, outline weight, and material behavior fit both
vanilla RimWorld and Emerald Isle.

A single constrained refinement candidate explored slight rim irregularity, limited
capstone variation, and a deeper pit. It was rejected because the result enlarged
several capstones, increased surface texture density, and produced a more regular
ring without a clear gameplay-zoom improvement. Per the maintainer's stop guidance,
the approved baseline was frozen instead of iterating further. No runtime texture,
dimensions, pivot implication, transparency, filename, or asset path changed.
