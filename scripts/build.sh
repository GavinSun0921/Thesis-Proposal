#!/usr/bin/env bash
set -euo pipefail

# 根据脚本位置定位工程，允许从任意工作目录运行。
project_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

for tool in latexmk xelatex bibtex; do
  if ! command -v "$tool" >/dev/null 2>&1; then
    printf '错误：未找到 %s。请安装 TeX Live / MacTeX，并将其加入 PATH。\n' "$tool" >&2
    exit 1
  fi
done

cd "$project_root/latex"
latexmk -xelatex -halt-on-error -interaction=nonstopmode main.tex

printf '\n编译完成：%s/latex/build/main.pdf\n' "$project_root"
