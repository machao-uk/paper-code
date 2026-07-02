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

## Primary Proof Object Files

```text
CERTIFICATE_LEDGER.md
global-certificates/MathZ_boundary_phi12_bernstein_modcrt.md
global-certificates/MathZ_boundary_phi12_bernstein_modcrt.py
global-certificates/MathZ_gamma3_hard_corner_closed.md
outputs/REFERENCE_OUTPUT.md
reproduce_gamma3_hard_corner.py
```

These files are the primary reproducible proof objects for the finite
exact-arithmetic certificates cited in the paper.

## Archival Logs

The following files record exploratory calculations, failed approaches, and
historical state snapshots.  They are retained for auditability but are not
used as standalone proof certificates.

```text
global-certificates/MathZ_COMPLETE_STATE_2026-06-28.md
global-certificates/MathZ_n4_closure_summary.md
global-certificates/MathZ_schur_step_certificates.md
global-certificates/MathZ_contraction_proof.md
global-certificates/MathZ_gamma2_strict.md
global-certificates/MathZ_polytope_cert.md
```

## SHA256

```text
7f0e2730350bfa2ec0ec2dfd5c09d52fb5f7b90d554e0a1a95670864e38c9a80  CERTIFICATE_LEDGER.md
4a4a90d07746aa5a347a5ecc664a290c072be1a0bbc251f942ae20fe0839f11a  global-certificates/MathZ_COMPLETE_STATE_2026-06-28.md
b4015dd6e1eae27d976776f9bd4691c2f1aa40f366b2856777454b4f1df23179  global-certificates/MathZ_boundary_phi12_bernstein_modcrt.md
aa8140ec2ce7c305e0629f2a52a267cbcaf41e746e9af8b9ad1529352c1fff05  global-certificates/MathZ_boundary_phi12_bernstein_modcrt.py
2e921c1afe81ecc4f04dc206bd7c2d3c0a312f5d7d1da80db20c4b7e5405207e  global-certificates/MathZ_contraction_proof.md
9b1c6df79b0c2947fffaf18fd0f64daf5db09728c00ed72f705cf8630ce5f48a  global-certificates/MathZ_gamma2_strict.md
a9a38ac97bf92dd240fc5d7a7c25a9ce950c525b4b74603663de4bde656615b6  global-certificates/MathZ_gamma3_hard_corner_closed.md
9ffaa9ca7d32b30ea725e6edf0c5aba7501a3f4a711087b64c39a94fd4a61334  global-certificates/MathZ_n4_closure_summary.md
0db263addf3ffa7058cf16b2e5c4bed9f7ed7347fc79be0d2b37b388ee832548  global-certificates/MathZ_polytope_cert.md
a08b5007709799b23e5f9e3c61d12f51b380d6d86fed3c9387c0fbbd799835ba  global-certificates/MathZ_schur_step_certificates.md
8bee1dfc8aa6334f0f0e2bb3045e11d1f96e305d005607937af37287231e126b  inputs/MathZ_gamma3_blowup_S.pkl
61192c6a2c5423e79d396b42cb08de430b81232f9fa16cf819644be84ea86d57  inputs/MathZ_gamma3_blowup_T.pkl
df3c820174d404c34add5e8b9b793ac9ad6c92a3c53eaadc4bcc98979050857e  inputs/MathZ_gamma3_primitive_norm_expr.pkl
6801a61acfa1834fb01171ffbf351b16f8d2d86254523b0a6e7024d805704db3  outputs/REFERENCE_OUTPUT.md
473ac0d3875c1c3989ff42f1291b8db4ee104b3e4769283fdc1c754a5568dabc  reproduce_gamma3_hard_corner.py
```
