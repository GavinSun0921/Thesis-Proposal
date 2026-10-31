# Figure Manager

`manage_figures.py` checks the figure manifest and the TeX dependency graph, prints an inventory, and supports explicit, per-ID exports. Its default mode is read-only and requires only Python 3's standard library:

```sh
python3 -B latex/figures/scripts/manage_figures.py
python3 -B latex/figures/scripts/manage_figures.py --inventory
python3 -B latex/figures/scripts/manage_figures.py --list
```

`--check` verifies every declared source, output, preview, and asset directory; verifies `source_sha256`, `output_sha256`, and per-file `asset_sha256` fields when present; parses each active SVG and reports external resource references; and walks TeX inputs from `latex/main.tex`. TeX comments are stripped, and local `\foreach` lists are expanded when collecting graphic references. The check enforces 13 included manifest entries, confirms their outputs or in-report TikZ source are reachable, and fails if active figures still depend on paths outside the chapter-scoped figure tree. `--inventory` prints compact JSON and writes no files.

## Export

SVG exports require CairoSVG in the Python environment running the command and a discoverable system Cairo library. Route exports use that same Python interpreter. These dependencies are unnecessary for read-only checks and normal report builds, which use the saved PDFs.

Export is never implicit. Use one manifest ID, optionally with `--dry-run`:

```sh
python3 -B latex/figures/scripts/manage_figures.py --export ch01.reconstruction-timeline --dry-run
python3 -B latex/figures/scripts/manage_figures.py --export ch03.continuous-time-route
python3 -B latex/figures/scripts/manage_figures.py --export ch01.psvla-method
```

Only these backends are configured:

- The three Chapter 1 clean timeline SVGs use CairoSVG, matching their documented conversion.
- The four detailed Chapter 3 routes delegate to `export_route_diagrams.py` in a temporary copy of the source, exporter, and manifest. Only the resulting PDF is copied to the declared output, so the primary manifest is not rewritten.
- PS-VLA uses local XeLaTeX in a temporary directory with `ctex` and the report's `fontset=fandol` configuration. The source is compiled as-is; fonts and source text are not normalized.

The research framework and overall route preserve their documented macOS WebKit provenance. This CLI has no WebKit exporter, so their exports fail clearly instead of using CairoSVG. The world-model-loop PDF has no documented local renderer and is also not regenerated here. CoFuse4D is compiled as part of the main report with its adjacent assets; the spacecraft infographic has no editable source. These cases are intentionally unsupported until their original build paths are established.

An explicit export replaces only that figure's declared PDF. It does not render previews, download material, or update the manifest; the manifest owner must update any recorded hashes after reviewing an export. Export dependencies are loaded only for the selected backend. No export command is run by `--check`, `--inventory`, or `--list`.
