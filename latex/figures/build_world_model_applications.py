#!/usr/bin/env python3
"""Build a source-backed photo composition with vector labels and print proofs."""
from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
from pathlib import Path

from build_research_framework import WRAPPER

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
WORK = ROOT / "tmp" / "world-model-applications-build"
OUT = HERE / "generated" / "world_model_applications"
TITLE = "世界模型支撑的典型应用场景示意"


def main() -> None:
    WORK.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)
    wrapper = WRAPPER.replace("连续动态世界模型研究框架", TITLE).replace(
        "figures/research_framework.tex", "figures/world_model_applications.tex"
    )
    tex = WORK / "world-model-applications.tex"
    tex.write_text(wrapper)
    with (WORK / "build.log").open("w") as log:
        subprocess.run([
            "xelatex", "-halt-on-error", "-interaction=nonstopmode",
            "-file-line-error", f"-output-directory={WORK}", str(tex),
        ], cwd=HERE.parent, stdout=log, stderr=subprocess.STDOUT, check=True)
    shutil.copy2(tex.with_suffix(".pdf"), OUT / "figure.pdf")
    for name, gray in [("figure", False), ("figure-gray", True)]:
        subprocess.run([
            "pdftoppm", "-singlefile", "-scale-to", "2400", "-png",
            *(["-gray"] if gray else []),
            str(OUT / "figure.pdf"), str(OUT / name),
        ], check=True, capture_output=True)
    source = HERE / "world_model_applications.tex"
    (OUT / "manifest.json").write_text(json.dumps({
        "title": TITLE,
        "source": source.name,
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "provenance": "Original TikZ composition using credited NASA photographs.",
        "materials": json.loads((HERE / "materials" / "world_model_applications" /
                                 "source-manifest.json").read_text()),
        "scope": "Illustrative application needs, not experimental results or a method architecture.",
    }, ensure_ascii=False, indent=2) + "\n")
    print(f"Built vector illustration and color/grayscale proofs in {OUT}")


if __name__ == "__main__":
    main()
