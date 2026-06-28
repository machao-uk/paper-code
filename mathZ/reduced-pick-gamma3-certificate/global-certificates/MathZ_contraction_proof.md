# Two-point pseudo-hyperbolic contraction proof notes

## Task 1: radial-square line C=0

- `f(q) = q**20 - 2*q**11 + 2*q**10 - 2*q**9 + 1`
- `f(1) = 0`
- `f'(1) = 0`
- `f(q)/(1-q)^2 = (q**2 + 1)*(q**16 + 2*q**15 + 2*q**14 + 2*q**13 + 3*q**12 + 4*q**11 + 4*q**10 + 4*q**9 + 5*q**8 + 4*q**7 + 4*q**6 + 4*q**5 + 3*q**4 + 2*q**3 + 2*q**2 + 2*q + 1)`
- coefficients of `g`: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]`

All coefficients of `g` are positive, so `g(q)>0` for `0<q<1`.
- real roots of `g` in `(0,1)`: `0`
- `g(0)=1`, `g(1)=98`

## Task 2: boundary q=1

- `F_same|q=1 = F_opp|q=1 = (S - 1)**2*(5*S**3 + 9*S**2 + 9*S + 9)**2`
- expanded coefficients in `S`: `[25, 40, 16, 0, -90, -72, 0, 0, 81]`

This is

```text
25*S^8 + 40*S^7 + 16*S^6 + 0*S^5 - 90*S^4 - 72*S^3 + 81
```

It is nonnegative on `[0,1]`, with equality only at `S=1`:
- open-interval roots in `(0,1)`: `0` by the displayed factorization
- value at `S=0`: `81`
- value at `S=1`: `0`

## Task 3: dense grid for general paired F

- grid: `2000 x 2000` over `q in (0,1)`, `C in (-1,1)`
- minimum of `min(F_same,F_opp)`: `9.4433971753460355e-09`
- location `(q,C)`: `(0.999999, -0.0005002496248124322)`
- active type: `opp`

The minimum is approached at the radial-square boundary `q->1`, `C->0`.

## Task 4: general centered quadruples

The checked polynomial ratio is

```text
|L_ij|^2*(1-|lambda_i|^2)*(1-|lambda_j|^2)
 / (768^2*(1-|r_i|^2)*(1-|r_j|^2))
