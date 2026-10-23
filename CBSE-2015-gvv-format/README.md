# CBSE Mathematics 2015 — EE1010-style working folder

This working directory is deliberately organized to follow the layout of
[`gadepall/ee1010-2026/EE26BTECH11202`](https://github.com/gadepall/ee1010-2026/tree/master/EE26BTECH11202): a root `main.tex`, course-style `.sty` files, question/solution sources under `chapters/`, Python code under `codes/`, `codes/CoordGeo/` helper subpackages, and generated images under `figs/`.

## Build

Run from a Linux shell with TeX Live, Python 3, NumPy, and Matplotlib installed:

```bash
./build.sh
```

The build script regenerates `figs/logo.jpg`, `figs/Tower.png`, `figs/TangentChord.png`, and `figs/TwoTangents.png` from the corresponding Python scripts before compiling `main.tex` twice. Compilation outputs (`main.pdf`, `.aux`, `.log`, etc.) are generated at the project root, just as in the reference repository.

The `CoordGeo` package here preserves the reference directory/module layout and provides the functions used by the included plots. It is a small compatible subset, not a byte-for-byte vendored copy of every upstream helper function.

## Content sources and audit flags

- Class X transcription: [`gadepall/cbse-papers/2015/math/10/cbse_2015_10.tex`](https://github.com/gadepall/cbse-papers/blob/main/2015/math/10/cbse_2015_10.tex)
- Class XII transcription: [`gadepall/cbse-papers/2015/math/12/main.tex`](https://github.com/gadepall/cbse-papers/blob/main/2015/math/12/main.tex), titled `2015 12th Set-3`
- Formatting reference: [`gadepall/ee1010-2026/EE26BTECH11202`](https://github.com/gadepall/ee1010-2026/tree/master/EE26BTECH11202)
- Official CBSE 2015 question-paper index: https://www.cbse.gov.in/curric~1/qpms2015/qpms2015.htm
- Official Class X marking scheme (verifies Q2 shadow length): https://www.cbse.gov.in/curric~1/qpms2015/MS_Book_2015/Class%20X%20Marking%20Scheme%202015.pdf

This is a working batch, not a completed assignment. Class X Q2 is verified against the official CBSE marking scheme: the shadow is `20√3 m` and the Sun altitude is `30°`. The Class X chord/tangent figure has been redrawn to match the official point placement, so Q4 gives `120°`. Class XII vectors 1 and 2 preserve the original wording defects and give only conditional interpretations. Remaining Class X sections and remaining Class XII topics have not yet been migrated or solved in this batch.
