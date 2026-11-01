#!/usr/bin/env python3
"""Build the mixed raster/vector spacecraft-maintenance research figure."""
from __future__ import annotations

import argparse
import base64
from html import escape
import math
from pathlib import Path
import xml.etree.ElementTree as ET

try:
    from PIL import Image
except ImportError as exc:
    raise SystemExit("Pillow is required to crop the NASA source image") from exc

ROOT = Path(__file__).resolve().parents[3]
FIGURES = ROOT / "latex" / "figures"
HERE = FIGURES / "chapters" / "ch01-basis" / "spacecraft-maintenance"
ASSETS = HERE / "assets"
SOURCE_IMAGE = ASSETS / "iss050e056301-original.jpg"
CROPPED_IMAGE = ASSETS / "iss050e056301-crop.jpg"
SVG_OUTPUT = HERE / "diagram.svg"
DRAWIO_OUTPUT = HERE / "diagram.drawio"
WIDTH, HEIGHT = 1600, 820
PHOTO_HEIGHT = 400
SVG_NS = "http://www.w3.org/2000/svg"
XLINK_NS = "http://www.w3.org/1999/xlink"

COLORS = {
    "ink": "#17232f",
    "muted": "#52616e",
    "border": "#d6dee4",
    "blue": "#1769aa",
    "green": "#16816f",
    "amber": "#bd6b17",
    "red": "#c4443e",
    "white": "#ffffff",
    "light": "#f5f7f8",
    "gray": "#8996a0",
}


class Figure:
    def __init__(self) -> None:
        self.items: list[dict] = []

    def add(self, kind: str, **values) -> None:
        self.items.append({"kind": kind, **values})

    def rect(self, x, y, w, h, fill, stroke="none", sw=0, radius=0, **extra) -> None:
        self.add("rect", x=x, y=y, w=w, h=h, fill=fill, stroke=stroke, sw=sw,
                 radius=radius, **extra)

    def text(self, x, y, lines, size, color=COLORS["ink"], family="SimSun",
             weight=400, align="start", line_height=None) -> None:
        if isinstance(lines, str):
            lines = [lines]
        self.add("text", x=x, y=y, lines=lines, size=size, color=color,
                 family=family, weight=weight, align=align,
                 line_height=line_height or int(size * 1.3))

    def line(self, points, color, sw=4, dash=None, arrow=False) -> None:
        self.add("line", points=points, color=color, sw=sw, dash=dash, arrow=arrow)

    def circle(self, cx, cy, r, fill, stroke="none", sw=0) -> None:
        self.add("circle", cx=cx, cy=cy, r=r, fill=fill, stroke=stroke, sw=sw)


def build_crop() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    with Image.open(SOURCE_IMAGE) as image:
        image = image.convert("RGB")
        width, height = image.size
        target_height = round(width / 4)
        top = 1000
        if top + target_height > height:
            top = height - target_height
        crop = image.crop((0, top, width, top + target_height))
        crop.thumbnail((2000, 500), Image.Resampling.LANCZOS)
        crop.save(CROPPED_IMAGE, "JPEG", quality=90, optimize=True, progressive=True)


