# FS-009 Pasture and Larder Asset Record

**Status:** Runtime exports complete; human in-game visual review pending

**Feature record:** Direct maintainer request restated in the implementation PR

**Production date:** 2026-07-21

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
| Kerry bull east | `Things/Pawn/Animal/KerryCattle/EI_KerryBull_east` | 256x256 RGBA | `f46b9d765d5fc3fce88c8e4fd04a08b78b8315589bfa0d6d8be0002ec16c10a3` |
| Kerry bull north | `Things/Pawn/Animal/KerryCattle/EI_KerryBull_north` | 256x256 RGBA | `b56dc3b60c1794b7b86329e7cbb864f9963b609af99c4f72fbd02f6dd74e707c` |
| Kerry bull south | `Things/Pawn/Animal/KerryCattle/EI_KerryBull_south` | 256x256 RGBA | `bfa7b8a1c23c6d9b7bb9812a358a2ae6124d29dbc12f03d8f5b543e4381326fc` |
| Kerry cow east | `Things/Pawn/Animal/KerryCattle/EI_KerryCow_east` | 256x256 RGBA | `a0524e31afc17c09722c94cc7cfbfd42f42068f75f60d5e7352fcdd244e07c77` |
| Kerry cow north | `Things/Pawn/Animal/KerryCattle/EI_KerryCow_north` | 256x256 RGBA | `7f45bcfb878010bb9f9c9ec96ce401fec51d45d42c02df82fee335b96c020f7e` |
| Kerry cow south | `Things/Pawn/Animal/KerryCattle/EI_KerryCow_south` | 256x256 RGBA | `609e36ff42050524247fcbda54c813309ef1f7989204dab544fb7a419064698c` |
| Desiccated Kerry east | `Things/Pawn/Animal/KerryCattle/EI_KerryDessicated_east` | 256x256 RGBA | `eb016272b640be6fe2707edb70fbe9169588cecf264361d065b52b661abac73d` |
| Desiccated Kerry north | `Things/Pawn/Animal/KerryCattle/EI_KerryDessicated_north` | 256x256 RGBA | `1ea7eac00b9061d5b7ad6743c595f5bc1772c95c5ed906ccce1644c11989ab39` |
| Desiccated Kerry south | `Things/Pawn/Animal/KerryCattle/EI_KerryDessicated_south` | 256x256 RGBA | `5bb96f58ead3ec3f62ecd7331b00e7deca3f9e00b6d4a8ece01aed2a506db194` |
| Farmhouse cheese | `Things/Item/Food/EI_FarmhouseCheese` | 128x128 RGBA | `b07aefe80e92c50cd47fd1b6700772ce5ee4c092bd07dadcb08b583b090d4c25` |

West-facing cattle use RimWorld's normal mirroring of the east export.

## Production Controls

The cattle prompts requested one original, predominantly black, small and
fine-boned dairy animal in north, east, and south views; neutral overhead light;
plain painterly game-sprite treatment; and no scenery, text, watermark, Dexter
traits, Holstein markings, yak coat, hump, or exaggerated beef musculature. The
cow prompt additionally required a modest udder and only a restrained white
udder marking. A sex-neutral desiccated-state prompt requested a small horned
cattle skeleton with weathered ivory bone, restrained dried-hide remnants, and no
blood, flesh, gore, or copied Core art. The cheese prompt requested one compact
straw-gold farmhouse wheel with a nearby cut wedge and excluded packaging, plate,
mold, holes, and scenery.

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
