# Steam Workshop Listing

**Status:** Version 0.2 published and verified. Patrick Mee applied the
description, change note, and replacement preview in Steam and confirmed the
public Workshop page reflects all three on 2026-07-14.<br>
**Workshop item:** [Emerald Isle 3763433723](https://steamcommunity.com/sharedfiles/filedetails/?id=3763433723)<br>
**Current release:** `v0.2.0` - The Hearth and Household<br>
**Publication owner:** Patrick Mee

Steam listing text is managed separately from `About/About.xml`. The code blocks
below are the exact current inputs for the Workshop description and Version 0.2
change note. Update them with each public release before uploading, then confirm
the public Workshop page matches this record.

## Description

```text
Emerald Isle is a lore-friendly RimWorld expansion inspired by Irish history, archaeology, material culture, language, and mythology.

[h1]Version 0.2 - The Hearth and Household[/h1]

Version 0.2 expands the first holding with a flax-to-linen household textile path and a permanent central hearth. The mod remains vanilla-friendly, XML-only, and focused on practical choices rather than strict upgrades.

[h1]Current content[/h1]

[list]
[*][b]Oats[/b] - A medium-cycle grain crop with a hand-quern processing chain for milled oats, oat porridge, and oat flatbread.
[*][b]Dry-stone wall[/b] - A material-efficient linked stone wall with original artwork.
[*][b]Flax and linen[/b] - Ground-grown flax is harvested as raw flax and processed into linen at vanilla work locations. Linen is a general Fabric with a warm-weather niche and lower durability than cloth.
[*][b]Linen tunic[/b] - A linen-only everyday garment with original ground and worn artwork.
[*][b]Central hearth[/b] - A stone-stuffable, continuously fueled household hearth providing heat, light, gathering-spot behavior, campfire-grade cooking, and Emerald Isle oat-food bills.
[/list]

[h1]Compatibility[/h1]

[b]Requires RimWorld 1.6 Core.[/b] No DLC is required. Royalty, Ideology, Biotech, Anomaly, and Odyssey are supported but add no Version 0.2-specific behavior.

Existing Version 0.1 saves can add the new content without custom migration or serialized state. Back up important saves before changing any mod list.

[url=https://github.com/PatrickMee/emerald-isle/releases/tag/v0.2.0]Version 0.2 release notes and manual download[/url]
```

## Version 0.2 Change Note

```text
Version 0.2.0 - The Hearth and Household

Added:
- Ground-grown flax, harvested raw flax, and processing bills at the Crafting Spot and tailoring benches.
- Linen as a general Fabric with a warm-weather niche and lower durability than cloth.
- A linen-only everyday tunic with complete ground and worn artwork.
- A stone-stuffable central hearth with continuous wood fuel, heat, light, gathering-spot behavior, campfire-grade cooking, and Emerald Isle oat-food bills.

Improved:
- Refined mature and pre-harvest flax artwork for clearer normal-zoom readability.
- Updated Emerald Isle package metadata and documentation for the complete Version 0.2 content set.

Compatibility:
- Requires RimWorld 1.6 Core; no DLC or other mod is required.
- Existing Version 0.1 saves can add the new content without custom migration.

Full release notes:
https://github.com/PatrickMee/emerald-isle/releases/tag/v0.2.0
```

## Verification

After applying both fields in Steam, verify through the public Workshop page or
Steam published-file API that:

- the description contains `Version 0.2 - The Hearth and Household`;
- the description names flax, linen, the linen tunic, and central hearth;
- the Version 0.2 change note is visible;
- the preview reads `VERSION 0.2` and `THE HEARTH AND HOUSEHOLD` and depicts the
  flax, linen, oats, and central-hearth household scene;
- the item still resolves to Workshop ID `3763433723`.

The replacement `About/Preview.png` is recorded in the
[Version 0.2 preview asset record](../art/assets/workshop-preview-v0.2.md). It
remains a candidate until maintainer visual acceptance and the public Workshop
page both confirm the replacement.
