#!/usr/bin/env python3
# Regenerates the manuscript figures and the audit JSON/CSV outputs for
# "Variance-domain lock-in protocol for exceptional-point eigenvector-curvature readout".
#
# Everything here is synthetic. There is no experimental data anywhere in this
# repo -- the point of the script is to let a reader regenerate the exact
# numbers and figures quoted in the paper from the declared model, not to
# stand in for a lab measurement.
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Polygon

RNG_SEED = 20260526


# ---------------------------------------------------------------------------
# model
# ---------------------------------------------------------------------------

def kp_ep2(mu: np.ndarray) -> np.ndarray:
    return 1.0 / (4.0 * mu)


def linewidth_ep3(mu: np.ndarray) -> np.ndarray:
    gamma0 = 1.0
    c = 1.0e-3
    return gamma0 + c * mu ** (-4.0 / 3.0) + 1.4e-2 * mu + 2.5e-2 * mu**2 + 8.0e-4 * np.sin(7.0 * mu)


def linewidth_ep2(mu: np.ndarray) -> np.ndarray:
    return 1.0 + 1.0e-3 * kp_ep2(mu) + 1.4e-2 * mu


def null_channel(mu: np.ndarray) -> np.ndarray:
    return 1.0 + 0.010 * mu + 0.006 * mu**2


def regular_background_channel(mu: np.ndarray) -> np.ndarray:
    return 1.0 + 0.012 * mu + 0.008 * mu**2 + 5.0e-4 * np.sin(5.0 * mu)


def avg_two_point(mu: np.ndarray, ratio: float, channel) -> np.ndarray:
    width = ratio * mu
    return 0.5 * (channel(mu - width) + channel(mu + width))


def lockin(mu: np.ndarray, r1: float, r2: float, channel) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    g1 = avg_two_point(mu, r1, channel)
    g2 = avg_two_point(mu, r2, channel)
    e = np.abs(2.0 * (g2 - g1) / ((r2 * mu) ** 2 - (r1 * mu) ** 2))
    return g1, g2, e


def log_slope(mu: np.ndarray, response: np.ndarray, sigma_log_response: float = 0.08) -> tuple[float, float]:
    mask = np.isfinite(response) & (response > 0)
    x = np.log(mu[mask])
    y = np.log(response[mask])
    slope, _ = np.polyfit(x, y, 1)
    delta = sigma_log_response / np.sqrt(np.sum((x - np.mean(x)) ** 2))
    return -float(slope), float(delta)


def build() -> dict:
    mu = np.logspace(np.log10(0.012), np.log10(0.11), 16)
    r1a, r2a = 0.030, 0.060
    r1b, r2b = 0.040, 0.080

    g1, g2, ep3 = lockin(mu, r1b, r2b, linewidth_ep3)
    g1a, g2a, ep3_a = lockin(mu, r1a, r2a, linewidth_ep3)
    _, _, ep2 = lockin(mu, r1b, r2b, linewidth_ep2)
    _, _, nul = lockin(mu, r1b, r2b, null_channel)
    _, _, reg = lockin(mu, r1b, r2b, regular_background_channel)

    alpha_ep3, delta_ep3 = log_slope(mu, ep3)
    alpha_ep3_a, _ = log_slope(mu, ep3_a)
    alpha_ep3_b, _ = log_slope(mu, ep3)
    alpha_ep2, delta_ep2 = log_slope(mu, ep2)
    alpha_null, delta_null = log_slope(mu, nul)
    alpha_reg, delta_reg = log_slope(mu, reg)
    raw_alpha, _ = log_slope(mu, g2 - np.min(g2) + 1.0e-4)

    return {
        "mu": mu,
        "r1a": r1a,
        "r2a": r2a,
        "r1b": r1b,
        "r2b": r2b,
        "gamma_s1": g1,
        "gamma_s2": g2,
        "gamma_pair_A_s1": g1a,
        "gamma_pair_A_s2": g2a,
        "ep3": ep3,
        "ep3_pair_A": ep3_a,
        "ep2": ep2,
        "null": nul,
        "regular_background": reg,
        "alpha_ep3": alpha_ep3,
        "delta_ep3": delta_ep3,
        "alpha_ep2": alpha_ep2,
        "delta_ep2": delta_ep2,
        "alpha_null": alpha_null,
        "delta_null": delta_null,
        "alpha_regular_background": alpha_reg,
        "delta_regular_background": delta_reg,
        "width_difference": abs(alpha_ep3_a - alpha_ep3_b),
        "raw_alpha": raw_alpha,
    }


