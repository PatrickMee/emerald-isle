#!/usr/bin/env python3
"""Render the reproducible Ringfort discovery layout proof as self-contained SVG."""

from __future__ import annotations

import argparse
import base64
import math
from collections import deque
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[3]
ATLAS_PATH = (
    REPO_ROOT
    / "Textures/Things/Building/Linked/DryStoneWall/EI_DryStoneWall_Atlas.png"
)
GATE_PATH = SCRIPT_DIR / "ringfort-gate-concept-source.png"
DEFAULT_OUTPUT = SCRIPT_DIR / "ringfort-layout-proof.svg"

UP = 1
RIGHT = 2
DOWN = 4
LEFT = 8

ATLAS_CELL = {
    LEFT | DOWN: (0, 0),
    UP | LEFT | DOWN: (0, 1),
    LEFT | RIGHT | DOWN: (0, 2),
    UP | RIGHT | DOWN | LEFT: (0, 3),
    LEFT: (1, 0),
    UP | LEFT: (1, 1),
    LEFT | RIGHT: (1, 2),
    UP | LEFT | RIGHT: (1, 3),
    DOWN: (2, 0),
    UP | DOWN: (2, 1),
    RIGHT | DOWN: (2, 2),
    UP | RIGHT | DOWN: (2, 3),
    0: (3, 0),
    UP: (3, 1),
    RIGHT: (3, 2),
    UP | RIGHT: (3, 3),
}


def image_uri(path: Path) -> str:
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:image/png;base64,{encoded}"


def regular_outline(rx: int, ry: int) -> set[tuple[int, int]]:
    xs = list(range(-rx, rx + 1))
    tops = []
    bottoms = []
    for x in xs:
        y = round(ry * math.sqrt(max(0.0, 1.0 - (x / rx) ** 2)))
        tops.append(-y)
        bottoms.append(y)
    return connected_outline(xs, tops, bottoms)


def irregular_outline() -> set[tuple[int, int]]:
    """A mild asymmetric oval, not a reconstruction of a particular monument."""

    xs = list(range(-17, 18))
    tops = []
    bottoms = []
    for x in xs:
        upper_x = (x + 1) / 16
        lower_x = (x - 1) / 16
        upper = (
            -round(11 * math.sqrt(max(0.0, 1.0 - upper_x * upper_x)))
            if abs(upper_x) <= 1
            else 0
        )
        lower = (
            round(12 * math.sqrt(max(0.0, 1.0 - lower_x * lower_x)))
            if abs(lower_x) <= 1
            else 0
        )
        tops.append(upper)
        bottoms.append(lower)
    return connected_outline(xs, tops, bottoms)


def connected_outline(
    xs: list[int], tops: list[int], bottoms: list[int]
) -> set[tuple[int, int]]:
    cells: set[tuple[int, int]] = set()
    for index, x in enumerate(xs):
        if index == 0:
            for y in range(tops[index], bottoms[index] + 1):
                cells.add((x, y))
            continue
        for y in range(
            min(tops[index - 1], tops[index]),
            max(tops[index - 1], tops[index]) + 1,
        ):
            cells.add((x, y))
        for y in range(
            min(bottoms[index - 1], bottoms[index]),
            max(bottoms[index - 1], bottoms[index]) + 1,
        ):
            cells.add((x, y))
    return cells


def interior_cell_count(boundary: set[tuple[int, int]]) -> int:
    """Count enclosed grid cells by flooding the space outside the boundary."""

    xs = [x for x, _ in boundary]
    ys = [y for _, y in boundary]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    outside: set[tuple[int, int]] = set()
    queue = deque([(min_x - 1, min_y - 1)])

    while queue:
        x, y = queue.popleft()
        cell = (x, y)
        if (
            cell in outside
            or cell in boundary
            or not (min_x - 1 <= x <= max_x + 1)
            or not (min_y - 1 <= y <= max_y + 1)
        ):
            continue
        outside.add(cell)
        queue.extend(((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)))

    return sum(
        (x, y) not in boundary and (x, y) not in outside
        for x in range(min_x, max_x + 1)
        for y in range(min_y, max_y + 1)
    )


