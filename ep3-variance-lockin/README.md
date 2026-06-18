# ep3-variance-lockin

Code behind *Variance-domain lock-in protocol for exceptional-point eigenvector-curvature readout*.

There's no lab data in here. `reproduce_ep3_figures.py` builds the synthetic
linewidth model used in the paper, runs the two-width estimator on it, and
spits out the four figures and the audit JSON/CSV outputs exactly as quoted
in the text. If you want to check a number in the manuscript, or poke at the
model yourself, this is the whole pipeline — nothing is precomputed or
hidden upstream.

The pipeline also runs EP2/null-channel/regular-background order-control
diagnostics, width-pair invariance checks, and a pass/fail audit certificate
used to support the manuscript's reproducibility statement.

## Running it

```bash
pip install -r requirements.txt
python reproduce_ep3_figures.py --figdir figures --auditdir audit_outputs
```

That writes four PDFs to `figures/` and JSON/CSV audit outputs to
`audit_outputs/`. Console output should read:

```
EP3 alpha = 3.331767 +/- 0.029373
EP2 alpha = 3.000000 +/- 0.029373
raw linewidth apparent slope = 2.577535
width-pair slope difference = 6.411e-06
```

If you get different numbers, something's off — the model is deterministic
(fixed seed, no sampling noise), so reruns should match bit for bit on any
machine.

Full reference slopes from the audit certificate:

- EP3 variance-lock-in slope: `3.331767`
- EP2 control slope: `3.000000`
- raw linewidth apparent slope: `2.577535`
- width-pair slope difference: `6.411e-06`
- null-channel slope: approximately `0`
- regular-background slope: approximately `0.197242`

## What's in the figures

- `fig1_mechanism.pdf` — the measurement chain: fix the mean detuning, inject
  jitter at two widths, fit, take the two-width difference.
- `fig2_order_dictionary.pdf` — log-log comparison of the EP3 curvature
  exponent against eigenvalue splitting and the static Petermann channel.
- `fig3_synthetic_benchmark.pdf` — the four-panel stress test: example
  spectra, the (uninformative) raw linewidth slope, the EP3/EP2 two-width
  response, and the pass/fail audit record.
- `fig4_analysis_record.pdf` — the decision chain that has to pass before an
  exponent gets reported instead of a diagnostic label.

## Files

- `reproduce_ep3_figures.py` — the whole pipeline.
- `audit_summary.json` — a saved copy of the audit output from a reference run.
- `audit_outputs/audit_summary.json` — generated audit summary written by the script.
- `audit_outputs/fitted_linewidth_tables.csv` — fitted synthetic linewidth values for the EP3 benchmark branch.
- `audit_outputs/jitter_moments.json` — symmetric jitter moments and width-pair definitions.
- `audit_outputs/width_pair_outputs.csv` — width-pair invariance outputs.
- `audit_outputs/ep2_control_output.csv` — EP2 order-control branch.
- `audit_outputs/null_channel_output.csv` — null-detector branch used for rejection.
- `audit_outputs/regular_background_output.csv` — regular-background branch used for rejection.
- `audit_outputs/certificate.json` — pass/fail audit gate record.
- `requirements.txt` — numpy + matplotlib, nothing exotic.
- `LICENSE` — MIT.

Questions or a bug report: open an issue, or email the address in the paper.
