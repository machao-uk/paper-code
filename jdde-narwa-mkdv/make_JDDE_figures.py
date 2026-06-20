#!/usr/bin/env python3

import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parent
FIG = ROOT / 'figures'
FIG.mkdir(exist_ok=True)

V0 = 1.0
rho0 = 0.3
beta = 0.5


def ep3_norm(tau):
    nilpotent = np.array(
        [[0.0, 1.0, 0.0],
         [0.0, 0.0, 1.0],
         [0.0, 0.0, 0.0]]
    )
    exp_nilpotent = np.eye(3) + tau * nilpotent + 0.5 * (tau ** 2) * (nilpotent @ nilpotent)
    return np.exp(beta * tau) * np.linalg.norm(exp_nilpotent, 2)


def normal_norm(tau):
    return np.exp(beta * tau)


def crossing(tau, values, level=1.0):
    tau = np.asarray(tau)
    values = np.asarray(values)
    indices = np.where(values >= level)[0]
    if len(indices) == 0:
        return None
    idx = int(indices[0])
    if idx == 0:
        return float(tau[0])
    x0, x1 = tau[idx - 1], tau[idx]
    y0, y1 = values[idx - 1], values[idx]
    return float(x0 + (level - y0) * (x1 - x0) / (y1 - y0))


def save(fig, name):
    fig.tight_layout()
    fig.savefig(FIG / f'{name}.pdf')
    plt.close(fig)


time_grid = np.linspace(0.0, 5.0, 400)
res_normal = np.ones_like(time_grid)
res_ep2 = [
    np.linalg.norm(np.eye(2) + tau * np.array([[0.0, 1.0], [0.0, 0.0]]), 2)
    for tau in time_grid
]
res_ep3 = [ep3_norm(tau) / np.exp(beta * tau) for tau in time_grid]

fig, ax = plt.subplots(figsize=(6.5, 4.2))
ax.plot(time_grid, res_normal, label='normal')
ax.plot(time_grid, res_ep2, label='EP2')
ax.plot(time_grid, res_ep3, label='EP3')
ax.set_xlabel('delay $\\tau$')
ax.set_ylabel('rescaled norm')
ax.set_title('Non-normal matrix amplification')
ax.legend()
save(fig, 'fig_matrix_amplification')


delay_grid = np.linspace(0.3, 2.5, 160)
D_normal = rho0 * np.array([normal_norm(tau) for tau in delay_grid])
D_ep3 = rho0 * np.array([ep3_norm(tau) for tau in delay_grid])
tau_normal = crossing(delay_grid, D_normal / V0)
tau_ep3 = crossing(delay_grid, D_ep3 / V0)


tau0 = 0.85
gap_normal = V0 - rho0 * normal_norm(tau0)
gap_ep3 = V0 - rho0 * ep3_norm(tau0)
time_response = np.linspace(0.0, 18.0, 300)
base_response = 1.0 + 0.18 * np.exp(-0.55 * time_response) * np.sin(1.6 * time_response) ** 2
response_normal = base_response * np.exp(-0.42 * gap_normal * time_response)
response_ep3 = (
    1.0 + 0.30 * np.exp(-0.35 * time_response) * np.sin(1.6 * time_response + 0.35) ** 2
) * np.exp(-0.42 * gap_ep3 * time_response)

fig, ax = plt.subplots(figsize=(6.5, 4.2))
ax.plot(time_response, response_normal, label='normal')
ax.plot(time_response, response_ep3, label='EP3')
ax.set_xlabel('time')
ax.set_ylabel('response indicator')
ax.set_title('Illustrative response profile, $\\tau_0=0.85$')
ax.legend()
save(fig, 'fig_transient_energy')


avg_normal = 0.18 + 0.35 / (np.maximum(V0 - D_normal, 0.05) + 0.45)
avg_ep3 = 0.18 + 0.35 / (np.maximum(V0 - D_ep3, 0.05) + 0.45)

fig, ax = plt.subplots(figsize=(6.5, 4.2))
ax.plot(delay_grid, avg_normal, label='normal')
ax.plot(delay_grid, avg_ep3, label='EP3')
if tau_ep3 is not None:
    ax.axvline(tau_ep3, linestyle='--', alpha=0.7, label='EP3 criterion')
if tau_normal is not None:
    ax.axvline(tau_normal, linestyle=':', alpha=0.8, label='normal criterion')
ax.set_xlabel('delay $\\tau$')
ax.set_ylabel('late-window indicator')
ax.set_title('Delay scan: admissible-window comparison')
ax.legend()
save(fig, 'fig_delay_scan_avg')


hist_normal = np.where(D_normal < V0, 1.0 / (V0 - D_normal + 0.08), np.nan)
hist_ep3 = np.where(D_ep3 < V0, 1.0 / (V0 - D_ep3 + 0.08), np.nan)

fig, ax = plt.subplots(figsize=(6.5, 4.2))
ax.plot(delay_grid, hist_normal, label='normal')
ax.plot(delay_grid, hist_ep3, label='EP3')
if tau_ep3 is not None:
    ax.axvline(tau_ep3, linestyle='--', alpha=0.7, label='EP3 criterion')
if tau_normal is not None:
    ax.axvline(tau_normal, linestyle=':', alpha=0.8, label='normal criterion')
ax.set_xlabel('delay $\\tau$')
ax.set_ylabel('history-window indicator')
ax.set_title('History-window indicator on admissible side')
ax.legend()
save(fig, 'fig_delay_scan_hist')


time_tail = np.linspace(0.0, 20.0, 300)
radii = [10, 15, 20, 25, 30]

fig, ax = plt.subplots(figsize=(6.5, 4.2))
for radius in radii:
    tail_profile = (
        np.exp(-0.20 * time_tail)
        * np.exp(-(radius - 10.0) / 8.0)
        * (0.05 + 0.02 * np.sin(0.8 * time_tail) ** 2)
    )
    ax.plot(time_tail, tail_profile, label=f'$R={radius}$')
ax.set_xlabel('time')
ax.set_ylabel('far-field mass indicator')
ax.set_title('Schematic tail profile')
ax.legend()
save(fig, 'fig_tail_decay')


params = {
    'V0': V0,
    'rho0': rho0,
    'beta': beta,
    'tau0_for_response_plot': tau0,
    'normal_D_over_V0_at_tau0': float(rho0 * normal_norm(tau0) / V0),
    'ep3_D_over_V0_at_tau0': float(rho0 * ep3_norm(tau0) / V0),
    'normal_gap_at_tau0': float(gap_normal),
    'ep3_gap_at_tau0': float(gap_ep3),
    'tau_normal_criterion': tau_normal,
    'tau_ep3_criterion': tau_ep3,
    'note': (
        'The response plot uses tau0=0.85, where both channels satisfy D_tau < V0. '
        'The delay-scan indicators are algebraic functions of the admissibility gap, '
        'and the tail plot is schematic rather than a PDE computation.'
    ),
}

with open(FIG / 'figure_parameters.json', 'w', encoding='utf-8') as handle:
    json.dump(params, handle, indent=2)

print(json.dumps(params, indent=2))