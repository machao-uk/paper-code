# Diagnostic manifest

This manifest describes how the files in this folder relate to the figures and table in the manuscript.

## Manuscript

Title: **Edge-Reservoir Geometry, Tauberian Relaxation, and Pseudospectral Gain in Fractional Delayed Fields**

This repository folder is meant to accompany the manuscript as a lightweight supplementary code package.

## Formula-generated diagnostics

The following figures are formula diagnostics.  They are included in the paper to visualize the proved asymptotic laws and finite-volume staircase effects.  They should not be described as independent numerical spectral experiments.

### Figures 1--2

Finite-volume staircase and integer-platform diagnostics for the coherent multiplicity-three subcritical active reservoir.

The points come from lattice-counting the analytic active interval radius on the grid

```text
xi_m = pi m / L.
```

### Figure 3

Formula-generated log-log comparison of the coherent `E^{1/alpha}` law and the stable cyclic Puiseux `E^{3/alpha}` law.

## Root-tracking diagnostics

The following diagnostics are reproduced by `physicaD_v42_root_tracking_protocol.py`.

### Figure 4

Newton iteration for the scalar delayed characteristic branch.  The script prints both the computed centered loss and the leading asymptotic loss.

### Figure 5

Exact algebraic multiplicity-three tracking for the nilpotent pencil

```text
g(lambda,s) I_3 - N_3.
```

The three plotted copies represent the algebraic triple root of the determinant `g^3`; this is a multiplicity check, not a separate matrix-diagonalization experiment.

### Figure 6

Cyclic Puiseux stable-branch log-log check with `eta=1`.  The delayed pullback rescales the leading coefficient by `D_tau^{-1}`.  The slope remains close to `alpha/3`.

### Table 1

Least-squares slopes over the range

```text
|xi| in [1e-4, 1e-2].
```

The script reproduces the reported values:

```text
coherent slope = 1.500
cyclic EP3 stable slope = 0.504
```

## Parameters

The diagnostic parameters are

```text
alpha = 1.5
nu = 1.0
tau = 1.0
lambda0 = -0.2
mu = lambda0 * exp(lambda0 * tau)
D_tau = 1 + tau * lambda0 = 0.8
a_tau = nu / D_tau = 1.25
eta = 1.0  # cyclic Puiseux diagnostic
```

## Reproducibility note

The script is intentionally short and readable.  Its purpose is to document the numerical values used in the manuscript diagnostics, not to serve as a production solver for delay spectra.