# Hearth/Larder Smoked Meat Asset Record

**Status:** Generated and static-inspection passed; human in-game acceptance pending<br>
**Feature:** Hearth, Larder, and Hospitality<br>
**Production date:** 2026-08-23<br>
**Human acceptance owner:** Patrick Mee

## Provenance and License

The original source was generated with OpenAI's built-in `image_gen` tool under
project art direction, without input images or third-party assets. The selected
generation was output as
`/Users/patrickmee/.codex/generated_images/01a03038-8f4a-76e0-89e1-eccc7395f562/exec-bece491a-6283-4b45-9620-d5b6fc5114b4.png`
on 2026-08-23. The source is a local production intermediate and is not a
runtime dependency or committed source-art file.

The runtime export is a creative asset governed by
[`CREATIVE_ASSETS_LICENSE.md`](../../../CREATIVE_ASSETS_LICENSE.md), not the MIT
source-code license.

## Generation Prompt

```text
Use case: stylized-concept
Asset type: RimWorld item icon
Primary request: one original ready-to-eat smoked meat food token for a colony survival game
Subject: a compact tied bundle of three to five smoked meat strips, clearly edible and shelf-stable
Style/medium: simplified hand-painted 2D game inventory icon; bold near-black outline; two or three broad matte tonal regions per strip; restrained texture; match a 128x128 vanilla-compatible item token
Composition/framing: single centered bundle in a three-quarter top-down view, generous transparent padding, opaque silhouette occupying about 70% of a square runtime canvas
Lighting/mood: neutral soft light with one warm edge highlight
Color palette: deep brown, charcoal, muted red-brown, small ochre tie
Materials/textures: dry smoked meat with broad blocky shading and slightly rough cut ends
Constraints: genuinely transparent background with preserved alpha; no text; no logos; no watermark; original design; readable at 64x64 and 128x128; no scenery; no copied game art
Avoid: photorealism, glossy product rendering, fine pores, high-frequency surface detail, blood, gore, bones, human anatomy, insects, green or magenta background, extra food items, plate, packaging, crumbs
```

## Runtime Export

| Asset | Runtime path | Dimensions | SHA-256 |
|---|---|---:|---|
| Smoked meat item icon | `Things/Item/Food/EI_SmokedMeat` | 128×128 RGBA | `d2be23160c0030e5a094eddc372745006d8f9f25eb72c648f9924c7c1a5d22ab` |

The generated 1254×1254 RGBA source was deterministically resized to 128×128
with macOS `sips`, preserving its transparent alpha channel. The final export
is the only smoked-meat art file committed to the repository.

## Review Disposition

Static inspection confirms a transparent, centered, readable food silhouette at
the project's existing 128×128 item convention. Human review remains required
for normal-zoom readability beside vanilla food, stockpile and inventory legibility,
and any selection or lighting concerns.