def mask_for(cell: tuple[int, int], cells: set[tuple[int, int]]) -> int:
    x, y = cell
    mask = 0
    if (x, y - 1) in cells:
        mask |= UP
    if (x + 1, y) in cells:
        mask |= RIGHT
    if (x, y + 1) in cells:
        mask |= DOWN
    if (x - 1, y) in cells:
        mask |= LEFT
    return mask


def atlas_tile(
    atlas_uri: str,
    x: float,
    y: float,
    size: float,
    mask: int,
) -> str:
    row, column = ATLAS_CELL[mask]
    return (
        f'<svg x="{x:.1f}" y="{y:.1f}" width="{size:.1f}" height="{size:.1f}" '
        f'viewBox="{column * 64} {row * 64} 64 64" overflow="hidden">'
        f'<image href="{atlas_uri}" x="0" y="0" width="256" height="256"/>'
        "</svg>"
    )


def px(origin: tuple[float, float], tile: float, x: float, y: float) -> tuple[float, float]:
    return origin[0] + (x + 17) * tile, origin[1] + (y + 11) * tile


def rect_for_cells(
    origin: tuple[float, float],
    tile: float,
    x: int,
    y: int,
    width: int,
    height: int,
    fill: str,
    stroke: str,
    label: str,
) -> str:
    left, top = px(origin, tile, x, y)
    cx = left + width * tile / 2
    cy = top + height * tile / 2
    return (
        f'<rect x="{left:.1f}" y="{top:.1f}" width="{width * tile:.1f}" '
        f'height="{height * tile:.1f}" rx="6" fill="{fill}" stroke="{stroke}" stroke-width="3"/>'
        f'<text x="{cx:.1f}" y="{cy:.1f}" class="map-label" text-anchor="middle" '
        f'dominant-baseline="middle">{label}</text>'
    )


def mini_shape(
    cells: set[tuple[int, int]],
    x: float,
    y: float,
    tile: float,
    label: str,
    note: str,
) -> str:
    min_x = min(cx for cx, _ in cells)
    min_y = min(cy for _, cy in cells)
    elements = [
        f'<text x="{x:.1f}" y="{y - 10:.1f}" class="mini-title">{label}</text>'
    ]
    for cx, cy in sorted(cells, key=lambda item: (item[1], item[0])):
        elements.append(
            f'<rect x="{x + (cx - min_x) * tile:.1f}" y="{y + (cy - min_y) * tile:.1f}" '
            f'width="{tile:.1f}" height="{tile:.1f}" fill="#847c72" stroke="#312d29" stroke-width="0.6"/>'
        )
    max_y = max(cy for _, cy in cells)
    elements.append(
        f'<text x="{x:.1f}" y="{y + (max_y - min_y + 1) * tile + 18:.1f}" class="mini-note">{note}</text>'
    )
    return "".join(elements)


