#!/usr/bin/env python3
"""Overlay editable typography on the supplied spacecraft infographic background."""
from __future__ import annotations

import argparse
import base64
from html import escape
from pathlib import Path
import shutil
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[3]
HERE = ROOT / "latex/figures/chapters/ch01-basis/spacecraft-maintenance"
ASSETS = HERE / "assets"
BACKGROUND_INPUT = Path.home() / "Downloads/Spacecraft Repair Infographic Above Earth.png"
REFERENCE_INPUT = Path.home() / "Downloads/卫星机械臂交互建模信息图.png"
BACKGROUND = ASSETS / "spacecraft-repair-background-no-text.png"
REFERENCE = ASSETS / "spacecraft-repair-text-reference.png"
SVG_OUTPUT = HERE / "diagram-overlay.svg"
DRAWIO_OUTPUT = HERE / "diagram-overlay.drawio"

WIDTH, HEIGHT = 1672, 941
SVG_NS = "http://www.w3.org/2000/svg"
XLINK_NS = "http://www.w3.org/1999/xlink"
COLORS = {
    "blue": "#0757a5",
    "green": "#007b5f",
    "amber": "#db6c0c",
    "red": "#df1616",
    "navy": "#133c75",
    "ink": "#17304a",
    "white": "#ffffff",
}


class Overlay:
    def __init__(self) -> None:
        self.items: list[dict] = []

    def rect(self, x, y, w, h, *, fill, stroke="none", sw=0, radius=0, opacity=1):
        self.items.append({"type": "rect", "x": x, "y": y, "w": w, "h": h,
                           "fill": fill, "stroke": stroke, "sw": sw,
                           "radius": radius, "opacity": opacity})

    def circle(self, x, y, radius, *, fill, stroke="none", sw=0):
        self.items.append({"type": "circle", "x": x, "y": y, "radius": radius,
                           "fill": fill, "stroke": stroke, "sw": sw})

    def text(self, x, y, value, *, size, color, family="SimSun", weight=400,
             anchor="start", italic=False):
        self.items.append({"type": "text", "x": x, "y": y, "value": value,
                           "size": size, "color": color, "family": family,
                           "weight": weight, "anchor": anchor, "italic": italic})

    def line(self, points, *, color, width=2):
        self.items.append({"type": "line", "points": points, "color": color, "width": width})


def pill(overlay, cx, cy, text, color, *, size=21, width=None, height=38, weight=600):
    width = width or max(82, len(text) * size + 28)
    overlay.rect(cx - width / 2, cy - height / 2, width, height,
                 fill="#ffffff", stroke=color, sw=2, radius=height / 2)
    overlay.text(cx, cy + size * 0.34, text, size=size, color=color,
                 family="SimHei", weight=weight, anchor="middle")


def make_overlay() -> Overlay:
    image = BACKGROUND.read_bytes()
    data_uri = "data:image/png;base64," + base64.b64encode(image).decode("ascii")
    overlay = Overlay()
    overlay.items.append({"type": "image", "href": data_uri})

    headers = [
        # center x, center y, title baseline x/y, number, title, theme
        (80, 77, 134, 89, "1", "连续时间建模", "blue"),
        (1222, 77, 1272, 91, "2", "对象时空一致性", "green"),
        (77, 510, 132, 526, "3", "物理连接变化建模", "amber"),
        (1223, 500, 1273, 518, "4", "动作后果预测", "red"),
    ]
    for cx, cy, tx, ty, number, title, theme in headers:
        color = COLORS[theme]
        overlay.circle(cx, cy, 23, fill=COLORS["white"])
        overlay.text(cx, cy + 10, number, size=34, color=color,
                     family="Times New Roman", weight=700, anchor="middle")
        overlay.text(tx, ty, title, size=34, color=COLORS["white"],
                     family="SimHei", weight=700)

    # Object identity labels and leader line are editable separately.
    pill(overlay, 1281, 165, "遮挡前", COLORS["green"], size=22, width=113, height=39)
    overlay.line([(1281, 185), (1281, 216)], color=COLORS["green"], width=2)
    pill(overlay, 1575, 165, "遮挡", COLORS["red"], size=22, width=92, height=39)
    overlay.line([(1575, 185), (1565, 214)], color=COLORS["red"], width=2)
    overlay.circle(1565, 214, 5, fill=COLORS["red"])

    # Topology labels sit below the three sequence frames.
    pill(overlay, 112, 772, "连接（完整）", COLORS["navy"], size=19, width=137, height=37)
    pill(overlay, 282, 772, "断裂", COLORS["red"], size=20, width=98, height=37)
    pill(overlay, 452, 772, "分离", COLORS["navy"], size=20, width=98, height=37)

    # Outcome labels align with the three small future-state thumbnails.
    pill(overlay, 1592, 575, "展开", COLORS["navy"], size=19, width=78, height=36)
    pill(overlay, 1592, 637, "半展开", COLORS["navy"], size=19, width=82, height=36)
    pill(overlay, 1592, 701, "未展开", COLORS["navy"], size=19, width=82, height=36)
    return overlay


