# Machine certificate: n=4 reduced Pick matrix PSD

Interval-arithmetic verification that the reduced Pick matrix
Π^red_λ is positive semidefinite for every centred, non-confluent
quadruple λ_1,λ_2,λ_3,λ_4 ∈ D̄.

## Script

`n4_reduced_pick_certificate.jl` — Julia, requires `IntervalArithmetic.jl` v1.0.9.

```
julia -e 'import Pkg; Pkg.add("IntervalArithmetic")'   # first time only
julia n4_reduced_pick_certificate.jl
```

## Method

Adaptive bisection on the five-dimensional real parameter box
[0,R] × [-R,R]^4 (R = 0.97), with λ_4 = -(λ_1+λ_2+λ_3).
Each sub-box is certified PSD via interval Cholesky decomposition.
Boxes with inf|λ_j|² ≥ R² are classified as outside and covered
analytically by the radial blow-up lemma.

## Result

- Certified boxes : 903,346,265
- Outside domain  : 31,253,719
- Failed boxes    : 6  (all at λ_1≈λ_2, |λ_4|≈R; covered analytically)

Six sub-boxes of diameter ≤ 10⁻⁸ were not certified by interval
Cholesky. All six correspond to λ_1 ≈ λ_2 ≈ 0.485 (confluent stratum)
and |λ_4| ≈ R = 0.97 (truncation boundary). Positive semidefiniteness
at these limit points follows from Prop. 5.7 (confluent layers) and
the radial blow-up lemma in the associated paper.

## Paper

C. Ma, *Braid monodromy and the sharp non-normal operator bound at n=4*,
submitted to Mathematische Zeitschrift.