def render() -> str:
    atlas_uri = image_uri(ATLAS_PATH)
    gate_uri = image_uri(GATE_PATH)
    origin = (64.0, 246.0)
    tile = 42.0

    complete_ring = irregular_outline()
    gate_cells = {(-1, 12), (0, 12)}
    wall_cells = complete_ring - gate_cells

    elements: list[str] = []
    elements.append(
        """<svg xmlns="http://www.w3.org/2000/svg" width="2048" height="1400" viewBox="0 0 2048 1400">
<defs>
  <pattern id="ground" width="28" height="28" patternUnits="userSpaceOnUse">
    <rect width="28" height="28" fill="#554c3f"/>
    <circle cx="6" cy="9" r="1.4" fill="#746958" opacity="0.50"/>
    <circle cx="21" cy="19" r="1.1" fill="#3c372f" opacity="0.60"/>
  </pattern>
  <pattern id="grid" width="42" height="42" patternUnits="userSpaceOnUse">
    <path d="M 42 0 L 0 0 0 42" fill="none" stroke="#d8c9aa" stroke-width="1" opacity="0.13"/>
  </pattern>
  <style>
    .title { font: 700 44px -apple-system, BlinkMacSystemFont, sans-serif; fill: #f1eadb; }
    .subtitle { font: 400 22px -apple-system, BlinkMacSystemFont, sans-serif; fill: #cfc5b2; }
    .map-label { font: 700 18px -apple-system, BlinkMacSystemFont, sans-serif; fill: #f5eddd; paint-order: stroke; stroke: #28231d; stroke-width: 4px; }
    .panel-title { font: 700 25px -apple-system, BlinkMacSystemFont, sans-serif; fill: #eee6d7; }
    .panel-body { font: 400 18px -apple-system, BlinkMacSystemFont, sans-serif; fill: #cfc5b2; }
    .panel-strong { font: 700 18px -apple-system, BlinkMacSystemFont, sans-serif; fill: #f0d39a; }
    .mini-title { font: 700 17px -apple-system, BlinkMacSystemFont, sans-serif; fill: #eee6d7; }
    .mini-note { font: 400 14px -apple-system, BlinkMacSystemFont, sans-serif; fill: #bfb5a2; }
  </style>
</defs>
<rect width="2048" height="1400" fill="#211f1b"/>
<text x="64" y="64" class="title">Ringfort Discovery — minimum modular proof</text>
<text x="64" y="104" class="subtitle">Grid-accurate rough layout at normal gameplay scale · existing dry-stone wall + one two-cell timber gate</text>
<rect x="48" y="156" width="1508" height="1082" rx="18" fill="url(#ground)" stroke="#8a806f" stroke-width="3"/>
<rect x="64" y="246" width="1470" height="1008" fill="url(#grid)"/>
"""
    )

    # Interior layout comes first so the wall remains visually dominant.
    path_left, path_top = px(origin, tile, -1, -1)
    elements.append(
        f'<rect x="{path_left:.1f}" y="{path_top:.1f}" width="{2 * tile:.1f}" height="{14 * tile:.1f}" fill="#8f7b5e" opacity="0.75"/>'
    )
    elements.append(
        rect_for_cells(origin, tile, -11, -6, 7, 5, "#66503f", "#b08b66", "cottage")
    )
    elements.append(
        rect_for_cells(origin, tile, 3, -7, 7, 4, "#66503f", "#b08b66", "larder / workshop")
    )
    elements.append(
        rect_for_cells(origin, tile, -1, -1, 2, 1, "#7a3e29", "#d99b63", "hearth")
    )

    crop_left, crop_top = px(origin, tile, -12, 3)
    elements.append(
        f'<rect x="{crop_left:.1f}" y="{crop_top:.1f}" width="{8 * tile:.1f}" height="{6 * tile:.1f}" rx="5" fill="#596442" stroke="#a9a66a" stroke-width="3"/>'
    )
    for line in range(1, 6):
        y = crop_top + line * tile
        elements.append(
            f'<path d="M {crop_left + 8:.1f} {y:.1f} H {crop_left + 8 * tile - 8:.1f}" stroke="#98a86c" stroke-width="3" opacity="0.7"/>'
        )
    elements.append(
        f'<text x="{crop_left + 4 * tile:.1f}" y="{crop_top + 3 * tile:.1f}" class="map-label" text-anchor="middle">crop yard</text>'
    )

    pen_left, pen_top = px(origin, tile, 5, 2)
    elements.append(
        f'<rect x="{pen_left:.1f}" y="{pen_top:.1f}" width="{9 * tile:.1f}" height="{7 * tile:.1f}" rx="5" fill="#4e5d3e" fill-opacity="0.72" stroke="#b39261" stroke-width="5" stroke-dasharray="18 8"/>'
    )
    for ox, oy in ((2.2, 2.1), (5.8, 4.6), (4.0, 2.9)):
        elements.append(
            f'<ellipse cx="{pen_left + ox * tile:.1f}" cy="{pen_top + oy * tile:.1f}" rx="{0.42 * tile:.1f}" ry="{0.28 * tile:.1f}" fill="#302d2a" stroke="#a28d70" stroke-width="2"/>'
        )
    elements.append(
        f'<text x="{pen_left + 4.5 * tile:.1f}" y="{pen_top + 1.1 * tile:.1f}" class="map-label" text-anchor="middle">inner pen</text>'
    )

    # Exact linked-wall atlas states for the selected stepped outline.
    for cell in sorted(wall_cells, key=lambda item: (item[1], item[0])):
        left, top = px(origin, tile, cell[0], cell[1])
        elements.append(atlas_tile(atlas_uri, left, top, tile, mask_for(cell, wall_cells)))

    # The source image includes its own rough jambs, which overlap the adjacent wall
    # cells; only the middle two cells are the proposed gate footprint.
    gate_left, gate_top = px(origin, tile, -2.5, 11.0)
    elements.append(
        f'<image href="{gate_uri}" x="{gate_left:.1f}" y="{gate_top:.1f}" width="{4 * tile:.1f}" height="{2 * tile:.1f}" preserveAspectRatio="xMidYMid meet"/>'
    )

    elements.append(
        """<text x="780" y="1298" class="subtitle" text-anchor="middle">Recommended reading: irregular oval holding, open courtyard, one vulnerable south gate; no bespoke curve or corner piece.</text>
<rect x="1580" y="156" width="420" height="1188" rx="18" fill="#2c2924" stroke="#766e62" stroke-width="3"/>
<text x="1612" y="204" class="panel-title">Prototype contract</text>
<text x="1612" y="242" class="panel-strong">35 × 24 outer footprint</text>
<text x="1612" y="272" class="panel-body">111 dry-stone wall tiles</text>
<text x="1612" y="300" class="panel-body">444 stone blocks</text>
<text x="1612" y="328" class="panel-body">1 gate · 40 wood · 2 cells</text>
<text x="1612" y="374" class="panel-title">Minimum pieces</text>
<text x="1612" y="410" class="panel-body">Wall: reuse EI_DryStoneWall</text>
<text x="1612" y="438" class="panel-body">Curves: stepped linked corners</text>
<text x="1612" y="466" class="panel-body">Entrance: layout, not a Def</text>
<text x="1612" y="494" class="panel-body">Gate: one 2 × 1 manual door</text>
<text x="1612" y="540" class="panel-title">Visible tradeoffs</text>
<text x="1612" y="576" class="panel-body">+ broad pawn / animal access</text>
<text x="1612" y="604" class="panel-body">+ 20% less stone per wall tile</text>
<text x="1612" y="632" class="panel-body">− long perimeter and dead space</text>
<text x="1612" y="660" class="panel-body">− wall blocks fire, not shooting cover</text>
<text x="1612" y="688" class="panel-body">− flammable two-cell breach point</text>
<text x="1612" y="736" class="panel-title">Square-grid shape check</text>
"""
    )
    elements.append(
        mini_shape(
            regular_outline(10, 10),
            1612,
            776,
            5.0,
            "Circular · 21 × 21",
            "Too scalloped at this scale",
        )
    )
    elements.append(
        mini_shape(
            regular_outline(16, 11),
            1612,
            946,
            4.4,
            "Oval · 33 × 23",
            "Readable but visibly diagrammatic",
        )
    )
    elements.append(
        mini_shape(
            complete_ring,
            1612,
            1116,
            4.2,
            "Irregular oval · 35 × 24",
            "Best fit for existing linked art",
        )
    )
    elements.append(
        '<text x="1612" y="1314" class="mini-note">Discovery art only · not a runtime asset</text></svg>'
    )
    return "".join(elements)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--metrics", action="store_true")
    args = parser.parse_args()
    if args.metrics:
        ring = irregular_outline()
        print(f"Oval: {len(ring)} perimeter cells, {interior_cell_count(ring)} interior cells")
        for label, width, height in (
            ("Compact rectangle", 26, 24),
            ("Same-bounds rectangle", 35, 24),
        ):
            print(
                f"{label}: {2 * width + 2 * height - 4} perimeter cells, "
                f"{(width - 2) * (height - 2)} interior cells"
            )
        return
    args.output.write_text(render(), encoding="utf-8")
    print(f"Rendered {args.output}")


if __name__ == "__main__":
    main()
