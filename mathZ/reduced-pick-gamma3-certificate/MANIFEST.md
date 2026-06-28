# MathZ n=4 reduced Pick certificate manifest

This reproducibility package supports the unconditional quartic reduced Pick
closure used in `paper/mathZ.tex`.

## Logical Coverage

The global certificate is assembled from the following closed components:

```text
1. K-region / compact interior reduction.
2. Paired family.
3. Boundary strata and confluent layers.
4. Real boundary face.
5. First Schur pivot gamma1.
6. Second Schur pivot gamma2 on the 3+1 layer.
7. Radial square model.
8. One-dimensional confluent family.
9. Third Schur pivot gamma3 hard corner.
```

The first eight components were already closed by the analytic/Bernstein
certificates listed in `global-certificates/`.  The only remaining hard corner
was component 9, which is reproduced by
`reproduce_gamma3_hard_corner.py`.

## Reproducible Hard-Corner Certificate

Run:

```bash
cd mathZ/reduced-pick-gamma3-certificate
python3 -m pip install -r requirements.txt
python3 reproduce_gamma3_hard_corner.py
diff -u outputs/REFERENCE_OUTPUT.md outputs/gamma3_hard_corner_certificate_output.md
```

Expected result: no diff, and the output contains

```text
hard corner closed: True
```

## Global Certificate Files

```text
global-certificates/MathZ_COMPLETE_STATE_2026-06-28.md
global-certificates/MathZ_n4_closure_summary.md
global-certificates/MathZ_schur_step_certificates.md
global-certificates/MathZ_boundary_phi12_bernstein_modcrt.md
global-certificates/MathZ_boundary_phi12_bernstein_modcrt.py
global-certificates/MathZ_contraction_proof.md
global-certificates/MathZ_gamma2_strict.md
global-certificates/MathZ_polytope_cert.md
global-certificates/MathZ_gamma3_hard_corner_closed.md
```

These files are not substitutes for the paper proof text; they are the
audit trail for the finite exact-arithmetic certificates cited there.

