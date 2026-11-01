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

Editable figure exports use one explicit font policy: Chinese text uses SimSun, Chinese headings use SimHei, Latin text and numbers use Times New Roman, and mathematical expressions use the report's default Computer Modern math fonts. Math is outlined in SVG so PDF output does not depend on a viewer's math-font fallback. The machine running the export must have the three text font families installed and fontconfig's `fc-match` available. Before writing a PDF, `figure_fonts.py` verifies that each requested family resolves to that family; missing fonts or a missing checker cause an explicit error instead of silent Cairo fallback.

Configured backends:

- Font-managed SVG figures use CairoSVG through `figure_fonts.py`, preserving the existing PDF page size when replacing it. The manager requires the saved PDF for these general SVG exports; if it is absent, restore it before exporting. Page dimensions are not yet stored separately in the manifest. The helper can take an explicit `page_size`; without one or an existing target PDF it uses the SVG canvas size. Chapter 3's four detailed route exports also validate their source geometry and label-font policy and preserve the saved PDF size when present.
- PS-VLA uses XeLaTeX with the adjacent standalone and font configuration files, matching the report's text and math fonts.

CoFuse4D is compiled as part of the main report with its adjacent assets. The spacecraft infographic is maintained in PowerPoint; the current PDF is used directly, with no managed PPTX-to-PDF export configured.

An explicit export replaces only that figure's declared PDF. It does not render previews, download material, or update the manifest; the manifest owner must update any recorded hashes after reviewing an export. Export dependencies are loaded only for the selected backend. No export command is run by `--check`, `--inventory`, or `--list`.
