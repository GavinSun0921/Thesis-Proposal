#!/usr/bin/env python3
"""Export the vector figure from the locally compiled proposal, without caption.

Run from any directory after ./scripts/build.sh. Requires pypdf, pdfplumber,
and pdftoppm. This crops the authoritative PDF; it does not compile a separate
LaTeX document or rasterize the PDF output. Only the PNG preview is rasterized.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

import pdfplumber
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject

HERE = Path(__file__).resolve().parent
MAIN = HERE.parent / "build" / "main.pdf"
OUT = HERE / "generated" / "world_model_paradigm"
TITLE = "连续动态世界模型的状态构建与演化预测示意"


def main() -> None:
    with pdfplumber.open(MAIN) as source:
        matches = [(i, p) for i, p in enumerate(source.pages) if p.search(TITLE)]
        if len(matches) != 1:
            raise ValueError(f"Expected one figure caption, found {len(matches)}")
        index, page = matches[0]
        caption = page.search(TITLE)[0]
        heading = page.search("有限视觉观测")[0]
        footers = [
            match for label in ["离散采样", "观测更新", "另一视角", "同一未来时刻"]
            for match in page.search(label)
            if heading["top"] < match["top"] < caption["top"]
        ]
        if len(footers) != 4 or len(page.images) != 7:
            raise ValueError("Unexpected figure layout; inspect the current PDF before exporting")
        # The left source photo starts at x=.02 and has width 3.16 in TikZ.
        photo = min(page.images, key=lambda image: image["x0"])
        unit = (photo["x1"] - photo["x0"]) / 3.16
        origin = photo["x0"] - .02 * unit
        left, right = origin - 3, origin + 15.6 * unit + 3
        top = heading["top"] - 7
        bottom = max(match["bottom"] for match in footers) + 6
        page_height = page.height

    reader = PdfReader(MAIN)
    writer = PdfWriter()
    target = writer.add_blank_page(width=right - left, height=bottom - top)
    target.merge_translated_page(reader.pages[index], -left, -(page_height - bottom))
    writer.pages[0].pop(NameObject("/Annots"), None)
    writer.add_metadata({"/Title": TITLE, "/Subject": "PhysTwin visual materials; editable TikZ layout in dynamic_world_motivation.tex"})
    OUT.mkdir(parents=True, exist_ok=True)
    with (OUT / "figure.pdf").open("wb") as stream:
        writer.write(stream)
    subprocess.run([
        "pdftoppm", "-singlefile", "-scale-to", "2400", "-png",
        str(OUT / "figure.pdf"), str(OUT / "figure"),
    ], check=True)
    print(f"Exported vector figure and 2400px preview from proposal page {index + 1} to {OUT}")


if __name__ == "__main__":
    main()
