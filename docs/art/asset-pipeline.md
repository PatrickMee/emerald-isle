# Asset Pipeline Guide

The Art Guide defines direction; this document defines production control.

## Stages

1. Approved feature art brief and cultural references
2. Silhouette, scale, state, and grayscale/readability review
3. Editable source production with creator and license metadata
4. Export using documented dimensions, color/profile, alpha, compression, and naming
5. Automated path/reference checks
6. In-game review at normal zoom, weather, light, damage, rotation, selection, and adjacency
7. Release export from clean sources; archive source and provenance

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
