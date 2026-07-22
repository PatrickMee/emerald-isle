# Release Strategy

## Channels

- **Development**: unversioned local builds, never presented as supported.
- **Preview**: explicitly opt-in builds for focused feedback; save risk stated.
- **Stable**: passed the release checklist and all applicable compatibility checks.

## Release Gate

A release PR freezes a coherent set of Done features, identifies the exact commit
and artifact digest, and obtains approval to publish. Prefer batching related
features so the player update and publication effort are coherent. A one-feature
release is valid when feedback, urgency, or product coherence justifies it; state
the reason in the release PR.

The candidate requires a clean package build, relevant static and automated
checks, clean in-game load, affected-path smoke tests, resolved blocker/critical
defects, localization and attribution checks, changelog, known issues,
installation/upgrade notes, and rollback preparation. Save/load, DLC/mod matrices,
performance, and cultural review are required only when the included changes or
supported configurations trigger them.

Test the exact archive to be published. Verify package ID, metadata, supported
versions, dependencies, load order, file casing, absence of source/editor files,
and behavior when optional integrations are missing.

Use `templates/release-checklist.md` in the release PR. An annotated, immutable Git
tag may be created only after that PR approves the exact reviewed commit and
artifact.

After merge, publish the same artifact through GitHub and the supported
distribution channel. Record download and smoke verification in the GitHub release
body or a comment on the merged release PR. Do not create a second bookkeeping PR
unless publication exposed a wrong durable fact or differed from the approved
candidate.

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
