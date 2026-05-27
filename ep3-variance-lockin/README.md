# EP3 variance-lock-in reproducibility code

This directory contains the reproducibility code and numerical audit output for the manuscript:

**Variance-lock-in spectroscopy of exceptional-point eigenvector curvature**

The archive contains no external experimental data. It provides a deterministic synthetic linewidth benchmark, EP3/EP2 order-control diagnostics, width-pair invariance checks, null-channel rejection, and audit-certificate fields used to support the manuscript's reproducibility statement.

## Files

- `reproduce_ep3_figures.py` — regenerates vector PDF figures and audit output.
- `audit_summary.json` — reference numerical audit output from the deterministic run.
- `requirements.txt` — minimal Python dependencies.
- `LICENSE` — MIT license for the code in this directory.

## Usage

```bash
pip install -r requirements.txt
python reproduce_ep3_figures.py --figdir figures --auditdir audit_outputs
```

The script writes vector figures to `figures/` and an updated `audit_summary.json` to `audit_outputs/`.

## Reference audit values

The reference run reports:

- EP3 variance-lock-in slope: `3.331767`
- EP2 control slope: `3.000000`
- raw linewidth apparent slope: `2.577535`
- width-pair slope difference: `6.411e-06`

These diagnostics are synthetic reproducibility checks, not external experimental data.