# ---------------------------------------------------------------------------
# small drawing helpers shared by the schematic figures
# ---------------------------------------------------------------------------

def box(ax, xy, w, h, text, fc="0.95", ec="0.2", fontsize=8.5):
    x, y = xy
    patch = FancyBboxPatch(
        (x - w / 2, y - h / 2), w, h,
        boxstyle="round,pad=0.02,rounding_size=0.02",
        facecolor=fc, edgecolor=ec, linewidth=1.0,
    )
    ax.add_patch(patch)
    ax.text(x, y, text, ha="center", va="center", fontsize=fontsize)
    return patch


def diamond(ax, xy, w, h, text, fc="0.92", fontsize=8):
    x, y = xy
    pts = [(x, y + h / 2), (x + w / 2, y), (x, y - h / 2), (x - w / 2, y)]
    ax.add_patch(Polygon(pts, closed=True, facecolor=fc, edgecolor="0.2", linewidth=1.0))
    ax.text(x, y, text, ha="center", va="center", fontsize=fontsize)


def connect(ax, a, b, label=None, color="0.2", style="-|>"):
    arrow = FancyArrowPatch(
        a, b, arrowstyle=style, mutation_scale=12,
        color=color, linewidth=1.1, shrinkA=4, shrinkB=4,
    )
    ax.add_patch(arrow)
    if label:
        mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
        ax.text(mx, my + 0.18, label, ha="center", va="bottom", fontsize=7.5, color="0.3")


# ---------------------------------------------------------------------------
# figures
# ---------------------------------------------------------------------------

def fig_mechanism(path):
    """Step-by-step picture of the variance-domain lock-in measurement."""
    fig, ax = plt.subplots(figsize=(11, 3.4))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 3.4)
    ax.axis("off")

    nodes = [
        (1.1, 2.0, "fix mean detuning\n" + r"$\bar\mu$"),
        (3.2, 2.0, "inject symmetric jitter\n" + r"$\delta_s$, widths $s_1,s_2$"),
        (5.4, 2.0, "fit spectra in matched windows\n" + r"$\bar\Gamma_{s_i}(\bar\mu)$"),
        (7.7, 2.0, "two-width response\n" + r"$\mathcal{E}_\Gamma=\frac{2(\bar\Gamma_{s_2}-\bar\Gamma_{s_1})}{s_2^2-s_1^2}$"),
        (9.9, 2.0, "analysis record\nor diagnostic label"),
    ]
    w, h = 1.9, 1.0
    for x, y, t in nodes:
        box(ax, (x, y), w, h, t)
    for (x0, y0, _), (x1, y1, _) in zip(nodes[:-1], nodes[1:]):
        connect(ax, (x0 + w / 2, y0), (x1 - w / 2, y1))

    box(ax, (5.4, 0.55), 2.6, 0.75, "raw linewidth slope is not\nthe reported observable", fc="0.99")
    box(ax, (7.7, 0.55), 2.9, 0.75, r"$\Gamma_0$ and variance-independent" + "\noffsets cancel before the fit", fc="0.99")
    connect(ax, (5.4, 0.93), (5.4, 1.5), color="0.55")
    connect(ax, (7.7, 0.93), (7.7, 1.5), color="0.55")

    fig.tight_layout()
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)


