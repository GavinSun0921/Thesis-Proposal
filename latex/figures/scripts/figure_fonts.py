"""Shared, explicit typography for the proposal's editable SVG figures.

Ordinary text remains editable. Each language run has its own embedded font;
positions are measured together so mixed Chinese/Latin labels stay anchored.
Inline formula outlines use the same Computer Modern math as the report.
"""
from __future__ import annotations

import copy
import hashlib
import itertools
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import xml.etree.ElementTree as ET

SVG = 'http://www.w3.org/2000/svg'
XLINK = 'http://www.w3.org/1999/xlink'
ET.register_namespace('', SVG)
ET.register_namespace('xlink', XLINK)
ROOT = Path(__file__).resolve().parents[3]
CACHE = ROOT / 'tmp' / 'figure-math-cache'
SERIAL = itertools.count()
FONT_POLICY = {'chinese': 'SimSun', 'heading': 'SimHei', 'western': 'Times New Roman', 'math': 'Computer Modern'}


def tag(name):
    return '{' + SVG + '}' + name


def number(value, default=0.0):
    if value is None:
        return default
    return float(re.search(r'[-+]?\d*\.?\d+', str(value)).group())


def is_chinese(char):
    cp = ord(char)
    return (0x2E80 <= cp <= 0xA4CF or 0xAC00 <= cp <= 0xD7AF or
            0xF900 <= cp <= 0xFAFF or 0xFE10 <= cp <= 0xFE6F or
            0xFF01 <= cp <= 0xFFEF or 0x20000 <= cp <= 0x3134F)


def font_runs(text, heading=False):
    for chinese, chars in itertools.groupby(text, key=is_chinese):
        yield ''.join(chars), FONT_POLICY['heading' if heading else 'chinese'] if chinese else FONT_POLICY['western']


def text_width(text, size, family, weight='400', style='normal', letter_spacing=0):
    import cairocffi as cairo
    context = cairo.Context(cairo.SVGSurface(None, 1, 1))
    bold = str(weight) in {'bold', 'bolder'} or (str(weight).isdigit() and int(weight) >= 550)
    slant = cairo.FONT_SLANT_ITALIC if style in {'italic', 'oblique'} else cairo.FONT_SLANT_NORMAL
    # SimHei has its own heavy strokes. Avoid artificial emboldening of CJK.
    context.select_font_face(family, slant, cairo.FONT_WEIGHT_BOLD if bold and family == FONT_POLICY['western'] else cairo.FONT_WEIGHT_NORMAL)
    context.set_font_size(size)
    return sum(context.text_extents(char)[4] for char in text) + max(0, len(text)-1)*letter_spacing


def _formula_asset(latex):
    key = hashlib.sha256(latex.encode()).hexdigest()[:20]
    CACHE.mkdir(parents=True, exist_ok=True)
    svg, metrics = CACHE / (key + '.svg'), CACHE / (key + '.json')
    if not svg.exists() or not metrics.exists():
        with tempfile.TemporaryDirectory(prefix='formula-', dir=CACHE) as temp:
            work = Path(temp)
            source = r'''\documentclass[border=0pt]{standalone}
\usepackage{amsmath,amssymb}
\newsavebox{\formulabox}
\begin{document}%
\sbox{\formulabox}{$@LATEX@$}%
\typeout{METRICS:\the\wd\formulabox;\the\ht\formulabox;\the\dp\formulabox}%
\usebox{\formulabox}%
\end{document}
'''.replace('@LATEX@', latex)
            (work / 'formula.tex').write_text(source)
            for args in [
                ['latex', '-no-shell-escape', '-halt-on-error', '-interaction=batchmode', 'formula.tex'],
                ['dvisvgm', '--no-fonts', '--bbox=papersize', '--output=formula.svg', 'formula.dvi'],
            ]:
                result = subprocess.run(args, cwd=work, text=True, capture_output=True)
                if result.returncode:
                    raise RuntimeError('Formula export failed: ' + ' '.join(args) + '\n' + result.stdout[-1500:] + result.stderr[-1500:])
            log = (work / 'formula.log').read_text()
            match = re.search(r'METRICS:([\d.]+)pt;([\d.]+)pt;([\d.]+)pt', log)
            if not match:
                raise RuntimeError('Missing formula dimensions')
            data = dict(zip(['width', 'height', 'depth'], map(float, match.groups())))
            shutil.copy2(work / 'formula.svg', svg)
            metrics.write_text(json.dumps(data))
    return ET.parse(svg).getroot(), json.loads(metrics.read_text())


