# Vector figure sources

This folder contains standalone TikZ/PGFPlots vector sources for the six diagnostic figures in the manuscript

**Edge-Reservoir Geometry, Tauberian Relaxation, and Pseudospectral Gain in Fractional Delayed Fields**.

Each file can be compiled independently with `pdflatex` if the LaTeX installation includes TikZ and PGFPlots.

Example:

```bash
pdflatex figure1_finite_volume_staircase.tex
```

The files are vector sources rather than raster exports.  They are included to make the figure package transparent and easy to regenerate for journal production.

## Files

- `figure1_finite_volume_staircase.tex`
- `figure2_integer_platform_diagnostic.tex`
- `figure3_exponent_dichotomy.tex`
- `figure4_scalar_root_tracking.tex`
- `figure5_coherent_multiplicity_three_tracking.tex`
- `figure6_cyclic_puiseux_root_tracking.tex`
