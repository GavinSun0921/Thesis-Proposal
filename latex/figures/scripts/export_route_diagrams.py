#!/usr/bin/env python3
"""Export and validate the four detailed route diagrams in Chapter 3.

Requires CairoSVG and Cairo. The source SVG and exported PDF live together in
one chapter-scoped directory. Run from the repository root with:

    python3 latex/figures/scripts/export_route_diagrams.py
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET

FIGURES = Path(__file__).resolve().parents[1]
NS = {"svg": "http://www.w3.org/2000/svg"}
ROUTES = {
    "continuous-time-route": "chapters/ch03-plan/continuous-time-route",
    "object-consistency-route": "chapters/ch03-plan/object-consistency-route",
    "topology-change-route": "chapters/ch03-plan/topology-change-route",
    "action-response-route": "chapters/ch03-plan/action-response-route",
}
STEMS = tuple(ROUTES)
COLUMNS = ("46", "787", "1528")


def check_rects(root: ET.Element, name: str) -> None:
    rects = root.findall(".//svg:rect", NS)
    dual_feedback = name == "action-response-route"
    result_y, result_height = ("888", "174") if dual_feedback else ("900", "162")
    feedback_height = "166" if dual_feedback else "108"
    output_y, output_height = ("1278", "76") if dual_feedback else ("1220", "124")

    def matching(x: str, y: str, width: str, height: str) -> list[ET.Element]:
        return [
            rect for rect in rects
            if (rect.get("x"), rect.get("y"), rect.get("width"), rect.get("height"))
            == (x, y, width, height)
        ]

    groups = [
        ([(x, "28", "702", "182") for x in COLUMNS], 3, "input frames"),
        ([(str(int(x) + 1), "29", "700", "64") for x in COLUMNS], 3, "input title bands"),
        ([(x, "270", "702", "804") for x in COLUMNS], 3, "main panels"),
        ([(str(int(x) + 22), y, "658", "136") for x in COLUMNS for y in ("420", "580", "740")], 9, "step cards"),
        ([(str(int(x) + 22), result_y, "658", result_height) for x in COLUMNS], 3, "result cards"),
        ([("146", "1094", "1988", feedback_height)], 1, "feedback band"),
        ([("46", output_y, "2184", output_height)], 1, "output band"),
    ]
    for coordinates, expected, label in groups:
        matched = [rect for item in coordinates for rect in matching(*item)]
        if len(matched) != expected:
            raise SystemExit(f"Unexpected {label} geometry in {name}: {len(matched)}/{expected}")

    styles = {
        "input frames": ("1.7", "15"),
        "main panels": ("2.2", "17"),
        "step cards": ("1.6", "12"),
        "result cards": ("1.6", "11"),
        "feedback band": ("1.7", "12"),
        "output band": ("1.8", "14"),
    }
    for coordinates, _, label in groups:
        if label not in styles:
            continue
        stroke_width, radius = styles[label]
        matched = [rect for item in coordinates for rect in matching(*item)]
        if any(rect.get("stroke-width") != stroke_width or rect.get("rx") != radius for rect in matched):
            raise SystemExit(f"Inconsistent {label} border style in {name}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--only", action="append", choices=STEMS)
    args = parser.parse_args()
    try:
        import cairosvg
    except (ImportError, OSError) as exc:
        raise SystemExit(f"CairoSVG/Cairo is required: {exc}") from exc

    manifest_path = FIGURES / "manifest.json"
    manifest = json.loads(manifest_path.read_text())
    records = []
    for stem in STEMS:
        if args.only and stem not in args.only:
            continue
        figure_dir = FIGURES / ROUTES[stem]
        source = figure_dir / "diagram.svg"
        target = figure_dir / "figure.pdf"
        data = source.read_bytes()
        root = ET.fromstring(data)
        if root.attrib.get("viewBox") != "0 0 2280 1380":
            raise SystemExit(f"Unexpected canvas in {source}")
        texts = root.findall(".//svg:text", NS)
        expected_texts = 49 if stem == "action-response-route" else 29
        if len(texts) != expected_texts:
            raise SystemExit(f"Expected {expected_texts} text blocks in {source}, got {len(texts)}")
        check_rects(root, stem)
        sizes = {float(text.attrib.get("font-size", 0)) for text in texts}
        if sizes != {42.0, 44.0, 46.0, 48.0, 50.0}:
            raise SystemExit(f"Unexpected shared typography in {source}: {sorted(sizes)}")
        for text in texts:
            if text.attrib.get("text-anchor") != "middle":
                raise SystemExit(f"Uncentred text block in {source}: {''.join(text.itertext())}")
            if text.attrib.get("font-family") != "Arial Unicode MS":
                raise SystemExit(f"Unexpected export font in {source}")
        cairosvg.svg2pdf(bytestring=data, write_to=str(target))
        record = {
            "source": str(source.relative_to(FIGURES)),
            "output": str(target.relative_to(FIGURES)),
            "text_blocks": len(texts),
            "font_sizes_px": sorted(sizes),
            "source_sha256": hashlib.sha256(data).hexdigest(),
            "output_sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
        }
        manifest["figures"]["ch03." + stem].update(record)
        records.append(record)
        print(json.dumps(record, ensure_ascii=False))
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    print(f"Exported {len(records)} detailed route diagram(s).")


if __name__ == "__main__":
    main()
