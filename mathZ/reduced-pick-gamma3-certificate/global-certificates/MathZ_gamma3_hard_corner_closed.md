# Gamma3 hard corner closure by blow-up

## Claim

The remaining gamma3 hard corner at

```text
(rho,y) = (1,1),    rho in [3/4,1], y in [3/4,1]
```

is closed by the ridge blow-up.  In the resolved coordinates, the primitive norm polynomial is positive in the hard corner by elementary leading-term estimates plus finite away-ridge Bernstein checks.

This file records the analytic certificate.

The certificate is reproducible by running

```text
python3 ../reproduce_gamma3_hard_corner.py
```

The last verified output is

```text
../outputs/REFERENCE_OUTPUT.md
```

## Coordinates

Let

```text
u = 1-rho,
v = 1-y,
Q(u,v) = P(1-u,1-v),
```

where `P(rho,y)` is the primitive numerator for the gamma3 norm defect.

The hard box under consideration is contained in

```text
0 <= u <= 1/16,
0 <= v <= 1/32.
```

The exact sparse expansion of `Q` at `(0,0)` gives

```text
ord Q = 11,
Lead(Q) = C v^9 (u-4v)^2,
C = 382511685112441262309376 > 0.
```

Thus the false Bernstein negatives come from the square ridge

```text
u = 4v.
```

They are not sign changes of `Q`.

## Ridge chart

Set

```text
u = 4v + vz,
S(z,v) = Q(4v+vz,v) / v^11.
```

Then exact expansion gives

```text
S(z,v)
= C (z^2 + 64v + 32vz - 320v^2) + R(z,v),
```

where every monomial of `R` contains at least one power of `v`.

The geometric range near the corner is

```text
z >= -4
```

because `u=4v+vz >= 0`.

## Inner ridge tube

For the ultra-close ridge tube set

```text
z = vq,
T(q,v) = S(vq,v) / v = Q(4v+v^2q,v) / v^12.
```

The exact coefficient absolute-value bound on `T` gives

```text
T(q,v) > 0
```

on

```text
|q| <= 16,
0 <= v <= 1/32.
```

Equivalently,

```text
S(z,v) > 0
```

on

```text
|z| <= 16v,
0 <= v <= 1/32.
```

The exact bound used is

```text
c00 - sum_{(a,b) != (0,0)} |c_ab| 16^a (1/32)^b > 0,
```

with relative margin approximately

```text
0.11342350686993992 * c00.
```

The reproduced exact output records

```text
c00 = 24480747847196240787800064,
relative margin = 0.1134235068699399217319812498264692476821.
```

This closes the ridge itself.

## Annulus around the ridge

It remains to cover

```text
16v < |z| < 1/4.
```

This region is elementary.  Since `|z| < 1/4` and `16v < |z|`, we automatically have

```text
0 <= v < 1/64.
```

Write

```text
M(z,v) = C (z^2 + 64v + 32vz - 320v^2).
```

For `|z| >= 16v`, the worst case for the mixed term is `z < 0`.  Put `x=|z|`.  Then

```text
M/C >= x^2 - 32vx + 64v - 320v^2.
```

For `x >= 16v`, the right hand side is minimized at `x=16v`, hence

```text
M/C >= 64v - 576v^2.
```

Since `v <= 1/64`,

```text
64v - 576v^2 >= 55v.
```

Thus

```text
M(z,v) >= 55 C v.
```

The exact sparse coefficient bound for the remainder on

```text
|z| <= 1/4,
0 <= v <= 1/64
```

is

```text
|R(z,v)| <= v * sum |r_ab| (1/4)^a (1/64)^(b-1)
          < 5 C v.
```

The computed exact rational check also gives the sharper value

```text
sum |r_ab| (1/4)^a (1/64)^(b-1) / C
= 4.0242699693795626990770705309229990531464891981352...
```

The reproducible certificate checks the strict inequalities

```text
|R| < 5 C v,
55C - remainder > 50C.
```

Therefore

```text
S(z,v) = M(z,v) + R(z,v) >= 50 C v > 0
```

throughout the annulus

```text
16v < |z| < 1/4.
```

This removes the last local gap near `z=0`.

## Away from the ridge

Exact Bernstein checks on the resolved polynomial `S(z,v)` over

```text
0 <= v <= 1/32
```

give nonnegative Bernstein coefficients on the following fixed `z` intervals:

```text
[-4,-2],
[-2,-1],
[-1,-1/2],
[-1/2,-1/4],
[1/4,1/2],
[1/2,1],
[1,2],
[2,4],
[4,8],
[8,16],
[16,32].
```

The negative side stops at `z=-4`, forced by `u>=0`.

For the positive tail `z>=32`, use the reciprocal chart

```text
v = ru.
```

The exact leading face is

```text
Q(u,ru) = C r^9 (4r-1)^2 u^11 + higher.
```

Large positive `z` means

```text
r = v/u <= 1/36,
```

so this chart is away from the ridge `r=1/4`.

The final compact check is performed on

```text
H(r,u) = Q(u,ru),
0 <= r <= 1/36,
0 <= u <= 1/16.
```

The exact Bernstein expansion of `H` on this rectangle has degree

```text
(28,62)
```

and has

```text
0 negative Bernstein coefficients.
```

The reproduced output records `367` zero Bernstein coefficients in this chart,
all lying on the already resolved boundary/corner faces; no negative
coefficient occurs.

The minimum Bernstein coefficient is the corner coefficient at `(0,0)`, equal to zero, as expected from the vanishing of `Q` at the corner.  All interior directions in this chart are nonnegative, and the only zero direction is the already resolved corner.

Therefore the positive tail `z>=32` is closed by a direct Bernstein check in the reciprocal variables.

## Conclusion

The hard corner is covered by the following regions:

```text
1. |z| <= 16v:
   closed by the ultra-ridge chart T(q,v) and exact l1 coefficient bound.

2. 16v < |z| < 1/4:
   closed by the explicit lower bound S >= 50 C v.

3. |z| >= 1/4, z <= 32:
   closed by exact Bernstein checks on S over fixed dyadic z intervals.

4. z >= 32:
   closed by exact Bernstein on H(r,u)=Q(u,ru) over
   r in [0,1/36], u in [0,1/16].
```

Thus the Bernstein hard corner is a resolved square-ridge artifact.  The gamma3 gap closes after blow-up; the original false negative coefficients are caused by applying rectangular Bernstein coordinates before extracting the factor geometry.
