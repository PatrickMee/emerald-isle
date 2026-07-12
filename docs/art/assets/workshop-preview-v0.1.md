# Version 0.1 Steam Workshop Preview Asset Record

**Status:** Published with Steam Workshop item 3763433723<br>
**Release:** v0.1.0 — The First Holding<br>
**Production date:** 2026-07-12<br>
**Human acceptance owner:** Patrick Mee

## Provenance and License

OpenAI image generation created an original 16:9 farmstead illustration under
project art direction. The generation used only Emerald Isle's project-owned oat,
dry-stone wall, hand-quern, porridge, and flatbread exports as visual identity
references. It did not use third-party images or copy RimWorld runtime art.

Codex deterministically cropped the illustration to 1280×720, added the exact
release title typography, applied a restrained title-field gradient and border,
and palette-optimized the PNG to meet Steam Workshop's one-megabyte preview limit.

The preview is a creative asset governed by
[`CREATIVE_ASSETS_LICENSE.md`](../../../CREATIVE_ASSETS_LICENSE.md), not the MIT
source-code license.

## Runtime Export

| Asset | Package path | Dimensions | SHA-256 |
|---|---|---:|---|
| Steam Workshop preview | `About/Preview.png` | 1280×720 PNG | `a944e2ebb7c47c96ee8737f4da3ead348193029dea817abd6ee85b032945207a` |

## Publication Contract

- The staging script includes the preview as ordinary `About/` metadata.
- Release-safety validation still excludes every developer-only path and marker.
- Steam created `About/PublishedFileId.txt` with item ID `3763433723` during the
  first successful upload on 2026-07-12. The tracked ID must be preserved for all
  future updates.
- The existing GitHub v0.1.0 archive remains immutable. The Workshop package adds
  only this listing preview and does not change gameplay or public identifiers.
