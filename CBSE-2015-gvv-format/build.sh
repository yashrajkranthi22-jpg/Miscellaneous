#!/usr/bin/env bash
# Rebuild all diagrams from their Python sources, run independent numerical
# checks, then produce both DVI and PDF outputs. latexmk records dependencies.
set -euo pipefail
cd "$(dirname "$0")"
for script in TitleLogo.py Tower.py TangentChord.py TwoTangents.py IncircleTriangle.py Aeroplane.py Tent.py CubeHemisphere.py CloudReflection.py FlowerBeds.py CylinderScooped.py; do
  python3 "codes/$script"
done
python3 codes/VerifyClass10.py
# The EPS siblings let classic latex emit DVI; pdflatex selects PNG/JPEG instead.
latexmk -dvi -interaction=nonstopmode -halt-on-error main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
# The index is intentionally empty until explicit \index entries are added.
makeindex main.idx
