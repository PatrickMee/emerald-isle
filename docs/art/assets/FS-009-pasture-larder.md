# FS-009 Pasture and Larder Asset Record

**Status:** Revised runtime exports complete; human in-game visual re-review pending

**Feature record:** Direct maintainer request restated in the implementation PR

**Production date:** 2026-07-21

**Visual revision date:** 2026-07-23

**Human acceptance owner:** Patrick Mee

## Provenance and License

The source sheets and cheese source image were generated with OpenAI's built-in
image-generation tool under project art direction, without input images or
third-party art. The generated sources are local production intermediates and are
not runtime dependencies or committed source-art files.

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
| Kerry bull east | `Things/Pawn/Animal/KerryCattle/EI_KerryBull_east` | 256x256 RGBA | `33aeba146b2966a8bbdb0fe8b326ddf6e0daa82082be6a33ef2cf256c101e1e4` |
| Kerry bull north | `Things/Pawn/Animal/KerryCattle/EI_KerryBull_north` | 256x256 RGBA | `038c17246da10492b78c216b602343c144991ecb350b72a4be29155642eb8a84` |
| Kerry bull south | `Things/Pawn/Animal/KerryCattle/EI_KerryBull_south` | 256x256 RGBA | `6dffd5c7f364197677f27a4f919b9d2f0a52db92e12aa18ffe59b0a502f51987` |
| Kerry cow east | `Things/Pawn/Animal/KerryCattle/EI_KerryCow_east` | 256x256 RGBA | `080962efcab9b43103ef4aa271ff7dab7ebfa16ef06b5a88f2ecb18c9dee65ed` |
| Kerry cow north | `Things/Pawn/Animal/KerryCattle/EI_KerryCow_north` | 256x256 RGBA | `2201d97b766406c97d46bbdc350a5eee8fe67c31bddbc834463b393add26182d` |
| Kerry cow south | `Things/Pawn/Animal/KerryCattle/EI_KerryCow_south` | 256x256 RGBA | `5fe2e13a080516e5d8e470a8843f6993830a8531ae3d849bb688a6231d43107f` |
| Desiccated Kerry east | `Things/Pawn/Animal/KerryCattle/EI_KerryDessicated_east` | 256x256 RGBA | `1c5dfdb1af5209459dee471f9461fa82d5691cf9f4778d276189932c89f2cabe` |
| Desiccated Kerry north | `Things/Pawn/Animal/KerryCattle/EI_KerryDessicated_north` | 256x256 RGBA | `9e6ed2092f68f28cb79917c34282365816c100019cde20a8808be8fc30fa9887` |
| Desiccated Kerry south | `Things/Pawn/Animal/KerryCattle/EI_KerryDessicated_south` | 256x256 RGBA | `33a3882964d96e03e52096d1ac09135228f1ff6b7d85de75faa8d8ae5b83dc5e` |
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
