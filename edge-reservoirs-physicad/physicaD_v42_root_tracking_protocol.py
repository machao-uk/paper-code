"""Root-tracking protocol for the Physica D edge-reservoir diagnostics.

This script reproduces the scalar delayed root-tracking values, the coherent
multiplicity-three check, and the cyclic Puiseux slope fit used in Figures 4--6
and Table 1 of the final manuscript.

The cyclic diagnostic uses eta=1.  Nonzero eta changes the prefactor, not the
fitted slope.  The delayed scalar chart rescales the Puiseux coefficient by
D_tau^{-1}; this also changes the prefactor, not the log-log exponent.
"""

import cmath
import math

import numpy as np


alpha = 1.5
nu = 1.0
tau = 1.0
lambda0 = -0.2
mu = lambda0 * math.exp(lambda0 * tau)
Dtau = 1.0 + tau * lambda0
atau = nu / Dtau


def newton_scalar_root(xi, lam_init=None, max_iter=40, tol=1e-14):
    """Solve the scalar delayed characteristic equation by Newton iteration."""
    s = abs(xi) ** alpha
    z = lambda0 - atau * s if lam_init is None else lam_init
    for _ in range(max_iter):
        f = z + nu * s - mu * cmath.exp(-tau * z)
        fp = 1.0 + tau * mu * cmath.exp(-tau * z)
        dz = f / fp
        z -= dz
        if abs(dz) < tol:
            break
    return z


def scalar_loss_values(xis):
    """Return centered losses for the scalar delayed branch."""
    out = []
    prev = None
    for x in xis:
        root = newton_scalar_root(x, prev)
        prev = root
        out.append(lambda0 - root.real)
    return np.array(out)


def cyclic_stable_loss_values(xis, eta=1.0):
    """Return stable-branch losses for the cyclic Puiseux diagnostic.

    Model determinant: (z + a s)^3 - eta s = 0 in the reduced variable.
    For real positive eta, one stable branch has omega = -1/2 + i sqrt(3)/2.
    The delayed scalar chart rescales the Puiseux coefficient by D_tau^{-1}.
    """
    vals = []
    a = atau
    omega = complex(-0.5, math.sqrt(3.0) / 2.0)
    eta13 = eta ** (1.0 / 3.0)
    for x in xis:
        s = abs(x) ** alpha
        u = s ** (1.0 / 3.0)
        z = -a * s + (eta13 / Dtau) * omega * u
        vals.append(-z.real)
    return np.array(vals)


def loglog_slope(xis, losses):
    """Least-squares slope of log(loss) against log(|xi|)."""
    xvals = np.log(np.asarray(xis, dtype=float))
    yvals = np.log(np.asarray(losses, dtype=float))
    slope, intercept = np.polyfit(xvals, yvals, 1)
    return slope, intercept


if __name__ == "__main__":
    scalar_xis = np.array([0.01, 0.02, 0.04, 0.08, 0.16, 0.32, 0.50])
    scalar_losses = scalar_loss_values(scalar_xis)
    print("Scalar delayed branch losses:")
    for x, y in zip(scalar_xis, scalar_losses):
        leading = atau * abs(x) ** alpha
        print(f"xi={x:.5g} loss={y:.9g} leading={leading:.9g}")

    fit_xis = np.logspace(-4, -2, 9)
    coherent_losses = scalar_loss_values(fit_xis)
    cyclic_losses = cyclic_stable_loss_values(fit_xis)
    coh_slope, _ = loglog_slope(fit_xis, coherent_losses)
    cyc_slope, _ = loglog_slope(fit_xis, cyclic_losses)

    print("\nLeast-squares slopes over [1e-4, 1e-2]:")
    print(f"coherent slope={coh_slope:.3f} predicted={alpha:.3f}")
    print(f"cyclic EP3 stable slope={cyc_slope:.3f} predicted={alpha/3:.3f}")