```

### 1M global random search

- accepted samples: `1000000`
- generated triples: `2400000`
- max transformed inequality ratio found: `5.1909231314671331e-02`
- square root of transformed ratio: `2.2783597458406635e-01`
- max pair: `(1, 3)`
- lambda at max: `[0.8701042128137895+0.4745758625590378j, -0.7356675200672603-0.5115672578878976j, -0.4771815656044013+0.8707349205231335j, 0.3427448728578721-0.8337435251942737j]`
- ratio quantiles `[50%,90%,99%,99.9%,max]`: `[0.00011987690871967401, 0.002720810525616023, 0.014047791136621302, 0.027033180154027593, 0.05190923131467133]`

### 500k hard boundary search

- accepted samples: `500000`
- generated triples: `8700000`
- max transformed inequality ratio found: `5.5183899397855458e-02`
- square root of transformed ratio: `2.3491253563370232e-01`
- max pair: `(0, 2)`
- lambda at max: `[0.2350407805943276+0.8653910018135325j, -0.1180393337524396-0.9915482839497659j, 0.8668504711688166-0.04512847048165456j, -0.9838519180107046+0.171285752617888j]`
- ratio quantiles `[50%,90%,99%,99.9%,max]`: `[0.0007748074802136217, 0.007692476771083106, 0.02438094067191986, 0.0369982751468491, 0.05518389939785546]`

## Conclusion

- The paired family contraction is analytically closed on the radial-square line and numerically verified on a dense general `(q,C)` grid.
- The sharpness point is the boundary `q->1`, `C->0`.
- General random centered quadruple searches found no violation; the largest observed ratios remain below `1`.

# General contraction: real-symmetric slice and factor probes

Real-symmetric slice: `lambda_1=x1`, `lambda_2=x2`, `lambda_3=x3`, `lambda_4=-(x1+x2+x3)`.
Target polynomial:

```text
Phi_ij = 768^2*(1-r_i^2)*(1-r_j^2) - L_ij^2*(1-lambda_i^2)*(1-lambda_j^2)
```

## Mod-p BM probes

### Pair `(0, 1)`
- coordinate-line BM seed `101`: `[39, 39, 41]`
- coordinate-line BM seed `202`: `[39, 39, 41]`
- coordinate-line BM seed `303`: `[39, 39, 41]`
- Kronecker BM weights `[1,17,289]`: `[(11, 130), (22, 130), (33, 130)]`

### Pair `(0, 3)`
- coordinate-line BM seed `101`: `[37, 39, 39]`
- coordinate-line BM seed `202`: `[37, 39, 39]`
- coordinate-line BM seed `303`: `[37, 39, 39]`
- Kronecker BM weights `[1,17,289]`: `[(11, 130), (22, 130), (33, 130)]`

## Exact expansion status

- direct SymPy expansion of `Phi_01` was attempted and interrupted after about 60 seconds.
- the bottleneck is expanding high powers in `r_i^2*r_j^2`, not the mod-p blackbox evaluation.
- next step should use sparse interpolation or exact low-dimensional specializations rather than direct full expansion.



# General contraction factor slices

These are exact real-symmetric specializations of `Phi_ij`.

The two-variable confluent slice `lambda=(a,a,b,-2a-b)` was attempted but direct factorization stalled; handle it by BM/sparse interpolation next.

## real paired cross pair (0,2)

- degree: `40`
- factorization:

```text
(5*a**18*b**2 - 56*a**16*b**4 + 236*a**14*b**6 - 520*a**12*b**8 + 670*a**10*b**10 - 48*a**10*b - 48*a**9*b**2 + 48*a**9 - 520*a**8*b**12 + 576*a**8*b**3 + 48*a**8*b + 576*a**7*b**4 - 576*a**7*b**2 + 236*a**6*b**14 - 1056*a**6*b**5 - 576*a**6*b**3 - 1056*a**5*b**6 + 1056*a**5*b**4 - 56*a**4*b**16 + 576*a**4*b**7 + 1056*a**4*b**5 + 576*a**3*b**8 - 576*a**3*b**6 + 5*a**2*b**18 - 48*a**2*b**9 - 576*a**2*b**7 - 48*a*b**10 + 48*a*b**8 + 48*b**9 - 2304)*(5*a**18*b**2 - 56*a**16*b**4 + 236*a**14*b**6 - 520*a**12*b**8 + 670*a**10*b**10 + 48*a**10*b + 48*a**9*b**2 - 48*a**9 - 520*a**8*b**12 - 576*a**8*b**3 - 48*a**8*b - 576*a**7*b**4 + 576*a**7*b**2 + 236*a**6*b**14 + 1056*a**6*b**5 + 576*a**6*b**3 + 1056*a**5*b**6 - 1056*a**5*b**4 - 56*a**4*b**16 - 576*a**4*b**7 - 1056*a**4*b**5 - 576*a**3*b**8 + 576*a**3*b**6 + 5*a**2*b**18 + 48*a**2*b**9 + 576*a**2*b**7 + 48*a*b**10 - 48*a*b**8 - 48*b**9 - 2304)
```

## real paired same pair (0,1)

- degree: `40`
- factorization:

```text
(5*a**8*b**2 - 16*a**6*b**4 + 18*a**4*b**6 - 8*a**2*b**8 + b**10 - 48)**2*(5*a**8*b**2 - 16*a**6*b**4 + 18*a**4*b**6 - 8*a**2*b**8 + b**10 + 48)**2
```

## double-pair confluent line pair (0,2)

- degree: `0`
- factorization:

```text
589824
```



# General contraction sparse interpolation probes

## Confluent two-variable slice

Slice: `lambda=(a,a,b,-2a-b)`.

### BM length probes
- pair `(0, 1)`, weights `(1, 41)`: BM length `130`
- pair `(0, 1)`, weights `(1, 17)`: BM length `130`
- pair `(0, 2)`, weights `(1, 41)`: BM length `130`
- pair `(0, 2)`, weights `(1, 17)`: BM length `130`

### Dense total-degree interpolation over F_p

- pair `(0, 1)`: `{'ok': True, 'mons': 861, 'support': 90, 'support_preview': [((0, 0), 589824), ((0, 20), 999999495), ((0, 40), 111111112), ((1, 19), 999989767), ((1, 39), 444444452), ((2, 16), 999997703), ((2, 18), 999916039), ((2, 38), 888888976), ((3, 15), 999963143), ((3, 17), 999655943), ((3, 37), 222223102), ((4, 14), 999778823), ((4, 16), 999412743), ((4, 36), 6232), ((5, 13), 999483911), ((5, 15), 630784), ((5, 35), 666696058), ((6, 12), 285696), ((6, 14), 4489216), ((6, 16), 999997703)]}`
- pair `(0, 2)`: `{'ok': True, 'mons': 861, 'support': 76, 'support_preview': [((0, 0), 589824), ((0, 18), 999999751), ((1, 17), 999994887), ((2, 16), 999958023), ((2, 20), 999999751), ((2, 38), 111111112), ((3, 15), 999827975), ((3, 19), 999994887), ((3, 37), 444444452), ((4, 14), 999704071), ((4, 18), 999958023), ((4, 36), 888888976), ((5, 13), 278528), ((5, 17), 999827975), ((5, 35), 222223102), ((6, 12), 2023424), ((6, 16), 999704071), ((6, 34), 6232), ((7, 11), 2146304), ((7, 15), 278528)]}`


# General contraction sparse interpolation probes

## Confluent two-variable slice

Slice: `lambda=(a,a,b,-2a-b)`.

### BM length probes
- pair `(0, 1)`, weights `(1, 41)`: BM length `130`
- pair `(0, 1)`, weights `(1, 17)`: BM length `130`
- pair `(0, 2)`, weights `(1, 41)`: BM length `130`
- pair `(0, 2)`, weights `(1, 17)`: BM length `130`

### Dense total-degree interpolation over F_p

- pair `(0, 1)`: `{'ok': True, 'mons': 861, 'support': 90, 'support_preview': [((0, 0), 589824), ((0, 20), 999999495), ((0, 40), 111111112), ((1, 19), 999989767), ((1, 39), 444444452), ((2, 16), 999997703), ((2, 18), 999916039), ((2, 38), 888888976), ((3, 15), 999963143), ((3, 17), 999655943), ((3, 37), 222223102), ((4, 14), 999778823), ((4, 16), 999412743), ((4, 36), 6232), ((5, 13), 999483911), ((5, 15), 630784), ((5, 35), 666696058), ((6, 12), 285696), ((6, 14), 4489216), ((6, 16), 999997703)]}`
- pair `(0, 2)`: `{'ok': True, 'mons': 861, 'support': 76, 'support_preview': [((0, 0), 589824), ((0, 18), 999999751), ((1, 17), 999994887), ((2, 16), 999958023), ((2, 20), 999999751), ((2, 38), 111111112), ((3, 15), 999827975), ((3, 19), 999994887), ((3, 37), 444444452), ((4, 14), 999704071), ((4, 18), 999958023), ((4, 36), 888888976), ((5, 13), 278528), ((5, 17), 999827975), ((5, 35), 222223102), ((6, 12), 2023424), ((6, 16), 999704071), ((6, 34), 6232), ((7, 11), 2146304), ((7, 15), 278528)]}`

### Signed small-coefficient factorization attempts

- pair `(0, 1)` factor length `1908`

```text
944784*a**36*b**4 + 1889568*a**35*b**5 - 8660520*a**34*b**6 - 20802744*a**33*b**7 + 31691817*a**32*b**8 + 102456576*a**31*b**9 - 48141216*a**30*b**10 - 295075872*a**29*b**11 - 30929688*a**28*b**12 - 458385863*a**27*b**13 + 285867168*a**26*b**14 + 363631815*a**25*b**15 + 161421525*a**24*b**16 - 130646859*a**23*b**17 - 354142198*a**22*b**18 - 1679616*a**22 - 152845615*a**21*b**19 + 423722399*a**20*b**20 + 8957952*a**20*b**2 + 3359232*a**20 + 455599450*a**19*b**21 + 995328*a**19*b**3 - 307189371*a**18*b**22 - 19657728*a**18*b**4 - 19408896*a**18*b**2 - 1679616*a**18 - 8957838*a**17*b**23 - 4644864*a**17*b**5 - 3483648*a**17*b**3 + 197129348*a**16*b**24 + 22413312*a**16*b**6 + 46904832*a**16*b**4 + 8957952*a**16*b**2 + 346154556*a**15*b**25 + 8589312*a**15*b**7 + 18137088*a**15*b**5 + 995328*a**15*b**3 - 143870959*a**14*b**26 - 13450752*a**14*b**8 - 59424768*a**14*b**6 - 19657728*a**14*b**4 + 128909615*a**13*b**27 - 7815168*a**13*b**9 - 38559744*a**13*b**7 - 4644864*a**13*b**5 - 93978999*a**12*b**28 + 3354624*a**12*b**10 + 38327296*a**12*b**8 + 22413312*a**12*b**6 + 114089039*a**11*b**29 + 3428352*a**11*b**11 + 42156032*a**11*b**9 + 8589312*a**11*b**7 - 113619823*a**10*b**30 + 285696*a**10*b**12 - 6049792*a**10*b**10 - 13450752*a**10*b**8 + 442746812*a**9*b**31 - 516096*a**9*b**13 - 23851008*a**9*b**11 - 7815168*a**9*b**9 + 221885930*a**8*b**32 - 221184*a**8*b**14 - 7525376*a**8*b**12 + 3354624*a**8*b**10 - 222126238*a**7*b**33 - 36864*a**7*b**15 + 5324800*a**7*b**13 + 3428352*a**7*b**11 - 222136510*a**6*b**34 - 2304*a**6*b**16 + 4489216*a**6*b**14 + 285696*a**6*b**12 - 333303949*a**5*b**35 + 630784*a**5*b**15 - 516096*a**5*b**13 + 6232*a**4*b**36 - 587264*a**4*b**16 - 221184*a**4*b**14 + 222223102*a**3*b**37 - 344064*a**3*b**17 - 36864*a**3*b**15 - 111111031*a**2*b**38 - 83968*a**2*b**18 - 2304*a**2*b**16 + 444444452*a*b**39 - 10240*a*b**19 + 111111112*b**40 - 512*b**20 + 589824
```
- pair `(0, 2)` factor length `1617`

```text
944784*a**38*b**2 + 1889568*a**37*b**3 - 8660520*a**36*b**4 - 20802744*a**35*b**5 + 31691817*a**34*b**6 + 102456576*a**33*b**7 - 48141216*a**32*b**8 - 295075872*a**31*b**9 - 30929688*a**30*b**10 - 458385863*a**29*b**11 + 285867168*a**28*b**12 + 363631815*a**27*b**13 + 161421525*a**26*b**14 - 130646859*a**25*b**15 - 354142198*a**24*b**16 - 152845615*a**23*b**17 + 423722399*a**22*b**18 + 455599450*a**21*b**19 - 307189371*a**20*b**20 - 746496*a**20*b**2 - 8957838*a**19*b**21 - 746496*a**19*b**3 + 197129348*a**18*b**22 + 3794688*a**18*b**4 - 746496*a**18 + 346154556*a**17*b**23 + 4423680*a**17*b**5 - 746496*a**17*b - 143870959*a**16*b**24 - 7299072*a**16*b**6 + 3794688*a**16*b**2 + 128909615*a**15*b**25 - 10690560*a**15*b**7 + 4423680*a**15*b**3 - 93978999*a**14*b**26 + 5712896*a**14*b**8 - 7299072*a**14*b**4 + 114089039*a**13*b**27 + 13262848*a**13*b**9 - 10690560*a**13*b**5 - 113619823*a**12*b**28 + 329728*a**12*b**10 + 5712896*a**12*b**6 + 442746812*a**11*b**29 - 8497152*a**11*b**11 + 13262848*a**11*b**7 + 221885930*a**10*b**30 - 3476992*a**10*b**12 + 329728*a**10*b**8 - 222126238*a**9*b**31 + 2146304*a**9*b**13 - 8497152*a**9*b**9 - 222136510*a**8*b**32 + 2023424*a**8*b**14 - 3476992*a**8*b**10 - 333303949*a**7*b**33 + 278528*a**7*b**15 + 2146304*a**7*b**11 + 6232*a**6*b**34 - 295936*a**6*b**16 + 2023424*a**6*b**12 + 222223102*a**5*b**35 - 172032*a**5*b**17 + 278528*a**5*b**13 - 111111031*a**4*b**36 - 41984*a**4*b**18 - 295936*a**4*b**14 + 444444452*a**3*b**37 - 5120*a**3*b**19 - 172032*a**3*b**15 + 111111112*a**2*b**38 - 256*a**2*b**20 - 41984*a**2*b**16 - 5120*a*b**17 - 256*b**18 + 589824
```


# Confluent slice rational reconstruction

Slice: `lambda=(a,a,b,-2a-b)`.

CRT primes: `[1000000007, 1000000009, 1000000033, 1000000087]`.

## pair `(0, 1)`

- support terms: `90`
- max total degree: `40`
- coefficient denominators: `[1, 3, 9]`
- factor string length: `1203`

```text
(2916*a**18*b**2 + 2916*a**17*b**3 - 14823*a**16*b**4 - 17280*a**15*b**5 + 28512*a**14*b**6 + 41760*a**13*b**7 - 22316*a**12*b**8 - 51808*a**11*b**9 - 3888*a**11 - 1288*a**10*b**10 + 33192*a**9*b**11 + 10368*a**9*b**2 + 3888*a**9 + 13582*a**8*b**12 + 1152*a**8*b**3 - 8384*a**7*b**13 - 8928*a**7*b**4 - 10368*a**7*b**2 - 7904*a**6*b**14 - 2304*a**6*b**5 - 1152*a**6*b**3 - 1088*a**5*b**15 + 2304*a**5*b**6 + 8928*a**5*b**4 + 1156*a**4*b**16 + 1152*a**4*b**7 + 2304*a**4*b**5 + 672*a**3*b**17 + 144*a**3*b**8 - 2304*a**3*b**6 + 164*a**2*b**18 - 1152*a**2*b**7 + 20*a*b**19 - 144*a*b**8 + b**20 - 2304)*(2916*a**18*b**2 + 2916*a**17*b**3 - 14823*a**16*b**4 - 17280*a**15*b**5 + 28512*a**14*b**6 + 41760*a**13*b**7 - 22316*a**12*b**8 - 51808*a**11*b**9 + 3888*a**11 - 1288*a**10*b**10 + 33192*a**9*b**11 - 10368*a**9*b**2 - 3888*a**9 + 13582*a**8*b**12 - 1152*a**8*b**3 - 8384*a**7*b**13 + 8928*a**7*b**4 + 10368*a**7*b**2 - 7904*a**6*b**14 + 2304*a**6*b**5 + 1152*a**6*b**3 - 1088*a**5*b**15 - 2304*a**5*b**6 - 8928*a**5*b**4 + 1156*a**4*b**16 - 1152*a**4*b**7 - 2304*a**4*b**5 + 672*a**3*b**17 - 144*a**3*b**8 + 2304*a**3*b**6 + 164*a**2*b**18 + 1152*a**2*b**7 + 20*a*b**19 + 144*a*b**8 + b**20 - 2304)/9
```

## pair `(0, 2)`

- support terms: `76`
- max total degree: `40`
- coefficient denominators: `[1, 3, 9]`
- factor string length: `577`

```text
(54*a**9 + 27*a**8*b - 144*a**7*b**2 - 88*a**6*b**3 + 116*a**5*b**4 + 94*a**4*b**5 - 16*a**3*b**6 - 32*a**2*b**7 - 10*a*b**8 - b**9 - 48)*(54*a**9 + 27*a**8*b - 144*a**7*b**2 - 88*a**6*b**3 + 116*a**5*b**4 + 94*a**4*b**5 - 16*a**3*b**6 - 32*a**2*b**7 - 10*a*b**8 - b**9 + 48)*(54*a**10*b + 27*a**9*b**2 - 144*a**8*b**3 - 88*a**7*b**4 + 116*a**6*b**5 + 94*a**5*b**6 - 16*a**4*b**7 - 32*a**3*b**8 - 10*a**2*b**9 - a*b**10 - 48)*(54*a**10*b + 27*a**9*b**2 - 144*a**8*b**3 - 88*a**7*b**4 + 116*a**6*b**5 + 94*a**5*b**6 - 16*a**4*b**7 - 32*a**3*b**8 - 10*a**2*b**9 - a*b**10 + 48)/9
```



# Confluent slice exact Bernstein certificate

Domain: `|a|<=1`, `|b|<=1`, `|2a+b|<=1`, with vertices `(0,-1),(1,-1),(0,1),(-1,1)`.

Triangulation:
- `T0=((0,-1),(1,-1),(0,1))`
- `T1=((0,-1),(0,1),(-1,1))`

## `48 + H`

- Bernstein positivity: `False`
- T0: degree `9`, coeffs `55`, min `-28520/63`, max `28640/63`, nonpositive `6`
- T1: degree `9`, coeffs `55`, min `-24952/63`, max `1184/3`, nonpositive `3`

## `48 - H`

- Bernstein positivity: `False`
- T0: degree `9`, coeffs `55`, min `-22592/63`, max `34568/63`, nonpositive `5`
- T1: degree `9`, coeffs `55`, min `-896/3`, max `31000/63`, nonpositive `4`

## `48 + a*b*H`

- Bernstein positivity: `False`
- T0: degree `11`, coeffs `78`, min `-196120/231`, max `37968/55`, nonpositive `9`
- T1: degree `11`, coeffs `78`, min `-32688/55`, max `218296/231`, nonpositive `6`

## `48 - a*b*H`

- Bernstein positivity: `False`
- T0: degree `11`, coeffs `78`, min `-32688/55`, max `218296/231`, nonpositive `6`
- T1: degree `11`, coeffs `78`, min `-196120/231`, max `37968/55`, nonpositive `9`

## `-Kplus`

- Bernstein positivity: `False`
- T0: degree `20`, coeffs `231`, min `-29041267692/20995`, max `5971629728/4845`, nonpositive `28`
- T1: degree `20`, coeffs `231`, min `-28701309972/20995`, max `78426538208/62985`, nonpositive `26`

## `-Kminus`

- Bernstein positivity: `False`
- T0: degree `20`, coeffs `231`, min `-28701309972/20995`, max `78426538208/62985`, nonpositive `26`
- T1: degree `20`, coeffs `231`, min `-29041267692/20995`, max `5971629728/4845`, nonpositive `28`

## Consequence

- Certificate failed for at least one polynomial.


# Confluent slice exact Bernstein certificate

Domain: `|a|<=1`, `|b|<=1`, `|2a+b|<=1`, with vertices `(0,-1),(1,-1),(0,1),(-1,1)`.

Triangulation:
- `T0=((0,-1),(1,-1),(0,1))`
- `T1=((0,-1),(0,1),(-1,1))`

Adaptive subdivision max depth: `8`.

## `48 + H`

- Bernstein positivity: `True`
- degree: `9`, checked nodes: `10`, certified leaves: `8`
- bad nodes by depth: `{0: 2}`

## `48 - H`

- Bernstein positivity: `True`
- degree: `9`, checked nodes: `10`, certified leaves: `8`
- bad nodes by depth: `{0: 2}`

## `48 + a*b*H`

- Bernstein positivity: `True`
- degree: `11`, checked nodes: `10`, certified leaves: `8`
- bad nodes by depth: `{0: 2}`

## `48 - a*b*H`

- Bernstein positivity: `True`
- degree: `11`, checked nodes: `10`, certified leaves: `8`
- bad nodes by depth: `{0: 2}`

## `-Kplus`

- Bernstein positivity: `True`
- degree: `20`, checked nodes: `10`, certified leaves: `8`
- bad nodes by depth: `{0: 2}`

## `-Kminus`

- Bernstein positivity: `True`
- degree: `20`, checked nodes: `10`, certified leaves: `8`
- bad nodes by depth: `{0: 2}`

## Consequence

- Exact Bernstein coefficients prove `48±H>0`, `48±abH>0`, and `Kplus,Kminus<0` on the closed confluent slice domain.
- Therefore `Phi_02=(H^2-48^2)((abH)^2-48^2)/9 > 0` in the interior, and `Phi_01=Kplus*Kminus/9 > 0` in the interior.


# Real-symmetric 3D sparse support recovery attempt

Attempted to recover the full 3-variable real-symmetric polynomial `Phi_01(x1,x2,x3)` using exponential Kronecker sparse interpolation with weights `[1,41,1681]`.

Result:

- BM on the exponential sequence with 300 samples gave length `150`.
- BM on the same sequence with 500 samples gave length `250`.
- The recovered recurrence validates on held-out sequence entries, but its characteristic polynomial has no roots among `g^E` for `0 <= E <= 70000`.

Interpretation:

- The earlier `BM=130` from the polynomial line `x_i=t^{w_i}` is a degree/complexity proxy, not the number of sparse monomial terms.
- Full 3D real-symmetric `Phi_ij` is not a ~130-term sparse polynomial under this encoding.
- The viable exact route remains low-dimensional slices plus factor/barrier extraction, not direct 3D sparse support recovery.


# Real-symmetric boundary face BM-only probes

- `x1=+1`, pair `(0, 1)`: `[((1, 17), 130), ((1, 41), 130), ((3, 47), 130)]`
- `x1=+1`, pair `(1, 2)`: `[((1, 17), 130), ((1, 41), 130), ((3, 47), 130)]`
- `x1=+1`, pair `(1, 3)`: `[((1, 17), 130), ((1, 41), 130), ((3, 47), 130)]`
- `x1=-1`, pair `(0, 1)`: `[((1, 17), 130), ((1, 41), 130), ((3, 47), 130)]`
- `x1=-1`, pair `(1, 2)`: `[((1, 17), 130), ((1, 41), 130), ((3, 47), 130)]`
- `x1=-1`, pair `(1, 3)`: `[((1, 17), 130), ((1, 41), 130), ((3, 47), 130)]`

Interpretation: dense interpolation was attempted but interrupted in the 861x861 modular solve; BM-only is used to select smaller follow-up slices.


# Boundary face r-factor probe

Face: `lambda=(1,a,b,-1-a-b)`. For pairs containing `lambda_0=1`, `Phi_0j=768^2*(1-r_0^2)*(1-r_j^2)`.

## `r_0`

- r length: `831`
- denominator of `1-r^2`: `36864`
- factor coeff: `-1`
- factor 0: exp `1`, degree `10`, length `831`
```text
4*a**10 + 20*a**9*b + 20*a**9 + 27*a**8*b**2 + 80*a**8*b + 21*a**8 - 12*a**7*b**3 + 68*a**7*b**2 + 44*a**7*b - 36*a**7 - 84*a**6*b**4 - 59*a**6*b**3 + 11*a**6*b**2 - 165*a**6*b - 79*a**6 - 126*a**5*b**5 - 163*a**5*b**4 + 108*a**5*b**3 - 42*a**5*b**2 - 214*a**5*b - 27*a**5 - 84*a**4*b**6 - 163*a**4*b**5 + 208*a**4*b**4 + 419*a**4*b**3 - 19*a**4*b**2 - 48*a**4*b + 39*a**4 - 12*a**3*b**7 - 59*a**3*b**6 + 108*a**3*b**5 + 419*a**3*b**4 + 160*a**3*b**3 - 113*a**3*b**2 + 32*a**3*b + 41*a**3 + 27*a**2*b**8 + 68*a**2*b**7 + 11*a**2*b**6 - 42*a**2*b**5 - 19*a**2*b**4 - 113*a**2*b**3 - 78*a**2*b**2 + 23*a**2*b + 15*a**2 + 20*a*b**9 + 80*a*b**8 + 44*a*b**7 - 165*a*b**6 - 214*a*b**5 - 48*a*b**4 + 32*a*b**3 + 23*a*b**2 + 10*a*b + 2*a + 4*b**10 + 20*b**9 + 21*b**8 - 36*b**7 - 79*b**6 - 27*b**5 + 39*b**4 + 41*b**3 + 15*b**2 + 2*b - 192
```
- factor 1: exp `1`, degree `10`, length `831`
```text
4*a**10 + 20*a**9*b + 20*a**9 + 27*a**8*b**2 + 80*a**8*b + 21*a**8 - 12*a**7*b**3 + 68*a**7*b**2 + 44*a**7*b - 36*a**7 - 84*a**6*b**4 - 59*a**6*b**3 + 11*a**6*b**2 - 165*a**6*b - 79*a**6 - 126*a**5*b**5 - 163*a**5*b**4 + 108*a**5*b**3 - 42*a**5*b**2 - 214*a**5*b - 27*a**5 - 84*a**4*b**6 - 163*a**4*b**5 + 208*a**4*b**4 + 419*a**4*b**3 - 19*a**4*b**2 - 48*a**4*b + 39*a**4 - 12*a**3*b**7 - 59*a**3*b**6 + 108*a**3*b**5 + 419*a**3*b**4 + 160*a**3*b**3 - 113*a**3*b**2 + 32*a**3*b + 41*a**3 + 27*a**2*b**8 + 68*a**2*b**7 + 11*a**2*b**6 - 42*a**2*b**5 - 19*a**2*b**4 - 113*a**2*b**3 - 78*a**2*b**2 + 23*a**2*b + 15*a**2 + 20*a*b**9 + 80*a*b**8 + 44*a*b**7 - 165*a*b**6 - 214*a*b**5 - 48*a*b**4 + 32*a*b**3 + 23*a*b**2 + 10*a*b + 2*a + 4*b**10 + 20*b**9 + 21*b**8 - 36*b**7 - 79*b**6 - 27*b**5 + 39*b**4 + 41*b**3 + 15*b**2 + 2*b + 192
```

## `r_1`

- r length: `825`
- denominator of `1-r^2`: `36864`
- factor coeff: `-1`
- factor 0: exp `1`, degree `10`, length `821`
```text
2*a**9*b + 2*a**9 + 15*a**8*b**2 + 10*a**8*b + 15*a**8 + 41*a**7*b**3 + 23*a**7*b**2 + 23*a**7*b + 41*a**7 + 39*a**6*b**4 + 32*a**6*b**3 - 78*a**6*b**2 + 32*a**6*b + 39*a**6 - 27*a**5*b**5 - 48*a**5*b**4 - 113*a**5*b**3 - 113*a**5*b**2 - 48*a**5*b - 27*a**5 - 79*a**4*b**6 - 214*a**4*b**5 - 19*a**4*b**4 + 160*a**4*b**3 - 19*a**4*b**2 - 214*a**4*b - 79*a**4 - 36*a**3*b**7 - 165*a**3*b**6 - 42*a**3*b**5 + 419*a**3*b**4 + 419*a**3*b**3 - 42*a**3*b**2 - 165*a**3*b - 36*a**3 + 21*a**2*b**8 + 44*a**2*b**7 + 11*a**2*b**6 + 108*a**2*b**5 + 208*a**2*b**4 + 108*a**2*b**3 + 11*a**2*b**2 + 44*a**2*b + 21*a**2 + 20*a*b**9 + 80*a*b**8 + 68*a*b**7 - 59*a*b**6 - 163*a*b**5 - 163*a*b**4 - 59*a*b**3 + 68*a*b**2 + 80*a*b + 20*a + 4*b**10 + 20*b**9 + 27*b**8 - 12*b**7 - 84*b**6 - 126*b**5 - 84*b**4 - 12*b**3 + 27*b**2 + 20*b - 188
```
- factor 1: exp `1`, degree `10`, length `821`
```text
2*a**9*b + 2*a**9 + 15*a**8*b**2 + 10*a**8*b + 15*a**8 + 41*a**7*b**3 + 23*a**7*b**2 + 23*a**7*b + 41*a**7 + 39*a**6*b**4 + 32*a**6*b**3 - 78*a**6*b**2 + 32*a**6*b + 39*a**6 - 27*a**5*b**5 - 48*a**5*b**4 - 113*a**5*b**3 - 113*a**5*b**2 - 48*a**5*b - 27*a**5 - 79*a**4*b**6 - 214*a**4*b**5 - 19*a**4*b**4 + 160*a**4*b**3 - 19*a**4*b**2 - 214*a**4*b - 79*a**4 - 36*a**3*b**7 - 165*a**3*b**6 - 42*a**3*b**5 + 419*a**3*b**4 + 419*a**3*b**3 - 42*a**3*b**2 - 165*a**3*b - 36*a**3 + 21*a**2*b**8 + 44*a**2*b**7 + 11*a**2*b**6 + 108*a**2*b**5 + 208*a**2*b**4 + 108*a**2*b**3 + 11*a**2*b**2 + 44*a**2*b + 21*a**2 + 20*a*b**9 + 80*a*b**8 + 68*a*b**7 - 59*a*b**6 - 163*a*b**5 - 163*a*b**4 - 59*a*b**3 + 68*a*b**2 + 80*a*b + 20*a + 4*b**10 + 20*b**9 + 27*b**8 - 12*b**7 - 84*b**6 - 126*b**5 - 84*b**4 - 12*b**3 + 27*b**2 + 20*b + 196
```

## `r_2`

- r length: `825`
- denominator of `1-r^2`: `36864`
- factor coeff: `-1`
- factor 0: exp `1`, degree `10`, length `821`
```text
4*a**10 + 20*a**9*b + 20*a**9 + 21*a**8*b**2 + 80*a**8*b + 27*a**8 - 36*a**7*b**3 + 44*a**7*b**2 + 68*a**7*b - 12*a**7 - 79*a**6*b**4 - 165*a**6*b**3 + 11*a**6*b**2 - 59*a**6*b - 84*a**6 - 27*a**5*b**5 - 214*a**5*b**4 - 42*a**5*b**3 + 108*a**5*b**2 - 163*a**5*b - 126*a**5 + 39*a**4*b**6 - 48*a**4*b**5 - 19*a**4*b**4 + 419*a**4*b**3 + 208*a**4*b**2 - 163*a**4*b - 84*a**4 + 41*a**3*b**7 + 32*a**3*b**6 - 113*a**3*b**5 + 160*a**3*b**4 + 419*a**3*b**3 + 108*a**3*b**2 - 59*a**3*b - 12*a**3 + 15*a**2*b**8 + 23*a**2*b**7 - 78*a**2*b**6 - 113*a**2*b**5 - 19*a**2*b**4 - 42*a**2*b**3 + 11*a**2*b**2 + 68*a**2*b + 27*a**2 + 2*a*b**9 + 10*a*b**8 + 23*a*b**7 + 32*a*b**6 - 48*a*b**5 - 214*a*b**4 - 165*a*b**3 + 44*a*b**2 + 80*a*b + 20*a + 2*b**9 + 15*b**8 + 41*b**7 + 39*b**6 - 27*b**5 - 79*b**4 - 36*b**3 + 21*b**2 + 20*b - 188
```
- factor 1: exp `1`, degree `10`, length `821`
```text
4*a**10 + 20*a**9*b + 20*a**9 + 21*a**8*b**2 + 80*a**8*b + 27*a**8 - 36*a**7*b**3 + 44*a**7*b**2 + 68*a**7*b - 12*a**7 - 79*a**6*b**4 - 165*a**6*b**3 + 11*a**6*b**2 - 59*a**6*b - 84*a**6 - 27*a**5*b**5 - 214*a**5*b**4 - 42*a**5*b**3 + 108*a**5*b**2 - 163*a**5*b - 126*a**5 + 39*a**4*b**6 - 48*a**4*b**5 - 19*a**4*b**4 + 419*a**4*b**3 + 208*a**4*b**2 - 163*a**4*b - 84*a**4 + 41*a**3*b**7 + 32*a**3*b**6 - 113*a**3*b**5 + 160*a**3*b**4 + 419*a**3*b**3 + 108*a**3*b**2 - 59*a**3*b - 12*a**3 + 15*a**2*b**8 + 23*a**2*b**7 - 78*a**2*b**6 - 113*a**2*b**5 - 19*a**2*b**4 - 42*a**2*b**3 + 11*a**2*b**2 + 68*a**2*b + 27*a**2 + 2*a*b**9 + 10*a*b**8 + 23*a*b**7 + 32*a*b**6 - 48*a*b**5 - 214*a*b**4 - 165*a*b**3 + 44*a*b**2 + 80*a*b + 20*a + 2*b**9 + 15*b**8 + 41*b**7 + 39*b**6 - 27*b**5 - 79*b**4 - 36*b**3 + 21*b**2 + 20*b + 196
```

## `r_3`

- r length: `772`
- denominator of `1-r^2`: `36864`
- factor coeff: `-1`
- factor 0: exp `1`, degree `10`, length `771`
```text
2*a**9*b + 2*a**9 + 3*a**8*b**2 + 26*a**8*b + 3*a**8 - 7*a**7*b**3 + 39*a**7*b**2 + 39*a**7*b - 7*a**7 - 4*a**6*b**4 - 32*a**6*b**3 + 8*a**6*b**2 - 32*a**6*b - 4*a**6 + 12*a**5*b**5 - 89*a**5*b**4 - 47*a**5*b**3 - 47*a**5*b**2 - 89*a**5*b + 12*a**5 - 4*a**4*b**6 - 89*a**4*b**5 - 6*a**4*b**4 + 230*a**4*b**3 - 6*a**4*b**2 - 89*a**4*b - 4*a**4 - 7*a**3*b**7 - 32*a**3*b**6 - 47*a**3*b**5 + 230*a**3*b**4 + 230*a**3*b**3 - 47*a**3*b**2 - 32*a**3*b - 7*a**3 + 3*a**2*b**8 + 39*a**2*b**7 + 8*a**2*b**6 - 47*a**2*b**5 - 6*a**2*b**4 - 47*a**2*b**3 + 8*a**2*b**2 + 39*a**2*b + 3*a**2 + 2*a*b**9 + 26*a*b**8 + 39*a*b**7 - 32*a*b**6 - 89*a*b**5 - 89*a*b**4 - 32*a*b**3 + 39*a*b**2 + 26*a*b + 2*a + 2*b**9 + 3*b**8 - 7*b**7 - 4*b**6 + 12*b**5 - 4*b**4 - 7*b**3 + 3*b**2 + 2*b - 192
```
- factor 1: exp `1`, degree `10`, length `771`
```text
2*a**9*b + 2*a**9 + 3*a**8*b**2 + 26*a**8*b + 3*a**8 - 7*a**7*b**3 + 39*a**7*b**2 + 39*a**7*b - 7*a**7 - 4*a**6*b**4 - 32*a**6*b**3 + 8*a**6*b**2 - 32*a**6*b - 4*a**6 + 12*a**5*b**5 - 89*a**5*b**4 - 47*a**5*b**3 - 47*a**5*b**2 - 89*a**5*b + 12*a**5 - 4*a**4*b**6 - 89*a**4*b**5 - 6*a**4*b**4 + 230*a**4*b**3 - 6*a**4*b**2 - 89*a**4*b - 4*a**4 - 7*a**3*b**7 - 32*a**3*b**6 - 47*a**3*b**5 + 230*a**3*b**4 + 230*a**3*b**3 - 47*a**3*b**2 - 32*a**3*b - 7*a**3 + 3*a**2*b**8 + 39*a**2*b**7 + 8*a**2*b**6 - 47*a**2*b**5 - 6*a**2*b**4 - 47*a**2*b**3 + 8*a**2*b**2 + 39*a**2*b + 3*a**2 + 2*a*b**9 + 26*a*b**8 + 39*a*b**7 - 32*a*b**6 - 89*a*b**5 - 89*a*b**4 - 32*a*b**3 + 39*a*b**2 + 26*a*b + 2*a + 2*b**9 + 3*b**8 - 7*b**7 - 4*b**6 + 12*b**5 - 4*b**4 - 7*b**3 + 3*b**2 + 2*b + 192
```



# Boundary face exact Bernstein certificate for `1-r_i^2`

Face: `lambda=(1,a,b,-1-a-b)`.
Feasible domain is the triangle with vertices `(-1,-1),(-1,1),(1,-1)`.

## `1-r_0^2` numerator

- nonnegative Bernstein certificate: `True`
- degree: `20`, checked nodes: `5`, certified leaves: `4`
- bad nodes by depth: `{0: 1}`

## `1-r_1^2` numerator

- nonnegative Bernstein certificate: `True`
- degree: `20`, checked nodes: `5`, certified leaves: `4`
- bad nodes by depth: `{0: 1}`

## `1-r_2^2` numerator

- nonnegative Bernstein certificate: `True`
- degree: `20`, checked nodes: `5`, certified leaves: `4`
- bad nodes by depth: `{0: 1}`

## `1-r_3^2` numerator

- nonnegative Bernstein certificate: `True`
- degree: `20`, checked nodes: `5`, certified leaves: `4`
- bad nodes by depth: `{0: 1}`

## Consequence

- On the real boundary face `x1=1`, every `1-r_i^2 >= 0` is certified exactly by rational Bernstein subdivision.
- Therefore every contraction inequality for pairs containing the boundary node reduces to a product of certified nonnegative factors.


# Boundary face fast modular interpolation

Face: `lambda=(1,a,b,-1-a-b)`.

## pair `(1, 2)`

- result: `{'pair': (1, 2), 'ok': True, 'mons': 861, 'support': 855, 'max_total_degree': 40}`
- preview: `[((0, 0), 111700424), ((0, 1), 222217106), ((0, 2), 333313835), ((0, 3), 888859804), ((0, 4), 263914319), ((0, 5), 750186104), ((0, 6), 83646060), ((0, 7), 708423873), ((0, 8), 999920648), ((0, 9), 894894460), ((0, 10), 968960831), ((0, 11), 506136367), ((0, 12), 809067310), ((0, 13), 859684125), ((0, 14), 897078194), ((0, 15), 760229059), ((0, 16), 279935603), ((0, 17), 442948549), ((0, 18), 597965624), ((0, 19), 127722203), ((0, 20), 952954051), ((0, 21), 536144097), ((0, 22), 911237060), ((0, 23), 580715035), ((0, 24), 639449887), ((0, 25), 963674397), ((0, 26), 543029531), ((0, 27), 868052067), ((0, 28), 677492223), ((0, 29), 578106923)]`

## pair `(1, 3)`

- result: `{'pair': (1, 3), 'ok': True, 'mons': 861, 'support': 848, 'max_total_degree': 40}`
- preview: `[((0, 0), 589568), ((0, 1), 999997959), ((0, 2), 27772722), ((0, 3), 361110922), ((0, 4), 270853017), ((0, 5), 194482881), ((0, 6), 664964140), ((0, 7), 939227545), ((0, 8), 835415583), ((0, 9), 731621590), ((0, 10), 215592360), ((0, 11), 758663279), ((0, 12), 255269493), ((0, 13), 971415680), ((0, 14), 59908902), ((0, 15), 367171310), ((0, 16), 747386156), ((0, 17), 703125069), ((0, 18), 529948856), ((0, 19), 945312980), ((0, 20), 841146530), ((0, 21), 945312724), ((0, 22), 529947448), ((0, 23), 703124621), ((0, 24), 747396044), ((0, 25), 367187854), ((0, 26), 59895782), ((0, 27), 971353856), ((0, 28), 255208197), ((0, 29), 758680687)]`

## pair `(2, 3)`

- result: `{'pair': (2, 3), 'ok': True, 'mons': 861, 'support': 848, 'max_total_degree': 40}`
- preview: `[((0, 0), 589568), ((0, 1), 999997959), ((0, 2), 27772466), ((0, 3), 361108618), ((0, 4), 187512643), ((0, 5), 194476096), ((0, 6), 213578092), ((0, 7), 140616331), ((0, 8), 515961777), ((0, 9), 155271782), ((0, 10), 773875831), ((0, 11), 400278058), ((0, 12), 101213963), ((0, 13), 999150244), ((0, 14), 59010863), ((0, 15), 65950188), ((0, 16), 337656795), ((0, 17), 975686190), ((0, 18), 700085049), ((0, 19), 217881540), ((0, 20), 690537085), ((0, 21), 136284324), ((0, 22), 634549325), ((0, 23), 189236522), ((0, 24), 289930191), ((0, 25), 785589954), ((0, 26), 754340390), ((0, 27), 993055761), ((0, 28), 230902809), ((0, 29), 916666611)]`



# Boundary face non-boundary pair numerical margin

Face: `lambda=(1,a,b,-1-a-b)`, feasible triangle `-1<=a,b<=1`, `-2<=a+b<=0`.

Grid scan `801 x 801` on the triangle found no negative values for non-boundary pairs:

- pair `(1,2)`: minimum `589312.1111111111` at `(a,b,x4)=(0,0,-1)`
- pair `(1,3)`: minimum `589312.1111111111` at `(a,b,x4)=(0,-1,0)`
- pair `(2,3)`: minimum `589312.1111111111` at `(a,b,x4)=(-1,0,0)`

Interpretation: the real boundary face has large positive margin for pairs not containing the boundary node. The obstruction is computational representation, not a near-zero boundary phenomenon.


# Boundary pair `(1,2)` Bernstein CRT certificate attempt

Face: `lambda=(1,a,b,-1-a-b)`, triangle `(-1,-1),(-1,1),(1,-1)`.

- primes: `[1000000007, 1000000009, 1000000033, 1000000087]`
- Bernstein coefficient count: `861`
- rational reconstruction failures: `172`
- all reconstructed coefficients nonnegative: `False`
- min coefficient: `-20283824404627456/358701`
- max coefficient: `29399914251616256/8544965`
- zero coefficient count: `0`


# Boundary pair `(1,2)` Bernstein CRT certificate attempt

Face: `lambda=(1,a,b,-1-a-b)`, triangle `(-1,-1),(-1,1),(1,-1)`.

- primes: `[1000000007, 1000000009, 1000000033, 1000000087]`
- Bernstein coefficient count per triangle: `861`

## triangle `0`
- vertices: `((-1, -1), (-1, 1), (1, -1))`
- rational reconstruction failures: `172`
- all reconstructed coefficients nonnegative: `False`
- min coefficient: `-20283824404627456/358701`
- max coefficient: `29399914251616256/8544965`
- zero coefficient count: `0`

## triangle `1`
- vertices: `((-1, -1), (-1, 0), (0, -1))`
- rational reconstruction failures: `156`
- all reconstructed coefficients nonnegative: `False`
- min coefficient: `-574175140515796979/16699157567324034`
- max coefficient: `21938547769430129/37131087744`
- zero coefficient count: `0`

## triangle `2`
- vertices: `((-1, 0), (-1, 1), (0, 0))`
- rational reconstruction failures: `231`
- all reconstructed coefficients nonnegative: `False`
- min coefficient: `-472814249482696498/7346936323734993`
- max coefficient: `304095037716647999/445573052928`
- zero coefficient count: `0`

## triangle `3`
- vertices: `((0, -1), (0, 0), (1, -1))`
- rational reconstruction failures: `231`
- all reconstructed coefficients nonnegative: `False`
- min coefficient: `-472814249482696498/7346936323734993`
- max coefficient: `304095037716647999/445573052928`
- zero coefficient count: `0`

## triangle `4`
- vertices: `((-1, 0), (0, 0), (0, -1))`
- rational reconstruction failures: `273`
- all reconstructed coefficients nonnegative: `False`
- min coefficient: `-618253406891148262/6271155927824173`
- max coefficient: `633913843116000293/1072675868160`
- zero coefficient count: `0`


# Boundary pair `(1,2)` Bernstein CRT certificate attempt

Face: `lambda=(1,a,b,-1-a-b)`, triangle `(-1,-1),(-1,1),(1,-1)`.

- primes: `[1000000007, 1000000009, 1000000021, 1000000033, 1000000087, 1000000093, 1000000097, 1000000103]`
- Bernstein coefficient count per triangle: `861`

## triangle `0`
- vertices: `((-1, -1), (-1, 1), (1, -1))`
- rational reconstruction failures: `0`
- all reconstructed coefficients nonnegative: `False`
- min coefficient: `-6998697958231790780416/8205150525`
- max coefficient: `652388939808724926398464/310154689845`
- zero coefficient count: `0`

## triangle `1`
- vertices: `((-1, -1), (-1, 0), (0, -1))`
- rational reconstruction failures: `0`
- all reconstructed coefficients nonnegative: `True`
- min coefficient: `145824997960108339/248123751876`
- max coefficient: `21938547769430129/37131087744`
- zero coefficient count: `0`

## triangle `2`
- vertices: `((-1, 0), (-1, 1), (0, 0))`
- rational reconstruction failures: `0`
- all reconstructed coefficients nonnegative: `True`
- min coefficient: `12379630443454/650194155`
- max coefficient: `26125008243146940239/36202810550400`
- zero coefficient count: `0`

## triangle `3`
- vertices: `((0, -1), (0, 0), (1, -1))`
- rational reconstruction failures: `0`
- all reconstructed coefficients nonnegative: `True`
- min coefficient: `12379630443454/650194155`
- max coefficient: `26125008243146940239/36202810550400`
- zero coefficient count: `0`

## triangle `4`
- vertices: `((-1, 0), (0, 0), (0, -1))`
- rational reconstruction failures: `0`
- all reconstructed coefficients nonnegative: `True`
- min coefficient: `7408559845218295807/12603111206400`
- max coefficient: `633913843116000293/1072675868160`
- zero coefficient count: `0`


# Boundary non-boundary pairs Bernstein CRT certificates

Face: `lambda=(1,a,b,-1-a-b)`, triangle `(-1,-1),(-1,1),(1,-1)`.

- primes: `[1000000007, 1000000009, 1000000021, 1000000033, 1000000087, 1000000093, 1000000097, 1000000103]`
- Bernstein coefficient count per triangle: `861`
- Certification criterion: the four depth-1 subtriangles all have nonnegative reconstructed Bernstein coefficients.

## pair `(1, 2)`


## triangle `0`
- vertices: `((-1, -1), (-1, 1), (1, -1))`
- rational reconstruction failures: `0`
- all reconstructed coefficients nonnegative: `False`
- min coefficient: `-6998697958231790780416/8205150525`
- max coefficient: `652388939808724926398464/310154689845`
- zero coefficient count: `0`

## triangle `1`
- vertices: `((-1, -1), (-1, 0), (0, -1))`
- rational reconstruction failures: `0`
- all reconstructed coefficients nonnegative: `True`
- min coefficient: `145824997960108339/248123751876`
- max coefficient: `21938547769430129/37131087744`
- zero coefficient count: `0`

## triangle `2`
- vertices: `((-1, 0), (-1, 1), (0, 0))`
- rational reconstruction failures: `0`
- all reconstructed coefficients nonnegative: `True`
- min coefficient: `12379630443454/650194155`
- max coefficient: `26125008243146940239/36202810550400`
- zero coefficient count: `0`

## triangle `3`
- vertices: `((0, -1), (0, 0), (1, -1))`
- rational reconstruction failures: `0`
- all reconstructed coefficients nonnegative: `True`
- min coefficient: `12379630443454/650194155`
- max coefficient: `26125008243146940239/36202810550400`
- zero coefficient count: `0`

## triangle `4`
- vertices: `((-1, 0), (0, 0), (0, -1))`
- rational reconstruction failures: `0`
- all reconstructed coefficients nonnegative: `True`
- min coefficient: `7408559845218295807/12603111206400`
- max coefficient: `633913843116000293/1072675868160`
- zero coefficient count: `0`

- depth-1 subtriangle certificate for pair `(1, 2)`: `True`

## pair `(1, 3)`


## triangle `0`
- vertices: `((-1, -1), (-1, 1), (1, -1))`
- rational reconstruction failures: `0`
- all reconstructed coefficients nonnegative: `False`
- min coefficient: `-13645224513574224068608/8503519635`
- max coefficient: `295629849722257600741376/310154689845`
- zero coefficient count: `0`

## triangle `1`
- vertices: `((-1, -1), (-1, 0), (0, -1))`
- rational reconstruction failures: `0`
- all reconstructed coefficients nonnegative: `True`
- min coefficient: `7408559845218295807/12603111206400`
- max coefficient: `633913843116000293/1072675868160`
- zero coefficient count: `0`

## triangle `2`
- vertices: `((-1, 0), (-1, 1), (0, 0))`
- rational reconstruction failures: `0`
- all reconstructed coefficients nonnegative: `True`
- min coefficient: `300776934762098/650194155`
- max coefficient: `31854862323390365/45253513188`
- zero coefficient count: `0`

## triangle `3`
- vertices: `((0, -1), (0, 0), (1, -1))`
- rational reconstruction failures: `0`
- all reconstructed coefficients nonnegative: `True`
- min coefficient: `1460420608/2997`
- max coefficient: `147205589535418/169870545`
- zero coefficient count: `0`

## triangle `4`
- vertices: `((-1, 0), (0, 0), (0, -1))`
- rational reconstruction failures: `0`
- all reconstructed coefficients nonnegative: `True`
- min coefficient: `7408559845218295807/12603111206400`
- max coefficient: `633913843116000293/1072675868160`
- zero coefficient count: `0`

- depth-1 subtriangle certificate for pair `(1, 3)`: `True`

## pair `(2, 3)`


## triangle `0`
- vertices: `((-1, -1), (-1, 1), (1, -1))`
- rational reconstruction failures: `0`
- all reconstructed coefficients nonnegative: `False`
- min coefficient: `-13645224513574224068608/8503519635`
- max coefficient: `295629849722257600741376/310154689845`
- zero coefficient count: `0`

## triangle `1`
- vertices: `((-1, -1), (-1, 0), (0, -1))`
- rational reconstruction failures: `0`
- all reconstructed coefficients nonnegative: `True`
- min coefficient: `7408559845218295807/12603111206400`
- max coefficient: `633913843116000293/1072675868160`
- zero coefficient count: `0`

## triangle `2`
- vertices: `((-1, 0), (-1, 1), (0, 0))`
- rational reconstruction failures: `0`
- all reconstructed coefficients nonnegative: `True`
- min coefficient: `1460420608/2997`
- max coefficient: `147205589535418/169870545`
- zero coefficient count: `0`

## triangle `3`
- vertices: `((0, -1), (0, 0), (1, -1))`
- rational reconstruction failures: `0`
- all reconstructed coefficients nonnegative: `True`
- min coefficient: `300776934762098/650194155`
- max coefficient: `31854862323390365/45253513188`
- zero coefficient count: `0`

## triangle `4`
- vertices: `((-1, 0), (0, 0), (0, -1))`
- rational reconstruction failures: `0`
- all reconstructed coefficients nonnegative: `True`
- min coefficient: `145824997960108339/248123751876`
- max coefficient: `21938547769430129/37131087744`
- zero coefficient count: `0`

- depth-1 subtriangle certificate for pair `(2, 3)`: `True`

## Consequence

- All non-boundary pairs on the real boundary face `x1=1` are certified nonnegative by CRT-reconstructed rational Bernstein coefficients after one subdivision.
