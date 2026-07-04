# Localization Guide

## Source Text

English source text must be concise, player-centered, and understandable without
research context. Keep player-critical nouns and actions consistent with the
Glossary. Avoid concatenated fragments, embedded layout spacing, unexplained idiom,
and text baked into textures.

## Keys and Context

Use stable `EI_<Domain>_<Concept>_<Purpose>` keys. Renaming source English does not
rename keys. Translator context states screen/location, speaker, placeholders,
grammar, length constraints, rich text, and relevant screenshot.

Def-injected and keyed translations follow the exact folder convention verified
for the supported RimWorld version. Validate missing, duplicate, and orphaned keys.

## Irish Language

Irish is meaningful content, not ornament. Record standard/dialect choice,
translation, grammatical form, mutation/plural behavior, pronunciation where
useful, source, and competent reviewer. Machine output is a draft only. Critical
controls remain comprehensible to players who do not know Irish.

## QA and Contribution

Pseudo-localize for expansion, truncation, missing glyphs, placeholder ordering,
and hard-coded text. Test representative long strings in-game. Translation PRs
identify language, reviewer competence, changed keys, screenshots where layout is
affected, and machine assistance. Never overwrite another translator's locale
wholesale to change a few entries.
