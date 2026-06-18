# EP3 variance-lock-in reproducibility code

This directory contains the reproducibility code and numerical audit output for the manuscript:

**Variance-lock-in spectroscopy of exceptional-point eigenvector curvature**

The archive contains no external experimental data. It provides a deterministic synthetic linewidth benchmark, EP3/EP2 order-control diagnostics, width-pair invariance checks, null-channel rejection, regular-background rejection, and audit-certificate fields used to support the manuscript's reproducibility statement.

## Files

- `reproduce_ep3_figures.py` - regenerates vector PDF figures and audit outputs.
- `audit_summary.json` - top-level reference numerical audit output from the deterministic run.
- `audit_outputs/audit_summary.json` - generated audit summary written by the script.
- `audit_outputs/fitted_linewidth_tables.csv` - fitted synthetic linewidth values for the EP3 benchmark branch.
- `audit_outputs/jitter_moments.json` - symmetric jitter moments and width-pair definitions.
- `audit_outputs/width_pair_outputs.csv` - width-pair invariance outputs.
- `audit_outputs/ep2_control_output.csv` - EP2 order-control branch.
- `audit_outputs/null_channel_output.csv` - null-detector branch used for rejection.
- `audit_outputs/regular_background_output.csv` - regular-background branch used for rejection.
- `audit_outputs/certificate.json` - pass/fail audit gate record.
- `requirements.txt` - minimal Python dependencies.
- `LICENSE` - MIT license for the code in this directory.

The script regenerates the synthetic benchmark, order-dictionary, audit-certificate, and input-output-channel vector PDF figures. The mechanism schematic in the manuscript is embedded as TikZ in the LaTeX source for submission portability.

## Usage

```bash
pip install -r requirements.txt
python reproduce_ep3_figures.py --figdir figures --auditdir audit_outputs
```

The script writes vector figures to `figures/` and updated JSON/CSV audit outputs to `audit_outputs/`.

## Reference audit values

The reference run reports:

- EP3 variance-lock-in slope: `3.331767`
- EP2 control slope: `3.000000`
- raw linewidth apparent slope: `2.577535`
- width-pair slope difference: `6.411e-06`
- null-channel slope: approximately `0`
- regular-background slope: approximately `0.197242`

These diagnostics are synthetic reproducibility checks, not external experimental data.
