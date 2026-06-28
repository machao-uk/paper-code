import math
import random
from pathlib import Path

import numpy as np
import sympy as sp
from sympy.ntheory.modular import crt


PRIMES = [1_000_000_007, 1_000_000_009, 1_000_000_021, 1_000_000_033, 1_000_000_087, 1_000_000_093, 1_000_000_097, 1_000_000_103]
DEG = 40
PAIRS = [(1, 2), (1, 3), (2, 3)]


def solve_np(A, b, p):
    A = np.asarray(A, dtype=np.int64)
    b = np.asarray(b, dtype=np.int64).reshape((-1, 1))
    M = np.concatenate([A, b], axis=1)
    n, mp1 = M.shape
    m = mp1 - 1
    row = 0
    for col in range(m):
        nz = np.nonzero(M[row:, col] % p)[0]
        if nz.size == 0:
            continue
        piv = row + int(nz[0])
        if piv != row:
            M[[row, piv], :] = M[[piv, row], :]
        inv = pow(int(M[row, col] % p), p - 2, p)
        M[row, col:] = (M[row, col:] * inv) % p
        targets = np.nonzero(M[:, col] % p)[0]
        targets = targets[targets != row]
        for start in range(0, len(targets), 64):
            idx = targets[start : start + 64]
            fac = M[idx, col].copy().reshape((-1, 1))
            M[idx, col:] = (M[idx, col:] - fac * M[row, col:]) % p
        row += 1
        if row == n:
            break
    if row != m:
        raise RuntimeError(f"rank {row} < {m}")
    return [int(M[r, m] % p) for r in range(m)]


def phi_face(a, b, pair, p):
    inv768 = pow(768, p - 2, p)
    lam = [1, a % p, b % p, (-1 - a - b) % p]
    a2 = 0
    a1 = 0
    for i in range(4):
        for j in range(i + 1, 4):
            a2 = (a2 + lam[i] * lam[j]) % p
    for i in range(4):
        for j in range(i + 1, 4):
            for k in range(j + 1, 4):
                a1 = (a1 - lam[i] * lam[j] * lam[k]) % p
    a0 = lam[0] * lam[1] % p * lam[2] % p * lam[3] % p
    c1 = (-512 * a0 * a0 * a2 - 144 * a0 * a1 * a1 + 192 * a0 * pow(a2, 3, p) - 132 * a1 * a1 * a2 * a2 - 16 * pow(a2, 5, p)) % p
    c2 = (-288 * a0 * a1 * a2 + 108 * pow(a1, 3, p) + 8 * a1 * pow(a2, 3, p)) % p
    c3 = (-768 * a0 * a0 + 256 * a0 * a2 * a2 - 144 * a1 * a1 * a2 - 16 * pow(a2, 4, p)) % p
    rvals = [((c1 + c2 * z + c3 * z * z) * inv768) % p for z in lam]
    i, j = pair
    L = (c2 + c3 * (lam[i] + lam[j])) % p
    return (768 * 768 * (1 - rvals[i] * rvals[i]) % p * (1 - rvals[j] * rvals[j]) - L * L % p * (1 - lam[i] * lam[i]) % p * (1 - lam[j] * lam[j])) % p


def interpolate_coeffs(p, pair):
    mons = [(i, j) for i in range(DEG + 1) for j in range(DEG + 1 - i)]
    n = len(mons)
    rng = random.Random(9090 + p)
    pts = []
    vals = []
    while len(pts) < n:
        aa = rng.randrange(1, p)
        bb = rng.randrange(1, p)
        pts.append((aa, bb))
        vals.append(phi_face(aa, bb, pair, p))
    A = []
    for aa, bb in pts:
        ap = [1]
        bp = [1]
        for _ in range(DEG):
            ap.append(ap[-1] * aa % p)
            bp.append(bp[-1] * bb % p)
        A.append([ap[i] * bp[j] % p for i, j in mons])
    return mons, solve_np(A, vals, p)


def poly_mul(A, B, p):
    out = {}
    for (i, j), a in A.items():
        for (k, l), b in B.items():
            key = (i + k, j + l)
            out[key] = (out.get(key, 0) + a * b) % p
    return out


def poly_pow_linear(c, cu, cv, n, p):
    out = {(0, 0): 1}
    base = {}
    if c % p:
        base[(0, 0)] = c % p
    if cu % p:
        base[(1, 0)] = cu % p
    if cv % p:
        base[(0, 1)] = cv % p
    for _ in range(n):
        out = poly_mul(out, base, p)
    return out


def to_reference_monomial(mons, coeffs, p, tri):
    # Map reference simplex (u,v) to the given triangle:
    # (a,b)=p0 + u*(p1-p0) + v*(p2-p0).
    (a0, b0), (a1, b1), (a2, b2) = tri
    inv_denoms = []
    def modq(x):
        q = sp.Rational(x)
        return int(q.p % p) * pow(int(q.q % p), p - 2, p) % p
    ac = modq(a0)
    au = modq(a1 - a0)
    av = modq(a2 - a0)
    bc = modq(b0)
    bu = modq(b1 - b0)
    bv = modq(b2 - b0)
    out = {}
    pow_a = [poly_pow_linear(ac, au, av, n, p) for n in range(DEG + 1)]
    pow_b = [poly_pow_linear(bc, bu, bv, n, p) for n in range(DEG + 1)]
    for (i, j), c in zip(mons, coeffs):
        if not c:
            continue
        prod = poly_mul(pow_a[i], pow_b[j], p)
        for key, val in prod.items():
            out[key] = (out.get(key, 0) + c * val) % p
    return out


