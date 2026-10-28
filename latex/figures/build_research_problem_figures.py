#!/usr/bin/env python3
"""Export the four editable Section 2.2 problem illustrations.

Uses local MacTeX/XeLaTeX and pdftoppm. Each figure remains a TikZ source;
exports are vector PDFs plus color/grayscale PNG proofs. No network or photos.
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
WORK = ROOT / "tmp" / "research-problem-figures-build"
OUTPUT = FIGURES / "generated" / "research_problems"

PANELS = [
    ("research_problem_time", "有限观测下的连续运动歧义"),
    ("research_problem_space", "不完整观测下的空间归属"),
    ("research_problem_topology", "真实结构变化后的表征更新"),
    ("research_problem_response", "动作响应对初始状态的依赖"),
]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    for command in ["xelatex", "pdftoppm"]:
        if not shutil.which(command):
            raise SystemExit(f"Required local tool is missing: {command}")
    OUTPUT.mkdir(parents=True, exist_ok=True)
    records = []
    for stem, title in PANELS:
        build = WORK / stem
        build.mkdir(parents=True, exist_ok=True)
        source = build / "figure.tex"
        wrapper = WRAPPER.replace("连续动态世界模型研究框架", title).replace(
            "figures/research_framework.tex", f"figures/{stem}.tex"
        )
        source.write_text(wrapper)
        with (build / "build.log").open("w") as log:
            result = subprocess.run([
                "xelatex", "-halt-on-error", "-interaction=nonstopmode",
                "-file-line-error", f"-output-directory={build}", str(source),
            ], cwd=LATEX, stdout=log, stderr=subprocess.STDOUT)
        if result.returncode:
            raise SystemExit(f"Figure compilation failed: {build / 'build.log'}")
        shutil.copy2(build / "figure.pdf", OUTPUT / f"{stem}.pdf")
        for suffix, options in [("", []), ("-gray", ["-gray"])]:
            result = subprocess.run([
                "pdftoppm", "-singlefile", "-scale-to", "2200", "-png",
                *options, str(OUTPUT / f"{stem}.pdf"), str(OUTPUT / f"{stem}{suffix}"),
            ], check=True, capture_output=True, text=True)
            if "Syntax Error" in result.stderr:
                raise SystemExit(result.stderr[:1200])
        records.append({
            "title": title, "source": f"figures/{stem}.tex",
            "source_sha256": digest(FIGURES / f"{stem}.tex"),
            "pdf": f"{stem}.pdf", "pdf_sha256": digest(OUTPUT / f"{stem}.pdf"),
        })
    manifest = {
        "kind": "original editable qualitative problem illustrations",
        "shared_styles_sha256": digest(FIGURES / "research_problem_styles.tex"),
        "figures": records,
        "scope": [
            "Neither curve in the time illustration is a ground-truth trajectory or a method result.",
            "Space: co-moving objects remain distinct; the hatched face of A already existed before it became visible.",
            "Topology: the hatched cut faces are physically newborn boundaries; stable surface history can continue.",
            "Response: other conditions are held fixed; pale outlines are current reference positions and dashed outlines are conceptual futures.",
            "The expected representation capabilities are research objectives, not completed experiments or a prescribed network architecture.",
        ],
    }
    (OUTPUT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    print(f"Built four editable vector illustrations and grayscale proofs in {OUTPUT}")


if __name__ == "__main__":
    main()
