# n=4 closure summary

## Status

The previously listed components are assumed closed:

```text
K-region,
paired family,
boundary layer,
real boundary face,
gamma1,
gamma2,
radiating square,
1D family.
```

The only remaining gap was the gamma3 Bernstein hard corner

```text
rho in [3/4,1],
y   in [3/4,1],
(rho,y) near (1,1).
```

That gap is now closed by the blow-up certificate in

```text
/Users/ray/Downloads/MathZ_gamma3_hard_corner_closed.md
```

The exact certificate script and last output are

```text
/Users/ray/Downloads/MathZ_gamma3_hard_corner_certificate.py
/Users/ray/Downloads/MathZ_gamma3_hard_corner_certificate_output.md
```

## Key point

The original Bernstein failure was caused by a square ridge at the hard corner.

With

```text
u = 1-rho,
v = 1-y,
Q(u,v)=P(1-u,1-v),
```

the exact lowest homogeneous part is

```text
Lead(Q) = C v^9 (u-4v)^2,
C = 382511685112441262309376 > 0.
```

Thus rectangular Bernstein in `(rho,y)` sees a high-order nearly tangent zero and produces false negative coefficients.

## Resolved charts

Use the ridge chart

```text
u = 4v + vz,
S(z,v)=Q(4v+vz,v)/v^11.
```

Then

```text
S(z,v)=C(z^2+64v+32vz-320v^2)+R(z,v).
```

The hard corner is covered by four regions.

## Region 1: inner ridge tube

Use

```text
z=vq,
T(q,v)=S(vq,v)/v.
```

Exact coefficient absolute-value bound proves

```text
T(q,v)>0
```

on

```text
|q|<=16,
0<=v<=1/32.
```

Equivalently,

```text
S(z,v)>0
```

on

```text
|z|<=16v.
```

## Region 2: annulus around ridge

For

```text
16v<|z|<1/4
```

one has `v<1/64`.  The main part satisfies

```text
C(z^2+64v+32vz-320v^2) >= 55 C v.
```

The exact sparse remainder bound gives

```text
|R(z,v)| < 5 C v.
```

Therefore

```text
S(z,v) >= 50 C v > 0.
```

## Region 3: fixed z away from zero

Exact Bernstein checks on `S(z,v)` for `0<=v<=1/32` pass on

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

The reproduced output reports degree `(62,51)` and `0` negative Bernstein
coefficients on every listed interval.

The lower endpoint `z=-4` is forced by `u>=0`.

## Region 4: positive z tail

For `z>=32`, switch to

```text
v=ru,
H(r,u)=Q(u,ru).
```

The condition `z>=32` implies

```text
0<=r<=1/36.
```

Exact Bernstein on

```text
0<=r<=1/36,
0<=u<=1/16
```

has degree

```text
(28,62)
```

and

```text
0 negative Bernstein coefficients.
```

The reproduced output records `367` zero coefficients, all on the resolved
corner/boundary faces.

So the positive tail is closed.

## Conclusion

The gamma3 hard corner is covered by resolved coordinates and explicit rational certificates.  Combined with the already closed components listed above, this closes the remaining n=4 reduced Pick positivity gap.

Operationally, the remaining gap in `prop:interior-machine-certificate` is now
replaced by the four-region certificate above.  No uncaptured Bernstein hard
corner remains in the `(rho,y)` gamma3 chart.
