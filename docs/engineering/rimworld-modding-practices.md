# RimWorld Modding Practices

**Status:** Pre-implementation baseline; verify against the installed supported
game version before Version 0.1.

RimWorld has no formal stable modding API; community documentation and current
game definitions/assemblies must be checked together. Never treat copied snippets
or decompiled symbols from another version as contracts.

## Package and Data

- A distributable mod requires a case-sensitive `About/About.xml`; create it only
  after package ID, support versions, dependencies, and licenses are decided.
- Use recognized `Defs`, `Patches`, `Languages`, `Textures`, `Sounds`, and
  `Assemblies` folders as needed; do not create empty folders for appearance.
- Prefer vanilla-style Def folder organization even though Def file paths are not
  runtime identifiers.
- Treat `defName`, package ID, translation keys, C# type names in saves, and
  serialization fields as stable compatibility contracts.
- Use version/DLC load folders only after the support matrix requires them; always
  include intended common/root content explicitly.

References: [Mod folder structure](https://rimworldwiki.com/wiki/Modding_Tutorials/Mod_Folder_Structure),
[About.xml](https://rimworldwiki.com/wiki/Modding_Tutorials/About.xml), and
[XML Defs](https://rimworldwiki.com/wiki/Modding_Tutorials/XML_Defs).

## XML and Patches

- Define original content through Defs and supported composition first.
- Patch external content with narrow, defensive PatchOperations.
- Do not overwrite whole vanilla/mod Defs or abstract bases to change a field.
- Scope conditional patches to explicit package IDs and verify target absence.
- Investigate the first XML/config error first because parser failures cascade.

References: [PatchOperations](https://rimworldwiki.com/wiki/Modding_Tutorials/PatchOperations)
and [compatibility guidance](https://rimworldwiki.com/wiki/Modding_Tutorials/Compatibility).

## C# and Harmony

- Prefer existing Defs, comps, mod extensions, and supported components before
  subclassing or patching runtime methods.
- Separate pure logic from Verse/RimWorld state and expect nullable/destroyed state.
- Save state uses explicit `ExposeData` lifecycles and migration-safe defaults.
- Harmony is a last-resort interoperability tool, not a default architecture.
  Prefer postfixes or narrow guarded patches; destructive prefixes require
  exceptional justification and compatibility evidence.
- Verify every target signature against the exact supported game assembly.

## Verification

Use RimWorld development mode and config errors during development. Test clean
startup, definitions, player path, save/load, removal or upgrade as supported,
optional DLC/mod absence, load-order interactions, and a sanitized Player.log.
Claims of compatibility only cover the published test matrix.
