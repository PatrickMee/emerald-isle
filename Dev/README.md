# Emerald Isle Developer Testing Framework

This directory contains development-only testing assets for Emerald Isle.

Nothing under `Dev/` is copied by the production staging script. Public releases
must be built from `tools/stage-mod.sh`, which also runs release-safety checks
that fail if developer-only assets or identifiers enter the staged package.

Use `tools/stage-dev-mod.sh` to build the optional companion mod:

```sh
./tools/stage-dev-mod.sh
```

The companion mod is intended for local regression testing only. It must never be
uploaded, archived, or distributed as part of an Emerald Isle public release.
