#!/usr/bin/env python3
"""Build the editable research framework as a standalone vector PDF and PNG.

Uses local MacTeX/XeLaTeX; previews use pdftoppm, falling back to Ghostscript
when it is absent. The proposal and its current PDF are left in place. Run from
any directory; only Python's standard library is used.
"""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

FIGURES = Path(__file__).resolve().parent
LATEX = FIGURES.parent
ROOT = LATEX.parent
WORK = ROOT / "tmp" / "research-framework-build"
OUTPUT = FIGURES / "generated" / "research_framework"

WRAPPER = r"""\documentclass[border=3mm]{standalone}
\usepackage[UTF8,fontset=fandol]{ctex}
\usepackage{amsmath}
\usepackage{tikz}
\usepackage{float}
\usepackage{subcaption}
\captionsetup[subfigure]{font=small,labelformat=parens,labelsep=space,skip=2pt,justification=centering}
% Same panel-label fonts as the ones declared in the report preamble, so the
% standalone exports match the in-report figures exactly.
\DeclareCaptionFont{figsubheiti}{\heiti\fontsize{9.6pt}{12pt}\selectfont}
\DeclareCaptionFont{figsubsongti}{\songti\fontsize{9.4pt}{11.5pt}\selectfont}
\DeclareCaptionFont{figsublittitle}{\heiti\fontsize{10.2pt}{12.5pt}\selectfont}
\DeclareCaptionFont{figsubroute}{\songti\fontsize{9.2pt}{11.2pt}\selectfont}
\usetikzlibrary{arrows.meta,calc}
\IfFontExistsTF{Times New Roman}{\setmainfont{Times New Roman}}{%
  \setmainfont{texgyretermes-regular.otf}[
    BoldFont=texgyretermes-bold.otf,
    ItalicFont=texgyretermes-italic.otf,
    BoldItalicFont=texgyretermes-bolditalic.otf]}
\IfFontExistsTF{SimSun}{%
  \setCJKmainfont{SimSun}[AutoFakeBold=2]
  \setCJKfamilyfont{zhsong}{SimSun}[AutoFakeBold=2]
}{\IfFontExistsTF{Songti SC}{%
  \setCJKmainfont{Songti SC}[AutoFakeBold=2]
  \setCJKfamilyfont{zhsong}{Songti SC}[AutoFakeBold=2]
}{}}
\IfFontExistsTF{SimHei}{\setCJKfamilyfont{zhhei}{SimHei}[AutoFakeBold=2]}{%
  \IfFontExistsTF{Heiti SC}{\setCJKfamilyfont{zhhei}{Heiti SC}[AutoFakeBold=2]}{}}
\usepackage[unicode,hidelinks]{hyperref}
\hypersetup{pdftitle={连续动态世界模型研究框架},pdfauthor={}}
\begin{document}
% standalone sets its content in LR mode, where floats are unavailable, so wrap
% the figure in a paragraph box to give \subcaption the float context it needs.
% The box is as wide as the drawing itself (16cm canvas in every figure source),
% so the exported page keeps the figure's natural width.
\begin{minipage}{16cm}
\begin{figure}[H]
\centering
\input{figures/research_framework.tex}
\end{figure}
\end{minipage}
\end{document}
"""


def main() -> None:
    if not shutil.which("xelatex"):
        raise SystemExit("Required local tool is missing: xelatex")
    if shutil.which("pdftoppm"):
        previewer = "pdftoppm"
    elif shutil.which("gs"):
        previewer = "gs"
    else:
        raise SystemExit("Required preview tool is missing: pdftoppm or gs")
    WORK.mkdir(parents=True, exist_ok=True)
    OUTPUT.mkdir(parents=True, exist_ok=True)
    source = WORK / "research-framework.tex"
    # Keep the shared float/minipage wrapper unchanged for the other figure
    # builders. This overview has no subfigures and exports at its natural size.
    framework_wrapper = WRAPPER.replace("border=3mm", "border=1mm")
    framework_wrapper = framework_wrapper.split(r"\begin{document}", 1)[0] + r"""\begin{document}
\input{figures/research_framework.tex}
\end{document}
"""
    source.write_text(framework_wrapper)
    with (WORK / "build.log").open("w") as log:
        result = subprocess.run([
            "xelatex", "-halt-on-error", "-interaction=nonstopmode",
            "-file-line-error", f"-output-directory={WORK}", str(source),
        ], cwd=LATEX, stdout=log, stderr=subprocess.STDOUT)
    if result.returncode:
        raise SystemExit(f"XeLaTeX failed; inspect {WORK / 'build.log'}")
    shutil.copy2(WORK / "research-framework.pdf", OUTPUT / "figure.pdf")
    for name, gray in [("figure", False), ("figure-gray", True)]:
        if previewer == "pdftoppm":
            preview = subprocess.run([
                "pdftoppm", "-singlefile", "-scale-to", "2400", "-png",
                *(["-gray"] if gray else []),
                str(OUTPUT / "figure.pdf"), str(OUTPUT / name),
            ], check=True, capture_output=True, text=True)
            if "Syntax Error" in preview.stderr:
                raise SystemExit(f"PDF preview reported an error: {preview.stderr[:1200]}")
        else:
            subprocess.run([
                "gs", "-q", "-dNOPAUSE", "-dBATCH",
                f"-sDEVICE={'pnggray' if gray else 'png16m'}", "-r386",
                "-dFirstPage=1", "-dLastPage=1",
                f"-sOutputFile={OUTPUT / (name + '.png')}",
                str(OUTPUT / "figure.pdf"),
            ], check=True)
    print(f"Built editable vector framework, color preview and grayscale proof in {OUTPUT}")


if __name__ == "__main__":
    main()
