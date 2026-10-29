#!/usr/bin/env python3
"""Prepare traceable PhysTwin panels for the editable 1.1 TikZ figure.

Normal use needs Pillow only and uses the checked-in, original JPEG panels:
    python3 latex/figures/build_world_model_paradigm.py

To re-extract those panels, supply the author's arXiv PDF (pypdf required):
    python3 latex/figures/build_world_model_paradigm.py --paper /path/to/paper.pdf

The central silhouettes are 2D crops of published novel-view *model renders*.
No new geometry, motion, prediction, or invisible surface is synthesized.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter

HERE = Path(__file__).resolve().parent
MATERIALS = HERE / "materials" / "phystwin_cloth"
GENERATED = HERE / "generated" / "world_model_paradigm"
PAPER_URL = "https://arxiv.org/pdf/2503.17973"
PROJECT_URL = "https://jianghanxiao.github.io/phystwin-web/"
FORMAL_URL = (
    "https://openaccess.thecvf.com/content/ICCV2025/html/"
    "Jiang_PhysTwin_Physics-Informed_Reconstruction_and_Simulation_of_"
    "Deformable_Objects_from_Videos_ICCV_2025_paper.html"
)

# Pages are physical, one-based PDF pages. Columns are zero-based, left to right.
# The first three columns belong to the reconstruction interval; the next three
# are explicitly marked Future Prediction in the source figure.
PANELS = [
    ("observation_t1", 6, 3, "Observation", 0, "/Image4", "observed prefix"),
    ("observation_t2", 6, 3, "Observation", 2, "/Image6", "observed prefix"),
    ("state_t1_view2", 15, 9, "Viewpoint 2", 0, "/Image8", "reconstructed prefix"),
    ("state_t2_view2", 15, 9, "Viewpoint 2", 2, "/Image13", "reconstructed prefix"),
    ("prediction_future", 6, 3, "PhysTwin (Ours)", 3, "/Image12", "held-out future prediction"),
    ("execution_future", 6, 3, "Observation", 3, "/Image7", "held-out future reference"),
]

# Hand-traced image-space silhouettes. They only hide the table/background in
# the two novel-view renders; the original JPEGs remain unchanged alongside.
SILHOUETTES = {
    "state_t1_view2": [
        (42, 138), (65, 135), (83, 122), (114, 128), (141, 138),
        (165, 142), (175, 125), (171, 113), (174, 105), (185, 101),
        (212, 120), (238, 143), (261, 160), (281, 171), (301, 187),
        (283, 200), (273, 209), (251, 217), (226, 229), (205, 238),
        (176, 245), (145, 255), (117, 260), (88, 267), (77, 263),
        (64, 248), (65, 230), (58, 211), (57, 190), (49, 171),
    ],
    "state_t2_view2": [
        (165, 78), (184, 88), (200, 98), (213, 117), (215, 129),
        (243, 153), (252, 174), (249, 192), (241, 204), (224, 204),
        (216, 200), (211, 210), (200, 222), (178, 229), (162, 236),
        (145, 242), (132, 240), (120, 233), (106, 214), (104, 196),
        (100, 178), (92, 162), (85, 151), (70, 140), (63, 127),
        (64, 116), (80, 113), (96, 105), (117, 94), (141, 84),
    ],
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def extract(paper: Path) -> None:
    from pypdf import PdfReader

    reader = PdfReader(paper)
    records = []
    for name, page, figure, row, column, xobject, phase in PANELS:
        images = reader.pages[page - 1].images
        keys = [key for key in images.keys() if key[-1] == xobject]
        if len(keys) != 1:
            raise ValueError(f"Expected one {xobject} on page {page}: {keys}")
        data = images[keys[0]].data
        dest = MATERIALS / f"{name}.jpg"
        dest.write_bytes(data)
        with Image.open(dest) as image:
            size = image.size
        records.append({
            "file": dest.name, "pdf_page": page, "figure": figure,
            "case": "top red-and-gold cloth case", "row": row,
            "column_zero_based": column, "xobject": keys[0], "phase": phase,
            "size_px": list(size), "sha256": sha256(dest),
        })
    manifest = {
        "title": "PhysTwin: Physics-Informed Reconstruction and Simulation of Deformable Objects from Videos",
        "publication": "ICCV 2025, pp. 7219-7230", "bibtex_key": "phystwin2025",
        "project_url": PROJECT_URL, "formal_url": FORMAL_URL,
        "download_url": PAPER_URL, "source_pdf_sha256": sha256(paper),
        "source_pdf_version": str(reader.metadata.get("/CreationDate", "")),
        "panels": records,
        "time_labels": "t1 and t2=t indicate selected prefix order, not measured seconds; future pair uses the same held-out column",
        "protocol": "Source paper section 4.1: 7:3 video split; only training portion used for construction; control-point positions specify actions",
        "scope": "The selected paper supplies a visual example, not a claim that it implements every capability proposed in this thesis.",
    }
    (MATERIALS / "source-manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n"
    )


def build() -> None:
    manifest = json.loads((MATERIALS / "source-manifest.json").read_text())
    for panel in manifest["panels"]:
        path = MATERIALS / panel["file"]
        if sha256(path) != panel["sha256"]:
            raise ValueError(f"Source image changed: {path}")
    for name, polygon in SILHOUETTES.items():
        image = Image.open(MATERIALS / f"{name}.jpg").convert("RGBA")
        mask = Image.new("L", image.size, 0)
        ImageDraw.Draw(mask).polygon(polygon, fill=255)
        # Remove neutral table pixels near the manually traced cloth boundary.
        # This is an alpha mask only: no RGB pixel is recolored or synthesized.
        rgb = image.convert("RGB").tobytes()
        chroma = Image.frombytes("L", image.size, bytes(
            255 if r > 1.09 * g and r > 1.10 * b and r - g > 8 else 0
            for r, g, b in zip(rgb[0::3], rgb[1::3], rgb[2::3])
        ))
        chroma = chroma.filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.MinFilter(5))
        mask = ImageChops.multiply(mask, chroma)
        # A sub-pixel feather avoids stair-stepped display edges; all RGB values
        # inside the object remain from the source model render.
        mask = mask.filter(ImageFilter.GaussianBlur(0.45))
        image.putalpha(mask)
        image.crop(mask.getbbox()).save(GENERATED / f"{name}_cutout.png")
    (GENERATED / "derivatives.json").write_text(json.dumps({
        "source_manifest": "../../materials/phystwin_cloth/source-manifest.json",
        "operation": "image-space polygon and chroma alpha masking; transparent background; no RGB recoloring, geometric transformation or prediction synthesis",
        "silhouettes_px": SILHOUETTES,
        "files": {f"{name}_cutout.png": sha256(GENERATED / f"{name}_cutout.png")
                  for name in SILHOUETTES},
    }, indent=2) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--paper", type=Path)
    args = parser.parse_args()
    MATERIALS.mkdir(parents=True, exist_ok=True)
    GENERATED.mkdir(parents=True, exist_ok=True)
    if args.paper:
        extract(args.paper)
    build()
    print(f"Verified {len(PANELS)} original panels; wrote {len(SILHOUETTES)} display silhouettes to {GENERATED}")


if __name__ == "__main__":
    main()
