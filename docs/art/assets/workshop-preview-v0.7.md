# Version 0.7 Steam Workshop Preview Asset Record

**Status:** Maintainer accepted; publication pending<br>
**Release candidate:** v0.7.1 - Version 0.7 Workshop Preview<br>
**Production date:** 2026-08-23<br>
**Human acceptance owner:** Patrick Mee<br>
**Human acceptance date:** 2026-08-23

## Art Brief

The Version 0.7 preview preserves the established wide isometric holding, quiet
left-side title field, dry-stone enclosure, thatched cottage, crops, Kerry cattle,
and domestic wolfhound. The household focus moves to the warmly lit central
hearth: a colonist tends the fire, preserved meat rests on the worktable, and oats,
hops, and a plain wooden fermenting barrel suggest the alternate route into vanilla
wort and beer without depicting a new brewing system or drinking scene.

The rough-coated iron-grey wolfhound remains beside the colonist and outside the
cattle pen. The exact release typography reads `EMERALD ISLE`, `VERSION 0.7`, and
`HEARTH & LARDER`.

## Provenance and License

OpenAI's built-in image-generation tool produced an original edit using the
project-owned Version 0.5 preview as the scene, composition, and style reference.
The first pass established the Version 0.7 hearth-and-larder scene and exact text.
A second constrained pass changed only the dog to restore the approved rough-coated
wolfhound silhouette, again using the Version 0.5 preview as the identity reference.

No RimWorld screenshot, Core-art pixel, third-party image, or unsupported asset was
copied or composited into the preview. The generated source is a local production
intermediate and is not a runtime dependency or committed source-art file. The
preview is governed by
[`CREATIVE_ASSETS_LICENSE.md`](../../../CREATIVE_ASSETS_LICENSE.md).

## Runtime Export

Pillow 11.0.0 fitted the selected 1672x941 RGB source to 1280x720 with Lanczos
resampling, converted it to a 256-color indexed palette with median-cut
quantization and Floyd-Steinberg dithering, and wrote an optimized level-9 PNG.

| Asset | Package path | Dimensions | Size | SHA-256 |
|---|---|---:|---:|---|
| Steam Workshop preview and event banner | `About/Preview.png` | 1280x720 indexed PNG | 800,692 bytes | `863cd1310a894d2eff70a25a81b8081550789c02c2dffcf49d366dcb4946f7e1` |

## Acceptance Targets

- exact title text remains legible at full size and 400x225 thumbnail size;
- the central hearth is the scene's warm focal point without implying a separate
  smoker, brewing system, or drinking mechanic;
- preserved meat, oats, hops, and the fermenting barrel remain secondary household
  details rather than clutter;
- the rough-coated grey hound reads as the approved wolfhound and remains outside
  the livestock pen;
- the cottage, walls, cattle, fields, grounded palette, and isometric composition
  preserve continuity with the established holding;
- production staging preserves `About/Preview.png`, excludes production
  intermediates, stays below Steam's one-megabyte preview ceiling, and retains
  Workshop ID `3763433723`; and
- the public Workshop page must show the replacement before this record is marked
  published.

## Review Disposition

Patrick Mee approved the Version 0.7 image after reviewing the full-size candidate
on 2026-08-23. Automated inspection confirms the exact dimensions, indexed PNG
format, file-size ceiling, typography, thumbnail readability, and SHA-256. Public
Workshop publication and signed-out verification remain release-gate work.
