# Class X build report — CBSE Mathematics 2015, code 30/1

## Build result

- `main.pdf`: 20 pages; compiled successfully with `latexmk -pdf`.
- `main.dvi`: compiled successfully with `latexmk -dvi` and uses the EPS versions of the generated diagrams.
- `main.fdb_latexmk` and `main.fls`: emitted by `latexmk`.
- `main.ilg` and `main.ind`: emitted by `makeindex`. The `.ind` file is intentionally empty because no explicit `\index{...}` terms are currently used.
- `python3 codes/VerifyClass10.py`: passed; checks selected numerical results, presence of all 31 question labels, and the generated raster/vector assets.

## Source audit

The content follows the official 30/1 order: Q1–Q4, Q5–Q10, Q11–Q20, Q21–Q31. Formulae precede solutions in `chapters/class10_formulae.tex`; every coordinate-geometry calculation is expressed with vectors, dot products, determinants, or a matrix setup when useful. Class XII source is retained in `chapters/class12.tex` but is not included in this build.

Primary source: [official CBSE 2015 paper, Outside Delhi, code 30/1](https://www.cbse.gov.in/curric~1/qpms2015/Question_Papers_Class_X_XII_Main_Exam_2015/CLASS%20X%20-%202015%20MAIN%20EXAMS/CLASS%20X%20-%20OUTSIDE%20-%202015%20-%20MAIN%20EXAM/30-1%20MATHEMATICS.pdf).
Independent cross-check: [CBSE 2015 Outside Delhi 30/1 marking scheme](https://files.supercop.in/cbse-board-papers/class10/maths/ans_m_2015.pdf).

Note: `.fdb_latexmk` and `.fls` record the toolchain and local paths used when the build was run. Re-run `./build.sh` on the target machine to regenerate environment-specific dependency metadata.
