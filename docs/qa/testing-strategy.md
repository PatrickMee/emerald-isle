# Testing Strategy

Quality evidence is layered. No single layer proves the mod works.

## Layers

1. **Static validation**: XML parsing, schemas where practical, duplicate names,
   missing references, localization keys, texture paths, packaging, analyzers.
2. **Unit tests**: pure C# calculations, selection rules, transformations, and
   regression cases.
3. **Integration tests**: definition loading, serialization boundaries, DLC and
   mod-presence adapters, and Harmony target discovery.
4. **In-game smoke tests**: clean load, new colony, spawn/acquire/use/destroy path,
   save/load, removal behavior, and log review.
5. **Playtests**: player comprehension, decision quality, balance, pacing,
   exploits, and story outcomes.
6. **Compatibility matrix**: supported game versions, DLC combinations, and a
   small risk-based set of major mods.

## Regression Rule

A regression test must fail against the defective behavior and pass after the
fix. Visual changes require in-game evidence at representative zoom and states.

## Evidence

Test reports record build, game version, DLC/mod list, save origin, scenario,
steps, expected and actual results, logs, screenshots, severity, and disposition.
Release candidates must be tested from a clean package, not a developer tree.
