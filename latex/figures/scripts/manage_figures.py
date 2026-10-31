#!/usr/bin/env python3
"""Check, inventory, and explicitly export managed report figures."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[3]
LATEX = ROOT / "latex"
FIGURES = LATEX / "figures"
MANIFEST = FIGURES / "manifest.json"
EXPECTED_ACTIVE = 13
EXTENSIONS = (".pdf", ".png", ".jpg", ".jpeg", ".eps")
COMMAND = re.compile(r"\\([A-Za-z@]+)")
FOREACH = re.compile(r"\s*((?:\\[A-Za-z@]+)(?:\s*/\s*\\[A-Za-z@]+)*)\s+in\b")
CSS_URL = re.compile(r"url\(\s*(['\"]?)(.*?)\1\s*\)", re.IGNORECASE)
CSS_IMPORT = re.compile(r"@import\s+(['\"])(.*?)\1", re.IGNORECASE)
ROUTES = {
    "ch03.continuous-time-route", "ch03.object-consistency-route",
    "ch03.topology-change-route", "ch03.action-response-route",
}
CAIROSVG = {
    "ch01.reconstruction-timeline", "ch01.world-model-evolution",
    "ch01.action-learning-timeline",
}
WEBKIT = {"ch02.research-framework", "ch03.overall-technical-route"}
XELATEX = {"ch01.psvla-method"}


def repo_rel(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        return str(path)


def inside(path: Path, parent: Path) -> bool:
    try:
        path.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


def figure_path(value: str, label: str) -> Path:
    path = (FIGURES / value).resolve()
    if not inside(path, FIGURES):
        raise ValueError(f"{label} escapes figures root: {value}")
    return path


def load_manifest() -> dict:
    try:
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read {repo_rel(MANIFEST)}: {exc}") from exc
    if not isinstance(data, dict) or not isinstance(data.get("figures"), dict):
        raise ValueError("manifest must contain a figures object")
    expected_root = FIGURES.relative_to(ROOT).as_posix()
    if data.get("root") != expected_root:
        raise ValueError(f"manifest root is {data.get('root')!r}, expected {expected_root!r}")
    if any(not isinstance(value, dict) for value in data["figures"].values()):
        raise ValueError("every manifest figure entry must be an object")
    return data


def strip_comments(text: str) -> str:
    result = []
    for line in text.splitlines(keepends=True):
        out = []
        for char in line:
            if char == "%":
                slashes = 0
                for prev in reversed(out):
                    if prev != "\\":
                        break
                    slashes += 1
                if slashes % 2 == 0:
                    break
            out.append(char)
        result.append("".join(out))
    return "".join(result)


def skip_space(text: str, index: int) -> int:
    while index < len(text) and text[index].isspace():
        index += 1
    return index


def group(text: str, index: int, opening: str, closing: str):
    index = skip_space(text, index)
    if index >= len(text) or text[index] != opening:
        return None
    start, depth = index + 1, 1
    index += 1
    while index < len(text):
        char = text[index]
        if char in "{}[]":
            slashes, cursor = 0, index - 1
            while cursor >= 0 and text[cursor] == "\\":
                slashes += 1
                cursor -= 1
            if slashes % 2:
                index += 1
                continue
        if char == opening:
            depth += 1
        elif char == closing:
            depth -= 1
            if depth == 0:
                return text[start:index], index + 1
        index += 1
    return None


def split_top(value: str, delimiter: str) -> list[str]:
    result, start, depth = [], 0, 0
    for index, char in enumerate(value):
        if char == "{":
            depth += 1
        elif char == "}":
            depth = max(0, depth - 1)
        elif char == delimiter and depth == 0:
            if value[start:index].strip():
                result.append(value[start:index].strip())
            start = index + 1
    if value[start:].strip():
        result.append(value[start:].strip())
    return result


def substitute(text: str, values: dict[str, str]) -> str:
    for name, value in values.items():
        pattern = re.compile(r"(?<![A-Za-z@])\\" + re.escape(name) + r"(?![A-Za-z@])")
        text = pattern.sub(lambda _match, replacement=value: replacement, text)
    return text


def tex_references(text: str):
    inputs, graphics, issues = [], [], []

    def scan(segment: str, inherited: dict[str, str]) -> None:
        index = 0
        while index < len(segment):
            match = COMMAND.match(segment, index)
            if not match:
                index += 1
                continue
            command, after = match.group(1), match.end()
            if command == "foreach":
                declaration = FOREACH.match(segment, after)
                if not declaration:
                    issues.append("could not parse \\foreach declaration")
                    index = after
                    continue
                names = re.findall(r"\\([A-Za-z@]+)", declaration.group(1))
                values = group(segment, declaration.end(), "{", "}")
                body = group(segment, values[1], "{", "}") if values else None
                if not values or not body:
                    issues.append("could not parse \\foreach value list/body")
                    index = declaration.end()
                    continue
                for item in split_top(values[0], ","):
                    fields = [field.strip() for field in item.split("/")]
                    if len(fields) != len(names):
                        issues.append(f"\\foreach tuple has {len(fields)} values for {len(names)} variables")
                        continue
                    mapping = dict(inherited)
                    mapping.update(zip(names, fields))
                    scan(substitute(body[0], mapping), mapping)
                index = body[1]
                continue
            if command in {"input", "include", "subfile"}:
                parsed = group(segment, after, "{", "}")
                if parsed:
                    inputs.append(substitute(parsed[0].strip(), inherited).strip())
                    index = parsed[1]
                    continue
            if command == "includegraphics":
                cursor = skip_space(segment, after)
                if cursor < len(segment) and segment[cursor] == "*":
                    cursor = skip_space(segment, cursor + 1)
                if cursor < len(segment) and segment[cursor] == "[":
                    options = group(segment, cursor, "[", "]")
                    if options:
                        cursor = options[1]
                parsed = group(segment, cursor, "{", "}")
                if parsed:
                    graphics.append(substitute(parsed[0].strip(), inherited).strip())
                    index = parsed[1]
                    continue
            index = after

    scan(strip_comments(text), {})
    return inputs, graphics, issues


def resolve_tex(raw: str, current: Path, kind: str):
    if not raw or re.search(r"\\[A-Za-z@]+", raw):
        return None, f"unexpanded TeX command in {kind} path {raw!r}"
    requested = Path(raw)
    bases = [LATEX] if requested.is_absolute() else [LATEX, current.parent]
    suffixes = [""] if requested.suffix else ([".tex"] if kind == "input" else list(EXTENSIONS))
    candidates = []
    for base in bases:
        for suffix in suffixes:
            path = requested if requested.is_absolute() else base / requested
            if suffix:
                path = path.with_suffix(suffix)
            path = path.resolve()
            if path not in candidates:
                candidates.append(path)
    for path in candidates:
        if path.is_file():
            if not inside(path, ROOT):
                return None, f"{kind} resolves outside repository: {raw}"
            return path, None
    return None, f"missing {kind} reference {raw!r} from {repo_rel(current)}"


def walk_tex():
    errors, seen, inputs, graphics = [], set(), set(), set()
    pending = [LATEX / "main.tex"]
    while pending:
        current = pending.pop().resolve()
        if current in seen:
            continue
        seen.add(current)
        if not current.is_file():
            errors.append(f"missing TeX input {repo_rel(current)}")
            continue
        try:
            text = current.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"cannot read {repo_rel(current)}: {exc}")
            continue
        raw_inputs, raw_graphics, issues = tex_references(text)
        errors.extend(f"{repo_rel(current)}: {issue}" for issue in issues)
        for raw in raw_inputs:
            path, issue = resolve_tex(raw, current, "input")
            if issue:
                errors.append(issue)
            else:
                inputs.add(path)
                if inside(path, FIGURES):
                    local = path.relative_to(FIGURES.resolve())
                    if not local.parts or local.parts[0] != "chapters":
                        errors.append(f"active legacy TeX input: {repo_rel(path)}")
                if path.suffix.lower() == ".tex":
                    pending.append(path)
        for raw in raw_graphics:
            path, issue = resolve_tex(raw, current, "graphic")
            if issue:
                errors.append(issue)
            else:
                graphics.add(path)
    return seen, inputs, graphics, errors


def digest(path: Path) -> str:
    checksum = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            checksum.update(block)
    return checksum.hexdigest()


def external_svg_resources(path: Path) -> list[str]:
    try:
        root = ET.fromstring(path.read_bytes())
    except (OSError, ET.ParseError) as exc:
        return [f"cannot parse SVG {repo_rel(path)}: {exc}"]
    found = []

    def check(value: str, context: str) -> None:
        value = value.strip().strip("\"'")
        if value and not value.startswith("#") and not value.lower().startswith("data:"):
            found.append(f"{context}: {value}")

    resource_tags = {"image", "use", "feimage", "script", "link"}
    for element in root.iter():
        tag = element.tag.rsplit("}", 1)[-1].lower() if isinstance(element.tag, str) else ""
        for key, value in element.attrib.items():
            name = key.rsplit("}", 1)[-1].lower()
            context = f"{repo_rel(path)} <{tag}> @{name}"
            if name == "base":
                check(value, context)
            elif name == "href" and tag in resource_tags:
                check(value, context)
            for match in CSS_URL.finditer(value):
                check(match.group(2), context + " url()")
        if tag == "style" and element.text:
            for match in CSS_URL.finditer(element.text):
                check(match.group(2), f"{repo_rel(path)} <style> url()")
            for match in CSS_IMPORT.finditer(element.text):
                check(match.group(2), f"{repo_rel(path)} <style> @import")
    return found


def check_project():
    manifest = load_manifest()
    entries = manifest["figures"]
    active = {key: item for key, item in entries.items() if item.get("included") is True}
    errors = []
    if len(active) != EXPECTED_ACTIVE:
        errors.append(f"manifest has {len(active)} included figures; expected {EXPECTED_ACTIVE}")

    resolved, hashes_checked = {}, 0
    for figure_id, entry in entries.items():
        resolved[figure_id] = {}
        for field in ("source", "output", "preview", "assets"):
            value = entry.get(field)
            if value is None:
                continue
            if not isinstance(value, str):
                errors.append(f"{figure_id}: {field} must be a path string or null")
                continue
            try:
                path = figure_path(value, f"{figure_id}.{field}")
            except ValueError as exc:
                errors.append(str(exc))
                continue
            resolved[figure_id][field] = path
            exists = path.is_dir() if field == "assets" else path.is_file()
            if not exists:
                errors.append(f"{figure_id}: missing {field} path {repo_rel(path)}")
        for hash_field, path_field in (("source_sha256", "source"), ("output_sha256", "output")):
            expected = entry.get(hash_field)
            if expected is None:
                continue
            path = resolved[figure_id].get(path_field)
            if path is None or not path.is_file():
                errors.append(f"{figure_id}: {hash_field} set but {path_field} is unavailable")
                continue
            actual = digest(path)
            hashes_checked += 1
            if actual.lower() != str(expected).lower():
                errors.append(f"{figure_id}: {hash_field} mismatch for {repo_rel(path)}")

        asset_hashes = entry.get("asset_sha256", {})
        if not isinstance(asset_hashes, dict):
            errors.append(f"{figure_id}: asset_sha256 must be an object")
            continue
        asset_dir = resolved[figure_id].get("assets")
        for asset_name, expected in asset_hashes.items():
            try:
                asset_path = figure_path(asset_name, f"{figure_id}.asset_sha256")
            except ValueError as exc:
                errors.append(str(exc))
                continue
            if asset_dir is None or not inside(asset_path, asset_dir):
                errors.append(f"{figure_id}: asset hash is outside its assets directory: {asset_name}")
                continue
            if not asset_path.is_file():
                errors.append(f"{figure_id}: missing hashed asset {repo_rel(asset_path)}")
                continue
            actual = digest(asset_path)
            hashes_checked += 1
            if actual.lower() != str(expected).lower():
                errors.append(f"{figure_id}: asset_sha256 mismatch for {repo_rel(asset_path)}")

    tex_files, tex_inputs, graphics, graph_errors = walk_tex()
    errors.extend(graph_errors)
    outputs, asset_dirs = set(), set()
    for figure_id, entry in active.items():
        paths = resolved.get(figure_id, {})
        output, source, assets = paths.get("output"), paths.get("source"), paths.get("assets")
        if output:
            if output in outputs:
                errors.append(f"duplicate active output {repo_rel(output)}")
            outputs.add(output)
            if output not in graphics:
                errors.append(f"included output is not referenced from main.tex: {figure_id} ({repo_rel(output)})")
        elif source and source.suffix.lower() == ".tex" and source not in tex_inputs:
            errors.append(f"in-report TikZ source is not reachable from main.tex: {figure_id} ({repo_rel(source)})")
        if assets:
            asset_dirs.add(assets.resolve())

    legacy, unmanaged = [], []
    for path in graphics:
        if not inside(path, FIGURES):
            continue
        rel = path.resolve().relative_to(FIGURES.resolve())
        if not rel.parts or rel.parts[0] != "chapters":
            legacy.append(path)
        elif path not in outputs and not any(inside(path, directory) for directory in asset_dirs):
            unmanaged.append(path)
    errors.extend(f"active legacy graphic dependency: {repo_rel(path)}" for path in legacy)
    errors.extend(f"active graphic absent from manifest outputs/assets: {repo_rel(path)}" for path in unmanaged)

    svg_sources = []
    for figure_id in active:
        source = resolved.get(figure_id, {}).get("source")
        if source and source.suffix.lower() == ".svg":
            svg_sources.append(source)
            errors.extend(f"external SVG resource: {item}" for item in external_svg_resources(source))
    return {
        "manifest": manifest, "active": active, "tex_files": tex_files,
        "tex_inputs": tex_inputs, "graphics": graphics, "legacy": legacy,
        "hashes_checked": hashes_checked, "svg_sources": svg_sources, "errors": errors,
    }


def backend_for(figure_id: str) -> str:
    if figure_id in ROUTES:
        return "route exporter (isolated temporary manifest)"
    if figure_id in CAIROSVG:
        return "CairoSVG (documented timeline conversion)"
    if figure_id in WEBKIT:
        return "unsupported here; preserve macOS WebKit backend"
    if figure_id in XELATEX:
        return "XeLaTeX standalone, fontset=fandol"
    if figure_id == "ch01.world-model-loop":
        return "unsupported; existing renderer undocumented"
    if figure_id == "ch01.cofuse4d-method":
        return "unsupported standalone; included in main with assets"
    if figure_id == "ch01.spacecraft-maintenance":
        return "unsupported; raster-only source"
    return "unsupported; no backend configured"


def print_inventory(result) -> None:
    figures = []
    for figure_id, entry in result["manifest"]["figures"].items():
        figures.append({
            "id": figure_id, "included": bool(entry.get("included")),
            "chapter": entry.get("chapter"), "source": entry.get("source"),
            "assets": entry.get("assets"), "output": entry.get("output"),
            "backend": backend_for(figure_id),
        })
    payload = {
        "manifest": repo_rel(MANIFEST), "active_count": len(result["active"]),
        "active_graphic_count": len(result["graphics"]),
        "active_graphics": sorted(repo_rel(path) for path in result["graphics"]),
        "active_tex": sorted(repo_rel(path) for path in result["tex_files"]),
        "legacy_dependencies": sorted(repo_rel(path) for path in result["legacy"]),
        "hashes_checked": result["hashes_checked"], "figures": figures,
        "errors": result["errors"],
    }
    print(json.dumps(payload, ensure_ascii=False, separators=(",", ":")))


def atomic_install(source: Path, destination: Path) -> None:
    destination = destination.resolve()
    if not inside(destination, FIGURES):
        raise ValueError(f"refusing output outside figures root: {repo_rel(destination)}")
    if not destination.parent.is_dir():
        raise ValueError(f"output directory does not exist: {repo_rel(destination.parent)}")
    staged = None
    try:
        with tempfile.NamedTemporaryFile(prefix=f".{destination.name}.", suffix=".tmp", dir=destination.parent, delete=False) as handle:
            staged = Path(handle.name)
            with source.open("rb") as generated:
                shutil.copyfileobj(generated, handle)
        os.replace(staged, destination)
    finally:
        if staged is not None and staged.exists():
            staged.unlink()


def export_route(figure_id: str, entry: dict, output: Path) -> None:
    exporter = FIGURES / "scripts" / "export_route_diagrams.py"
    route_name = figure_id.split(".", 1)[1]
    source = figure_path(entry["source"], f"{figure_id}.source")
    if not exporter.is_file():
        raise ValueError(f"route exporter not found: {repo_rel(exporter)}")
    with tempfile.TemporaryDirectory(prefix="manage-figure-route-") as scratch:
        temp_figures = Path(scratch) / "latex" / "figures"
        temp_script = temp_figures / "scripts" / exporter.name
        temp_source = temp_figures / source.relative_to(FIGURES.resolve())
        temp_output = temp_figures / output.relative_to(FIGURES.resolve())
        temp_script.parent.mkdir(parents=True)
        temp_source.parent.mkdir(parents=True, exist_ok=True)
        temp_output.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(exporter, temp_script)
        shutil.copy2(MANIFEST, temp_figures / "manifest.json")
        shutil.copy2(source, temp_source)
        result = subprocess.run(
            [sys.executable, str(temp_script), "--only", route_name],
            text=True, capture_output=True, check=False,
        )
        if result.returncode:
            detail = (result.stderr or result.stdout).strip()
            raise ValueError(f"route exporter failed ({result.returncode}): {detail[-2000:]}")
        if not temp_output.is_file():
            raise ValueError("route exporter completed without its declared PDF")
        atomic_install(temp_output, output)


def export_psvla(entry: dict, output: Path) -> None:
    xelatex = shutil.which("xelatex")
    if not xelatex:
        raise ValueError("PS-VLA export requires local XeLaTeX with ctex/Fandol fonts")
    source = figure_path(entry["source"], "PS-VLA source")
    wrapper = r"""\documentclass[border=0pt]{standalone}
