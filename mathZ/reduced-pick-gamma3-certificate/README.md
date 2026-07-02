# MathZ quartic reduced Pick certificate

This directory contains the reproducibility package for the quartic reduced
Pick matrix hard-corner certificate used in `mathZ.tex`.

Start with `CERTIFICATE_LEDGER.md`.  It lists the closed certificate blocks,
the exact verifier outputs, and which archival logs support each block.

## What It Verifies

The script verifies the only hard corner in the two-parameter `3+1` chart for
the third Schur pivot `gamma3`:

```text
rho in [3/4, 1],
y   in [3/4, 1],
(rho, y) near (1, 1).
```

After the blow-up

```text
u = 1-rho,
v = 1-y,
u = 4v + vz,
S(z,v) = Q(4v+vz,v)/v^11,
```

the script checks four regions:

```text
1. |z| <= 16v:
   exact coefficient l1 bound for T(q,v)=S(vq,v)/v.

2. 16v < |z| < 1/4:
   explicit estimate S >= 50 C v.

3. 1/4 <= |z| <= 32:
   exact rational Bernstein checks on S over fixed z intervals.

4. z >= 32:
   reciprocal chart H(r,u)=Q(u,ru), exact rational Bernstein check.
```

## Files

```text
reproduce_gamma3_hard_corner.py
```

Main reproducibility script.

```text
inputs/MathZ_gamma3_primitive_norm_expr.pkl
inputs/MathZ_gamma3_blowup_S.pkl
inputs/MathZ_gamma3_blowup_T.pkl
```

Exact SymPy polynomial caches used by the certificate.

```text
outputs/REFERENCE_OUTPUT.md
```

Reference output from the verified run.

```text
outputs/gamma3_hard_corner_certificate_output.md
```

Generated output path when the script is run.

```text
paper/mathZ.tex
paper/mathZ.pdf
```

Snapshot of the paper file and compiled PDF containing the certificate text.

## Reproduce

From this directory:

```bash
python3 -m pip install -r requirements.txt
python3 reproduce_gamma3_hard_corner.py
diff -u outputs/REFERENCE_OUTPUT.md outputs/gamma3_hard_corner_certificate_output.md
```

Expected result:

```text
hard corner closed: True
```

The run is exact rational arithmetic. On the original machine it takes roughly
1-2 minutes.

The real-boundary CRT certificate is reproduced by:

```bash
cd global-certificates
python3 MathZ_boundary_phi12_bernstein_modcrt.py
```

Expected result: the depth-1 subtriangle certificates for pairs `(1,2)`,
`(1,3)`, and `(2,3)` are all `True`, with zero rational reconstruction
failures.
