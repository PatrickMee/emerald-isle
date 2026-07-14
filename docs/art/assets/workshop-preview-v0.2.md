# Version 0.2 Steam Workshop Preview Asset Record

**Status:** Accepted and published. Patrick Mee accepted the preview, uploaded it
to the Workshop listing, and confirmed the public page on 2026-07-14.<br>
**Release:** v0.2.0 - The Hearth and Household<br>
**Production date:** 2026-07-13<br>
**Human acceptance owner:** Patrick Mee

## Art Brief

The Version 0.2 preview preserves the established wide isometric holding,
dry-stone construction, thatched cottage, grounded material palette, and quiet
left-side title field. The revised household depicts the release's flax and linen
work beside oats, with a low permanent stone-lined hearth as the warm courtyard
focal point. The subtitle changes from `The First Holding` to
`The Hearth and Household`, with Version 0.2 identified separately.

The image must remain legible at Steam thumbnail size without relying on generic
green identity, decorative Celtic shorthand, copied RimWorld runtime art, or
fantasy spectacle.

## Provenance and License

OpenAI image generation created the revised original 16:9 farmstead illustration
under project art direction. Inputs were limited to Emerald Isle's project-owned
Version 0.1 preview and approved central-hearth, mature-flax, folded-linen, and
linen-tunic exports. No third-party images or copied game textures were used.

Codex deterministically fit the generated illustration to 1280x720, added the
exact title and release typography with locally installed fonts, applied a
restrained title-field treatment and border, and palette-optimized the PNG below
Steam Workshop's one-megabyte preview limit. The generated source and local
render helper are ignored production intermediates rather than runtime
dependencies or committed source art.

The preview is a creative asset governed by
[`CREATIVE_ASSETS_LICENSE.md`](../../../CREATIVE_ASSETS_LICENSE.md), not the MIT
source-code license.

## Runtime Export

| Asset | Package path | Dimensions | Size | SHA-256 |
|---|---|---:|---:|---|
| Steam Workshop preview | `About/Preview.png` | 1280x720 indexed PNG | 665,684 bytes | `6f5412f528dce5854b90b73b29baf5343108ed28976f3617aedb474ddcbbb71c` |

## Acceptance Targets

- The exact text reads `EMERALD ISLE`, `VERSION 0.2`, and
  `THE HEARTH AND HOUSEHOLD`, with no generated pseudo-text.
- Full-size and 400x225 thumbnail checks preserve title legibility and keep the
  flax plot, oat plot, linen worker, dry-stone walls, cottage, and hearth distinct.
- The hearth reads as a permanent stone-lined household fixture rather than an
  oversized bonfire or a decorative fantasy object.
- The staging and release-safety paths include the replacement at the existing
  `About/Preview.png` compatibility path and preserve Workshop ID `3763433723`.
- The public Workshop page must show the replacement before this record is marked
  published; candidate creation alone is not publication evidence.

## Review Disposition

Automated export inspection confirms the candidate dimensions, indexed PNG
format, file-size ceiling, and recorded SHA-256. Maintainer visual acceptance and
public Steam verification remain open.
