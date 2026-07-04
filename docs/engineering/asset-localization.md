# Asset Organization and Localization

## Asset Organization

Game-ready paths mirror gameplay domains so code, defs, and assets can be traced
from a feature record. Use stable names and case consistently across platforms.
Keep source art/audio in a documented source tree or external art repository;
exports belong in RimWorld package paths. Build outputs and editor backups are
ignored. Every third-party asset records creator, source, license, modifications,
and required attribution.

Large binary sources should use Git LFS only after an ADR confirms hosting,
contributor, and release implications.

## Localization

- English is the source language, not a hard-coded runtime fallback strategy.
- Player-facing text uses stable keyed or def-injected translations.
- Keys use `EI_<Domain>_<Concept>_<Purpose>` and survive copy edits.
- Avoid concatenated fragments; translators need complete sentences and context.
- Placeholders are named where supported and documented with examples.
- Gender, pluralization, grammar, width, capitalization, and rich-text behavior
  are tested in context.
- Irish words include meaning, grammatical form, pronunciation guidance where
  useful, and reviewer status in the terminology record.
- Pseudo-localization and missing-key checks are release gates once runtime
  content exists.

The initial supported languages and Irish-language policy must be decided before
Version 0.1 content freeze.
