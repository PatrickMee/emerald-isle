# AN-01 Wolfhound Asset Record

**Status:** Runtime exports complete; human in-game visual acceptance pending

**Feature record:** Direct maintainer request restated in the implementation PR

**Production date:** 2026-08-06

**Human acceptance owner:** Patrick Mee

## Provenance and License

The source images were generated with OpenAI's built-in image-generation tool
under project art direction. A maintainer-supplied modern-breed image-search
screenshot was used only to identify high-level anatomical traits; no reference
pixels or backgrounds were copied or composited. The corrected east-facing
prototype anchored the living directions, and the living set plus the first
desiccated direction anchored the remaining skeletal directions. The approved
Kerry-cattle sprite supplied only project-level guidance for top-down projection,
detail economy, and hidden-limb treatment. A later maintainer-supplied RimWorld
screenshot established the required lateral east/west camera treatment. No Core,
DLC, Kerry-cattle, screenshot, or third-party art pixels were copied or
composited into the exports.

The generated sources are local production intermediates and are not runtime
dependencies or committed source-art files. Codex removed a flat magenta chroma
key with the installed ImageGen helper and a one-pixel matte contraction. A
targeted cleanup neutralized a small number of unintended complementary-green
and magenta edge pixels before the alpha images were resampled to transparent
256x256 runtime canvases. The exports are creative assets governed by
[`CREATIVE_ASSETS_LICENSE.md`](../../../CREATIVE_ASSETS_LICENSE.md).

The subject uses descriptive traits associated with a large rough-coated
coursing hound: a lean continuous torso with subtle chest-to-waist taper, slim
neck, narrow bearded muzzle, folded ears, long low tail, and restrained iron-gray
coat. Long-legged stature is implied through massing rather than literal standing
legs, which remain strongly foreshortened beneath the torso in RimWorld's pawn
projection. Those traits provide development provenance only; the player-facing
animal is original RimWorld fiction and does not claim to reproduce a historical
or modern pedigree breed.

## Runtime Exports

| Asset | Runtime path | Dimensions | SHA-256 |
|---|---|---:|---|
| Wolfhound east | `Things/Pawn/Animal/Wolfhound/EI_Wolfhound_east` | 256x256 RGBA | `cd39d6811d54cda080837875f2ea0f58e2b09a82caf8e0b65d63eb68139eb3bb` |
| Wolfhound north | `Things/Pawn/Animal/Wolfhound/EI_Wolfhound_north` | 256x256 RGBA | `511a077e151b3b4086278c78097fe2720e15d29846b3876456943a31c26da607` |
| Wolfhound south | `Things/Pawn/Animal/Wolfhound/EI_Wolfhound_south` | 256x256 RGBA | `5c119f9ea6cf2940270d34d46d996c901459c0b124242b3cd27d1d10f661454e` |
| Desiccated wolfhound east | `Things/Pawn/Animal/Wolfhound/EI_WolfhoundDessicated_east` | 256x256 RGBA | `a0bd67a70f8a1da5e30f719e6e0d3059c810ce1dbe95e8d41e311ab9be55a2db` |
| Desiccated wolfhound north | `Things/Pawn/Animal/Wolfhound/EI_WolfhoundDessicated_north` | 256x256 RGBA | `b7617225f99f9ef3be7c5686ee69cba6539fb1e163f817f7d3701f45b9b76b2f` |
| Desiccated wolfhound south | `Things/Pawn/Animal/Wolfhound/EI_WolfhoundDessicated_south` | 256x256 RGBA | `3def5612ead116ab106b2820d98e1937c448a5988708a191131285929dacce49` |

West-facing sprites use RimWorld's normal mirroring of the east exports. Puppy,
juvenile, and adult stages reuse the same directional set at definition-controlled
draw sizes, matching the installed Core canine pattern.

## Production Controls

The first committed runtime set was rejected by the maintainer because its tan,
rounded mass and short head read as a compact terrier rather than an Irish
wolfhound-inspired hound. The replacement set changes the identifying cues that
remain visible in RimWorld's projection: iron-gray rough coat, substantially
narrower bearded muzzle, smaller folded ears, leaner continuous torso, subtle
chest-to-waist taper, and a long low tail. It deliberately does not expose full
long legs, which would break the established top-down animal-token language.

A second maintainer review identified that the first replacement east sprite
still used the north/south overhead camera. The final east sprite therefore uses
a strict lateral profile: one visible eye, one dominant folded ear, side-on
muzzle, raised neck, lean back, tucked lower belly, and low tail. RimWorld mirrors
that export for west. North and south retain their appropriate overhead views.

A third maintainer review found that the lateral muzzle's separate pointed hair
strands read as otter whiskers. The final east export replaces them with one
compact, connected rough beard beneath the lower muzzle and chin, using a short
blunt edge and broad tufts while preserving the lean profile.

A fourth maintainer review requested a more immediately recognizable wolfhound
silhouette without exposing anatomically long legs. The revised east export
raises the torso modestly on short simplified paw stubs, shortens and lightens
the body, lifts the shoulder line, lengthens the neck, and strengthens the deep
chest-to-tucked-waist transition. The head retains the connected beard while
using a longer rectangular muzzle and stronger brow. Broad value groups and a
cleaner outer contour preserve the rough coat with less edge noise at gameplay
zoom; the sprite canvas and draw scale are unchanged.

All replacement living prompts required a bold near-black contour, four or five
broad matte iron-gray coat tones, sparse rough-coat tufts, heavily foreshortened
or occluded legs, and no photorealistic anatomy, armor, collar, ornament,
scenery, shadow, or text. Each direction preserves identity while using its
vanilla camera convention rather than rotating one projection mechanically.

The desiccated prompts kept the same compact silhouette and used broad skull,
rib, spine, pelvis, and folded-limb cues. They prohibited blood, flesh, gore,
organs, horror presentation, humanlike anatomy, and copied game art. Downsampling
subordinates the source detail to a normal map-scale carcass read.

## Review Checklist

- [x] corrected east prototype is a readable lateral profile at 64x64 and keeps
  full legs hidden;
- [x] all required directional, life-stage, and desiccated runtime paths resolve;
- [x] transparent corners, alpha channel, dimensions, and hashes are verified;
- [ ] adult scale and silhouette read correctly beside Labrador, husky, timber
  wolf, bog hound, and greatwolf at normal gameplay zoom;
- [ ] directional sprites remain coherent under rotation and east/west mirroring;
- [ ] outline, value range, and desiccated state pass weather, darkness, selection,
  and corpse review in-game;
- [ ] human maintainer accepts the final visual set.
