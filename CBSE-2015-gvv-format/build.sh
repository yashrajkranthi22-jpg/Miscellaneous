#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 codes/TitleLogo.py
python3 codes/Tower.py
python3 codes/TangentChord.py
python3 codes/TwoTangents.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
