#!/usr/bin/env python3
"""Generate figures and numerical data for the PRR response-invariants manuscript.

The script contains direct active-pencil calculations, a method-of-steps
DDE transfer integrator, one-pole fitting, Petermann scaling, and degree-excess
checks.  It writes the PDF figures used by the manuscript in the current
working directory.
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

TAU = 1.0
RNG = np.random.default_rng(12345)


def logfit(x: np.ndarray, y: np.ndarray) -> tuple[float, float]:
    coeff = np.polyfit(np.log(np.abs(x)), np.log(np.abs(y)), 1)
    return float(coeff[0]), float(coeff[1])


def cbrt_branch(p: float, branch: int = 0) -> complex:
    return p ** (1.0 / 3.0) * np.exp(2j * np.pi * branch / 3.0)


def ret2_W(lam: complex, p: float, tau: float = TAU) -> complex:
    return lam**2 * (1.0 - np.exp(-lam * tau)) - p * np.exp(-lam * tau)


def ret2_dW(lam: complex, p: float, tau: float = TAU) -> complex:
    return 2 * lam * (1 - np.exp(-lam * tau)) + tau * lam**2 * np.exp(-lam * tau) + tau * p * np.exp(-lam * tau)


def newton_root(func, dfunc, guess: complex, args: tuple, maxiter: int = 40) -> complex:
    z = complex(guess)
    for _ in range(maxiter):
        f = func(z, *args)
        df = dfunc(z, *args)
        if abs(df) < 1e-14:
            break
        step = f / df
        z -= step
        if abs(step) < 1e-13 * max(1.0, abs(z)):
            break
    return z


def ret2_root(p: float, branch: int = 0, tau: float = TAU) -> complex:
    guess = tau ** (-1.0 / 3.0) * cbrt_branch(p, branch)
    return newton_root(ret2_W, ret2_dW, guess, (p, tau))


def inst2_root(p: float, branch: int = 0) -> complex:
    return (1 if branch == 0 else -1) * math.sqrt(p)


def inst2_denom(p: float) -> complex:
    return 2 * inst2_root(p, 0)


def degree_excess_W(lam: complex, p: float, n: int = 3, q: int = 1, tau: float = TAU) -> complex:
    return lam**n * (1 - np.exp(-lam * tau))**q - p * np.exp(-lam * tau)


def degree_excess_dW(lam: complex, p: float, n: int = 3, q: int = 1, tau: float = TAU) -> complex:
    a = 1 - np.exp(-lam * tau)
    da = tau * np.exp(-lam * tau)
    return n * lam ** (n - 1) * a**q + lam**n * q * a ** (q - 1) * da + tau * p * np.exp(-lam * tau)


def degree_excess_root(p: float, n: int = 3, q: int = 1, branch: int = 0, tau: float = TAU) -> complex:
    m = n + q
    guess = tau ** (-q / m) * p ** (1.0 / m) * np.exp(2j * np.pi * branch / m)
    return newton_root(degree_excess_W, degree_excess_dW, guess, (p, n, q, tau))


@dataclass
class DDEResult:
    omega: np.ndarray
    response: np.ndarray
    pole: complex
    residue: complex
    background: complex


def delayed_state(ts: np.ndarray, xs: np.ndarray, t_delay: float) -> np.ndarray:
    if t_delay <= 0.0:
        return np.zeros(xs.shape[1], dtype=complex)
    idx = np.searchsorted(ts, t_delay) - 1
    if idx < 0:
        return np.zeros(xs.shape[1], dtype=complex)
    if idx >= len(ts) - 1:
        return xs[-1]
    t0, t1 = ts[idx], ts[idx + 1]
    if t1 == t0:
        return xs[idx]
    w = (t_delay - t0) / (t1 - t0)
    return (1 - w) * xs[idx] + w * xs[idx + 1]


def integrate_single_frequency(p: float, omega: float, input_port: int, output_port: int,
                               tau: float = TAU, kappa: float = 0.60,
                               dt: float = 0.035, t_final: float = 190.0,
                               average_fraction: float = 0.35) -> complex:
    J3 = np.array([[0, 1, 0], [0, 0, 1], [0, 0, 0]], dtype=complex)
    E31 = np.zeros((3, 3), dtype=complex)
    E31[2, 0] = 1.0
    A0 = J3 - kappa * np.eye(3, dtype=complex)
    b = np.zeros(3, dtype=complex)
    b[input_port] = 1.0
    nsteps = int(t_final / dt) + 1
    ts = np.linspace(0.0, dt * (nsteps - 1), nsteps)
    xs = np.zeros((nsteps, 3), dtype=complex)
    for k in range(nsteps - 1):
        t = ts[k]
        x = xs[k]
        xd = delayed_state(ts[: k + 1], xs[: k + 1], t - tau)
        force = b * np.exp(1j * omega * t)
        rhs = A0 @ x + p * (E31 @ xd) + force
        xs[k + 1] = x + dt * rhs
    start = int((1.0 - average_fraction) * nsteps)
    y = xs[start:, output_port]
    phase = np.exp(-1j * omega * ts[start:])
    return np.mean(y * phase)


def shifted_platform_pole(p: float, branch: int = 1, tau: float = TAU, kappa: float = 0.60) -> complex:
    # z=lambda+kappa solves z^3 - p exp(-(z-kappa)tau)=0.
    omega = np.exp(2j * np.pi * branch / 3.0)
    guess_z = (np.exp(kappa * tau) * p) ** (1 / 3) * omega

    def F(lam: complex, pp: float, tt: float, kk: float) -> complex:
        z = lam + kk
        return z**3 - pp * np.exp(-lam * tt)

    def dF(lam: complex, pp: float, tt: float, kk: float) -> complex:
        z = lam + kk
        return 3 * z**2 + tt * pp * np.exp(-lam * tt)

    return newton_root(F, dF, -kappa + guess_z, (p, tau, kappa))


def direct_platform_transfer(omega: float, p: float, input_port: int, output_port: int,
                             tau: float = TAU, kappa: float = 0.60) -> complex:
    J3 = np.array([[0, 1, 0], [0, 0, 1], [0, 0, 0]], dtype=complex)
    E31 = np.zeros((3, 3), dtype=complex); E31[2, 0] = 1.0
    A0 = J3 - kappa * np.eye(3, dtype=complex)
    lam = 1j * omega
    D = lam * np.eye(3) - A0 - p * np.exp(-lam * tau) * E31
    b = np.zeros(3, dtype=complex); b[input_port] = 1.0
    x = np.linalg.solve(D, b)
    return x[output_port]


def fit_one_pole(omega: np.ndarray, response: np.ndarray, pole: complex) -> tuple[complex, complex, complex]:
    omega0 = pole.imag
    A = np.column_stack([
        np.ones_like(omega, dtype=complex),
        (omega - omega0).astype(complex),
        1.0 / (1j * omega - pole),
    ])
    coeff, *_ = np.linalg.lstsq(A, response, rcond=None)
    bg0, bg1, residue = coeff
    return residue, bg0, bg1




def shifted_platform_poles(p: float, tau: float = TAU, kappa: float = 0.40) -> np.ndarray:
    return np.array([shifted_platform_pole(p, branch=b, tau=tau, kappa=kappa) for b in (0, 1, 2)])

def fit_cluster_poles(omega: np.ndarray, response: np.ndarray, poles: np.ndarray) -> np.ndarray:
    omega0 = poles[1].imag
    cols = [np.ones_like(omega, dtype=complex), (omega - omega0).astype(complex)]
    cols += [1.0 / (1j * omega - pole) for pole in poles]
    A = np.column_stack(cols)
    coeff, *_ = np.linalg.lstsq(A, response, rcond=None)
    return coeff[2:]

def simulate_dde_transfer(p: float, input_port: int = 2, output_port: int = 0,
                          tau: float = TAU) -> DDEResult:
    poles = shifted_platform_poles(p, tau=tau, kappa=0.40)
    pole = poles[1]
    w0 = pole.imag
    width = 0.8 * max(abs(pole.real), abs(poles[0].imag - poles[1].imag), 0.02)
    omega = np.linspace(w0 - width, w0 + width, 15)
    response = np.array([
        integrate_single_frequency(p, w, input_port, output_port, tau=tau, kappa=0.40)
        for w in omega
    ])
    residues = fit_cluster_poles(omega, response, poles)
    return DDEResult(omega=omega, response=response, pole=pole, residue=residues[1], background=0.0)


def compute_data():
    pwide = np.logspace(-10, -3, 140)
    ptime = np.logspace(-4, -2, 8)
    ret_roots = np.array([ret2_root(float(p), branch=0) for p in pwide])
    ret_h = np.array([ret2_dW(ret_roots[i], float(pwide[i])) for i in range(len(pwide))])
    inst_roots = np.sqrt(pwide)
    inst_h = 2 * inst_roots
    ret_K = 1.0 / np.abs(ret_h) ** 2
    inst_K = 1.0 / np.abs(inst_h) ** 2

    deg_roots = np.array([degree_excess_root(float(p), n=3, q=1, branch=0) for p in pwide])
    deg_h = np.array([degree_excess_dW(deg_roots[i], float(pwide[i]), n=3, q=1) for i in range(len(pwide))])

    # Direct active-pencil and DDE-extracted residue comparison for a singular channel.
    channel = (2, 0)  # input e_3, readout e_1, zero-based (2 -> 0); singular channel.
    dde_res = []
    direct_res = []
    for pp in ptime:
        sim = simulate_dde_transfer(float(pp), input_port=channel[0], output_port=channel[1])
        dde_res.append(sim.residue)
        # Use direct frequency-domain samples with the same cluster-pole fitting routine as the DDE data.
        poles = shifted_platform_poles(float(pp), kappa=0.40)
        response = np.array([direct_platform_transfer(float(w), float(pp), channel[0], channel[1], kappa=0.40) for w in sim.omega])
        rr = fit_cluster_poles(sim.omega, response, poles)[1]
        direct_res.append(rr)
    dde_res = np.array(dde_res)
    direct_res = np.array(direct_res)

    return dict(pwide=pwide, ptime=ptime, ret_roots=ret_roots, ret_h=ret_h,
                inst_roots=inst_roots, inst_h=inst_h, ret_K=ret_K, inst_K=inst_K,
                deg_roots=deg_roots, deg_h=deg_h, dde_res=dde_res, direct_res=direct_res)


def make_memory_comparison(data, outdir: Path):
    p = data["pwide"]
    fig, axs = plt.subplots(1, 3, figsize=(11.0, 3.1))
    x = np.linspace(0, 1, 200)
    axs[0].plot(x, x**3, label=r"retarded cubic")
    axs[0].plot(x, x**2, linestyle="--", label=r"instantaneous quadratic")
    axs[0].set_xlabel(r"local root coordinate")
    axs[0].set_ylabel(r"control balance")
    axs[0].legend(fontsize=7)
    axs[0].set_title("Leading balance")

    axs[1].loglog(p, np.abs(data["ret_roots"]), label=r"retarded $p^{1/3}$")
    axs[1].loglog(p, np.abs(data["inst_roots"]), linestyle="--", label=r"instantaneous $p^{1/2}$")
    axs[1].set_xlabel(r"$|p|$")
    axs[1].set_ylabel(r"$|\lambda_a|$")
    axs[1].legend(fontsize=7)
    axs[1].set_title("Branch exponent")

    mat = np.array([[0, -2/3], [1/3, -1/3]])
    im = axs[2].imshow(mat, vmin=-2/3, vmax=1/3)
    axs[2].set_xticks([0, 1]); axs[2].set_yticks([0, 1])
    axs[2].set_xticklabels([r"$b_1$", r"$b_2$"])
    axs[2].set_yticklabels([r"$c_1$", r"$c_2$"])
    for i in range(2):
        for j in range(2):
            axs[2].text(j, i, f"{mat[i,j]:.2f}", ha="center", va="center")
    axs[2].set_title("Retarded two-port exponents")
    fig.colorbar(im, ax=axs[2], fraction=0.046, pad=0.04)
    fig.tight_layout()
    fig.savefig(outdir / "fig_memory_induced_comparison.pdf")
    plt.close(fig)


def make_dictionary(outdir: Path):
    fig, ax = plt.subplots(figsize=(7.5, 3.6))
    ax.axis("off")
    boxes = [
        (0.08, 0.62, r"retarded pencil\n$D(\lambda,p)$"),
        (0.38, 0.62, r"active branch\n$\lambda_a(p)$"),
        (0.68, 0.62, r"tested denominator\n$\mathfrak{h}_a=\ell(\partial_\lambda D)r$"),
        (0.20, 0.20, r"Keldysh residue"),
        (0.50, 0.20, r"Petermann proxy"),
        (0.78, 0.20, r"channel residues"),
    ]
    for x, y, s in boxes:
        ax.text(x, y, s, ha="center", va="center", fontsize=9,
                bbox=dict(boxstyle="round,pad=0.35", fc="white", ec="black"))
    arrows = [((0.20,0.62),(0.31,0.62)), ((0.50,0.62),(0.59,0.62)),
              ((0.68,0.55),(0.24,0.30)), ((0.68,0.55),(0.52,0.30)), ((0.68,0.55),(0.78,0.30))]
    for a,b in arrows:
        ax.annotate("", xy=b, xytext=a, arrowprops=dict(arrowstyle="->", lw=1.2))
    ax.text(0.50, 0.90, "Reduction-stable retarded response denominator", ha="center", fontsize=11)
    fig.tight_layout()
    fig.savefig(outdir / "fig_denominator_universality_class.pdf")
    plt.close(fig)


def compute_nine_channel_fits() -> np.ndarray:
    p_fit = np.logspace(-7, -2, 180)
    roots = np.array([degree_excess_root(float(p), n=3, q=1, branch=0) for p in p_fit])
    pe = p_fit * np.exp(-roots)
    denom = 3 * roots**2 + pe
    fitted = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            row, col = i, j
            if row == 0 and col == 0: num = roots**2
            elif row == 0 and col == 1: num = roots
            elif row == 0 and col == 2: num = np.ones_like(roots)
            elif row == 1 and col == 0: num = pe
            elif row == 1 and col == 1: num = roots**2
            elif row == 1 and col == 2: num = roots
            elif row == 2 and col == 0: num = roots * pe
            elif row == 2 and col == 1: num = pe
            else: num = roots**2
            residues = np.abs(num / denom)
            slope, _ = logfit(p_fit, residues)
            fitted[i, j] = slope
    return fitted


def make_heatmap(outdir: Path):
    predicted = np.array([[0, -1/3, -2/3], [1/3, 0, -1/3], [2/3, 1/3, 0]])
    fitted = compute_nine_channel_fits()
    fig, axs = plt.subplots(1, 2, figsize=(8.5, 3.4))
    for ax, mat, title in zip(axs, [predicted, fitted], ["Predicted", "Fitted"]):
        im = ax.imshow(mat, vmin=-2/3, vmax=2/3)
        ax.set_title(title)
        ax.set_xticks(range(3)); ax.set_yticks(range(3))
        ax.set_xticklabels([r"$b_1$", r"$b_2$", r"$b_3$"])
        ax.set_yticklabels([r"$c_1$", r"$c_2$", r"$c_3$"])
        for i in range(3):
            for j in range(3):
                ax.text(j, i, f"{mat[i,j]:.2f}", ha="center", va="center", fontsize=8)
    fig.colorbar(im, ax=axs.ravel().tolist(), fraction=0.04, pad=0.03)
    fig.savefig(outdir / "fig_platform_heatmap.pdf")
    plt.close(fig)


def make_reproducible_scaling(data, outdir: Path):
    p = data["pwide"]
    ptime = data["ptime"]
    fig, axs = plt.subplots(2, 2, figsize=(9.5, 7.2))
    ax = axs[0,0]
    ax.loglog(p, np.abs(data["ret_roots"]), label="retarded branch")
    ax.loglog(p, np.abs(data["inst_roots"]), linestyle="--", label="instantaneous branch")
    sr, _ = logfit(p[:80], np.abs(data["ret_roots"])[:80])
    si, _ = logfit(p[:80], np.abs(data["inst_roots"])[:80])
    ax.set_title(f"Branch slopes: {sr:.3f} vs {si:.3f}")
    ax.set_xlabel(r"$|p|$"); ax.set_ylabel(r"$|\lambda_a|$"); ax.legend(fontsize=7)

    ax = axs[0,1]
    ax.loglog(p, data["ret_K"], label=r"retarded $K_a$")
    ax.loglog(p, data["inst_K"], linestyle="--", label=r"instantaneous $K_a$")
    skr, _ = logfit(p[:80], data["ret_K"][:80])
    ski, _ = logfit(p[:80], data["inst_K"][:80])
    ax.set_title(f"Petermann slopes: {skr:.3f} vs {ski:.3f}")
    ax.set_xlabel(r"$|p|$"); ax.set_ylabel(r"$K_a$"); ax.legend(fontsize=7)

    ax = axs[1,0]
    ax.loglog(ptime, np.abs(data["direct_res"]), marker="o", label="direct active-pencil fit")
    ax.loglog(ptime, np.abs(data["dde_res"]), marker="s", linestyle="--", label="time-domain DDE fit")
    sd, _ = logfit(ptime, np.abs(data["direct_res"]))
    st, _ = logfit(ptime, np.abs(data["dde_res"]))
    ax.set_title(f"Residue slopes: {sd:.3f} direct, {st:.3f} DDE")
    ax.set_xlabel(r"$|p|$"); ax.set_ylabel(r"$|R_{13}|$"); ax.legend(fontsize=7)

    ax = axs[1,1]
    ax.loglog(p, np.abs(data["deg_h"]), label=r"$W_{3,1}$ denominator")
    sdeg, _ = logfit(p[:80], np.abs(data["deg_h"])[:80])
    ax.loglog(p, p**0.75 * np.abs(data["deg_h"][79]) / (p[79]**0.75), linestyle="--", label=r"$p^{3/4}$")
    ax.set_title(f"Degree-excess slope: {sdeg:.3f}")
    ax.set_xlabel(r"$|p|$"); ax.set_ylabel(r"$|\partial_\lambda W_{3,1}|$"); ax.legend(fontsize=7)

    fig.tight_layout()
    fig.savefig(outdir / "fig_reproducible_scaling.pdf")
    plt.close(fig)


def main():
    outdir = Path.cwd()
    data = compute_data()
    make_memory_comparison(data, outdir)
    make_dictionary(outdir)
    make_heatmap(outdir)
    make_reproducible_scaling(data, outdir)
    print("Generated figures in", outdir)
    # Print fitted slopes for audit trail.
    print("ret branch", logfit(data["pwide"][:80], np.abs(data["ret_roots"])[:80])[0])
    print("inst branch", logfit(data["pwide"][:80], np.abs(data["inst_roots"])[:80])[0])
    print("ret Petermann", logfit(data["pwide"][:80], data["ret_K"][:80])[0])
    print("inst Petermann", logfit(data["pwide"][:80], data["inst_K"][:80])[0])
    print("DDE residue", logfit(data["ptime"], np.abs(data["dde_res"]))[0])
    print("degree excess", logfit(data["pwide"][:80], np.abs(data["deg_h"])[:80])[0])


if __name__ == "__main__":
    main()