\usepackage[UTF8,fontset=fandol]{ctex}
\usepackage{xcolor}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,calc,positioning,fit,shapes.geometric}
\pagestyle{empty}
\begin{document}
\input{@SOURCE@}
\end{document}
""".replace("@SOURCE@", source.name)
    with tempfile.TemporaryDirectory(prefix="manage-figure-psvla-") as scratch:
        work = Path(scratch)
        shutil.copy2(source, work / source.name)
        tex = work / "standalone.tex"
        tex.write_text(wrapper, encoding="utf-8")
        result = subprocess.run([
            xelatex, "-no-shell-escape", "-halt-on-error", "-interaction=nonstopmode",
            f"-output-directory={work}", str(tex),
        ], cwd=LATEX, text=True, capture_output=True, check=False)
        generated = work / "standalone.pdf"
        if result.returncode or not generated.is_file():
            detail = (result.stderr or result.stdout).strip()
            raise ValueError(f"PS-VLA XeLaTeX export failed: {detail[-2500:]}")
        atomic_install(generated, output)


def run_export(figure_id: str, dry_run: bool) -> int:
    manifest = load_manifest()
    entry = manifest["figures"].get(figure_id)
    if not isinstance(entry, dict) or entry.get("included") is not True:
        raise ValueError(f"unknown or inactive figure ID: {figure_id}")
    if not isinstance(entry.get("source"), str) or not isinstance(entry.get("output"), str):
        raise ValueError(f"figure lacks standalone source/output: {figure_id}")
    source = figure_path(entry["source"], f"{figure_id}.source")
    output = figure_path(entry["output"], f"{figure_id}.output")
    if not source.is_file():
        raise ValueError(f"missing source: {repo_rel(source)}")
    if output.suffix.lower() != ".pdf" or source.resolve() == output.resolve():
        raise ValueError(f"unsafe source/output pair for {figure_id}")
    print(f"ID: {figure_id}\nBackend: {backend_for(figure_id)}\nSource: {repo_rel(source)}\nOutput: {repo_rel(output)}")
    if dry_run:
        print("Dry run: no files written.")
        return 0

    if figure_id in ROUTES:
        external = external_svg_resources(source)
        if external:
            raise ValueError("route SVG has external resource links: " + "; ".join(external))
        export_route(figure_id, entry, output)
    elif figure_id in CAIROSVG:
        external = external_svg_resources(source)
        if external:
            raise ValueError("SVG has external resource links: " + "; ".join(external))
        try:
            import cairosvg
        except (ImportError, OSError) as exc:
            raise ValueError(f"CairoSVG/Cairo required for documented export: {exc}") from exc
        with tempfile.TemporaryDirectory(prefix="manage-figure-svg-") as scratch:
            generated = Path(scratch) / "figure.pdf"
            cairosvg.svg2pdf(bytestring=source.read_bytes(), write_to=str(generated))
            if not generated.is_file():
                raise ValueError("CairoSVG completed without producing a PDF")
            atomic_install(generated, output)
    elif figure_id in XELATEX:
        export_psvla(entry, output)
    elif figure_id in WEBKIT:
        raise ValueError(
            "existing PDF uses the documented macOS WebKit backend; no WebKit exporter is configured, "
            "so CairoSVG was not used and no file changed"
        )
    elif figure_id == "ch01.world-model-loop":
        raise ValueError("existing PDF has no documented local renderer; refusing to guess a conversion")
    else:
        raise ValueError(f"no safe exporter configured for {figure_id}; no file changed")
    print("Exported declared PDF only; no preview or manifest was written.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    actions = parser.add_mutually_exclusive_group()
    actions.add_argument("--check", action="store_true", help="validate manifest and active TeX graph (default)")
    actions.add_argument("--inventory", action="store_true", help="print compact JSON without writing files")
    actions.add_argument("--list", action="store_true", help="list IDs and configured export backends")
    actions.add_argument("--export", metavar="ID", help="explicitly export one figure")
    parser.add_argument("--dry-run", action="store_true", help="show an export without writing")
    args = parser.parse_args()
    if args.dry_run and not args.export:
        parser.error("--dry-run requires --export ID")
    try:
        if args.export:
            return run_export(args.export, args.dry_run)
        manifest = load_manifest()
        if args.list:
            for figure_id, entry in manifest["figures"].items():
                print(f"{figure_id}\tincluded={str(bool(entry.get('included'))).lower()}\tbackend={backend_for(figure_id)}")
            return 0
        result = check_project()
        if args.inventory:
            print_inventory(result)
        elif result["errors"]:
            for error in result["errors"]:
                print(f"ERROR: {error}", file=sys.stderr)
        else:
            print(
                f"OK: {len(result['active'])} active figures; {len(result['graphics'])} unique active graphics; "
                f"{result['hashes_checked']} manifest hashes checked; no active dependency in legacy paths."
            )
        return 1 if result["errors"] else 0
    except (OSError, ValueError, KeyError, TypeError, subprocess.SubprocessError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
