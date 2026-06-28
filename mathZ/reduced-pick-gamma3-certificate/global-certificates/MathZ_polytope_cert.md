# Polytope Bernstein/SOS certificate attempt

## SOS availability

No SDP/SOS stack is installed in this environment (`cvxpy`, `ncpol2sdpa`, `sostools` unavailable), so Putinar SOS certificates were not attempted computationally.

## Polytope vertices and triangulation

- vertices found: `6`
- vertices: `[[-1.0, -1.0, 1.0], [-1.0, 1.0, -1.0], [-1.0, 1.0, 1.0], [1.0, -1.0, -1.0], [1.0, -1.0, 1.0], [1.0, 1.0, -1.0]]`
- ConvexHull facets: `8`
- Delaunay tetrahedra: `4`

## P3/P7 polynomial data

- `P3 = 32-c1-c2+c3` degree `12`, monomials `246`
- `P7 = 32-c1+c2+c3` degree `12`, monomials `246`

## Tight family `{t,-t,0,0}`

```text
P3(t,-t,0) = -16*(t - 1)*(t + 1)*(t**8 + 2*t**6 + 2*t**4 + 2*t**2 + 2)
P7(t,-t,0) = -16*(t - 1)*(t + 1)*(t**8 + 2*t**6 + 2*t**4 + 2*t**2 + 2)
```

Equivalently,

```text
P3 = P7 = 16*(1-t^2)*(t^8 + 2*t^6 + 2*t^4 + 2*t^2 + 2),
```

which is nonnegative on `[-1,1]` and zero only at `t=±1`.

## Simplex Bernstein probe

A prototype simplex-Bernstein routine is included in the script, but the direct SymPy affine expansion of the degree-12 polynomial on every tetrahedron did not finish within the interactive time budget. I therefore did not report floating-point Bernstein coefficients as a certificate. A production version should use sparse polynomial composition over rational affine maps rather than `expand` on dense SymPy expressions.

## Rational substitution status

The Cayley substitution `xi=(1-ti^2)/(1+ti^2)` enforces `|xi|<1` for the first three coordinates but does not enforce `|x1+x2+x3|<1`; clearing denominators would certify a larger non-feasible domain and is therefore not directly useful for this polytope. A correct rational parametrization must also encode the slab constraint, or work in barycentric/simplex coordinates.

## Assessment

Task 4 is closed analytically by the displayed factorization on `{t,-t,0,0}`. The full polytope certificate is not closed. The generated vertex set and Delaunay triangulation provide the correct geometric starting point, but a rigorous certificate needs exact rational simplex Bernstein coefficients and subdivision, or an installed SDP/SOS solver for the Putinar certificate.
