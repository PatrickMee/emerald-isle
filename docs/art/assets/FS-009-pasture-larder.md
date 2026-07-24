# FS-009 Pasture and Larder Asset Record

**Status:** Revised runtime exports complete; human in-game visual re-review pending

**Feature record:** Direct maintainer request restated in the implementation PR

**Production date:** 2026-07-21

**Visual revision date:** 2026-07-23

**Anatomy revision date:** 2026-07-24

**Human acceptance owner:** Patrick Mee

## Provenance and License

The source sheets and cheese source image were generated with OpenAI's built-in
image-generation tool under project art direction. The 2026-07-24 anatomy
revision used a maintainer-provided in-game comparison screenshot as a
style-and-perspective reference for the abstract animal-token construction; the
prompt explicitly excluded the failed black Kerry sprites visible in that image.
No screenshot or Core-art pixels were copied or composited into the exports. The
generated sources are local production intermediates and are not runtime
dependencies or committed source-art files.

Codex removed a flat magenta chroma key, contracted the cattle matte by one pixel
to remove a visible fringe, split the directional sheets, and deterministically
fit the subjects into the runtime canvases. The exports are creative assets
governed by [`CREATIVE_ASSETS_LICENSE.md`](../../../CREATIVE_ASSETS_LICENSE.md).

Visual breed direction used descriptive facts, not copied artwork. The Irish
Native Rare Breed Society describes Kerry cattle as small, black dairy-type
cattle with fine bone, occasional white at the udder, slender pale horns with dark
tips, and notable hardiness. The Kerry Cattle Society identifies the breed as an
Irish native dairy breed.

- <https://inrbs.ie/kerry-cattle/> (accessed 2026-07-21)
- <https://www.kerrycattle.ie/> (accessed 2026-07-21)

## Runtime Exports

| Asset | Runtime path | Dimensions | SHA-256 |
|---|---|---:|---|
| Kerry bull east | `Things/Pawn/Animal/KerryCattle/EI_KerryBull_east` | 256x256 RGBA | `03fed68d8263fe0cbd84f53617f3105ffc8d3bbc4145b989d8c3e346e31a8437` |
| Kerry bull north | `Things/Pawn/Animal/KerryCattle/EI_KerryBull_north` | 256x256 RGBA | `47e5e999f48527bfd053ce9a15f28de5ea54a1f3d25cf97b554e22d64dcfb3fd` |
| Kerry bull south | `Things/Pawn/Animal/KerryCattle/EI_KerryBull_south` | 256x256 RGBA | `0020753a54effff80d06164899fc4a4af7e4f0a8cf6d1ed8bd28a901fb922602` |
| Kerry cow east | `Things/Pawn/Animal/KerryCattle/EI_KerryCow_east` | 256x256 RGBA | `cd6c9120207eef3b633cfb2c4bf33499716f11a3df43301a3c906a8436d728ec` |
| Kerry cow north | `Things/Pawn/Animal/KerryCattle/EI_KerryCow_north` | 256x256 RGBA | `96c0cc0472d7e99453fd47444e640cabc9b31990b1402d47ef8a166904219502` |
| Kerry cow south | `Things/Pawn/Animal/KerryCattle/EI_KerryCow_south` | 256x256 RGBA | `cbc5b7bea469468706ba1c9dec2652a1262a4b65b824e73ea1ba6123a6711d85` |
| Desiccated Kerry east | `Things/Pawn/Animal/KerryCattle/EI_KerryDessicated_east` | 256x256 RGBA | `eac68129492ca33ead7e9ca6658ea9002c3e30ea578a803ba7f7b7638d4ee39d` |
| Desiccated Kerry north | `Things/Pawn/Animal/KerryCattle/EI_KerryDessicated_north` | 256x256 RGBA | `4e53b8497c94c4de2142e9ac107c09cbe3da198c876fd55541de1d3d0063f84b` |
| Desiccated Kerry south | `Things/Pawn/Animal/KerryCattle/EI_KerryDessicated_south` | 256x256 RGBA | `b838c23eb5819e51c9e8625ae2d9e36f711ad8928cb97c0b245fc5b8af319a8c` |
| Farmhouse cheese | `Things/Item/Food/EI_FarmhouseCheese` | 128x128 RGBA | `b07aefe80e92c50cd47fd1b6700772ce5ee4c092bd07dadcb08b583b090d4c25` |

West-facing cattle use RimWorld's normal mirroring of the east export.

## Production Controls

The original cattle prompts requested one predominantly black, small and
fine-boned dairy animal in north, east, and south views. Human in-game review on
2026-07-23 showed that those exports retained too much photographic anatomy and
detail and read too large beside pawns. The replacement style-transfer prompts
therefore required an original, compact RimWorld-native sprite treatment with a
bold contour, chunky silhouette, broad matte value blocks, three to four coat
tones, simplified anatomy, and no photorealism, individual hair, glossy detail,
or fine musculature. The cow retained a modest udder and restrained light
marking; the bull used the revised cow sheet as its style-and-scale reference.
The replacement desiccated prompt applied the same simplified visual language
with only major skull, rib, spine, and leg forms and no blood, flesh, gore, or
copied Core art. The cheese prompt requested one compact straw-gold farmhouse
wheel with a nearby cut wedge and excluded packaging, plate, mold, holes, and
scenery.

The 2026-07-24 comparison review found that the simplified cattle still used
standing side-elevation anatomy with long, individually readable legs, unlike
RimWorld's compact top-down animal tokens. The final anatomy prompts used the
maintainer screenshot's vanilla cow, alpaca, and muffalo only as style and
perspective references. They required a dominant bean/egg/lozenge torso,
small attached head, and at most tiny hoof nubs integrated into the lower body
edge. The bull prompt prohibited udder, teats, and visible genital anatomy; a
targeted correction removed an incorrectly inherited udder before export. The
desiccated prompt retained the same compact silhouette with only broad skull,
rib, and spine cues rather than a standing skeleton.

The same review showed that art replacement alone could not correct map scale:
runtime export fitting fills each texture canvas. Adult bull/cow draw sizes were
therefore reduced from `2.15`/`2.05` to `1.85`/`1.75`, compared with the verified
vanilla adult bull/cow baseline of `2.7`/`2.6`. Calf and juvenile sizes were
reduced proportionally.

All three prompts required a uniform `#ff00ff` background, crisp separated
subjects, generous padding, and no magenta in the subject. Runtime exports were
fitted with Lanczos resampling into fixed transparent RGBA canvases without
further painting or copied game assets.

## Review Checklist

- confirm all four cattle directions read as one breed at normal gameplay zoom;
- confirm cow and bull remain distinguishable and visibly smaller than vanilla cows;
- inspect outlines in snow, darkness, and selection highlighting for residual fringe;
- confirm calf scaling remains legible without implying a separate adult-sized calf;
- confirm the cheese reads as food in stockpiles and bill/product icons.
