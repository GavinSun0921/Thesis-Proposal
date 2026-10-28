#!/usr/bin/env python3
"""Export the vector figure from the locally compiled proposal, without caption.

Run from any directory after ./scripts/build.sh. Requires pypdf and pdfplumber;
the PNG preview uses pdftoppm, falling back to Ghostscript when it is absent.
This crops the authoritative PDF; it does not compile a separate LaTeX document
or rasterize the vector output. Only the PNG preview is rasterized.
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
TITLE = "连续动态世界模型的状态构建与演化预测概念示意"
# Layout constants in cm, matching dynamic_world_motivation.tex:
# bounding box 15.6 x 7.10; observation_t1 at x=1.9, top y=6.383, width 3.7.
FIG_W, FIG_H = 15.6, 7.10
PHOTO_X, PHOTO_TOP, PHOTO_W = 1.9, 6.383, 3.7


def main() -> None:
    with pdfplumber.open(MAIN) as source:
        matches = [(i, p) for i, p in enumerate(source.pages) if p.search(TITLE)]
        if len(matches) != 1:
            raise ValueError(f"Expected one figure caption, found {len(matches)}")
        index, page = matches[0]
        caption = page.search(TITLE)[0]
        # The row labels are the leftmost occurrences above the caption.
        rows = [min(page.search(label), key=lambda match: match["x0"])
                for label in ("视觉观测", "三维状态")]
        if any(row["top"] > caption["top"] for row in rows):
            raise ValueError("Unexpected figure layout; inspect the current PDF before exporting")
        if len(page.images) != 6:
            raise ValueError("Unexpected figure images; inspect the current PDF before exporting")
        # Topmost image is the first observation frame (top y=6.383 in TikZ).
        photo = min(page.images, key=lambda image: (round(image["top"], 1), image["x0"]))
        unit = (photo["x1"] - photo["x0"]) / PHOTO_W
        origin_x = photo["x0"] - PHOTO_X * unit
        origin_bottom = photo["top"] + PHOTO_TOP * unit
        left, right = origin_x - 3, origin_x + FIG_W * unit + 3
        top = origin_bottom - FIG_H * unit - 3
        bottom = origin_bottom + 3
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
    try:
        subprocess.run([
            "pdftoppm", "-singlefile", "-scale-to", "2400", "-png",
            str(OUT / "figure.pdf"), str(OUT / "figure"),
        ], check=True)
    except FileNotFoundError:
        subprocess.run([
            "gs", "-q", "-dNOPAUSE", "-dBATCH", "-sDEVICE=png16m", "-r386",
            "-dFirstPage=1", "-dLastPage=1",
            f"-sOutputFile={OUT / 'figure.png'}", str(OUT / "figure.pdf"),
        ], check=True)
    print(f"Exported vector figure and 2400px preview from proposal page {index + 1} to {OUT}")


if __name__ == "__main__":
    main()
