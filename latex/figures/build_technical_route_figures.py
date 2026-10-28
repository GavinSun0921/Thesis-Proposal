#!/usr/bin/env python3
"""Export five editable technical-route diagrams with local MacTeX.

Exports vector PDFs, PNG previews, grayscale proofs and a source manifest.
The diagrams show proposed mechanisms; they contain no experiment results.
"""
from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
from pathlib import Path

from build_research_framework import WRAPPER

FIGURES = Path(__file__).resolve().parent
LATEX = FIGURES.parent
ROOT = LATEX.parent
WORK = ROOT / "tmp" / "technical-route-figures-build"
OUTPUT = FIGURES / "generated" / "technical_routes"
PANELS = [
    ("technical_route_overview", "连续动态世界模型总体技术路线"),
    ("technical_route_time", "连续时间状态构建技术路线"),
    ("technical_route_space", "连续运动引导的空间结构表征技术路线"),
    ("technical_route_topology", "拓扑自适应表征技术路线"),
    ("technical_route_response", "连续状态驱动的动作响应技术路线"),
]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    for name in ("xelatex", "pdftoppm"):
        if not shutil.which(name):
            raise SystemExit(f"Required local tool is missing: {name}")
    OUTPUT.mkdir(parents=True, exist_ok=True)
    records = []
    for stem, title in PANELS:
        work = WORK / stem
        work.mkdir(parents=True, exist_ok=True)
        wrapper = WRAPPER.replace("\\usepackage{amsmath}", "\\usepackage{amsmath,amssymb}")
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
        shutil.copy2(work / "figure.pdf", OUTPUT / f"{stem}.pdf")
        for suffix, options in (("", []), ("-gray", ["-gray"])):
            result = subprocess.run([
                "pdftoppm", "-singlefile", "-scale-to", "2400", "-png", *options,
                str(OUTPUT / f"{stem}.pdf"), str(OUTPUT / f"{stem}{suffix}"),
            ], check=True, capture_output=True, text=True)
            if "Syntax Error" in result.stderr:
                raise SystemExit(result.stderr[:1000])
        records.append({
            "title": title, "source": f"figures/{stem}.tex",
            "source_sha256": digest(FIGURES / f"{stem}.tex"),
            "pdf": f"{stem}.pdf", "pdf_sha256": digest(OUTPUT / f"{stem}.pdf"),
        })
    manifest = {
        "kind": "proposed technical routes, editable vector diagrams",
        "shared_styles_sha256": digest(FIGURES / "technical_route_styles.tex"),
        "figures": records,
        "scope": [
            "Filled numbered markers indicate research emphasis, not originality or validated performance.",
            "Muted blue, green, ochre and violet identify research stages; local colors distinguish trajectories, parts, connection validity, histories and actions. Text and frames stay black.",
            "Local colors are paired with line styles, node shapes, interval markers or labels for grayscale reading.",
            "Explanatory legends, complete-sentence sketch notes and schematic-scope notes belong to adjacent method prose. Figures retain module, variable, interval and necessary relation labels.",
            "The integrated prediction mode uses observations available by t0 only.",
            "Association, physical connection and proximity/contact candidates are distinct relations.",
            "Surface history is distinct from material-motion history and first visibility.",
            "Future geometry and motion are model predictions; new observations arrive after execution.",
        ],
    }
    (OUTPUT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    print(f"Built five editable technical-route diagrams and grayscale proofs in {OUTPUT}")


if __name__ == "__main__":
    main()
