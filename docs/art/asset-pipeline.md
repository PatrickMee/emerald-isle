# Asset Pipeline Guide

The Art Guide defines direction; this document defines production control.

## Stages

1. Approved feature art brief and cultural references
2. Installed-build vanilla comparison and silhouette, scale, state, and grayscale review
3. One representative runtime prototype approved at normal zoom and 64×64 preview
4. Editable source production with creator and license metadata
5. Export using documented dimensions, color/profile, alpha, compression, and naming
6. Automated path/reference checks
7. In-game review at normal zoom, weather, light, damage, rotation, selection, and adjacency
8. Release export from clean sources; archive source and provenance

For pawn and animal sets, do not generate every direction or state before the
representative prototype passes. The comparison review must place the prototype
beside at least two relevant vanilla pawns and check projection, anatomical
occlusion, outline weight, texture density, and map-scale silhouette.

Texture framing and runtime scale are separate controls. Validate both the
exported opaque bounds and the consuming definition's draw size; source padding
does not make a subject smaller when the export process fits opaque pixels to the
runtime canvas.

## Source and Export Separation

Editable layered files are not game-ready assets. Store sources under a deliberate
source-art policy or repository only after Git LFS/hosting ADR. Game exports mirror
feature domains and never include editor backups. Do not hand-edit generated exports.

## Acceptance Record

Record asset ID, feature, owner, source path, export path, dimensions/states,
references, license/provenance, export tool/settings, in-game screenshots, reviewer,
and visual acceptance. The asset record owns provenance, export, and visual-review
facts; it does not own feature Done or Released state. Do not update it solely
because a lifecycle gate changed. Replacement assets retain compatibility paths
unless migration is approved.

AI-generated and third-party material follows the Design Bible's provenance and
human-direction requirements. Unclear rights block inclusion.
