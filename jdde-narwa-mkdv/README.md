# jdde-narwa-mkdv

Figure-generation script for the delayed fractional vector mKdV paper (non-normal delay amplification, modified $H^2$ Lyapunov closure, zero-history attraction; candidate journal: JDDE).

- `make_JDDE_figures.py` — generates the matrix-channel amplification figure (Jordan vs. normal block) plus the supplementary schematic indicators (transient response, delay scan, tail decay). Run with `python3 make_JDDE_figures.py`; output goes to `figures/`.
- `figure_parameters.json` — the parameter values and crossing points used by the script ($V_0$, $\rho_0$, $\beta$, admissibility-gap crossings).

All plots are generated from closed-form threshold formulas, not from a numerical discretization of the PDE.