def svg_bytes(overlay: Overlay) -> bytes:
    ET.register_namespace("", SVG_NS)
    ET.register_namespace("xlink", XLINK_NS)
    root = ET.Element(f"{{{SVG_NS}}}svg", {
        "width": f"{WIDTH}px", "height": f"{HEIGHT}px",
        "viewBox": f"0 0 {WIDTH} {HEIGHT}", "version": "1.1",
        "role": "img", "aria-labelledby": "title desc",
    })
    ET.SubElement(root, f"{{{SVG_NS}}}title", {"id": "title"}).text = (
        "卫星机械臂交互建模科研信息图文字层")
    ET.SubElement(root, f"{{{SVG_NS}}}desc", {"id": "desc"}).text = (
        "以用户提供的无文字信息图为底图，覆盖可编辑的四项研究需求标题与局部状态标签。")
    for index, item in enumerate(overlay.items):
        kind = item["type"]
        if kind == "image":
            ET.SubElement(root, f"{{{SVG_NS}}}image", {
                "id": "background", "x": "0", "y": "0",
                "width": str(WIDTH), "height": str(HEIGHT),
                "preserveAspectRatio": "none",
                f"{{{XLINK_NS}}}href": item["href"],
            })
        elif kind == "rect":
            ET.SubElement(root, f"{{{SVG_NS}}}rect", {
                "id": f"overlay-shape-{index}", "x": str(item["x"]),
                "y": str(item["y"]), "width": str(item["w"]),
                "height": str(item["h"]), "rx": str(item["radius"]),
                "fill": item["fill"], "stroke": item["stroke"],
                "stroke-width": str(item["sw"]), "fill-opacity": str(item["opacity"]),
            })
        elif kind == "circle":
            ET.SubElement(root, f"{{{SVG_NS}}}circle", {
                "id": f"overlay-shape-{index}", "cx": str(item["x"]),
                "cy": str(item["y"]), "r": str(item["radius"]),
                "fill": item["fill"], "stroke": item["stroke"],
                "stroke-width": str(item["sw"]),
            })
        elif kind == "text":
            attrs = {
                "id": f"editable-text-{index}", "x": str(item["x"]),
                "y": str(item["y"]), "font-family": item["family"],
                "font-size": str(item["size"]), "font-weight": str(item["weight"]),
                "text-anchor": item["anchor"], "fill": item["color"],
            }
            if item["italic"]:
                attrs["font-style"] = "italic"
            ET.SubElement(root, f"{{{SVG_NS}}}text", attrs).text = item["value"]
        elif kind == "line":
            ET.SubElement(root, f"{{{SVG_NS}}}polyline", {
                "id": f"overlay-line-{index}",
                "points": " ".join(f"{x},{y}" for x, y in item["points"]),
                "fill": "none", "stroke": item["color"],
                "stroke-width": str(item["width"]), "stroke-linecap": "round",
            })
    ET.indent(root, space="  ")
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def drawio_bytes(overlay: Overlay) -> bytes:
    mxfile = ET.Element("mxfile", {
        "host": "app.diagrams.net", "agent": "Codex",
        "version": "24.7.17", "type": "device",
    })
    diagram = ET.SubElement(mxfile, "diagram", {
        "id": "spacecraft-maintenance-overlay", "name": "图2 文字层预览",
    })
    model = ET.SubElement(diagram, "mxGraphModel", {
        "dx": str(WIDTH), "dy": str(HEIGHT), "grid": "1", "gridSize": "10",
        "guides": "1", "tooltips": "1", "connect": "1", "arrows": "1",
        "page": "1", "pageScale": "1", "pageWidth": str(WIDTH),
        "pageHeight": str(HEIGHT), "math": "0", "shadow": "0",
    })
    root = ET.SubElement(model, "root")
    ET.SubElement(root, "mxCell", {"id": "0"})
    ET.SubElement(root, "mxCell", {"id": "1", "parent": "0"})
    for index, item in enumerate(overlay.items, start=2):
        kind = item["type"]
        cell_id = str(index)
        if kind == "image":
            style = "shape=image;html=1;aspect=fixed;image=" + item["href"]
            cell = ET.SubElement(root, "mxCell", {
                "id": cell_id, "value": "", "style": style,
                "vertex": "1", "parent": "1",
            })
            ET.SubElement(cell, "mxGeometry", {
                "x": "0", "y": "0", "width": str(WIDTH),
                "height": str(HEIGHT), "as": "geometry",
            })
        elif kind in {"rect", "circle"}:
            if kind == "rect":
                x, y, w, h = item["x"], item["y"], item["w"], item["h"]
                shape = "rounded=1;arcSize=50;"
            else:
                x, y = item["x"] - item["radius"], item["y"] - item["radius"]
                w = h = item["radius"] * 2
                shape = "ellipse;aspect=fixed;"
            style = (
                shape + "html=1;whiteSpace=wrap;"
                f"fillColor={item['fill']};strokeColor={item['stroke']};"
                f"strokeWidth={max(1, item['sw'])};opacity={int(item.get('opacity', 1) * 100)};"
            )
            cell = ET.SubElement(root, "mxCell", {
                "id": cell_id, "value": "", "style": style,
                "vertex": "1", "parent": "1",
            })
            ET.SubElement(cell, "mxGeometry", {
                "x": str(x), "y": str(y), "width": str(w),
                "height": str(h), "as": "geometry",
            })
        elif kind == "text":
            align = {"start": "left", "middle": "center", "end": "right"}[item["anchor"]]
            width = max(55, len(item["value"]) * item["size"] * 1.12)
            if align == "middle":
                x = item["x"] - width / 2
            elif align == "right":
                x = item["x"] - width
            else:
                x = item["x"]
            style = (
                "text;html=1;whiteSpace=wrap;overflow=hidden;verticalAlign=middle;"
                f"align={align};fontFamily={item['family']};fontSize={item['size']};"
                f"fontColor={item['color']};fontStyle={1 if item['weight'] >= 600 else 0};"
            )
            if item["italic"]:
                style += "fontStyle=2;"
            cell = ET.SubElement(root, "mxCell", {
                "id": cell_id, "value": escape(item["value"]), "style": style,
                "vertex": "1", "parent": "1",
            })
            ET.SubElement(cell, "mxGeometry", {
                "x": f"{x:.2f}", "y": f"{item['y'] - item['size']:.2f}",
                "width": f"{width:.2f}", "height": str(item["size"] + 12),
                "as": "geometry",
            })
        elif kind == "line":
            cell = ET.SubElement(root, "mxCell", {
                "id": cell_id, "value": "",
                "style": f"edgeStyle=none;html=1;endArrow=none;strokeColor={item['color']};strokeWidth={item['width']};",
                "edge": "1", "parent": "1",
            })
            geometry = ET.SubElement(cell, "mxGeometry", {"relative": "1", "as": "geometry"})
            ET.SubElement(geometry, "mxPoint", {
                "x": str(item["points"][0][0]), "y": str(item["points"][0][1]),
                "as": "sourcePoint",
            })
            ET.SubElement(geometry, "mxPoint", {
                "x": str(item["points"][-1][0]), "y": str(item["points"][-1][1]),
                "as": "targetPoint",
            })
    ET.indent(mxfile, space="  ")
    return ET.tostring(mxfile, encoding="utf-8", xml_declaration=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="save the SVG and Draw.io source")
    parser.add_argument("--background", type=Path, default=BACKGROUND_INPUT)
    parser.add_argument("--reference", type=Path, default=REFERENCE_INPUT)
    args = parser.parse_args()
    if not args.background.is_file():
        raise SystemExit(f"Missing text-free background: {args.background}")
    ASSETS.mkdir(parents=True, exist_ok=True)
    if args.background.resolve() != BACKGROUND.resolve():
        shutil.copy2(args.background, BACKGROUND)
    if args.reference.is_file() and args.reference.resolve() != REFERENCE.resolve():
        shutil.copy2(args.reference, REFERENCE)
    image_width, image_height = __import__("PIL.Image", fromlist=["Image"]).open(BACKGROUND).size
    if (image_width, image_height) != (WIDTH, HEIGHT):
        raise SystemExit(f"Unexpected background size {(image_width, image_height)}; expected {(WIDTH, HEIGHT)}")
    overlay = make_overlay()
    if args.write:
        SVG_OUTPUT.write_bytes(svg_bytes(overlay))
        DRAWIO_OUTPUT.write_bytes(drawio_bytes(overlay))
        print(f"Wrote {SVG_OUTPUT.relative_to(ROOT)} and {DRAWIO_OUTPUT.relative_to(ROOT)}")
    else:
        print(f"Background: {BACKGROUND.relative_to(ROOT)} ({WIDTH}x{HEIGHT})")
        print(f"Layout reference: {REFERENCE.relative_to(ROOT)}")
        print("Use --write to generate the editable SVG and Draw.io source.")


if __name__ == "__main__":
    main()
