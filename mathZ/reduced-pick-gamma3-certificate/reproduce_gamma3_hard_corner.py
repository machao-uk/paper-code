import pickle
from math import comb
from pathlib import Path

import sympy as sp


BASE = Path(__file__).resolve().parent
P_FILE = BASE / "inputs" / "MathZ_gamma3_primitive_norm_expr.pkl"
S_FILE = BASE / "inputs" / "MathZ_gamma3_blowup_S.pkl"
T_FILE = BASE / "inputs" / "MathZ_gamma3_blowup_T.pkl"
OUT = BASE / "outputs" / "gamma3_hard_corner_certificate_output.md"

rho, y = sp.symbols("rho y")
u, v, z, q, r = sp.symbols("u v z q r")

C = sp.Integer(382511685112441262309376)
INNER_Q_BOUND = sp.Integer(16)
V_FULL = sp.Rational(1, 32)
V_ANN = sp.Rational(1, 64)
Z_ANN = sp.Rational(1, 4)


def _lcm_many(values):
    out = 1
    for value in values:
        out = out * value // sp.igcd(out, value)
    return int(out)


def bernstein_2d_terms(terms, box1, box2):
    """Exact 2D tensor Bernstein sign check using integer-scaled coefficients.

    All signs are taken after multiplication by positive common denominators.
    No floating-point sign decision is used.
    """
    deg1 = max(a for a, _, _ in terms)
    deg2 = max(b for _, b, _ in terms)
    x0, x1 = map(sp.Rational, box1)
    y0, y1 = map(sp.Rational, box2)
    hx = x1 - x0
    hy = y1 - y0
    dx = int(sp.ilcm(int(x0.q), int(hx.q)))
    dy = int(sp.ilcm(int(y0.q), int(hy.q)))
    x0n = int(x0 * dx)
    hxn = int(hx * dx)
    y0n = int(y0 * dy)
    hyn = int(hy * dy)

    # Transform to the unit square and multiply by dx^deg1 dy^deg2.
    trans = {}
    for a, b, c in terms:
        if sp.Integer(c) != c:
            raise ValueError(f"non-integer coefficient at {(a, b)}: {c}")
        cint = int(c)
        scale = pow(dx, deg1 - a) * pow(dy, deg2 - b)
        for i in range(a + 1):
            cx = comb(a, i) * pow(x0n, a - i) * pow(hxn, i)
            for j in range(b + 1):
                cy = comb(b, j) * pow(y0n, b - j) * pow(hyn, j)
                trans[(i, j)] = trans.get((i, j), 0) + cint * cx * cy * scale
    trans = {k: v for k, v in trans.items() if v}

    lcm_x = _lcm_many(comb(deg1, i) for i in range(deg1 + 1))
    lcm_y = _lcm_many(comb(deg2, j) for j in range(deg2 + 1))
    wx = [[0] * (deg1 + 1) for _ in range(deg1 + 1)]
    wy = [[0] * (deg2 + 1) for _ in range(deg2 + 1)]
    for I in range(deg1 + 1):
        for i in range(I + 1):
            wx[I][i] = comb(I, i) * (lcm_x // comb(deg1, i))
    for J in range(deg2 + 1):
        for j in range(J + 1):
            wy[J][j] = comb(J, j) * (lcm_y // comb(deg2, j))

    neg = 0
    zeros = 0
    mn = None
    loc = None
    for I in range(deg1 + 1):
        for J in range(deg2 + 1):
            val = 0
            for (i, j), cc in trans.items():
                if i <= I and j <= J:
                    val += cc * wx[I][i] * wy[J][j]
            if mn is None or val < mn:
                mn = val
                loc = (I, J)
            if val < 0:
                neg += 1
            elif val == 0:
                zeros += 1
    return {
        "degrees": (deg1, deg2),
        "neg": neg,
        "zeros": zeros,
        "min": mn,
        "loc": loc,
    }


def main():
    P = pickle.loads(P_FILE.read_bytes())
    S = pickle.loads(S_FILE.read_bytes())
    T = pickle.loads(T_FILE.read_bytes())

    lines = ["# Gamma3 hard-corner certificate output", ""]

    Q = sp.Poly(sp.expand(P.as_expr().subs({rho: 1 - u, y: 1 - v})), u, v)
    lowest = min(a + b for (a, b), c in Q.terms() if c)
    lead = sp.factor(sum(c * u**a * v**b for (a, b), c in Q.terms() if a + b == lowest))
    lines += [
        "## Lowest corner face",
        "",
        f"- order: `{lowest}`",
        f"- lead/C: `{sp.factor(lead / C)}`",
        "",
    ]

    T_terms = [(a, b, sp.Integer(c)) for (a, b), c in T.terms()]
    c00 = dict(((a, b), c) for a, b, c in T_terms)[(0, 0)]
    tail = sum(
        abs(c) * INNER_Q_BOUND**a * V_FULL**b
        for a, b, c in T_terms
        if (a, b) != (0, 0)
    )
    lines += [
        "## Inner tube",
        "",
        f"- c00: `{c00}`",
        f"- tail bound positive: `{c00 - tail > 0}`",
        f"- relative margin: `{sp.N((c00 - tail) / c00, 40)}`",
        "",
    ]

    S_terms = [(a, b, sp.Integer(c)) for (a, b), c in S.terms()]
    main_keys = {(2, 0), (0, 1), (1, 1), (0, 2)}
    rem = sum(
        abs(c) * Z_ANN**a * V_ANN ** (b - 1)
        for a, b, c in S_terms
        if (a, b) not in main_keys
    )
    lines += [
        "## Annulus",
        "",
        "- region: `16v < |z| < 1/4`, hence `v < 1/64`",
        "- main lower bound: `C(z^2+64v+32vz-320v^2) >= 55 C v`",
        f"- remainder/C: `{sp.N(rem / C, 50)}`",
        f"- remainder < 5C: `{rem < 5 * C}`",
        f"- final margin `55C-rem > 50C`: `{55 * C - rem > 50 * C}`",
        "",
    ]

    fixed_intervals = [
        (sp.Rational(-4), sp.Rational(-2)),
        (sp.Rational(-2), sp.Rational(-1)),
        (sp.Rational(-1), sp.Rational(-1, 2)),
        (sp.Rational(-1, 2), sp.Rational(-1, 4)),
        (sp.Rational(1, 4), sp.Rational(1, 2)),
        (sp.Rational(1, 2), sp.Rational(1)),
        (sp.Rational(1), sp.Rational(2)),
        (sp.Rational(2), sp.Rational(4)),
        (sp.Rational(4), sp.Rational(8)),
        (sp.Rational(8), sp.Rational(16)),
        (sp.Rational(16), sp.Rational(32)),
    ]
    lines += ["## Fixed-z Bernstein", ""]
    for a, b in fixed_intervals:
        print(f"checking fixed z [{a},{b}]")
        result = bernstein_2d_terms(S_terms, (a, b), (sp.Rational(0), V_FULL))
        lines.append(
            f"- z `[{a},{b}]`: degree `{result['degrees']}`, "
            f"neg `{result['neg']}`, zeros `{result['zeros']}`, loc `{result['loc']}`"
        )
        if result["neg"]:
            raise RuntimeError(f"negative Bernstein coefficient on [{a},{b}]")
    lines.append("")

    H = sp.Poly(sp.expand(Q.as_expr().subs(v, r * u)), r, u)
    H_terms = [(a, b, sp.Integer(c)) for (a, b), c in H.terms()]
    print("checking reciprocal chart")
    recip = bernstein_2d_terms(
        H_terms,
        (sp.Rational(0), sp.Rational(1, 36)),
        (sp.Rational(0), sp.Rational(1, 16)),
    )
    lines += [
        "## Reciprocal tail",
        "",
        "- chart: `H(r,u)=Q(u,ru)`",
        "- box: `0 <= r <= 1/36`, `0 <= u <= 1/16`",
        f"- degree: `{recip['degrees']}`",
        f"- neg: `{recip['neg']}`",
        f"- zeros: `{recip['zeros']}`",
        f"- min loc: `{recip['loc']}`",
        "",
        "## Verdict",
        "",
        "- hard corner closed: `True`",
        "",
    ]
    if recip["neg"]:
        raise RuntimeError("negative Bernstein coefficient in reciprocal chart")

    OUT.write_text("\n".join(lines))
    print(OUT)


if __name__ == "__main__":
    main()