def math_group(latex, *, x=0, y=0, font_size=32, fill='#000000', anchor='start'):
    """Return an SVG group at a baseline, plus its advance width in user units."""
    asset, metrics = _formula_asset(latex)
    scale = font_size / 10.0
    width = metrics['width'] * scale
    height = (metrics['height'] + metrics['depth']) * scale
    start = x - (width / 2 if anchor == 'middle' else width if anchor == 'end' else 0)
    group = ET.Element(tag('g'), {'data-latex': latex, 'data-math-font': FONT_POLICY['math'],
                                  'data-font-size': str(font_size), 'fill': fill})
    asset = copy.deepcopy(asset)
    prefix = 'math-' + hashlib.sha256(latex.encode()).hexdigest()[:10] + '-' + str(next(SERIAL)) + '-'
    ids = {el.get('id'): prefix + el.get('id') for el in asset.iter() if el.get('id')}
    for el in asset.iter():
        for key, value in list(el.attrib.items()):
            if key == 'id':
                el.set(key, ids[value])
            else:
                for old, new in ids.items():
                    value = value.replace('url(#'+old+')', 'url(#'+new+')')
                    if value == '#'+old:
                        value = '#'+new
                el.set(key, value)
    asset.set('x', f'{start:.6f}'); asset.set('y', f'{y-metrics["height"]*scale:.6f}')
    asset.set('width', f'{width:.6f}'); asset.set('height', f'{height:.6f}')
    asset.set('overflow', 'visible')
    # dvisvgm's geometry is black by default; inherit the label's actual ink.
    for el in asset.iter():
        if el.get('fill') in {'#000', '#000000', 'black'}:
            el.attrib.pop('fill')
    group.append(asset)
    return group, width


WORLD_LOOP_SYMBOLS = {
    'symbol_observation': r'\mathbf{o}_t',
    'symbol_observation_flow': r'\mathbf{o}_t',
    'symbol_time': r't',
    'symbol_estimate_current': r'\widehat{\mathbf{s}}_t',
    'symbol_estimate_future': r'\widehat{\mathbf{s}}_{t+\Delta}',
    'symbol_candidate_action': r'\mathbf{a}',
    'symbol_executed_action': r'\mathbf{a}_t',
    'symbol_next_observation': r'\mathbf{o}_{t+1}',
}


def normalize_world_model_loop(root):
    """Match the report's upright bold vectors and italic scalar time."""
    parents = {child: parent for parent in root.iter() for child in parent}
    for element_id, latex in WORLD_LOOP_SYMBOLS.items():
        label = next((item for item in root.iter() if item.get('id') == element_id), None)
        if label is None or label.get('data-latex'):
            continue
        sample = next((item for item in label.iter() if item.tag == tag('text')), None)
        if sample is None:
            raise ValueError(f'missing text source for {element_id}')
        formula, _ = math_group(
            latex,
            x=number(sample.get('x')),
            y=number(sample.get('y')),
            font_size=number(label.get('font-size'), 32),
            fill=label.get('fill', '#000000'),
        )
        for key in ('id', 'data-figure-label', 'aria-label', 'data-text-anchor', 'data-font-role'):
            if label.get(key) is not None:
                formula.set(key, label.get(key))
        parent = parents.get(label)
        if parent is None:
            raise ValueError(f'missing parent for {element_id}')
        parent[list(parent).index(label)] = formula

    for element_id in ('symbol_estimate_current_hat', 'symbol_estimate_future_hat'):
        mark = next((item for item in root.iter() if item.get('id') == element_id), None)
        if mark is not None:
            parents[mark].remove(mark)
    return root