def build_content() -> Figure:
    figure = Figure()
    photo_data = base64.b64encode(CROPPED_IMAGE.read_bytes()).decode("ascii")
    figure.add("image", x=0, y=0, w=WIDTH, h=PHOTO_HEIGHT,
               href="data:image/jpeg;base64," + photo_data)
    figure.rect(0, 0, WIDTH, PHOTO_HEIGHT, "#07111a", "none", 0, 0, opacity="0.12")
    figure.rect(26, 24, 414, 122, "#10202c", "none", 0, 12, opacity="0.88")
    figure.text(48, 65, "NASA RRM-P2", 32, COLORS["white"], "Times New Roman", 400)
    figure.text(48, 117, "在轨维护任务场景", 38, COLORS["white"], "SimHei", 400)
    figure.rect(1187, 24, 387, 106, "#10202c", "none", 0, 12, opacity="0.88")
    figure.text(1211, 63, "应用背景", 25, "#c5d5df", "SimSun")
    figure.text(1211, 104, "机械臂在轨作业", 32, COLORS["white"], "SimHei")
    figure.rect(1105, 346, 470, 34, "#10202c", "none", 0, 7, opacity="0.88")
    figure.text(1120, 370, "NASA / iss050e056301 / 2017-03-08", 22,
                COLORS["white"], "Times New Roman", 400)

    figure.rect(0, PHOTO_HEIGHT, WIDTH, HEIGHT - PHOTO_HEIGHT, COLORS["light"])
    panels = [
        (24, "1", "连续时间建模", COLORS["blue"],
         ["由离散观测恢复", "观测间连续状态"]),
        (416, "2", "对象时空一致性", COLORS["green"],
         ["遮挡与形变下维持", "对象跨时关联"]),
        (808, "3", "物理连接变化建模", COLORS["amber"],
         ["识别连接改变并更新", "区分新边界与再显露"]),
        (1200, "4", "动作后果预测", COLORS["red"],
         ["执行前推演当前动作", "可能引起的状态变化"]),
    ]
    for x, number, title, color, detail in panels:
        figure.rect(x, 421, 370, 376, COLORS["white"], COLORS["border"], 2, 13)
        figure.rect(x, 421, 370, 9, color, "none", 0, 4)
        figure.circle(x + 39, 472, 22, color)
        figure.text(x + 39, 481, number, 26, COLORS["white"],
                    "Times New Roman", 700, "middle")
        figure.text(x + 72, 483, title, 31, color, "SimHei", 400)
        figure.text(x + 185, 716, detail, 30, COLORS["ink"], "SimSun", 400,
                    "middle", 43)

    # Continuous trajectory constrained by sparse observations.
    x = 24
    figure.line([(x + 38, 637), (x + 332, 637)], COLORS["border"], 3)
    observations = [(x + 46, 619), (x + 122, 576), (x + 205, 598), (x + 302, 552)]
    # Sample a cubic Hermite curve so both SVG and draw.io retain vector geometry.
    anchors = observations + [(x + 329, 539)]
    trajectory = []
    for i in range(len(anchors) - 1):
        p0 = anchors[max(0, i - 1)]
        p1, p2 = anchors[i], anchors[i + 1]
        p3 = anchors[min(len(anchors) - 1, i + 2)]
        for j in range(18):
            t = j / 18
            pt = []
            for axis in range(2):
                a, b, c, d = p0[axis], p1[axis], p2[axis], p3[axis]
                pt.append(round(0.5 * ((2*b) + (-a+c)*t +
                    (2*a-5*b+4*c-d)*t*t + (-a+3*b-3*c+d)*t*t*t), 2))
            trajectory.append(tuple(pt))
    trajectory.append(anchors[-1])
    figure.line(trajectory, COLORS["blue"], 5, arrow=True)
    for index, (cx, cy) in enumerate(observations):
        figure.circle(cx, cy, 10, COLORS["white"], COLORS["blue"], 5)
        figure.text(cx, 668, f"t{index}", 23, COLORS["muted"],
                    "Times New Roman", 400, "middle")

    # Stable object identity carried between partially occluded observations.
    x = 416
    for frame_x, label in [(x + 29, "t0"), (x + 210, "t1")]:
        figure.rect(frame_x, 532, 130, 108, "#fbfcfd", COLORS["border"], 2, 8)
        figure.text(frame_x + 65, 554, label, 23, COLORS["muted"],
                    "Times New Roman", 400, "middle")
    figure.rect(x + 66, 571, 46, 42, "#d9edf8", COLORS["blue"], 4, 5)
    figure.text(x + 89, 601, "A", 25, COLORS["blue"], "Times New Roman", 700, "middle")
    figure.rect(x + 106, 559, 24, 78, "#c8d0d6", "none", 0, 5)
    figure.rect(x + 247, 571, 46, 42, "#d9edf8", COLORS["blue"], 4, 5)
    figure.text(x + 270, 601, "A", 25, COLORS["blue"], "Times New Roman", 700, "middle")
    figure.line([(x + 135, 591), (x + 240, 591)], COLORS["green"], 4,
                dash="8 7", arrow=True)
    figure.text(x + 94, 668, "局部遮挡", 22, COLORS["muted"], "SimSun", 400, "middle")
    figure.text(x + 275, 668, "身份延续", 22, COLORS["muted"], "SimSun", 400, "middle")

    # The scene graph updates when an attachment relation is severed.
    x = 808
    left_a, left_b = (x + 87, 591), (x + 145, 591)
    right_a, right_b = (x + 247, 575), (x + 309, 611)
    figure.circle(*left_a, 18, "#f8e8d4", COLORS["amber"], 4)
    figure.circle(*left_b, 18, "#f8e8d4", COLORS["amber"], 4)
    figure.line([left_a, left_b], COLORS["amber"], 7)
    figure.line([(x + 180, 591), (x + 211, 591)], COLORS["gray"], 4, arrow=True)
    figure.circle(*right_a, 18, "#f8e8d4", COLORS["amber"], 4)
    figure.circle(*right_b, 18, "#f8e8d4", COLORS["amber"], 4)
    figure.line([right_a, right_b], COLORS["gray"], 3, dash="7 7")
    figure.line([(x + 267, 581), (x + 288, 601)], COLORS["red"], 5)
    figure.line([(x + 288, 581), (x + 267, 601)], COLORS["red"], 5)
    figure.text(x + 116, 668, "连接有效", 22, COLORS["muted"],
                "SimSun", 400, "middle")
    figure.text(x + 279, 668, "连接更新", 22, COLORS["muted"],
                "SimSun", 400, "middle")

    # An action conditions a set of possible future states.
    x = 1200
    figure.circle(x + 56, 590, 28, "#fde5e2", COLORS["red"], 4)
    figure.text(x + 56, 598, "s", 25, COLORS["red"], "Times New Roman", 400, "middle")
    figure.text(x + 56, 668, "当前状态", 22, COLORS["muted"], "SimSun", 400, "middle")
    figure.line([(x + 86, 590), (x + 134, 590)], COLORS["red"], 4, arrow=True)
    figure.rect(x + 141, 562, 62, 56, "#fff7f6", COLORS["red"], 3, 7)
    figure.text(x + 172, 598, "a", 25, COLORS["red"], "Times New Roman", 400, "middle")
    figure.text(x + 172, 668, "给定动作", 22, COLORS["muted"], "SimSun", 400, "middle")
    figure.line([(x + 206, 590), (x + 255, 590)], COLORS["red"], 3)
    for cy in [546, 590, 634]:
        figure.line([(x + 255, 590), (x + 285, cy),
                     (x + 309, cy)], COLORS["red"], 3, arrow=True)
        figure.circle(x + 327, cy, 9, "#fde5e2", COLORS["red"], 3)
    figure.text(x + 297, 668, "可能响应", 22, COLORS["muted"], "SimSun", 400, "middle")

    return figure