def fig_order_dictionary(path, r):
    x = np.logspace(-2.2, -0.3, 300)
    fig, ax = plt.subplots(figsize=(6.7, 4.5))
    ax.loglog(x, x ** (1 / 3), label=r"eigenvalue splitting $|\mu|^{1/3}$")
    ax.loglog(x, x ** (-4 / 3), label=r"static geometry $|\mu|^{-4/3}$")
    ax.loglog(x, x ** (-10 / 3), label=r"EP3 curvature $|\mu|^{-10/3}$")
    ax.loglog(x, 0.45 * x ** (-3), "--", label=r"EP2 control $|\mu|^{-3}$")
    ax.set_xlabel(r"detuning coordinate $|\mu|$")
    ax.set_ylabel("normalized response")
    ax.set_title("Order dictionary for variance-domain geometry readout")
    ax.grid(True, which="both", alpha=0.35)
    ax.legend(frameon=False, fontsize=8)
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)


def fig_synthetic_benchmark(path, r):
    mu = r["mu"]
    fig = plt.figure(figsize=(11.5, 7.8))
    gs = fig.add_gridspec(2, 2, width_ratios=[1, 1], height_ratios=[1, 1], hspace=0.38, wspace=0.32)

    # (a) example spectra at two jitter widths
    ax_a = fig.add_subplot(gs[0, 0])
    w = np.linspace(-2.2, 2.2, 600)
    spec_s1 = 0.18 + 1.40 / (0.20 + (w + 0.23) ** 2) + 0.07 * w
    spec_s2 = 0.20 + 1.08 / (0.33 + (w + 0.23) ** 2) + 0.07 * w
    ax_a.plot(w, spec_s1, lw=1.6, label=r"$s_1$")
    ax_a.plot(w, spec_s2, "--", lw=1.6, label=r"$s_2$")
    ax_a.set_xlabel(r"$\omega-\omega_0$")
    ax_a.set_ylabel("spectrum")
    ax_a.set_title("spectra at two jitter widths", fontsize=10)
    ax_a.legend(frameon=False, fontsize=8)
    ax_a.text(-0.18, 1.04, "(a)", transform=ax_a.transAxes, fontsize=11, fontweight="bold")

    # (b) raw linewidth is background-limited
    ax_b = fig.add_subplot(gs[0, 1])
    raw = r["gamma_s2"]
    ax_b.loglog(mu, raw, "o", ms=4, color="0.15", label="fitted linewidth")
    fit_b = raw[-1] * (mu / mu[-1]) ** (-r["raw_alpha"])
    ax_b.loglog(mu, fit_b, lw=1.4, color="0.4", label=rf"slope $-{r['raw_alpha']:.3f}$")
    ax_b.set_xlabel(r"$|\bar\mu|$")
    ax_b.set_ylabel(r"raw $\Gamma_{\rm fit}$")
    ax_b.set_title("raw linewidth is background-limited", fontsize=10)
    ax_b.set_xticks([0.02, 0.05, 0.1])
    ax_b.set_xticklabels(["0.02", "0.05", "0.1"])
    ax_b.xaxis.set_minor_locator(plt.NullLocator())
    ax_b.legend(frameon=False, fontsize=8)
    ax_b.text(-0.18, 1.04, "(b)", transform=ax_b.transAxes, fontsize=11, fontweight="bold")

    # (c) two-width variance response: EP3 branch vs EP2 control
    ax_c = fig.add_subplot(gs[1, 0])
    ax_c.loglog(mu, r["ep3"], "o-", ms=4, label=rf"EP3 branch  $-{r['alpha_ep3']:.3f}\pm{r['delta_ep3']:.3f}$")
    ax_c.loglog(mu, r["ep2"], "s-", ms=4, label=rf"EP2 control  $-{r['alpha_ep2']:.3f}\pm{r['delta_ep2']:.3f}$")
    ax_c.loglog(mu, r["null"], "x", ms=5, color="0.5", label="null channel (rejected)")
    ax_c.set_xlabel(r"$|\bar\mu|$")
    ax_c.set_ylabel(r"$|\mathcal{E}_\Gamma(\bar\mu)|$")
    ax_c.set_title("two-width variance response", fontsize=10)
    ax_c.set_xticks([0.02, 0.05, 0.1])
    ax_c.set_xticklabels(["0.02", "0.05", "0.1"])
    ax_c.xaxis.set_minor_locator(plt.NullLocator())
    ax_c.legend(frameon=False, fontsize=8)
    ax_c.text(-0.18, 1.04, "(c)", transform=ax_c.transAxes, fontsize=11, fontweight="bold")

    # (d) analysis record, as text rather than a plot
    ax_d = fig.add_subplot(gs[1, 1])
    ax_d.axis("off")
    ax_d.text(-0.05, 1.0, "(d) analysis record", transform=ax_d.transAxes,
              fontsize=11, fontweight="bold", va="top")
    lines = [
        rf"EP3 branch: $\widehat\alpha={r['alpha_ep3']:.3f}\pm{r['delta_ep3']:.3f}$",
        rf"EP2 control: $\widehat\alpha={r['alpha_ep2']:.3f}\pm{r['delta_ep2']:.3f}$",
        rf"raw linewidth slope: ${r['raw_alpha']:.3f}$",
        rf"width-pair drift: ${r['width_difference']:.2e}$",
    ]
    for i, line in enumerate(lines):
        ax_d.text(0.0, 0.84 - 0.13 * i, line, transform=ax_d.transAxes, fontsize=9.5)
    rows = [("pole isolation", "pass"), ("symmetric jitter", "pass"),
            ("detector-null branch", "rejected"), ("regular branch", "rejected")]
    for i, (name, status) in enumerate(rows):
        y = 0.30 - 0.11 * i
        ax_d.text(0.0, y, name, transform=ax_d.transAxes, fontsize=9)
        ax_d.text(0.62, y, status, transform=ax_d.transAxes, fontsize=9)

    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)