DEFAULT_MATH = re.compile(r'(?<![A-Za-z])(?:[GCMZER]\(t\)|r_t)(?![A-Za-z])')


def _pieces(text, math_map):
    if math_map is None:
        yield text, None
        return
    pattern = re.compile('|'.join(re.escape(k) for k in sorted(math_map, key=len, reverse=True))) if math_map else DEFAULT_MATH
    offset = 0
    for match in pattern.finditer(text):
        if match.start() > offset:
            yield text[offset:match.start()], None
        value = match.group()
        latex = math_map.get(value) if math_map else (r'r_t' if value == 'r_t' else r'\mathcal{' + value[0] + '}(t)')
        yield value, latex
        offset = match.end()
    if offset < len(text):
        yield text[offset:], None


def normalize_text(element, *, heading=False, math_map=None, inherited=None):
    """Replace a text block in-place with measured, editable language runs.

    math_map=None preserves literal strings. math_map={} enables state-symbol
    detection; an explicit dict maps literal substrings to LaTeX expressions.
    Original line/label metadata makes future checks independent of run count.
    """
    inherited = inherited or {}
    attrs = {**inherited, **element.attrib}
    original = ''.join(element.itertext())
    lines = []

    def walk(node, parent_attrs):
        # Relative cursor shifts apply once to the first character of a span;
        # inheriting them into nested spans would lower subscripts twice.
        current = {**{k: v for k, v in parent_attrs.items() if k not in {'dx', 'dy'}}, **node.attrib}
        if 'style' in current:
            current.update(dict(pair.strip().split(':', 1) for pair in current['style'].split(';') if ':' in pair))
        if node.text and node.text.strip():
            yield node.text, current
        for child in node:
            yield from walk(child, current)
            if child.tail and child.tail.strip():
                yield child.tail, {k: v for k, v in current.items() if k not in {'dx', 'dy'}}

    tokens = list(walk(element, inherited))
    # Explicit x/y on a child denotes a new line. Relative dx/dy remains inline.
    last_position = None
    for text, style in tokens:
        xy = (style.get('x', attrs.get('x', '0')), style.get('y', attrs.get('y', '0')))
        if not lines or (xy != last_position and (style.get('x') is not None or style.get('y') is not None)):
            lines.append({'x': number(xy[0]), 'y': number(xy[1]), 'tokens': []})
        lines[-1]['tokens'].append((text, style))
        last_position = xy
    group_attrs = {k: v for k, v in element.attrib.items() if k not in {'x', 'y', 'dx', 'dy', 'font-family', 'font-style', 'font-weight', 'text-anchor', 'style'}}
    group_attrs.update({'data-figure-label': 'true', 'aria-label': original.strip(), 'data-text-anchor': attrs.get('text-anchor', 'start'),
                        'data-font-role': 'heading' if heading else 'body', 'font-family': FONT_POLICY['chinese']})
    group = ET.Element(tag('g'), group_attrs)
    if element.tail:
        group.tail = element.tail
    for line in lines:
        runs = []
        for text, style in line['tokens']:
            size = number(style.get('font-size', attrs.get('font-size')), 12)
            weight = style.get('font-weight', attrs.get('font-weight', '400'))
            slant = style.get('font-style', attrs.get('font-style', 'normal'))
            fill = style.get('fill', attrs.get('fill', '#000000'))
            dx, dy = number(style.get('dx')), number(style.get('dy'))
            spacing = number(style.get('letter-spacing'))
            first = True
            for value, latex in _pieces(text, math_map):
                if latex is not None:
                    item, advance = math_group(latex, font_size=size, fill=fill)
                    runs.append((item, advance, dx if first else 0, dy if first else 0))
                    first = False
                else:
                    for value, family in font_runs(value, heading):
                        item = ET.Element(tag('text'), {'font-family': family, 'font-size': str(size), 'font-weight': weight if family == FONT_POLICY['western'] else '400',
                                                       'font-style': slant if family == FONT_POLICY['western'] else 'normal', 'text-anchor': 'start', 'fill': fill,
                                                       '{http://www.w3.org/XML/1998/namespace}space': 'preserve'})
                        if spacing:
                            item.set('letter-spacing', str(spacing))
                        item.text = value
                        advance = text_width(value, size, family, weight, slant, spacing)
                        runs.append((item, advance, dx if first else 0, dy if first else 0))
                        first = False
        total = sum(advance + dx for _, advance, dx, _ in runs)
        anchor = attrs.get('text-anchor', 'start')
        cursor = line['x'] - (total / 2 if anchor == 'middle' else total if anchor == 'end' else 0)
        baseline = line['y']
        for item, advance, dx, dy in runs:
            cursor += dx; baseline += dy
            if item.tag == tag('text'):
                item.set('x', f'{cursor:.6f}'); item.set('y', f'{baseline:.6f}')
            else:
                item.set('transform', f'translate({cursor:.6f} {baseline:.6f})')
            group.append(item)
            cursor += advance
    return group