def reference_monomial_to_bern(poly, p):
    # On simplex u>=0,v>=0,u+v<=1, monomial coeffs d_pq to degree DEG Bernstein b_ij.
    bern = []
    for i in range(DEG + 1):
        for j in range(DEG + 1 - i):
            val = 0
            for (pp, qq), coeff in poly.items():
                if i >= pp and j >= qq:
                    num = math.comb(i, pp) * math.comb(j, qq)
                    den = math.comb(DEG, pp + qq)
                    val = (val + coeff * (num % p) * pow(den % p, p - 2, p)) % p
            bern.append(val)
    return bern


def rational_reconstruct(residue, modulus):
    bound = math.isqrt((modulus - 1) // 2)
    r0, r1 = modulus, residue
    t0, t1 = 0, 1
    while abs(r1) > bound:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        t0, t1 = t1, t0 - q * t1
    num, den = r1, t1
    if den < 0:
        num, den = -num, -den
    if den == 0 or den > bound or math.gcd(num, den) != 1 or (num - residue * den) % modulus:
        raise RuntimeError("rational reconstruction failed")
    return sp.Rational(num, den)


def run_pair(pair):
    base_tri = ((sp.Rational(-1), sp.Rational(-1)), (sp.Rational(-1), sp.Rational(1)), (sp.Rational(1), sp.Rational(-1)))
    p0, p1, p2 = base_tri
    m01 = ((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2)
    m12 = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
    m20 = ((p2[0] + p0[0]) / 2, (p2[1] + p0[1]) / 2)
    triangles = [base_tri, (p0, m01, m20), (m01, p1, m12), (m20, m12, p2), (m01, m12, m20)]

    coeffs_by_prime = []
    mons0 = None
    for p in PRIMES:
        mons, coeffs = interpolate_coeffs(p, pair)
        mons0 = mons if mons0 is None else mons0
        coeffs_by_prime.append((p, coeffs))
    modulus = math.prod(PRIMES)
    summaries = []
    for tri_idx, tri in enumerate(triangles):
        residues = []
        for p, coeffs in coeffs_by_prime:
            ref = to_reference_monomial(mons0, coeffs, p, tri)
            residues.append(reference_monomial_to_bern(ref, p))
        bern = []
        failures = 0
        for idx in range(len(residues[0])):
            residue = int(crt(PRIMES, [row[idx] for row in residues])[0] % modulus)
            try:
                bern.append(rational_reconstruct(residue, modulus))
            except RuntimeError:
                failures += 1
                bern.append(None)
        known = [x for x in bern if x is not None]
        summaries.append({
            "tri_idx": tri_idx,
            "tri": tri,
            "failures": failures,
            "nonneg": all(x >= 0 for x in known) and failures == 0,
            "min": min(known) if known else None,
            "max": max(known) if known else None,
            "zero": sum(1 for x in known if x == 0),
        })
    lines = [f"## pair `{pair}`", ""]
    for s in summaries:
        lines.append("")
        lines.append(f"## triangle `{s['tri_idx']}`")
        lines.append(f"- vertices: `{s['tri']}`")
        lines.append(f"- rational reconstruction failures: `{s['failures']}`")
        lines.append(f"- all reconstructed coefficients nonnegative: `{s['nonneg']}`")
        lines.append(f"- min coefficient: `{s['min']}`")
        lines.append(f"- max coefficient: `{s['max']}`")
        lines.append(f"- zero coefficient count: `{s['zero']}`")
    all_sub = all(s["nonneg"] for s in summaries[1:])
    return all_sub, "\n".join(lines)


def main():
    lines = [
        "# Boundary non-boundary pairs Bernstein CRT certificates",
        "",
        "Face: `lambda=(1,a,b,-1-a-b)`, triangle `(-1,-1),(-1,1),(1,-1)`.",
        "",
        f"- primes: `{PRIMES}`",
        f"- Bernstein coefficient count per triangle: `{(DEG + 1) * (DEG + 2) // 2}`",
        "- Certification criterion: the four depth-1 subtriangles all have nonnegative reconstructed Bernstein coefficients.",
        "",
    ]
    all_ok = True
    for pair in PAIRS:
        ok, text = run_pair(pair)
        all_ok = all_ok and ok
        lines.append(text)
        lines.append("")
        lines.append(f"- depth-1 subtriangle certificate for pair `{pair}`: `{ok}`")
        lines.append("")
    lines.append("## Consequence")
    lines.append("")
    if all_ok:
        lines.append("- All non-boundary pairs on the real boundary face `x1=1` are certified nonnegative by CRT-reconstructed rational Bernstein coefficients after one subdivision.")
    else:
        lines.append("- At least one non-boundary pair failed the depth-1 Bernstein certificate.")
    out = "\n".join(lines)
    Path("/Users/ray/Downloads/MathZ_boundary_phi12_bernstein_modcrt.md").write_text(out)
    with open("/Users/ray/Downloads/MathZ_contraction_proof.md", "a") as f:
        f.write("\n\n" + out + "\n")
    print(out)


if __name__ == "__main__":
    main()
