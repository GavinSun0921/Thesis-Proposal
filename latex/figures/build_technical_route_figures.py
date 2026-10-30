#!/usr/bin/env python3
"""Export the five editable technical-route diagrams with local MacTeX.

Exports vector PDFs, colour PNG previews, grayscale proofs and a source
manifest.  The diagrams show proposed mechanisms; they contain no experiment
results.

The overview was redrawn from the confirmed 2026-10-29 v2 preview.  The four
detailed route figures were redrawn on 2026-10-30 from the reviewed v3
mechanism previews, compacted to a natural 15.56 cm width and integrated in
Section 3.2.  Pass one or more ``--only`` stems to export a subset, for
example::

    python3 latex/figures/build_technical_route_figures.py --only technical_route_time
"""
from __future__ import annotations

import argparse
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

# stem, caption, status, note
PANELS = [
    (
        "technical_route_overview",
        "连续动态世界模型总体技术路线",
        "redrawn",
        "Redrawn 2026-10-29 from the confirmed v2 preview; five-component formula, offline prediction evaluation and recorded-observation updates; application experiment commitments removed 2026-10-30.",
    ),
    (
        "technical_route_time",
        "不确定性感知的连续时间场景表征技术路线",
        "integrated",
        "Redrawn 2026-10-30 from the v3 mechanism preview: compact three-stage evidence/support/joint-solve route with symbolic observation input (Omega_k, Pi), both residual and shared-constraint inputs, and a two-line output strip.",
    ),
    (
        "technical_route_space",
        "连续运动引导的空间结构表征技术路线",
        "integrated",
        "Redrawn 2026-10-30: compact cross-time membership and shared-range panels with the joint motion-geometry-membership recovery.",
    ),
    (
        "technical_route_topology",
        "物理连接变化下的连续动态场景表征技术路线",
        "integrated",
        "Redrawn 2026-10-30: one split event, local connection/surface update and separate material-motion and surface-existence histories.",
    ),
    (
        "technical_route_response",
        "基于连续动态表征的动作后果预测技术路线",
        "integrated",
        "Redrawn 2026-10-30: typed relation propagation, learned dynamics with stepwise integration, offline prediction evaluation and subsequent recorded-observation correction.",
    ),
]