def normalize_svg_fonts(root, heading_predicate=None, math_map=None):
    """Normalize all text blocks once, preserving non-text geometry."""
    def visit(parent, inherited):
        current = {**inherited, **parent.attrib}
        for i, child in enumerate(list(parent)):
            if child.tag == tag('text'):
                heading = bool(heading_predicate(child)) if heading_predicate else False
                parent[i] = normalize_text(child, heading=heading, math_map=math_map, inherited=current)
            elif child.get('data-figure-label') != 'true':
                visit(child, current)
    visit(root, {})
    root.set('data-font-policy', 'SimSun / SimHei / Times New Roman / Computer Modern')
    return root


def save_svg(root, path):
    path = Path(path)
    ET.indent(root, space='  ')
    ET.ElementTree(root).write(path, encoding='utf-8', xml_declaration=True)


def check_export_fonts():
    """Reject fontconfig fallback before Cairo writes a replacement PDF."""
    matcher = shutil.which('fc-match')
    if matcher is None:
        raise ValueError(
            'SVG export requires fontconfig fc-match to verify SimSun, SimHei, '
            'and Times New Roman before rendering'
        )
    resolved = {}
    failures = []
    for role in ('chinese', 'heading', 'western'):
        family = FONT_POLICY[role]
        result = subprocess.run(
            [matcher, '-f', '%{family}\n', family],
            text=True, capture_output=True, check=False, timeout=10,
        )
        actual = result.stdout.strip()
        names = {name.strip().casefold() for name in actual.split(',')}
        if result.returncode or family.casefold() not in names:
            failures.append(f'{family} (resolved to {actual or "no font"})')
        else:
            resolved[family] = actual
    if failures:
        raise ValueError(
            'Required SVG text fonts are unavailable: ' + '; '.join(failures) +
            '. Install the required fonts; fallback rendering is disabled.'
        )
    return resolved


def export_svg(source, target=None, *, page_size=None):
    check_export_fonts()
    import cairosvg
    source = Path(source)
    target = Path(target) if target else source.with_name('figure.pdf')
    if page_size is None and target.exists():
        from pypdf import PdfReader
        box = PdfReader(target).pages[0].mediabox
        page_size = float(box.width), float(box.height)
    options = {}
    if page_size:
        options.update(output_width=page_size[0] / .75, output_height=page_size[1] / .75)
    cairosvg.svg2pdf(bytestring=source.read_bytes(), write_to=str(target), **options)
    return target
