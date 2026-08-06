# AN-01 Wolfhound Asset Record

**Status:** Runtime exports complete; human in-game visual acceptance pending

**Feature record:** Direct maintainer request restated in the implementation PR

**Production date:** 2026-08-06

**Human acceptance owner:** Patrick Mee

## Provenance and License

The source images were generated with OpenAI's built-in image-generation tool
under project art direction. The approved east-facing prototype was used only as
a design, palette, projection, and identity reference for the other directions.
The living directional images and the desiccated east image then anchored the
remaining desiccated directions. No Core, DLC, Kerry-cattle, or third-party art
pixels were copied or composited into the exports.

The generated sources are local production intermediates and are not runtime
dependencies or committed source-art files. Codex removed a flat magenta chroma
key with the installed ImageGen helper, used a one-pixel matte contraction and
despill, cropped the resulting alpha bounds, fit each subject within a 216x216
area using Lanczos resampling, and centered it on a transparent 256x256 canvas.
The exports are creative assets governed by
[`CREATIVE_ASSETS_LICENSE.md`](../../../CREATIVE_ASSETS_LICENSE.md).

The subject uses descriptive traits associated with a large rough-coated
coursing hound: an elongated body, narrow muzzle, folded ears, deep chest, long
tail, and restrained gray-tawny coat. Those traits provide development
provenance only; the player-facing animal is original RimWorld fiction and does
not claim to reproduce a historical or modern pedigree breed.

## Runtime Exports

| Asset | Runtime path | Dimensions | SHA-256 |
|---|---|---:|---|
| Wolfhound east | `Things/Pawn/Animal/Wolfhound/EI_Wolfhound_east` | 256x256 RGBA | `a4c229c83f53f549afed8dbf45b0fece82413de1296c68c295b46536721a2114` |
| Wolfhound north | `Things/Pawn/Animal/Wolfhound/EI_Wolfhound_north` | 256x256 RGBA | `0e70635192d9fe7289ae0ceee1142ecbcb6b48c3ccb3dda4633f02b88e658a69` |
| Wolfhound south | `Things/Pawn/Animal/Wolfhound/EI_Wolfhound_south` | 256x256 RGBA | `6a236102726548e50bb78c142d370ef4ef0112005263582b0e7b63f2aaf91f03` |
| Desiccated wolfhound east | `Things/Pawn/Animal/Wolfhound/EI_WolfhoundDessicated_east` | 256x256 RGBA | `03a36dec5fb9182b60e1d32c27cfd20192f1a8ab25a78fb9c990c3656d9c4ed8` |
| Desiccated wolfhound north | `Things/Pawn/Animal/Wolfhound/EI_WolfhoundDessicated_north` | 256x256 RGBA | `b08d5e8ba5b9a2585c4162e9633c39e44c7c061b7348e07720becbeec615e667` |
| Desiccated wolfhound south | `Things/Pawn/Animal/Wolfhound/EI_WolfhoundDessicated_south` | 256x256 RGBA | `a10c310bb59b4319f488c415f605f930c7de48ecd9114f432b52ea27bcff2267` |

West-facing sprites use RimWorld's normal mirroring of the east exports. Puppy,
juvenile, and adult stages reuse the same directional set at definition-controlled
draw sizes, matching the installed Core canine pattern.

## Production Controls

The first east-facing prototype had clean alpha and remained readable at 64x64,
but its rounded coat mass read as a compact terrier rather than a coursing hound.
A single targeted revision lengthened and narrowed the torso, reduced coat bulk,
and emphasized the muzzle while preserving the compact top-down animal-token
projection.

All living prompts required a torso-dominant bean or lozenge silhouette, bold
near-black contour, three to four broad matte coat tones, sparse rough-coat tufts,
heavily foreshortened or occluded legs, and no standing side elevation,
photorealistic anatomy, armor, collar, ornament, scenery, shadow, or text.
Directional prompts preserved the accepted east identity while changing only
the facing and necessary perspective.

The desiccated prompts kept the same compact silhouette and used broad skull,
rib, spine, pelvis, and folded-limb cues. They prohibited blood, flesh, gore,
organs, horror presentation, humanlike anatomy, and copied game art. Downsampling
subordinates the source detail to a normal map-scale carcass read.

## Review Checklist

- [x] east prototype is readable at 64x64 and uses compact top-down token anatomy;
- [x] all required directional, life-stage, and desiccated runtime paths resolve;
- [x] transparent corners, alpha channel, dimensions, and hashes are verified;
- [ ] adult scale and silhouette read correctly beside Labrador, husky, timber
  wolf, bog hound, and greatwolf at normal gameplay zoom;
- [ ] directional sprites remain coherent under rotation and east/west mirroring;
- [ ] outline, value range, and desiccated state pass weather, darkness, selection,
  and corpse review in-game;
- [ ] human maintainer accepts the final visual set.