# All five figures use the report's natural drawing width. The type is not
# scaled with the exported page box.
PAGE_WIDTHS = {
    "technical_route_overview": 15.56,
    "technical_route_time": 15.56,
    "technical_route_space": 15.56,
    "technical_route_topology": 15.56,
    "technical_route_response": 15.56,
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def page_size_cm(path: Path) -> tuple[float, float]:
    """Return the standalone PDF page size in centimetres."""
    info = subprocess.run(
        ["pdfinfo", str(path)], check=True, capture_output=True, text=True
    ).stdout
    line = next(
        (row for row in info.splitlines() if row.startswith("Page size:")), ""
    )
    fields = line.replace("Page size:", "").split()
    if len(fields) < 3:
        raise SystemExit(f"Cannot read page size from {path}: {line!r}")
    return round(float(fields[0]) / 72 * 2.54, 2), round(
        float(fields[2]) / 72 * 2.54, 2
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--only",
        action="append",
        choices=[stem for stem, _, _, _ in PANELS],
        help="export only the named stem; may be repeated",
    )
    args = parser.parse_args()

    for name in ("xelatex", "pdftoppm", "pdfinfo"):
        if not shutil.which(name):
            raise SystemExit(f"Required local tool is missing: {name}")

    selected = [
        panel for panel in PANELS if not args.only or panel[0] in set(args.only)
    ]
    OUTPUT.mkdir(parents=True, exist_ok=True)
    records = []
    for stem, title, status, note in selected:
        work = WORK / stem
        work.mkdir(parents=True, exist_ok=True)
        wrapper = WRAPPER.replace(
            "\\usepackage{amsmath}", "\\usepackage{amsmath,amssymb}"
        )
        wrapper = wrapper.replace("连续动态世界模型研究框架", title)
        wrapper = wrapper.replace(
            "figures/research_framework.tex", f"figures/{stem}.tex"
        )
        width = PAGE_WIDTHS[stem]
        if stem == "technical_route_overview":
            wrapper = wrapper.replace(
                r"\begin{minipage}{16cm}", rf"\begin{{minipage}}{{{width}cm}}"
            )
            source_text = wrapper
        else:
            # A tight standalone box: no float and no line-end spaces, so the
            # exported page is exactly the 15.56 cm drawing plus its 1 mm border.
            wrapper = wrapper.replace("border=3mm", "border=1mm")
            preamble = wrapper.split(r"\begin{document}", 1)[0]
            source_text = preamble + rf"""\begin{{document}}%
\begin{{minipage}}{{{width}cm}}%
\input{{figures/{stem}.tex}}%
\end{{minipage}}%
\end{{document}}
"""
        source = work / "figure.tex"
        source.write_text(source_text)
        with (work / "build.log").open("w") as log:
            result = subprocess.run(
                [
                    "xelatex",
                    "-halt-on-error",
                    "-interaction=nonstopmode",
                    "-file-line-error",
                    f"-output-directory={work}",
                    str(source),
                ],
                cwd=LATEX,
                stdout=log,
                stderr=subprocess.STDOUT,
            )
        if result.returncode:
            raise SystemExit(f"Figure compilation failed: {work / 'build.log'}")
        shutil.copy2(work / "figure.pdf", OUTPUT / f"{stem}.pdf")
        for suffix, options in (("", []), ("-gray", ["-gray"])):
            result = subprocess.run(
                [
                    "pdftoppm",
                    "-singlefile",
                    "-scale-to",
                    "2400",
                    "-png",
                    *options,
                    str(OUTPUT / f"{stem}.pdf"),
                    str(OUTPUT / f"{stem}{suffix}"),
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            if "Syntax Error" in result.stderr:
                raise SystemExit(result.stderr[:1000])
        width_cm, height_cm = page_size_cm(OUTPUT / f"{stem}.pdf")
        records.append(
            {
                "title": title,
                "status": status,
                "note": note,
                "source": f"figures/{stem}.tex",
                "source_sha256": digest(FIGURES / f"{stem}.tex"),
                "pdf": f"{stem}.pdf",
                "pdf_sha256": digest(OUTPUT / f"{stem}.pdf"),
                "page_width_cm": width_cm,
                "page_height_cm": height_cm,
                "png": f"{stem}.png",
                "png_gray": f"{stem}-gray.png",
            }
        )

    # Keep records for figures that were not selected in this run, so a partial
    # export does not silently drop them from the manifest.
    manifest_path = OUTPUT / "manifest.json"
    if args.only and manifest_path.exists():
        old = json.loads(manifest_path.read_text())
        by_title = {record["title"]: record for record in old.get("figures", [])}
        for stem, title, status, note in PANELS:
            if stem not in {record["source"].split("/")[-1][:-4] for record in records}:
                if title in by_title:
                    records.append(by_title[title])
    order = {title: index for index, (_, title, _, _) in enumerate(PANELS)}
    records.sort(key=lambda record: order.get(record["title"], 99))

    manifest = {
        "kind": "proposed technical routes, editable vector diagrams",
        "shared_styles_sha256": digest(FIGURES / "technical_route_styles.tex"),
        "typography_source": "figures/technical_route_styles.tex",
        "style_review": "2026-10-30: shared type hierarchy, natural-width text, equal peer panels and unobstructed connector labels.",
        "figures": records,
        "scope": [
            "The overall route is the 2026-10-29 redraw; the four detailed routes were compacted and integrated on 2026-10-30 from the reviewed v3 mechanism previews.",
            "Filled numbered markers or dark header bands indicate stages that carry the study's own mechanism, not originality or validated performance.",
            "Muted blue, green, ochre and violet identify the four studies; local colours distinguish trajectories, parts, connection validity, histories and actions. Body text is black; headers and frames use the corresponding theme.",
            "Local colours are paired with line styles, node shapes, interval markers or labels for grayscale reading.",
            "Explanatory legends and complete-sentence notes belong to the adjacent method prose; figures retain module, variable, interval and necessary relation labels.",
            "The integrated prediction mode uses observations and action history available by t0 only; subsequent recorded observations update only later prediction starts; evaluation uses public sequences.",
            "Material connection, spatial proximity and action effect are distinct relations; association edges and membership-derived shared weights are not physical connections.",
            "Surface history is distinct from material-motion history and from first visibility; a new boundary has no pre-formation surface history.",
        ],
    }
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"
    )
    print(
        f"Built {len(selected)} technical-route diagram(s), colour and grayscale "
        f"previews in {OUTPUT}"
    )


if __name__ == "__main__":
    main()
