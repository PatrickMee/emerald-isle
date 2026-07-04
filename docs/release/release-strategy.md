# Release Strategy

## Channels

- **Development**: unversioned local builds, never presented as supported.
- **Preview**: explicitly opt-in builds for focused feedback; save risk stated.
- **Stable**: passed release checklist and supported compatibility matrix.

## Release Gate

A release requires frozen scope, approved specs, clean package build, static and
automated checks, clean in-game load, targeted save/load and compatibility tests,
resolved blocker/critical defects, localization and attribution checks, changelog,
known issues, installation/upgrade notes, and rollback artifacts.

Test the exact archive to be published. Verify package ID, metadata, supported
versions, dependencies, load order, file casing, absence of source/editor files,
and behavior when optional integrations are missing.

Use `templates/release-checklist.md` for the signed release record. An annotated,
immutable Git tag may be created only after the checklist identifies the exact
reviewed commit and artifact.

## Versioning

Project releases use `MAJOR.MINOR.PATCH`. Before 1.0, MINOR may add or alter
features and PATCH is backward-compatible fixes or content tuning. After 1.0,
MAJOR signals intentional compatibility breaks, MINOR adds backward-compatible
features, and PATCH fixes behavior. Preview suffixes use `-alpha.N`, `-beta.N`,
or `-rc.N`.

Save-breaking changes require explicit migration analysis, prominent notice, and
major-version treatment after 1.0. RimWorld package metadata follows platform
requirements and does not replace project semantic versions.

## Support

Publish known issues and a reproducible bug-report format. Keep the prior stable
artifact available for rollback. Hotfixes branch from the affected stable tag and
receive focused regression plus packaging verification.
