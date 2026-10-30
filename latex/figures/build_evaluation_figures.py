#!/usr/bin/env python3
"""Export the editable motion-metric illustration and grayscale proof.

The PCK count and 3D error sketch explain evaluation definitions. No dataset
capture, application benchmark or physical experiment is implied.
"""
from __future__ import annotations

import hashlib
import json
import math
import shutil
import subprocess
from pathlib import Path

from build_research_framework import WRAPPER

FIGURES = Path(__file__).resolve().parent
LATEX = FIGURES.parent
ROOT = LATEX.parent
OUTPUT = FIGURES / "generated" / "evaluation"
WORK = ROOT / "tmp" / "evaluation-figures-build"
FIGURE_NAMES = [
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
        "updated_date": "2026-10-30", "figures": records,
        "typography_source": "figures/technical_route_styles.tex",
        "shared_styles_sha256": digest(FIGURES / "technical_route_styles.tex"),
        "metric_definition_source": "https://github.com/KAIR-BAIR/dycheck/blob/main/dycheck/core/metrics/keypoint.py",
        "pck_example": {"radius": radius, "errors": errors, "correct": correct, "score": 2/3},
        "scope": [
            "The PCK example is a count illustration, not a measured result. The 3D trajectory sketch is qualitative.",
            "PCK is evaluated in image coordinates; 3D position error requires corresponding references in a common coordinate system.",
            "Illustrations explain metric definitions and do not imply a data-collection or application experiment.",
        ],
    }
    (OUTPUT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    print(f"Built motion-metric illustration and grayscale proof in {OUTPUT}")


if __name__ == "__main__":
    main()
