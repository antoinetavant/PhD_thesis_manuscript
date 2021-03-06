# PhD Thesis

This repository contains the LaTeX source files of my PhD thesis entitled "Gradient-Damage Modeling of Dynamic Brittle Fracture: Variational Principles and Numerical Simulations".

Detailed information concerning the defense of the current thesis can be found at [http://thesis.litianyi.me](http://thesis.litianyi.me).

## PDF version

You can download [an author-generated PDF version](https://bitbucket.org/litianyi/thesis-manuscript/downloads/Thesis-Li.pdf) directly in the "Downloads" section of the current repository.

## Figures

You can download [here](https://bitbucket.org/litianyi/thesis-manuscript/downloads/Figs.7z) all the figures used in this thesis. Please put the `figs` folder in the current thesis workspace, namely inside the `thesis-manuscript` folder.

Many schematic figures are created proudly by the [ipe](http://ipe.otfried.org) software and its matplotlib backend available at [https://github.com/otfried/ipe-tools](https://github.com/otfried/ipe-tools). I would like to express my deep love to [ipe](http://ipe.otfried.org).

## LaTeX compilation

The simplest way is to use the `latexmk` script available in all latest TeXLive distributions. You only need to compile the main LaTeX file:

```
latexmk -pdf main.tex
```

It should include all the chapter TeX files in the `chapters` folder and automatically call several times `pdflatex` and `biber` to obtain the final `main.pdf` file.

## License information

This work is licensed under a [Creative Commons "Attribution 4.0 International" license](https://creativecommons.org/licenses/by/4.0). Licensees may copy, distribute, display and perform the work and make derivative works and remixes based on it only if they give the author the credits (attribution). The following BibTeX code can be used to cite the current document:

``` latex
@PhdThesis{Li:2016,
  author = {Li, Tianyi},
  title  = {{G}radient-{D}amage {M}odeling of {D}ynamic {B}rittle {F}racture: {V}ariational {P}rinciples and {N}umerical {S}imulations},
  school = {Université Paris-Saclay},
  year   = {2016},
  month  = oct,
}
```

Interested readers can freely use or adapt the document structure, the title page, etc., to their own needs.
