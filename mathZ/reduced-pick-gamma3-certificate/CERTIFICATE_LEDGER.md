# MathZ n=4 Reduced Pick Certificate Ledger

This file is the primary audit ledger for the exact-arithmetic certificate
used by `paper/mathZ.tex`.

## Closed Components

| block | certificate object | status |
|---|---|---|
| paired family | analytic factorization in `global-certificates/MathZ_contraction_proof.md` | closed |
| confluent slice | rational reconstruction and exact Bernstein in `global-certificates/MathZ_contraction_proof.md` | closed |
| real boundary face | 8-prime CRT Bernstein in `global-certificates/MathZ_boundary_phi12_bernstein_modcrt.md` | closed |
| gamma2 on the 3+1 layer | exact rational Bernstein table in `global-certificates/MathZ_schur_step_certificates.md` | closed |
| radial square | explicit factorization in `paper/mathZ.tex` and `global-certificates/MathZ_contraction_proof.md` | closed |
| gamma3 hard corner | blow-up verifier `reproduce_gamma3_hard_corner.py` and `outputs/REFERENCE_OUTPUT.md` | closed |

## Reproducible Commands

From this directory:

```bash
python3 reproduce_gamma3_hard_corner.py
diff -u outputs/REFERENCE_OUTPUT.md outputs/gamma3_hard_corner_certificate_output.md
```

Expected result: no diff and the output contains

```text
hard corner closed: True
```

For the real boundary face:

```bash
cd global-certificates
python3 MathZ_boundary_phi12_bernstein_modcrt.py
```

Expected result: the three depth-1 subtriangle certificates for pairs
`(1,2)`, `(1,3)`, and `(2,3)` are all `True`, with zero rational
reconstruction failures.

## Notes

The files under `global-certificates/` include historical exploratory logs as
well as final certificates.  The proof uses the closed components listed
above.  Failed exploratory probes in archival logs are not certificate
failures; they record discarded approaches.
