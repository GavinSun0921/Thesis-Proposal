#!/usr/bin/env python3
"""Prepare traceable literature panels and render the three editable 1.2 figures.

Default: verify the checked-in source panels, rebuild crops and previews.
--download: recover panels from the authors' public media and PointWorld PDF.
Only recovery needs pypdf and PyAV; normal use needs Pillow and local MacTeX.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
LATEX = HERE.parent
ROOT = LATEX.parent
MATERIALS = HERE / "materials" / "literature_review"
OUTPUT = HERE / "generated" / "literature_review"
WORK = ROOT / "tmp" / "literature-figures-build"

REMOTE = {
    "som_input_video": ("som_bear_input.mp4", "https://shape-of-motion.github.io/static/videos/bear_input.mp4"),
    "som_tracks_video": ("som_bear_tracks.mp4", "https://shape-of-motion.github.io/static/videos/bear-tracks.mp4"),
    "som_novel": ("som_bear_novel.jpg", "https://shape-of-motion.github.io/static/images/bear.jpg"),
    "retime_t0": ("retime_core_66.png", "https://william-wang2.github.io/RetimeGS/static/images/core_idea/ours/interp_0066.png"),
    "retime_mid": ("retime_core_69.png", "https://william-wang2.github.io/RetimeGS/static/images/core_idea/ours/interp_0069.png"),
    "retime_t1": ("retime_core_72.png", "https://william-wang2.github.io/RetimeGS/static/images/core_idea/ours/interp_0072.png"),
    "point_paper": ("pointworld.pdf", "https://arxiv.org/pdf/2601.03782"),
    "openvla_teaser": ("openvla_teaser.jpg", "https://openvla.github.io/static/images/openvla_teaser.jpg"),
    "dreamzero_overview": ("dreamzero_overview.png", "https://dreamzero0.github.io/images/project_overview.png"),
}

PANELS = [
    {"name": "som_observation", "raw": "som_observation.png", "source": "som_input_video", "frame": 40, "crop": [0, 40, 720, 472], "aspect": [5, 3], "role": "observed input video, representative frame"},
    {"name": "som_tracks", "raw": "som_tracks.png", "source": "som_tracks_video", "frame": 40, "crop": [200, 32, 848, 422], "aspect": [5, 3], "role": "author-rendered persistent 3D tracks"},
    {"name": "som_novel_view", "raw": "som_novel_view.jpg", "source": "som_novel", "crop": [0, 95, 2346, 1502], "aspect": [5, 3], "role": "author-provided novel-view reconstruction poster, same bear case"},
    *[{"name": f"retime_{phase}", "raw": f"retime_{phase}.png", "source": f"retime_{phase}", "crop": [200, 200, 920, 740], "aspect": [4, 3], "role": role} for phase, role in [
        ("t0", "sampling endpoint of the source interpolation demo"),
        ("mid", "model interpolation at the midpoint of the same observed interval"),
        ("t1", "sampling endpoint of the same interpolation demo"),
    ]],
    {"name": "point_observation_v1", "raw": "point_observation_v1.jpg", "source": "point_paper", "pdf_page": 33, "figure": 16, "xobject": "Image10.jpg", "aspect": [16, 9], "role": "first DROID cloth case, input RGB view 1"},
    {"name": "point_observation_v2", "raw": "point_observation_v2.jpg", "source": "point_paper", "pdf_page": 33, "figure": 16, "xobject": "Image11.jpg", "aspect": [16, 9], "role": "same case and initial instant, input RGB view 2"},
    {"name": "point_prediction_1s", "raw": "point_prediction_1s.jpg", "source": "point_paper", "pdf_page": 33, "figure": 16, "xobject": "Image8.jpg", "aspect": [1, 1], "role": "same case, model-predicted 3D point flow at 1.0 s"},
    {"name": "point_reference_1s", "raw": "point_reference_1s.jpg", "source": "point_paper", "pdf_page": 33, "figure": 16, "xobject": "Image9.jpg", "aspect": [1, 1], "role": "same case and 1.0 s horizon, author-provided GT annotation"},
    {"name": "openvla_scene", "raw": "openvla_teaser.jpg", "source": "openvla_teaser", "crop": [668, 385, 1000, 607], "aspect": [3, 2], "role": "Franka scene example from the official teaser, not a future prediction"},
    {"name": "dreamzero_scene", "raw": "dreamzero_overview.png", "source": "dreamzero_overview", "crop": [816, 340, 975, 426], "aspect": [3, 2], "role": "bimanual scene example from the official overview, not labeled as a predicted video frame"},
]

FIGURES = [
    ("literature_reconstruction", "动态场景重建的代表性结果"),
    ("literature_prediction", "动作条件下的三维场景预测"),
    ("literature_action_paradigms", "具身操作的典型建模范式"),
]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def recover_sources(cache: Path, decoder_path: Path | None) -> None:
    if decoder_path:
        sys.path.insert(0, str(decoder_path.resolve()))
    import av
    from pypdf import PdfReader

    cache.mkdir(parents=True, exist_ok=True)
    MATERIALS.mkdir(parents=True, exist_ok=True)
    old = json.loads((MATERIALS / "source-manifest.json").read_text()) if (MATERIALS / "source-manifest.json").exists() else None

    def fetch(item: tuple[str, tuple[str, str]]) -> tuple[str, dict]:
        key, (filename, url) = item
        path = cache / filename
        if not path.exists():
            with urllib.request.urlopen(url, timeout=60) as response:
                path.write_bytes(response.read())
        record = {"url": url, "sha256": digest(path), "bytes": path.stat().st_size}
        if old and old["sources"][key]["sha256"] != record["sha256"]:
            raise ValueError(f"Source bytes changed; inspect before replacing the record: {key}")
        return key, record

    with ThreadPoolExecutor(max_workers=5) as pool:
        sources = dict(pool.map(fetch, REMOTE.items()))
    paper = PdfReader(cache / REMOTE["point_paper"][0])
    records = []
    for panel in PANELS:
        target = MATERIALS / panel["raw"]
        source = cache / REMOTE[panel["source"]][0]
        record = dict(panel)
        if "frame" in panel:
            with av.open(str(source)) as container:
                stream = container.streams.video[0]
                record.update(fps=str(stream.average_rate), source_frame_count=stream.frames, decoder=f"PyAV {av.__version__}")
                for index, frame in enumerate(container.decode(stream)):
                    if index == panel["frame"]:
                        frame.to_image().save(target)
                        break
                else:
                    raise ValueError(f"Missing source video frame: {panel['name']}")
        elif "xobject" in panel:
            image = next(image for image in paper.pages[panel["pdf_page"] - 1].images if image.name == panel["xobject"])
            target.write_bytes(image.data)
        else:
            shutil.copy2(source, target)
        with Image.open(target) as image:
            record["raw_size_px"] = list(image.size)
        record["raw_sha256"] = digest(target)
        if old:
            previous = next(item for item in old["panels"] if item["name"] == panel["name"])
            if previous["raw_sha256"] != record["raw_sha256"]:
                raise ValueError(f"Extracted panel changed: {panel['name']}")
        records.append(record)
    manifest = {
        "retrieved_date": "2026-10-26", "sources": sources, "panels": records,
        "projects": {
            "Shape of Motion": "https://shape-of-motion.github.io/",
            "RetimeGS": "https://william-wang2.github.io/RetimeGS/",
            "PointWorld": "https://point-world.github.io/",
            "OpenVLA": "https://openvla.github.io/",
            "DreamZero": "https://dreamzero0.github.io/",
        },
        "scope": [
            "Shape of Motion panels are qualitative views of the same bear episode; they are not a synchronized camera or tracking-accuracy benchmark.",
            "RetimeGS panels 66, 69 and 72 belong to one seven-frame interpolation demo. Endpoints are labeled by sampling time; the midpoint is interpolation, not future extrapolation.",
            "PointWorld panels are Fig. 16, physical page 33, first DROID cloth episode. Predicted and reference panels share the 1.0 s horizon and author view; robot flow is a given action condition.",
            "PointWorld GT green points mark occlusion-affected reference annotations; no annotation is corrected or replaced here.",
            "OpenVLA, PointWorld and DreamZero scene thumbnails illustrate independent examples. The adjacent input/output arrows are our conceptual summary, not an experimental comparison or a copied model architecture.",
            "Processing is limited to recorded 2D crops, white padding and JPEG encoding. No geometry, trajectory, action or future frame is synthesized.",
        ],
    }
    (MATERIALS / "source-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")


def make_panels() -> None:
    manifest = json.loads((MATERIALS / "source-manifest.json").read_text())
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for panel in manifest["panels"]:
        source = MATERIALS / panel["raw"]
        if digest(source) != panel["raw_sha256"]:
            raise ValueError(f"Checked-in source panel changed: {source}")
        image = Image.open(source).convert("RGB")
        if panel.get("crop"):
            image = image.crop(tuple(panel["crop"]))
        numerator, denominator = panel["aspect"]
        width, height = image.size
        out_width = max(width, (height * numerator + denominator - 1) // denominator)
        out_height = max(height, (width * denominator + numerator - 1) // numerator)
        canvas = Image.new("RGB", (out_width, out_height), "white")
        canvas.paste(image, ((out_width - width) // 2, (out_height - height) // 2))
        dest = OUTPUT / f"{panel['name']}.jpg"
        canvas.save(dest, quality=96, subsampling=0, optimize=True)
        panel["processed_size_px"] = list(canvas.size)
        panel["processed_sha256"] = digest(dest)
    (OUTPUT / "panel-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")


def previews() -> None:
    from build_research_framework import WRAPPER

    for stem, title in FIGURES:
        build = WORK / stem
        build.mkdir(parents=True, exist_ok=True)
        tex = build / "figure.tex"
        wrapper = WRAPPER.replace("连续动态世界模型研究框架", title).replace("figures/research_framework.tex", f"figures/{stem}.tex")
        tex.write_text(wrapper)
        with (build / "build.log").open("w") as log:
            result = subprocess.run(["xelatex", "-halt-on-error", "-interaction=nonstopmode", "-file-line-error", f"-output-directory={build}", str(tex)], cwd=LATEX, stdout=log, stderr=subprocess.STDOUT)
        if result.returncode:
            raise SystemExit(f"Figure compilation failed; inspect {build / 'build.log'}")
        shutil.copy2(build / "figure.pdf", OUTPUT / f"{stem}.pdf")
        for suffix, options in [("", []), ("-gray", ["-gray"])]:
            rendered = subprocess.run(["pdftoppm", "-singlefile", "-scale-to", "2200", "-png", *options, str(OUTPUT / f"{stem}.pdf"), str(OUTPUT / f"{stem}{suffix}")], check=True, capture_output=True, text=True)
            if "Syntax Error" in rendered.stderr:
                raise SystemExit(rendered.stderr[:1200])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--download", action="store_true")
    parser.add_argument("--source-cache", type=Path, default=ROOT / "tmp" / "literature-source-cache")
    parser.add_argument("--decoder-path", type=Path)
    parser.add_argument("--panels-only", action="store_true")
    args = parser.parse_args()
    if args.download:
        recover_sources(args.source_cache, args.decoder_path)
    make_panels()
    if not args.panels_only:
        previews()
    print(f"Verified literature panels and figures in {OUTPUT}")


if __name__ == "__main__":
    main()
