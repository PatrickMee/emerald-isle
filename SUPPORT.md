# Support and Bug Reports

Install one copy of Emerald Isle from the
[Steam Workshop](https://steamcommunity.com/sharedfiles/filedetails/?id=3763433723)
or an immutable package from [GitHub releases](https://github.com/PatrickMee/emerald-isle/releases).
For a manual install, extract the package's `EmeraldIsle` folder into RimWorld's
`Mods` directory. Enable one Emerald Isle copy in the mod list; do not enable a
Workshop copy and a manual copy together.

Before upgrading an existing colony, back up its save and keep the exact mod
package it currently uses. For a manual upgrade, replace the old `EmeraldIsle`
folder completely rather than merging files. Load the colony with the new
package, check its content and bills, then save under a new name. If you need to
roll back, restore both the previous package and the save made before the
upgrade. A save written with a newer package may contain content the older
package cannot load correctly.

Removing Emerald Isle from a colony that uses its buildings, items, plants,
animals, or bills is not guaranteed to be safe. Keep a save backup before
removal; if the colony fails to load or loses content, restore the mod package
and that backup.

Support is best-effort for RimWorld 1.6 Core and the supported DLC listed in
[the platform policy](docs/engineering/supported-platforms.md). Third-party
mod combinations are not certified. Before reporting a bug, reproduce with the
exact packaged build, check its release notes and known issues, and reduce the
active mod list where safe. Use the repository issue template and include the
RimWorld version, Emerald Isle release or local build identifier, operating
system, DLC and mod list/order, whether the save is new or existing, steps to
reproduce, expected and actual behavior, and relevant `Player.log` excerpts.
Remove personal paths and secrets from logs before posting.

Feature ideas begin with design and milestone fit, not implementation requests.
Use the feature proposal template and expect ideas outside the active milestone to
remain deferred.
