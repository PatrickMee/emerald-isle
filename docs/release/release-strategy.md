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

Every release must use this artifact path:

1. Merge all included Done feature PRs into `main`; never release from an open
   feature branch.
2. On the release-record branch, run
   `python3 tools/build-release.py vX.Y.Z --candidate` and record its SHA-256 in
   the release PR.
3. After approval and merge, create the annotated tag on the reviewed commit,
   update local `main` from `origin/main`, and run
   `python3 tools/build-release.py vX.Y.Z`.
4. Refuse publication unless the final tagged-main ZIP has the approved candidate
   SHA-256. Publish that exact ZIP and checksum to the GitHub release.
5. Run `python3 tools/stage-workshop-release.py vX.Y.Z`. This downloads the
   GitHub asset and stages that content into RimWorld's local Mods folder; do not
   rebuild or copy loose feature-branch files for Steam.
6. Upload the staged local package to existing Workshop item `3763433723`.
7. On a separate subscribed client, run
   `python3 tools/verify-workshop-release.py vX.Y.Z`. This compares Steam's public
   package size and every subscribed file against the GitHub release artifact.

The release scripts print the next maintainer action so the human Steam upload
and independent subscriber check cannot be mistaken for automated steps. A game
reload does not prove that Steam downloaded a new Workshop manifest. If the
subscriber check fails after Steam publishes the expected size, exit RimWorld
and Steam, restart Steam, then unsubscribe/resubscribe before checking again.

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
