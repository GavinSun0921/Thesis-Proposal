#!/usr/bin/env python3
"""Build source-backed dataset examples and original motion-metric diagrams.

Uses only local saved sources. Default execution never downloads data or media.
Exports editable vector figures, color/grayscale proofs, crops and provenance.
"""
from __future__ import annotations

import hashlib
import json
import math
import shutil
import subprocess
from pathlib import Path

from PIL import Image

from build_research_framework import WRAPPER

FIGURES = Path(__file__).resolve().parent
LATEX = FIGURES.parent
ROOT = LATEX.parent
OUTPUT = FIGURES / "generated" / "evaluation"
WORK = ROOT / "tmp" / "evaluation-figures-build"
MATERIALS = FIGURES / "materials" / "evaluation"

# Only rectangular crops; original colors, geometry and annotation content stay intact.
PANELS = [
    ("dycheck_a", "materials/dycheck_apple/0_00000.png", (40, 370, 700, 810),
     "DyCheck iPhone apple, camera 0, frame 0; real observation"),
    ("dycheck_b", "materials/dycheck_apple/0_00332.png", (60, 420, 720, 860),
     "DyCheck iPhone apple, camera 0, frame 332; real observation"),
    ("pointodyssey_snow", "materials/evaluation/pointodyssey_pipeline.jpg", (1235, 170, 1565, 350),
     "Official PointOdyssey pipeline visual, first synthetic snow-scene RGB example"),
    ("pointodyssey_kitchen", "materials/evaluation/pointodyssey_pipeline.jpg", (1235, 676, 1565, 856),
     "Official PointOdyssey pipeline visual, first synthetic kitchen-scene RGB example"),
    ("phystwin_a", "materials/phystwin_cloth/observation_t1.jpg", None,
     "PhysTwin Figure 3, cloth case, first observed prefix example"),
    ("phystwin_b", "materials/phystwin_cloth/observation_t2.jpg", None,
     "PhysTwin Figure 3, same cloth case, later observed prefix example"),
    ("droid_view1", "materials/literature_review/point_observation_v1.jpg", None,
     "PointWorld Figure 16, DROID cloth episode, RGB observation view 1"),
    ("droid_view2", "materials/literature_review/point_observation_v2.jpg", None,
     "PointWorld Figure 16, same DROID episode and instant, RGB observation view 2"),
]
FIGURE_NAMES = [
    ("evaluation_datasets", "拟采用的动态场景与交互数据示例"),
    ("evaluation_motion_metrics", "二维对应与三维轨迹误差评价示意"),
]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def render_pdf(pdf: Path, stem: Path, gray: bool) -> None:
    """Rasterise one page, preferring pdftoppm and falling back to Ghostscript."""
    if shutil.which("pdftoppm"):
        result = subprocess.run([
            "pdftoppm", "-singlefile", "-scale-to", "2400", "-png",
            *(["-gray"] if gray else []), str(pdf), str(stem),
        ], check=True, capture_output=True, text=True)
        if "Syntax Error" in result.stderr:
            raise SystemExit(result.stderr[:1000])
    elif shutil.which("gs"):
        subprocess.run([
            "gs", "-q", "-dNOPAUSE", "-dBATCH", "-dSAFER", "-r386",
            "-dFirstPage=1", "-dLastPage=1",
            f"-sDEVICE={'pnggray' if gray else 'png16m'}",
            f"-sOutputFile={stem}.png", str(pdf),
        ], check=True)
    else:
        raise SystemExit("Required preview tool is missing: pdftoppm or gs")


def main() -> None:
    if not shutil.which("xelatex"):
        raise SystemExit("Required local tool is missing: xelatex")
    OUTPUT.mkdir(parents=True, exist_ok=True)
    source_records = []
    for name, source, crop, role in PANELS:
        original = FIGURES / source
        with Image.open(original) as image:
            raw_size = image.size
            image = image.convert("RGB")
            if crop:
                x0, y0, x1, y1 = crop
                if not (0 <= x0 < x1 <= image.width and 0 <= y0 < y1 <= image.height):
                    raise ValueError(f"Crop outside original image: {name}")
                image = image.crop(crop)
            target = OUTPUT / f"{name}.png"
            image.save(target)
        source_records.append({
            "name": name, "source": source, "source_sha256": digest(original),
            "source_size_px": raw_size, "crop": crop, "role": role,
            "output": target.name, "output_sha256": digest(target),
        })

    # Check the illustrated geometric count: each mark is drawn at a fixed offset
    # from its disc centre, and only the third one falls outside the tolerance.
    radius = 0.80
    errors = [math.hypot(0.30, 0.22), math.hypot(0.34, 0.26), math.hypot(0.86, 0.54)]
    correct = [error < radius for error in errors]
    if correct != [True, True, False]:
        raise ValueError("PCK illustration must show two correct points out of three")

    records = []
    for stem, title in FIGURE_NAMES:
        work = WORK / stem
        work.mkdir(parents=True, exist_ok=True)
        wrapper = WRAPPER.replace("\\usepackage{amsmath}", "\\usepackage{amsmath,amssymb,graphicx}")
        wrapper = wrapper.replace("连续动态世界模型研究框架", title)
        wrapper = wrapper.replace("figures/research_framework.tex", f"figures/{stem}.tex")
        source = work / "figure.tex"
        source.write_text(wrapper)
        with (work / "build.log").open("w") as log:
            result = subprocess.run([
                "xelatex", "-halt-on-error", "-interaction=nonstopmode",
                "-file-line-error", f"-output-directory={work}", str(source),
            ], cwd=LATEX, stdout=log, stderr=subprocess.STDOUT)
        if result.returncode:
            raise SystemExit(f"Figure compilation failed: {work / 'build.log'}")
        pdf = OUTPUT / f"{stem}.pdf"
        shutil.copy2(work / "figure.pdf", pdf)
        for suffix, gray in (("", False), ("-gray", True)):
            render_pdf(pdf, OUTPUT / f"{stem}{suffix}", gray)
        records.append({
            "title": title, "source": f"figures/{stem}.tex",
            "source_sha256": digest(FIGURES / f"{stem}.tex"),
            "pdf": pdf.name, "pdf_sha256": digest(pdf),
        })

    manifest = {
        "retrieved_date": "2026-10-27", "panels": source_records, "figures": records,
        "new_media": {
            "path": "materials/evaluation/pointodyssey_pipeline.jpg",
            "url": "https://pointodyssey.com/assets/pipeline.jpg",
            "sha256": digest(MATERIALS / "pointodyssey_pipeline.jpg"),
        },
        "metric_definition_source": "https://github.com/KAIR-BAIR/dycheck/blob/main/dycheck/core/metrics/keypoint.py",
        "pck_example": {"radius": radius, "errors": errors, "correct": correct, "score": 2/3},
        "scope": [
            "Dataset panels show real observations or author-published synthetic inputs, never model predictions.",
            "The two PointOdyssey panels are different synthetic scenes, not successive frames of one scene.",
            "DyCheck and PhysTwin time labels indicate ordering only; the DROID pair is synchronized views.",
            "The PCK example is a count illustration, not a measured result. The 3D trajectory sketch is qualitative.",
            "PCK is evaluated in image coordinates; 3D position error requires 3D references in a common coordinate system.",
            "PointWorld-DROID annotations are estimated references with validity/confidence masks, not complete physical ground truth.",
            "True cutting/tearing validation remains a planned controlled-data component and is not depicted as an existing public dataset.",
        ],
    }
    (OUTPUT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    print(f"Built dataset and motion-metric figures, source map and grayscale proofs in {OUTPUT}")


if __name__ == "__main__":
    main()