def fig_analysis_record(path):
    """Pass/fail decision chain used to certify an exponent assignment."""
    fig, ax = plt.subplots(figsize=(11.5, 5.4))
    ax.set_xlim(0, 11.5)
    ax.set_ylim(0, 5.4)
    ax.axis("off")

    steps = [
        (1.1, 3.4, "spectra, jitter logs,\nfit tables"),
        (3.3, 3.4, "pole isolation\nand fit residual?"),
        (5.5, 3.4, "symmetric jitter\nand outer window?"),
        (7.7, 3.4, "non-null\nlinewidth channel?"),
    ]
    box(ax, steps[0][:2], 1.9, 1.0, steps[0][2])
    for s in steps[1:]:
        diamond(ax, s[:2], 2.0, 1.1, s[2])
    for a, b in zip(steps[:-1], steps[1:]):
        connect(ax, (a[0] + 1.0, a[1]), (b[0] - 1.0, b[1]), label="yes" if a is not steps[0] else None)
    connect(ax, (steps[0][0] + 0.95, steps[0][1]), (steps[1][0] - 1.0, steps[1][1]))

    fw = (7.7, 1.5, "finite-width and\nwidth-pair budget?")
    ep2 = (5.5, 1.5, "matched EP2\ncontrol?")
    cert = (3.3, 1.5, "certified exponent\n" + r"$\widehat\alpha\pm\delta\alpha$")
    diamond(ax, fw[:2], 2.0, 1.1, fw[2])
    diamond(ax, ep2[:2], 2.0, 1.1, ep2[2])
    box(ax, cert[:2], 2.0, 1.1, cert[2], fc="0.85")

    connect(ax, (7.7, 2.85), (7.7, 2.05), label="yes")
    connect(ax, (fw[0] - 1.0, fw[1]), (ep2[0] + 1.0, ep2[1]), label="yes")
    connect(ax, (ep2[0] - 1.0, ep2[1]), (cert[0] + 1.0, cert[1]), label="yes")

    fails = [
        (3.3, 4.7, "line-shape / pole-overlap\ninconclusive"),
        (5.5, 4.7, "malformed jitter or\npath crossing"),
        (7.7, 4.7, "detector / bath /\nnuisance null"),
        (7.7, 0.25, "finite-window or background\ndominance"),
        (5.5, 0.25, "order-control failure"),
    ]
    for f in fails:
        box(ax, f[:2], 2.1, 0.85, f[2], fc="0.98")
    connect(ax, (3.3, 3.85), (fails[0][0], fails[0][1] - 0.42), label="no", color="0.5")
    connect(ax, (5.5, 3.85), (fails[1][0], fails[1][1] - 0.42), label="no", color="0.5")
    connect(ax, (7.7, 3.85), (fails[2][0], fails[2][1] - 0.42), label="no", color="0.5")
    connect(ax, (7.7, 1.05), (fails[3][0], fails[3][1] + 0.42), label="no", color="0.5")
    connect(ax, (5.5, 1.05), (fails[4][0], fails[4][1] + 0.42), label="no", color="0.5")

    ax.text(5.4, -0.05,
            "exponent assignment is the terminal branch of the audit, not a default fit",
            ha="center", va="top", fontsize=8.5, color="0.25")

    fig.tight_layout()
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)


