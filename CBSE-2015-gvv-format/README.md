# CBSE Mathematics 2015 — Class X, Code 30/1

This folder follows the root-level LaTeX + `chapters/` + `codes/` + `codes/CoordGeo/` + `figs/` layout used in [`gadepall/ee1010-2026/EE26BTECH11202`](https://github.com/gadepall/ee1010-2026/tree/master/EE26BTECH11202). It is deliberately Class X only in this iteration; `chapters/class12.tex` is retained but is not included in `main.tex` until the Class X format is finalized.

## Build and verification

Requirements: TeX Live (`pdflatex`, `latexmk`, `makeindex`), Python 3, NumPy, and Matplotlib.

```bash
./build.sh
python3 codes/VerifyClass10.py
```

The build regenerates every figure from its Python source, compiles both DVI and PDF, and generates the usual index/build products. `main.dvi`, `main.fdb_latexmk`, `main.fls`, `main.ilg`, and `main.ind` are intentionally part of the expected build output, following the reference repository's convention.

## Apply to an existing repository clone

The folder contains `sync_to_repo.sh` for overlaying these files onto an existing `Miscellaneous` clone without deleting unrelated files. From this extracted folder, run `./sync_to_repo.sh /path/to/Miscellaneous`, then rebuild from `Miscellaneous/CBSE-2015-gvv-format` and review `git diff` before committing. The `.fdb_latexmk` and `.fls` files should be regenerated on that machine because they contain local path/toolchain metadata.

## Source hierarchy

- `main.tex`: book-style entry point and Class X-only build scope.
- `chapters/class10_formulae.tex`: formula-first reference sheet; solutions link back to these identities.
- `chapters/class10.tex`: all 31 questions in the official Section A/B/C/D ordering.
- `codes/*.py`: one generator per nontrivial figure plus independent numeric checks.
- `codes/CoordGeo/`: documented reusable subset of the `CoordGeo` package hierarchy (line, conic, plotting, matrix, and triangle helpers).
- `figs/`: generated output images only; regenerate them with the scripts rather than editing images by hand.

## Sources and verification notes

- Official CBSE 2015 Class X paper, Outside Delhi, code 30/1: [PDF](https://www.cbse.gov.in/curric~1/qpms2015/Question_Papers_Class_X_XII_Main_Exam_2015/CLASS%20X%20-%202015%20MAIN%20EXAMS/CLASS%20X%20-%20OUTSIDE%20-%202015%20-%20MAIN%20EXAM/30-1%20MATHEMATICS.pdf).
- Official CBSE 2015 paper/marking-scheme index: [CBSE index](https://www.cbse.gov.in/curric~1/qpms2015/qpms2015.htm).
- Cross-check used for code 30/1: [Outside Delhi Mathematics marking scheme PDF](https://files.supercop.in/cbse-board-papers/class10/maths/ans_m_2015.pdf), which records the expected answers and stepwise value points.
- Formatting reference: [`EE26BTECH11202`](https://github.com/gadepall/ee1010-2026/tree/master/EE26BTECH11202).
- Coordinate-geometry reference: [`gadepall/matgeo`](https://github.com/gadepall/matgeo), described upstream as “Matrices in Geometry.”
- Public CBSE transcription used for cross-checking: [`gadepall/cbse-papers/2015/math/10/cbse_2015_10.tex`](https://github.com/gadepall/cbse-papers/blob/main/2015/math/10/cbse_2015_10.tex).

The upstream transcription printed the tower shadow as `203 m` in plain text due to a lost radical/multiplier. The official paper specifies `20 sqrt(3) m`, which gives the Sun altitude `30 degrees`; the present source uses the official value. The independent marking scheme agrees with the numerical results checked here, including `p=3`, `1/9`, `120 degrees`, Q13 speed `720 km/h`, Q17 contribution Rs 379,500, Q19 painting cost about Rs 33.93, Q29 roots `3` and `-9/2`, Q30 area `504 m^2`, and Q31 wire length `158.4 cm`.
