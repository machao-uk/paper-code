# Edge-reservoir diagnostics for the Physica D manuscript

This folder contains the small reproducibility package for the manuscript

**Edge-Reservoir Geometry, Tauberian Relaxation, and Pseudospectral Gain in Fractional Delayed Fields**

by Chao Ma.

The manuscript is a theory paper.  Most of the figures in the paper are not large-scale simulations; they are deliberately simple diagnostics for the local edge-reservoir formulas proved in the text.  This folder keeps the numerical side honest: it records exactly which quantities are formula-generated and which quantities are obtained by root tracking.

## What is in this folder

- `physicaD_v42_root_tracking_protocol.py` reproduces the root-tracking protocol used for Figures 4--6 and Table 1 of the final polished manuscript.
- `requirements.txt` lists the minimal Python dependencies.
- `REFERENCE_OUTPUT.txt` records the expected terminal output from the script.
- `MANIFEST.md` explains which manuscript diagnostics are formula-generated and which are root-tracking checks.

## What the script checks

The script performs three small checks.

First, it solves the scalar delayed characteristic equation by Newton iteration and compares the computed centered loss with the leading subcritical asymptotic loss coefficient.

Second, it records the coherent multiplicity-three nilpotent block as three algebraic copies of the same scalar delayed root.  This is not an independent diagonalization experiment; it reflects the exact determinant identity `det(g I_3 - N_3)=g^3`.

Third, it tracks the stable branch of the cyclic Puiseux diagnostic.  The cyclic block uses `eta=1`.  Changing nonzero `eta` changes the prefactor but not the log-log slope.  The delayed scalar chart rescales the Puiseux coefficient by `D_tau^{-1}`, which again changes the prefactor but not the fitted exponent.

The expected slopes are

- coherent chain: approximately `1.500`, matching `alpha=1.5`;
- cyclic EP3 stable branch: approximately `0.504`, close to `alpha/3=0.500` over the stated finite fit range.

## How to run

From this folder:

```bash
python physicaD_v42_root_tracking_protocol.py
```

The script only requires NumPy.  A minimal setup is

```bash
python -m pip install -r requirements.txt
```

## Relation to the manuscript figures

Figures 1--2 in the manuscript are finite-volume staircase diagnostics generated from the analytic active-interval formulas.  They are not independent numerical spectral experiments.

Figure 3 is a formula-generated log-log comparison of the coherent `E^{1/alpha}` law and the stable Puiseux `E^{3/alpha}` law.

Figures 4--6 and Table 1 are the root-tracking diagnostics reproduced by the script in this folder.

## Notes

This code is intentionally small.  It is meant to make the numerical claims in the manuscript reproducible, not to provide a general-purpose spectral solver for delay equations or non-Hermitian pencils.

The parameters are fixed to the manuscript diagnostics:

- `alpha = 1.5`
- `nu = 1`
- `tau = 1`
- `lambda0 = -0.2`
- `D_tau = 0.8`
- `a_tau = 1.25`

The code is written as a transparent audit script rather than as a package.