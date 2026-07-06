# FS-002 Dry-Stone Wall Asset Record

**Status:** Release-candidate revision 4 approved by Patrick Mee, 2026-07-06<br>
**Feature:** [FS-002 — Dry-Stone Wall](../../specifications/FS-002-dry-stone-wall.md)<br>
**Production date:** 2026-07-06<br>
**Human acceptance owner:** Patrick Mee

## Provenance and License

The visual source was generated with OpenAI image generation under project art
direction, without third-party art. Art-review revision 2 edited the original
generated source to adopt the construction language of west-of-Ireland dry-stone
work—particularly flatter layering, irregular stone sizes, and larger capstones—
without reproducing a particular wall or changing the approved early medieval,
cashel-inspired identity. Final-polish revision 3 breaks up middle-course banding,
adds selected longer stones, varies capstone scale and joints, and modestly deepens
selected joint shadows. Release-candidate revision 4 makes only minor changes to
stone-length distribution, the scale of roughly 10–15% of stones, capstone widths,
and local joint contrast. Codex removed a flat magenta
chroma key and deterministically derived the 16 required linked states from the
original four-way dry-stone junction. Generated source images and the temporary
atlas-build script are ignored local production intermediates, not runtime
dependencies or committed source art.

The RimWorld Wiki linked-wall diagram was consulted only to verify the engine's
documented 4×4 cell ordering. No pixels, code, or artistic content from the diagram,
RimWorld, another mod, or a historical photograph were copied.

The runtime exports are creative assets governed by
[`CREATIVE_ASSETS_LICENSE.md`](../../../CREATIVE_ASSETS_LICENSE.md), not the MIT
source-code license.

## Runtime Exports

| Asset | Runtime path | Dimensions | SHA-256 |
|---|---|---:|---|
| Linked wall atlas | `Things/Building/Linked/DryStoneWall/EI_DryStoneWall_Atlas` | 256×256 RGBA | `c2ffa099c49ea240b728e2f29d45511de5f52d6917d6cf1b324a4534f052aa40` |
| Structure menu icon | `Things/Building/Linked/DryStoneWall/EI_DryStoneWall_MenuIcon` | 64×64 RGBA | `7b812e391cb9eee669ec123c5af115039a2854e008e88f9b98f95545ca03af17` |

## Verified Linked-Atlas Contract

RimWorld's `CornerFiller` wall atlas is a 4×4 sheet of 64×64 cells containing all
16 cardinal-link combinations. The verified row-major ordering is:

1. left+down; up+left+down; left+right+down; all four;
2. left; up+left; left+right; up+left+right;
3. down; up+down; right+down; up+right+down;
4. isolated; up; right; up+right.

This matches AR-002; no architecture amendment is required.

## Production Controls

- Built-in OpenAI image generation created an original orthographic four-way
  junction of irregular mortarless stone on a flat magenta background.
- The revision prompt preserved exact cardinal geometry while requiring varied
  stone sizes, flatter horizontal layers, irregular courses, larger capstones,
  neutral grayscale, dark readable joints, no scenery, no text, and no copied
  game, monument, or photographic art.
- The final-polish prompt targeted only middle-course rhythm, selected long stones,
  capstone-size variation, hand-laid joints, and understated joint depth while
  preserving every runtime and silhouette invariant.
- The release-candidate prompt explicitly constrained the edit to a minority of
  stones. Final post-processing also corrected the generated cut-edge outline to
  strict grayscale so no hidden hue bias affects Stuff tinting.
- The standard image-generation chroma helper converted the background to alpha.
- Deterministic post-processing converted the source to strict grayscale,
  normalized the two arm widths, created every exact
  cardinal-link state, added dark cut-edge silhouettes, and composed the 4×4 atlas.
- The horizontal link state supplies the dedicated menu icon.
- Exact filename case, dimensions, alpha, and runtime paths match AR-002.

## Review Disposition

Patrick Mee approved release-candidate revision 4 on 2026-07-06. The linked atlas,
normal-zoom readability, construction language, and overall style pass human art
review. Broader feature verification must still cover Stuff tint for all five Core
stones, wall/rock/door/fence adjacency, damage overlays, selection, paint, snow,
rain, and darkness. Broken tiling remains an art defect and must not change FS-002
gameplay.