def svg_bytes(figure: Figure) -> bytes:
    ET.register_namespace("", SVG_NS)
    ET.register_namespace("xlink", XLINK_NS)
    root = ET.Element(f"{{{SVG_NS}}}svg", {
        "width": f"{WIDTH}px", "height": f"{HEIGHT}px",
        "viewBox": f"0 0 {WIDTH} {HEIGHT}", "version": "1.1",
        "role": "img", "aria-labelledby": "title desc",
    })
    ET.SubElement(root, f"{{{SVG_NS}}}title", {"id": "title"}).text = (
        "面向在轨维护任务的世界模型动态环境建模需求")
    ET.SubElement(root, f"{{{SVG_NS}}}desc", {"id": "desc"}).text = (
        "NASA RRM-P2在轨机械臂照片与连续时间、对象一致性、物理连接变化、动作后果预测四项研究需求示意。")
    defs = ET.SubElement(root, f"{{{SVG_NS}}}defs")
    clip = ET.SubElement(defs, f"{{{SVG_NS}}}clipPath", {"id": "photoClip"})
    ET.SubElement(clip, f"{{{SVG_NS}}}rect", {
        "x": "0", "y": "0", "width": str(WIDTH), "height": str(PHOTO_HEIGHT), "rx": "4"})

    for item in figure.items:
        kind = item["kind"]
        if kind == "rect":
            attrs = {
                "x": str(item["x"]), "y": str(item["y"]),
                "width": str(item["w"]), "height": str(item["h"]),
                "fill": item["fill"], "stroke": item["stroke"],
                "stroke-width": str(item["sw"]), "rx": str(item["radius"]),
            }
            if "opacity" in item:
                attrs["fill-opacity"] = item["opacity"]
            ET.SubElement(root, f"{{{SVG_NS}}}rect", attrs)
        elif kind == "image":
            ET.SubElement(root, f"{{{SVG_NS}}}image", {
                "x": str(item["x"]), "y": str(item["y"]),
                "width": str(item["w"]), "height": str(item["h"]),
                "preserveAspectRatio": "none", "clip-path": "url(#photoClip)",
                f"{{{XLINK_NS}}}href": item["href"],
            })
        elif kind == "text":
            if len(item["lines"]) == 1 and len(item["lines"][0]) == 2 and item["lines"][0][0] == "t" and item["lines"][0][1].isdigit():
                # Explicit baselines avoid viewer-dependent baseline-shift support.
                size = item["size"]
                start_x = item["x"] - size * 0.29
                ET.SubElement(root, f"{{{SVG_NS}}}text", {
                    "x": str(start_x), "y": str(item["y"]),
                    "fill": item["color"], "font-family": "Times New Roman",
                    "font-size": str(size), "font-style": "italic",
                }).text = "t"
                ET.SubElement(root, f"{{{SVG_NS}}}text", {
                    "x": str(start_x + size * 0.30), "y": str(item["y"] + size * 0.22),
                    "fill": item["color"], "font-family": "Times New Roman",
                    "font-size": str(size * 0.72),
                }).text = item["lines"][0][1]
                continue
            anchor = {"start": "start", "middle": "middle", "end": "end"}[item["align"]]
            element = ET.SubElement(root, f"{{{SVG_NS}}}text", {
                "x": str(item["x"]), "y": str(item["y"]),
                "fill": item["color"], "font-family": item["family"],
                "font-size": str(item["size"]), "font-weight": str(item["weight"]),
                "text-anchor": anchor,
            })
            for index, line in enumerate(item["lines"]):
                attrs = {"x": str(item["x"])}
                if index:
                    attrs["dy"] = str(item["line_height"])
                span = ET.SubElement(element, f"{{{SVG_NS}}}tspan", attrs)
                span.text = line
                if line in {"s", "a"}:
                    element.set("font-style", "italic")
        elif kind == "circle":
            ET.SubElement(root, f"{{{SVG_NS}}}circle", {
                "cx": str(item["cx"]), "cy": str(item["cy"]), "r": str(item["r"]),
                "fill": item["fill"], "stroke": item["stroke"],
                "stroke-width": str(item["sw"]),
            })
        elif kind == "line":
            attrs = {
                "points": " ".join(f"{x},{y}" for x, y in item["points"]),
                "fill": "none", "stroke": item["color"],
                "stroke-width": str(item["sw"]), "stroke-linecap": "round",
                "stroke-linejoin": "round",
            }
            if item["dash"]:
                attrs["stroke-dasharray"] = item["dash"]
            ET.SubElement(root, f"{{{SVG_NS}}}polyline", attrs)
            if item["arrow"]:
                # Explicit filled arrowheads render consistently in SVG viewers.
                tip_x, tip_y = item["points"][-1]
                prev_x, prev_y = next(p for p in reversed(item["points"][:-1])
                                      if p != item["points"][-1])
                length = math.hypot(tip_x - prev_x, tip_y - prev_y)
                ux, uy = (tip_x - prev_x) / length, (tip_y - prev_y) / length
                arrow_length = max(12, min(18, item["sw"] * 3.3))
                half_width = max(5, item["sw"] * 1.25)
                bx, by = tip_x - ux * arrow_length, tip_y - uy * arrow_length
                points = [(tip_x, tip_y), (bx - uy * half_width, by + ux * half_width),
                          (bx + uy * half_width, by - ux * half_width)]
                ET.SubElement(root, f"{{{SVG_NS}}}polygon", {
                    "points": " ".join(f"{px:.2f},{py:.2f}" for px, py in points),
                    "fill": item["color"],
                })
    ET.indent(root, space="  ")
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def drawio_bytes(figure: Figure) -> bytes:
    mxfile = ET.Element("mxfile", {
        "host": "app.diagrams.net", "modified": "2026-11-01T00:00:00.000Z",
        "agent": "Codex", "version": "24.7.17", "type": "device",
    })
    diagram = ET.SubElement(mxfile, "diagram", {"id": "spacecraft-maintenance", "name": "图2 在轨维护科研示意"})
    model = ET.SubElement(diagram, "mxGraphModel", {
        "dx": "1600", "dy": "820", "grid": "1", "gridSize": "10",
        "guides": "1", "tooltips": "1", "connect": "1", "arrows": "1",
        "fold": "1", "page": "1", "pageScale": "1", "pageWidth": str(WIDTH),
        "pageHeight": str(HEIGHT), "math": "0", "shadow": "0",
    })
    root = ET.SubElement(model, "root")
    ET.SubElement(root, "mxCell", {"id": "0"})
    ET.SubElement(root, "mxCell", {"id": "1", "parent": "0"})
    next_id = 2
    for item in figure.items:
        kind = item["kind"]
        cell_id = str(next_id)
        next_id += 1
        if kind == "image":
            style = "shape=image;html=1;aspect=fixed;image=" + item["href"]
            cell = ET.SubElement(root, "mxCell", {
                "id": cell_id, "value": "", "style": style,
                "vertex": "1", "parent": "1",
            })
            ET.SubElement(cell, "mxGeometry", {
                "x": str(item["x"]), "y": str(item["y"]), "width": str(item["w"]),
                "height": str(item["h"]), "as": "geometry",
            })
        elif kind == "rect":
            style = (
                "rounded=1;arcSize=5;whiteSpace=wrap;html=1;"
                f"fillColor={item['fill']};strokeColor={item['stroke']};"
                f"strokeWidth={max(item['sw'], 1)};opacity={int(float(item.get('opacity', 1)) * 100)};"
            )
            cell = ET.SubElement(root, "mxCell", {
                "id": cell_id, "value": "", "style": style,
                "vertex": "1", "parent": "1",
            })
            ET.SubElement(cell, "mxGeometry", {
                "x": str(item["x"]), "y": str(item["y"]), "width": str(item["w"]),
                "height": str(item["h"]), "as": "geometry",
            })
        elif kind == "circle":
            style = (
                "ellipse;aspect=fixed;html=1;"
                f"fillColor={item['fill']};strokeColor={item['stroke']};strokeWidth={max(item['sw'], 1)};"
            )
            cell = ET.SubElement(root, "mxCell", {
                "id": cell_id, "value": "", "style": style,
                "vertex": "1", "parent": "1",
            })
            ET.SubElement(cell, "mxGeometry", {
                "x": str(item["cx"] - item["r"]), "y": str(item["cy"] - item["r"]),
                "width": str(item["r"] * 2), "height": str(item["r"] * 2),
                "as": "geometry",
            })
        elif kind == "text":
            value = "<div>" + "<br>".join(escape(line) for line in item["lines"]) + "</div>"
            align = {"start": "left", "middle": "center", "end": "right"}[item["align"]]
            family = "Times New Roman" if item["family"] == "Times New Roman" else item["family"]
            style = (
                "text;html=1;whiteSpace=wrap;overflow=hidden;verticalAlign=middle;"
                f"align={align};fontFamily={family};fontSize={item['size']};"
                f"fontColor={item['color']};fontStyle={1 if item['weight'] >= 600 else 0};"
            )
            height = item["size"] * (1 + max(0, len(item["lines"]) - 1) * 1.3)
            if align == "left":
                x = item["x"]
            elif align == "right":
                x = item["x"] - 300
            else:
                x = item["x"] - 180
            cell = ET.SubElement(root, "mxCell", {
                "id": cell_id, "value": value, "style": style,
                "vertex": "1", "parent": "1",
            })
            ET.SubElement(cell, "mxGeometry", {
                "x": str(x), "y": str(item["y"] - height), "width": "360",
                "height": str(height), "as": "geometry",
            })
        elif kind == "line":
            style = (
                "edgeStyle=none;rounded=1;html=1;startArrow=none;"
                f"endArrow={'block' if item['arrow'] else 'none'};endFill=1;"
                f"strokeColor={item['color']};strokeWidth={item['sw']};"
            )
            if item["dash"]:
                style += "dashed=1;dashPattern=8 7;"
            cell = ET.SubElement(root, "mxCell", {
                "id": cell_id, "value": "", "style": style,
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
            if len(item["points"]) > 2:
                points = ET.SubElement(geometry, "Array", {"as": "points"})
                for x, y in item["points"][1:-1]:
                    ET.SubElement(points, "mxPoint", {"x": str(x), "y": str(y)})
    ET.indent(mxfile, space="  ")
    return ET.tostring(mxfile, encoding="utf-8", xml_declaration=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write diagram.svg and diagram.drawio")
    parser.add_argument("--svg-only", action="store_true", help="update only the SVG draft")
    args = parser.parse_args()
    build_crop()
    figure = build_content()
    if args.write:
        SVG_OUTPUT.write_bytes(svg_bytes(figure))
        if not args.svg_only:
            DRAWIO_OUTPUT.write_bytes(drawio_bytes(figure))
        print(f"Wrote {SVG_OUTPUT.relative_to(ROOT)}")
    else:
        print(f"Source image: {SOURCE_IMAGE.relative_to(ROOT)}")
        print(f"Generated crop: {CROPPED_IMAGE.relative_to(ROOT)}")
        print(f"Use --write to generate {SVG_OUTPUT.name} and {DRAWIO_OUTPUT.name}")


if __name__ == "__main__":
    main()