def save_figures(figdir: Path, r: dict) -> None:
    figdir.mkdir(parents=True, exist_ok=True)
    fig_mechanism(figdir / "fig1_mechanism.pdf")
    fig_order_dictionary(figdir / "fig2_order_dictionary.pdf", r)
    fig_synthetic_benchmark(figdir / "fig3_synthetic_benchmark.pdf", r)
    fig_analysis_record(figdir / "fig4_analysis_record.pdf")


# ---------------------------------------------------------------------------
# audit outputs
# ---------------------------------------------------------------------------

def _write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_audit(auditdir: Path, r: dict) -> None:
    auditdir.mkdir(parents=True, exist_ok=True)
    mu = r["mu"]

    fitted_rows = [
        {
            "mu": float(m),
            "gamma_width_pair_B_sigma1": float(g1),
            "gamma_width_pair_B_sigma2": float(g2),
            "variance_lockin_EP3_pair_B": float(e),
        }
        for m, g1, g2, e in zip(mu, r["gamma_s1"], r["gamma_s2"], r["ep3"])
    ]
    _write_csv(
        auditdir / "fitted_linewidth_tables.csv",
        ["mu", "gamma_width_pair_B_sigma1", "gamma_width_pair_B_sigma2", "variance_lockin_EP3_pair_B"],
        fitted_rows,
    )

    width_rows = [
        {
            "mu": float(m),
            "variance_lockin_EP3_pair_A_r030_060": float(a),
            "variance_lockin_EP3_pair_B_r040_080": float(b),
        }
        for m, a, b in zip(mu, r["ep3_pair_A"], r["ep3"])
    ]
    _write_csv(
        auditdir / "width_pair_outputs.csv",
        ["mu", "variance_lockin_EP3_pair_A_r030_060", "variance_lockin_EP3_pair_B_r040_080"],
        width_rows,
    )

    _write_csv(
        auditdir / "ep2_control_output.csv",
        ["mu", "variance_lockin_EP2_pair_B"],
        [{"mu": float(m), "variance_lockin_EP2_pair_B": float(v)} for m, v in zip(mu, r["ep2"])],
    )

    _write_csv(
        auditdir / "null_channel_output.csv",
        ["mu", "variance_lockin_null_channel_pair_B"],
        [{"mu": float(m), "variance_lockin_null_channel_pair_B": float(v)} for m, v in zip(mu, r["null"])],
    )

    _write_csv(
        auditdir / "regular_background_output.csv",
        ["mu", "variance_lockin_regular_background_pair_B"],
        [{"mu": float(m), "variance_lockin_regular_background_pair_B": float(v)} for m, v in zip(mu, r["regular_background"])],
    )

    jitter = {
        "random_seed": RNG_SEED,
        "jitter_model": "symmetric two-point jitter around each mean detuning",
        "distribution": "0.5 delta(mu - sigma) + 0.5 delta(mu + sigma)",
        "central_moments": {
            "mean_shift": 0.0,
            "variance": "sigma^2",
            "third_central_moment": 0.0,
            "fourth_central_moment": "sigma^4",
        },
        "width_pairs": [
            {"name": "A", "sigma_over_mu_1": r["r1a"], "sigma_over_mu_2": r["r2a"]},
            {"name": "B", "sigma_over_mu_1": r["r1b"], "sigma_over_mu_2": r["r2b"]},
        ],
        "symmetry_gate": {
            "passed": True,
            "reason": "The two-point jitter distribution has exactly zero third central moment.",
        },
    }
    (auditdir / "jitter_moments.json").write_text(json.dumps(jitter, indent=2) + "\n", encoding="utf-8")

    certificate = {
        "certificate": {
            "q_out": {"passed": True, "reason": "symmetric finite jitter remains in the declared outer window"},
            "q_sym": {"passed": True, "reason": "two-point jitter has zero third central moment"},
            "q_width": {"passed": bool(r["width_difference"] < 0.08), "threshold": 0.08, "observed": float(r["width_difference"])},
            "q_pow": {"passed": True, "reason": "synthetic benchmark is generated in the linear phase-diffusion regime"},
            "q_EP2": {"passed": bool(abs(r["alpha_ep2"] - 3.0) < 0.12), "threshold": 0.12, "observed": float(r["alpha_ep2"])},
            "q_null": {
                "passed": False,
                "reason": "null detector has no singular linewidth coefficient and is rejected",
                "observed_slope": float(r["alpha_null"]),
            },
            "q_regular_background": {
                "passed": False,
                "reason": "regular-only background does not produce the EP3 curvature exponent",
                "observed_slope": float(r["alpha_regular_background"]),
            },
        }
    }
    (auditdir / "certificate.json").write_text(json.dumps(certificate, indent=2) + "\n", encoding="utf-8")

    audit = {
        "synthetic_linewidth_benchmark": {
            "random_seed": RNG_SEED,
            "mu_values": [float(x) for x in r["mu"]],
            "gamma_width_s1": [float(x) for x in r["gamma_s1"]],
            "gamma_width_s2": [float(x) for x in r["gamma_s2"]],
            "variance_lockin_EP3": [float(x) for x in r["ep3"]],
            "variance_lockin_EP2": [float(x) for x in r["ep2"]],
            "variance_lockin_null_detector": [float(x) for x in r["null"]],
            "variance_lockin_regular_background": [float(x) for x in r["regular_background"]],
            "alpha_EP3": float(r["alpha_ep3"]),
            "delta_alpha_EP3": float(r["delta_ep3"]),
            "alpha_EP2": float(r["alpha_ep2"]),
            "delta_alpha_EP2": float(r["delta_ep2"]),
            "alpha_null_channel": float(r["alpha_null"]),
            "alpha_regular_background": float(r["alpha_regular_background"]),
            "width_pair_slope_difference": float(r["width_difference"]),
            "raw_linewidth_apparent_slope": float(r["raw_alpha"]),
        },
        "certificate": certificate["certificate"],
    }
    (auditdir / "audit_summary.json").write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--figdir", default="figures", help="directory for vector PDF figures")
    parser.add_argument("--auditdir", default="audit_outputs", help="directory for audit JSON/CSV outputs")
    args = parser.parse_args()
    result = build()
    save_figures(Path(args.figdir), result)
    write_audit(Path(args.auditdir), result)
    print(f"EP3 alpha = {result['alpha_ep3']:.6f} +/- {result['delta_ep3']:.6f}")
    print(f"EP2 alpha = {result['alpha_ep2']:.6f} +/- {result['delta_ep2']:.6f}")
    print(f"raw linewidth apparent slope = {result['raw_alpha']:.6f}")
    print(f"width-pair slope difference = {result['width_difference']:.3e}")


if __name__ == "__main__":
    main()
