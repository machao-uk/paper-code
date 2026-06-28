# Schur-step certificates for the n=4 reduced Pick problem

## General 3+1 stratum, gamma2

Ordering: choose the unique interior node first, then a unit node.
After rotation, write the unit nodes as `1,x,y` and the interior node as
`-(1+s)`, where

\[
  s=x+y,\qquad xy=s/\bar s,\qquad |1+s|\le 1.
\]

Set `s=-1+rho exp(i psi)` and `cos psi=2y-1`.

For

\[
  \gamma_2=
  \frac{r(1)-r(-(1+s))}{1-\overline{r(-(1+s))}r(1)}
  \frac{1-\overline{(-(1+s))}}{1+(1+s)},
\]

exact symbolic reduction gives

\[
  1-|\gamma_2|^2 = \frac{N_2(\rho,y)}{D_2(\rho,y)}.
\]

The denominator is positive away from the limiting collision/square faces. The numerator `N_2` is an ordinary real polynomial because the pre-substitution numerator is even in `Im(s)`.

Polynomial data:

- bidegree in `(rho,y)`: `(54,25)`
- monomial terms: `778`

Exact rational Bernstein subdivision certificate:

| rho interval | y interval | min Bernstein coefficient | zero Bernstein coefficients |
|---|---:|---:|---:|
| `[0,1/2]` | `[0,1]` | `19525670366953761/1099511627776` | `0` |
| `[1/2,1]` | `[0,1/2]` | `0` | `6` |
| `[1/2,1]` | `[1/2,1]` | `0` | `81` |

Conclusion: `|gamma2|<=1` on the full two-angle `3+1` stratum for the order `(interior node, selected unit node, remaining unit nodes)`.

## Remaining tasks

- Compute and certify `gamma3` after the first two Schur steps.
- `gamma3` depends on one remaining unit root `x`, satisfying `x^2-sx+s/bar(s)=0`; the right representation is a quadratic-remainder certificate, not a full six-variable expansion.
- `gamma4` should then be a one-point terminal Schur parameter after two boundary nodes remain.

## General 3+1 stratum, gamma3 attempt

The same ordering was used: first the unique interior node, then the unit node fixed at `1`.  The remaining two unit nodes are `x` and `s-x`, with

\[
  x^2-sx+s/\bar s=0 .
\]

After two Schur contractions, `gamma3` is not a function of `(rho,y)` alone. It depends on the choice of the remaining quadratic root `x`.  Algebraically, after reducing modulo

\[
  x^2-sx+s/\bar s=0,
\]

`gamma3` is a rational function whose numerator and denominator are both affine in `x`.

Exact SymPy statistics for the reduced rational expression:

| object | total degree in `(x,s,bar s)` | monomial terms | degree in `x` |
|---|---:|---:|---:|
| numerator of `gamma3` | `76` | `1879` | `1` |
| denominator of `gamma3` | `85` | `2599` | `1` |

Consequences:

1. A pure two-variable `(rho,y)` Bernstein certificate for `1-|gamma3|^2` does not exist before eliminating the quadratic root choice.  One must certify both roots, or certify the affine remainder on the quadratic extension.
2. The naive numerator of `1-|gamma3|^2` necessarily exceeds degree `80` because the denominator of `gamma3` already has total degree `85`.
3. Direct expansion of `1-|gamma3|^2` stalls: `gamma3` itself has string length about `1.28e5`, and expanding the squared modulus produces a much larger expression.

Recommended factor stripping before any Bernstein run:

- Strip the positive Schur denominators from the first two contractions:
  \[
    1-|\gamma_1|^2,
    \qquad 1-|\gamma_2|^2,
  \]
  whose numerator certificates are already available as `N_1` and `N_2`.
- Strip node-separation factors from the Blaschke denominators:
  \[
    |z_i-z_j|^2,
    \qquad |1-\bar z_i z_j|^2,
  \]
  using the 3+1 parametrisation.  These factors are non-negative and vanish only on collision faces.
- Work with the reduced affine remainder
  \[
    A(s,\bar s)+B(s,\bar s)x
  \]
  modulo `x^2-sx+s/bar(s)=0`, and certify it at both quadratic roots through its trace and norm over the quadratic extension, rather than expanding the full square in `(x,s,bar s)`.

Conclusion: `gamma3` is computable by Schur recursion, but the requested direct `(rho,y)` Bernstein certificate is not the right representation.  The next viable certificate is a quadratic-extension certificate after stripping the already-positive `gamma1/gamma2` factors and node-separation factors.

## Gamma3 norm/trace attempt

Goal: eliminate the remaining quadratic root by using

\[
  P_1=(1-|\gamma_3(x_1)|^2)(1-|\gamma_3(x_2)|^2),
  \qquad
  P_2=(1-|\gamma_3(x_1)|^2)+(1-|\gamma_3(x_2)|^2).
\]

The computation was carried out in the quadratic algebra

\[
  x^2-sx+s/\bar s=0.
\]

Write

\[
  \gamma_3=\frac{A(s,\bar s)+B(s,\bar s)x}{C(s,\bar s)+D(s,\bar s)x}.
\]

Sparse exact statistics for this representation are:

| coefficient | total Laurent degree | terms | max `s` degree | max `bar s` degree |
|---|---:|---:|---:|---:|
| numerator constant `A` | `76` | `963` | `42` | `34` |
| numerator linear `B` | `75` | `916` | `41` | `34` |
| denominator constant `C` | `85` | `1322` | `44` | `41` |
| denominator linear `D` | `84` | `1277` | `43` | `41` |

For

\[
  H=1-|\gamma_3|^2
   =\frac{U_0(s,\bar s)+U_1(s,\bar s)x}
          {V_0(s,\bar s)+V_1(s,\bar s)x},
\]

sparse multiplication gives:

| coefficient | total Laurent degree | terms | max `s` degree | max `bar s` degree |
|---|---:|---:|---:|---:|
| `U_0` | `169` | `5132` | `85` | `84` |
| `U_1` | `168` | `5070` | `84` | `85` |
| `V_0` | `169` | `5132` | `85` | `84` |
| `V_1` | `168` | `5070` | `84` | `85` |

Consequences:

1. The norm/trace eliminants `P1` and `P2` are expected to have total degree roughly `338`, because they require quadratic products of the `U,V` coefficients.
2. This is well above the requested degree threshold `<=100`, so the direct norm/trace Bernstein route is not viable without factor stripping.
3. The exact sparse convolution for `P1,P2` was started but did not finish in the acceptable window; it was interrupted during the multiplication of two ~5000-term Laurent polynomials.

Recommended factor stripping before retrying norm/trace:

- Remove powers of the already-certified Schur denominators from `gamma1` and `gamma2`.
- Remove node-collision factors corresponding to the two remaining unit roots:
  \[
    x_1-x_2,\qquad 1-\bar x_1x_2,
  \]
  in the quadratic algebra.
- Work with the primitive numerator of `H` after saturation by these factors, then take trace/norm.

Conclusion: direct norm/trace elimination of `gamma3` does not meet the degree `<=100` criterion. The computation identifies the correct obstruction: the unstripped `H` numerator already has degree `169` and about `5000` terms per quadratic coefficient.


# Gamma3 factor stripping results

## Raw affine H data

- U0 raw: `{'deg': 169, 'terms': 5132, 'min_s': 1, 'min_t': 1, 'max_s': 85, 'max_t': 84}`
- U1 raw: `{'deg': 168, 'terms': 5070, 'min_s': 1, 'min_t': 2, 'max_s': 84, 'max_t': 85}`
- V0 raw: `{'deg': 169, 'terms': 5132, 'min_s': 1, 'min_t': 1, 'max_s': 85, 'max_t': 84}`
- V1 raw: `{'deg': 168, 'terms': 5070, 'min_s': 1, 'min_t': 2, 'max_s': 84, 'max_t': 85}`

## Stripped common factors

### U numerator
- U: stripped common monomial s^1 t^1
- U0 primitive: `{'deg': 167, 'terms': 5132, 'min_s': 0, 'min_t': 0, 'max_s': 84, 'max_t': 83}`
- U1 primitive: `{'deg': 166, 'terms': 5070, 'min_s': 0, 'min_t': 1, 'max_s': 83, 'max_t': 84}`

### V denominator
- V: stripped common monomial s^1 t^1
- V0 primitive: `{'deg': 167, 'terms': 5132, 'min_s': 0, 'min_t': 0, 'max_s': 84, 'max_t': 83}`
- V1 primitive: `{'deg': 166, 'terms': 5070, 'min_s': 0, 'min_t': 1, 'max_s': 83, 'max_t': 84}`
- gcd(Uprim0,Uprim1): degree `136`, terms `3435`, factor `(large)`
- gcd(Vprim0,Vprim1): degree `56`, terms `615`, factor `(large)`


# Gamma3 primitive numerator after gcd stripping

## U
- common monomial: `s^1 t^1`
- gcd degree: `136`
- gcd terms: `3435`
- primitive U0 stats: `{'deg': 31, 'terms': 187, 'min_s': 0, 'min_t': 0, 'max_s': 16, 'max_t': 15}`
- primitive U1 stats: `{'deg': 30, 'terms': 180, 'min_s': 0, 'min_t': 1, 'max_s': 15, 'max_t': 16}`
- gcd symmetric under `s<->t`: `True`

## V
- common monomial: `s^1 t^1`
- gcd degree: `56`
- gcd terms: `615`
- primitive V0 stats: `{'deg': 111, 'terms': 2269, 'min_s': 0, 'min_t': 0, 'max_s': 56, 'max_t': 55}`
- primitive V1 stats: `{'deg': 110, 'terms': 2230, 'min_s': 0, 'min_t': 1, 'max_s': 55, 'max_t': 56}`
- gcd symmetric under `s<->t`: `True`
- V gcd factorization: `(s + 2)*(t + 2)*(8*s**13*t**14 + 48*s**13*t**13 + 82*s**13*t**12 - 30*s**13*t**11 - 230*s**13*t**10 - 212*s**13*t**9 + 24*s**13*t**8 + 160*s**13*t**7 + 112*s**13*t**6 + 34*s**13*t**5 + 4*s**13*t**4 + 12*s**12*t**14 + 52*s**12*t**13 - 69*s**12*t**12 - 648*s**12*t**11 - 872*s**12*t**10 + 449*s**12*t**9 + 1622*s**12*t**8 + 712*s**12*t**7 - 582*s**12*t**6 - 647*s**12*t**5 - 219*s**12*t**4 - 26*s**12*t**3 - 28*s**11*t**14 - 140*s**11*t**13 - 649*s**11*t**12 - 1955*s**11*t**11 - 557*s**11*t**10 + 6503*s**11*t**9 + 7833*s**11*t**8 - 1496*s**11*t**7 - 6125*s**11*t**6 - 2229*s**11*t**5 + 450*s**11*t**4 + 307*s**11*t**3 + 30*s**11*t**2 - 16*s**10*t**14 + 128*s**10*t**13 + 13*s**10*t**12 - 1111*s**10*t**11 + 5053*s**10*t**10 + 17798*s**10*t**9 + 4445*s**10*t**8 - 24579*s**10*t**7 - 17226*s**10*t**6 + 7752*s**10*t**5 + 9014*s**10*t**4 + 1882*s**10*t**3 + 139*s**10*t**2 + 38*s**10*t + 48*s**9*t**14 + 60*s**9*t**13 - 977*s**9*t**12 + 1362*s**9*t**11 + 18416*s**9*t**10 + 20003*s**9*t**9 - 39587*s**9*t**8 - 80094*s**9*t**7 - 13924*s**9*t**6 + 48783*s**9*t**5 + 23154*s**9*t**4 - 2592*s**9*t**3 - 2258*s**9*t**2 - 244*s**9*t + 8*s**9 - 16*s**8*t**14 - 916*s**8*t**13 - 1736*s**8*t**12 + 8792*s**8*t**11 + 19216*s**8*t**10 - 28143*s**8*t**9 - 103954*s**8*t**8 - 64052*s**8*t**7 + 71660*s**8*t**6 + 91190*s**8*t**5 - 3380*s**8*t**4 - 28128*s**8*t**3 - 8992*s**8*t**2 - 1096*s**8*t - 80*s**8 - 28*s**7*t**14 - 124*s**7*t**13 + 4117*s**7*t**12 + 14937*s**7*t**11 - 10985*s**7*t**10 - 94693*s**7*t**9 - 89768*s**7*t**8 + 98403*s**7*t**7 + 219438*s**7*t**6 + 74784*s**7*t**5 - 75184*s**7*t**4 - 53760*s**7*t**3 - 11104*s**7*t**2 - 896*s**7*t + 12*s**6*t**14 + 440*s**6*t**13 + 2511*s**6*t**12 - 1623*s**6*t**11 - 34926*s**6*t**10 - 67440*s**6*t**9 + 28198*s**6*t**8 + 227514*s**6*t**7 + 223706*s**6*t**6 - 9732*s**6*t**5 - 95936*s**6*t**4 - 35488*s**6*t**3 - 3776*s**6*t**2 + 8*s**5*t**14 + 60*s**5*t**13 - 1107*s**5*t**12 - 7856*s**5*t**11 - 18948*s**5*t**10 - 4063*s**5*t**9 + 93270*s**5*t**8 + 186336*s**5*t**7 + 87100*s**5*t**6 - 66920*s**5*t**5 - 53904*s**5*t**4 - 8320*s**5*t**3 - 40*s**4*t**13 - 579*s**4*t**12 - 1866*s**4*t**11 + 312*s**4*t**10 + 22658*s**4*t**9 + 67324*s**4*t**8 + 64144*s**4*t**7 - 16928*s**4*t**6 - 44016*s**4*t**5 + 26144*s**4*t**4 + 14*s**3*t**12 + 314*s**3*t**11 + 3308*s**3*t**10 + 13600*s**3*t**9 + 18528*s**3*t**8 - 608*s**3*t**7 - 20192*s**3*t**6 - 8320*s**3*t**5 + 52*s**2*t**11 + 723*s**2*t**10 + 1838*s**2*t**9 - 5408*s**2*t**7 - 3776*s**2*t**6 - 26*s*t**10 - 324*s*t**9 - 824*s*t**8 - 896*s*t**7 - 8*t**9 - 80*t**8)*(8*s**14*t**13 + 12*s**14*t**12 - 28*s**14*t**11 - 16*s**14*t**10 + 48*s**14*t**9 - 16*s**14*t**8 - 28*s**14*t**7 + 12*s**14*t**6 + 8*s**14*t**5 + 48*s**13*t**13 + 52*s**13*t**12 - 140*s**13*t**11 + 128*s**13*t**10 + 60*s**13*t**9 - 916*s**13*t**8 - 124*s**13*t**7 + 440*s**13*t**6 + 60*s**13*t**5 - 40*s**13*t**4 + 82*s**12*t**13 - 69*s**12*t**12 - 649*s**12*t**11 + 13*s**12*t**10 - 977*s**12*t**9 - 1736*s**12*t**8 + 4117*s**12*t**7 + 2511*s**12*t**6 - 1107*s**12*t**5 - 579*s**12*t**4 + 14*s**12*t**3 - 30*s**11*t**13 - 648*s**11*t**12 - 1955*s**11*t**11 - 1111*s**11*t**10 + 1362*s**11*t**9 + 8792*s**11*t**8 + 14937*s**11*t**7 - 1623*s**11*t**6 - 7856*s**11*t**5 - 1866*s**11*t**4 + 314*s**11*t**3 + 52*s**11*t**2 - 230*s**10*t**13 - 872*s**10*t**12 - 557*s**10*t**11 + 5053*s**10*t**10 + 18416*s**10*t**9 + 19216*s**10*t**8 - 10985*s**10*t**7 - 34926*s**10*t**6 - 18948*s**10*t**5 + 312*s**10*t**4 + 3308*s**10*t**3 + 723*s**10*t**2 - 26*s**10*t - 212*s**9*t**13 + 449*s**9*t**12 + 6503*s**9*t**11 + 17798*s**9*t**10 + 20003*s**9*t**9 - 28143*s**9*t**8 - 94693*s**9*t**7 - 67440*s**9*t**6 - 4063*s**9*t**5 + 22658*s**9*t**4 + 13600*s**9*t**3 + 1838*s**9*t**2 - 324*s**9*t - 8*s**9 + 24*s**8*t**13 + 1622*s**8*t**12 + 7833*s**8*t**11 + 4445*s**8*t**10 - 39587*s**8*t**9 - 103954*s**8*t**8 - 89768*s**8*t**7 + 28198*s**8*t**6 + 93270*s**8*t**5 + 67324*s**8*t**4 + 18528*s**8*t**3 - 824*s**8*t - 80*s**8 + 160*s**7*t**13 + 712*s**7*t**12 - 1496*s**7*t**11 - 24579*s**7*t**10 - 80094*s**7*t**9 - 64052*s**7*t**8 + 98403*s**7*t**7 + 227514*s**7*t**6 + 186336*s**7*t**5 + 64144*s**7*t**4 - 608*s**7*t**3 - 5408*s**7*t**2 - 896*s**7*t + 112*s**6*t**13 - 582*s**6*t**12 - 6125*s**6*t**11 - 17226*s**6*t**10 - 13924*s**6*t**9 + 71660*s**6*t**8 + 219438*s**6*t**7 + 223706*s**6*t**6 + 87100*s**6*t**5 - 16928*s**6*t**4 - 20192*s**6*t**3 - 3776*s**6*t**2 + 34*s**5*t**13 - 647*s**5*t**12 - 2229*s**5*t**11 + 7752*s**5*t**10 + 48783*s**5*t**9 + 91190*s**5*t**8 + 74784*s**5*t**7 - 9732*s**5*t**6 - 66920*s**5*t**5 - 44016*s**5*t**4 - 8320*s**5*t**3 + 4*s**4*t**13 - 219*s**4*t**12 + 450*s**4*t**11 + 9014*s**4*t**10 + 23154*s**4*t**9 - 3380*s**4*t**8 - 75184*s**4*t**7 - 95936*s**4*t**6 - 53904*s**4*t**5 + 26144*s**4*t**4 - 26*s**3*t**12 + 307*s**3*t**11 + 1882*s**3*t**10 - 2592*s**3*t**9 - 28128*s**3*t**8 - 53760*s**3*t**7 - 35488*s**3*t**6 - 8320*s**3*t**5 + 30*s**2*t**11 + 139*s**2*t**10 - 2258*s**2*t**9 - 8992*s**2*t**8 - 11104*s**2*t**7 - 3776*s**2*t**6 + 38*s*t**10 - 244*s*t**9 - 1096*s*t**8 - 896*s*t**7 + 8*t**9 - 80*t**8)/64`



# Gamma3 primitive norm Bernstein attempt

- primitive U0 stats: `{'deg': 31, 'terms': 187, 'min_s': 0, 'min_t': 0, 'max_s': 16, 'max_t': 15}`
- primitive U1 stats: `{'deg': 30, 'terms': 180, 'min_s': 0, 'min_t': 1, 'max_s': 15, 'max_t': 16}`
- norm stats in `(s,t)`: `{'deg': 62, 'terms': 720, 'min_s': 0, 'min_t': 0, 'max_s': 31, 'max_t': 31}`
- norm degree in `(rho,y)`: `(62,28)`, terms `1012`

- box `(0, 1/2, 0, 1)`: degree `(62,28)`, min Bernstein `309190658327820801/1048576`, negative coeffs `0`, zeros `0`
- box `(1/2, 1, 0, 1/2)`: degree `(62,28)`, min Bernstein `0`, negative coeffs `0`, zeros `6`
- box `(1/2, 1, 1/2, 1)`: degree `(62,28)`, min Bernstein `-590461714015821921572093952/134456145839015`, negative coeffs `41`, zeros `120`
- 3-box Bernstein success: `False`



# Gamma3 hard-box local Bernstein analysis

- polynomial degree `(rho,y)`: `(62, 28, 1012)`

- box rho `1/2..3/4`, y `1/2..3/4`: min `906014968947135130547403/67108864`, neg `0`, zeros `0`, neg Bernstein indices `none`
- box rho `1/2..3/4`, y `3/4..1`: min `100434619660855359168782829488889/309485009821345068724781056`, neg `0`, zeros `0`, neg Bernstein indices `none`
- box rho `3/4..1`, y `1/2..3/4`: min `0`, neg `0`, zeros `6`, neg Bernstein indices `none`
- box rho `3/4..1`, y `3/4..1`: min `-274697155099742373440600284645277273/16151395234811033189744640`, neg `70`, zeros `114`, neg Bernstein indices `I 23-61 of 62, J 16-18 of 28`

- dyadic certified R0: `3/4` (all tested boxes with rho <= R0 have no negative Bernstein coefficients)
- divisibility by `1-rho`: `False`
- divisibility by `1+rho`: `False`
- divisibility by `1-rho^2`: `False`
- divisibility by `1-y`: `False`
- divisibility by `1-rho*y`: `False`
- negative coefficients remain only in: rho 3/4..1, y 3/4..1


# Gamma3 square-corner 4x4 Bernstein subdivision (direct 80-digit screen)

- polynomial degree `(rho,y)`: `(62,28)`, terms `1012`

- cell (0,0) rho `3/4..13/16`, y `3/4..13/16`: neg `0`, zeros `0`, approx min `2417626474934188.12`, approx min negative `None`
- cell (0,1) rho `3/4..13/16`, y `13/16..7/8`: neg `0`, zeros `0`, approx min `36244785691906.356`, approx min negative `None`
- cell (0,2) rho `3/4..13/16`, y `7/8..15/16`: neg `0`, zeros `0`, approx min `29698560573.748213`, approx min negative `None`
- cell (0,3) rho `3/4..13/16`, y `15/16..1`: neg `0`, zeros `0`, approx min `913.342977212062773`, approx min negative `None`
- cell (1,0) rho `13/16..7/8`, y `3/4..13/16`: neg `0`, zeros `0`, approx min `4279238294473095.96`, approx min negative `None`
- cell (1,1) rho `13/16..7/8`, y `13/16..7/8`: neg `0`, zeros `0`, approx min `54359210393448.837`, approx min negative `None`
- cell (1,2) rho `13/16..7/8`, y `7/8..15/16`: neg `0`, zeros `0`, approx min `29151198622.5295912`, approx min negative `None`
- cell (1,3) rho `13/16..7/8`, y `15/16..1`: neg `0`, zeros `0`, approx min `0.197982105158979362`, approx min negative `None`
- cell (2,0) rho `7/8..15/16`, y `3/4..13/16`: neg `0`, zeros `0`, approx min `8585160751179094.81`, approx min negative `None`
- cell (2,1) rho `7/8..15/16`, y `13/16..7/8`: neg `0`, zeros `0`, approx min `106162832743866.064`, approx min negative `None`
- cell (2,2) rho `7/8..15/16`, y `7/8..15/16`: neg `0`, zeros `0`, approx min `40794779326.8447007`, approx min negative `None`
- cell (2,3) rho `7/8..15/16`, y `15/16..1`: neg `52`, zeros `0`, approx min `-344787.013073226396`, approx min negative `-344787.013073226396`
- cell (3,0) rho `15/16..1`, y `3/4..13/16`: neg `0`, zeros `0`, approx min `18631381492077352.0`, approx min negative `None`
- cell (3,1) rho `15/16..1`, y `13/16..7/8`: neg `0`, zeros `0`, approx min `246202688954713.071`, approx min negative `None`
- cell (3,2) rho `15/16..1`, y `7/8..15/16`: neg `0`, zeros `0`, approx min `105252941864.269572`, approx min negative `None`
- cell (3,3) rho `15/16..1`, y `15/16..1`: neg `161`, zeros `0`, approx min `-342187.155070624543`, approx min negative `-342187.155070624543`

- neg=0 cells: `[(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2)]`
- bad cells: `[(2, 3, 52), (3, 3, 161)]`
- parent hard box neg count: `70`
- max child neg count: `161`
- parent min negative abs approx: `17007642442.4119576`
- smallest child min-negative abs approx: `342187.155070624543`
- largest child min-negative abs approx: `344787.013073226396`
- trend: neg count decreased `False`, smallest min-negative absolute value decreased `True`


# Gamma3 hard corner exact rational Bernstein

- polynomial degree `(rho,y)`: `(62,28)`, terms `1012`

## Step 1: exact hard corner
- box rho `[7/8,1]`, y `[15/16,1]`: neg `115`, zeros `114`, min `-1370816954660694560708263737002383106589294393224052434382740531/301655067728591803560026039243025241825848298004017053...`, minneg `-1370816954660694560708263737002383106589294393224052434382740531/301655067728591803560026039243025241825848298004017053...`, minloc `(25, 13)`

## Step 2: exact 2x2 subdivision
- child (0,0) rho `7/8..15/16`, y `15/16..31/32`: neg `0`, zeros `0`, min `488560865957804909681804658274562511434785217399689001481844695984247804223/36741893745967723947411581115946898571429370...`, minneg `none`, minloc `None`
- child (0,1) rho `7/8..15/16`, y `31/32..1`: neg `0`, zeros `0`, min `517341149503841066080143138088422028141397731138561512225/65820182292848241686198767302294020199309434625343194533944360...`, minneg `none`, minloc `None`
- child (1,0) rho `15/16..1`, y `15/16..31/32`: neg `0`, zeros `0`, min `23744041011906288111811649427857104219878713184865554671903326022925/803469022129495137770981046170581301261101496891396...`, minneg `none`, minloc `None`
- child (1,1) rho `15/16..1`, y `31/32..1`: neg `162`, zeros `114`, min `-372638583630311184353846413942246702152301354869031833027197049669293598147568193/2400704213726102584183637704613429137...`, minneg `-372638583630311184353846413942246702152301354869031833027197049669293598147568193/2400704213726102584183637704613429137...`, minloc `(12, 11)`
- exact bad children: `[(1, 1, 162, (12, 11))]`
- smallest exact child min-negative abs: `372638583630311184353846413942246702152301354869031833027197049669293598147568193/24007042137261025841836377046134291377...`
- approximate Bernstein-index coordinates for worst negatives: `[(1, 1, 471/496, 879/896)]`

# Gamma4 direct Schur-contraction attempt

Using the same ordering as above (interior node first, then the fixed unit node, then the two quadratic unit roots), direct SymPy construction of the terminal Schur parameter was attempted by running the third Schur contraction in the quadratic algebra

\[
  x^2-sx+s/\bar s=0.
\]

The first two contractions completed, leaving two residual points.  The third contraction stalled in the expansion/reduction of

\[
  \frac{(w_j-w_0)/(1-\bar w_0w_j)}{(z_j-z_0)/(1-\bar z_0z_j)}
\]

and was interrupted inside `expand(num)` during the reduction modulo the quadratic relation.  This means the direct affine-fraction representation of `gamma4` is not currently computationally viable with the naive SymPy expression tree.

Recommended replacement route:

- Do not form `gamma4` directly.
- Use the determinant-ratio identity for Schur parameters of a Pick matrix:
  \[
    \prod_{m=1}^k (1-|\gamma_m|^2)=\frac{\det P_k}{\det K_k}
  \]
  for the first `k` nodes, with the same ordering.
- Since `gamma1`, `gamma2`, and the primitive numerator for `gamma3` have already been computed, the terminal condition for `gamma4` should be obtained from the normalized `4x4` determinant divided by the certified lower-order factors.

Conclusion: direct `gamma4` construction is heavier than `gamma3`, not simpler, under naive symbolic contraction. The next viable route is determinant-ratio / normalized principal determinant rather than explicit terminal Schur fraction.

# Reduced Pick 4x4 determinant attempt on the 3+1 stratum

Goal: compute the determinant numerator of the full reduced Pick matrix on the general `3+1` stratum and use it as the determinant-ratio certificate for the terminal Schur parameter.

Two direct symbolic attempts were made.

## Boundary determinant is singular without radial regularization

Using boundary nodes

\[
  \lambda=-(1+s),\quad 1,\\quad x,\\quad s-x,
  \qquad x^2-sx+s/\bar s=0,
\]

the naive reduced Pick matrix entries contain diagonal `0/0` terms at the three unit nodes. SymPy returns `nan` for the determinant. This is mathematically expected: the boundary Pick matrix requires an angular-derivative limiting interpretation, not direct substitution into

\[
  \frac{1-r_i\bar r_j}{1-\lambda_i\bar\lambda_j}.
\]

## Radial regularization

A radial regularization was then used:

\[
  \lambda=q\{-(1+s),1,x,s-x\},\qquad 0<q<1,
\]

which preserves centering and makes all Pick entries finite. The reduced values were recomputed from the scaled elementary coefficients

\[
  a_2=q^2a_2^{(0)},\qquad a_1=q^3a_1^{(0)},\qquad a_0=q^4a_0^{(0)}.
\]

The 16 matrix entries were successfully constructed and reduced modulo

\[
  x^2-sx+s/\bar s=0.
\]

However, two determinant strategies stalled:

1. `Matrix.det(method='berkowitz')` followed by `factor/together` stalled in a full expression expansion.
2. A manual 24-term permutation determinant with reduction after each multiplication stalled in polynomial gcd/cancel during multiplication of rational entries.

Thus the determinant-ratio route is conceptually correct, but the direct rational determinant is still too heavy in the current SymPy representation.

## Next viable implementation

The next implementation should avoid rational-entry determinants. Options:

- Compute a fraction-free determinant after multiplying each row/column by known positive Szego denominators before reduction.
- Work modulo several machine primes and reconstruct the cleared numerator by sparse interpolation in `(q,s,bar s)`.
- Use the Schur determinant identity with already cached lower pivots and compute only the normalized principal determinant, not the raw Pick determinant.

Conclusion: direct `det Pi_red_4` on the boundary is ill-defined; radial regularization fixes the definition but not the computational size. No Bernstein certificate was produced in this run.
# Cleared reduced Pick determinant mod-p probe

- prime `1000000007`
- cleared blackbox used: `det(num_ij * product_all_den/den_ij) = D^4 det(Pi_red)`; polynomial away from sampled denominator zeros.

## 1000 random samples

- valid `1000`
- bad denominator samples `0`
- imaginary leakage `0`
- elapsed `0.10s`

## Berlekamp-Massey line complexity

- `random line`: BM recurrence length `130`, samples `260`, bad `0`, imag `0`
- `x1`: BM recurrence length `130`, samples `260`, bad `0`, imag `0`
- `x2`: BM recurrence length `130`, samples `260`, bad `0`, imag `0`
- `y2`: BM recurrence length `130`, samples `260`, bad `0`, imag `0`
- `x3`: BM recurrence length `130`, samples `260`, bad `0`, imag `0`
- `y3`: BM recurrence length `130`, samples `260`, bad `0`, imag `0`

Interpretation: for a univariate polynomial of degree d sampled on consecutive field points, BM length is d+1 generically. These values are a degree-complexity proxy for the heavily cleared determinant, not a formal sparse interpolation certificate.

# Cleared determinant clearing-variant probe

## Variant `global`
- 500 samples valid `500`, bad `0`, imag `0`, elapsed `0.05s`
- `random` BM length `130`, samples `260`, bad `0`, imag `0`
- `x1` BM length `130`, samples `260`, bad `0`, imag `0`
- `x2` BM length `130`, samples `260`, bad `0`, imag `0`
- `y2` BM length `130`, samples `260`, bad `0`, imag `0`
- `x3` BM length `130`, samples `260`, bad `0`, imag `0`
- `y3` BM length `130`, samples `260`, bad `0`, imag `0`

## Variant `row`
- 500 samples valid `500`, bad `0`, imag `0`, elapsed `0.05s`
- `random` BM length `93`, samples `260`, bad `0`, imag `0`
- `x1` BM length `87`, samples `260`, bad `0`, imag `0`
- `x2` BM length `87`, samples `260`, bad `0`, imag `0`
- `y2` BM length `87`, samples `260`, bad `0`, imag `0`
- `x3` BM length `87`, samples `260`, bad `0`, imag `0`
- `y3` BM length `87`, samples `260`, bad `0`, imag `0`



# Row-cleared determinant sparse/Kronecker probe

- target: row-cleared polynomial `D det(Pi_red)` in five real variables.
- method: substitute `v_i=a_i*tau^{w_i}` over F_p and use BM recurrence length as univariate support/degree proxy.

- weights `[1, 10, 100, 1000, 10000]`: BM length `160`, samples `320`, bad `0`, imag `0`, elapsed `0.04s`
- weights `[1, 7, 49, 343, 2401]`: BM length `160`, samples `320`, bad `0`, imag `0`, elapsed `0.03s`
- weights `[3, 5, 11, 17, 29]`: BM length `160`, samples `320`, bad `0`, imag `0`, elapsed `0.03s`
- weights `[1, 13, 17, 19, 23]`: BM length `160`, samples `320`, bad `0`, imag `0`, elapsed `0.03s`

Interpretation: large Kronecker weights encode multidegrees into a high univariate degree; BM length here is a collision-prone proxy for support/degree, not a certified term count. If lengths remain near the affine-line value (~93), the polynomial has strong cancellations/symmetry; if they explode, sparse interpolation will be expensive.


# Row-cleared determinant SOS slice probe

- target: row-cleared reduced Pick determinant `D det(Pi_red)` on fixed low-dimensional real slices.
- this is a numerical SOS feasibility probe, not a proof certificate.
- cvxpy available: `False`

## Base point 0: `[0.1, 0.05, 0.07, -0.08, 0.03]`
- value at base: `1.305371422270e-10`
- 1D slice `x1` degree `40` fit: sample min `8.751e-12`, max `3.849e-06`
  - SOS skipped: cvxpy not available
- 1D slice `x2` degree `40` fit: sample min `3.389e-11`, max `5.343e-06`
  - SOS skipped: cvxpy not available
- 1D slice `y2` degree `40` fit: sample min `3.953e-13`, max `7.922e-06`
  - SOS skipped: cvxpy not available
- 1D slice `x3` degree `40` fit: sample min `2.897e-11`, max `3.896e-06`
  - SOS skipped: cvxpy not available
- 1D slice `y3` degree `40` fit: sample min `8.518e-13`, max `3.385e-06`
  - SOS skipped: cvxpy not available
- 2D slice `(x3,y3)` total-degree fit/SOS size probe: `{'deg': 12, 'terms': 91, 'fit_rel_res': np.float64(1.041456592543943e-09), 'rank': np.int32(91), 'global_sos_gram_dim': 28, 'box_sos_note': 'interval SOS would need multiplier Gram matrices; this is size probe only'}`

## Base point 1: `[0.3, 0.1, 0.05, -0.12, 0.08]`
- value at base: `1.667518715450e-06`
- 1D slice `x1` degree `40` fit: sample min `4.867e-10`, max `9.601e-06`
  - SOS skipped: cvxpy not available
- 1D slice `x2` degree `40` fit: sample min `7.283e-09`, max `2.450e-05`
  - SOS skipped: cvxpy not available
- 1D slice `y2` degree `40` fit: sample min `9.329e-07`, max `4.040e-04`
  - SOS skipped: cvxpy not available
- 1D slice `x3` degree `40` fit: sample min `1.896e-07`, max `2.541e-05`
  - SOS skipped: cvxpy not available
- 1D slice `y3` degree `40` fit: sample min `5.271e-07`, max `1.780e-04`
  - SOS skipped: cvxpy not available
- 2D slice `(x3,y3)` total-degree fit/SOS size probe: `{'deg': 12, 'terms': 91, 'fit_rel_res': np.float64(6.60284286040688e-09), 'rank': np.int32(91), 'global_sos_gram_dim': 28, 'box_sos_note': 'interval SOS would need multiplier Gram matrices; this is size probe only'}`

## Conclusion

- Direct high-degree 5D SOS is not computationally viable from samples.
- Moderate 1D interval SOS slices are feasible to test with Markov-Lukacs Gram matrices.
- 2D SOS is only plausible for low-degree fitted slices; the true determinant degree proxy (~92) would create very large Gram systems.

# Logdet bad-condition rerun

The first near-collision finite-difference probe showed a large value at `h=1e-3`, but a local quadratic fit on the same ill-conditioned regime stabilized the estimate.

## Fit-based result

- accepted points: `60`
- points with `max|Delta| > 0.1`: `0/60`
- max `|Delta|` across all accepted coordinate Laplacians: `1.094428e-02`
- worst sample `kappa(Pi_red)`: `1.752594e+08`
- worst sample `|lambda1-lambda2|`: `3.370728e-03`
- worst sample Laplacians: `['-1.094428e-02', '2.997431e-03', '1.243992e-03']`

Interpretation: the bad-condition region does not currently refute a log-harmonic structure. The `h` search remains live.


# Numerical test of subharmonicity for log det(Pi_red)

- tested stronger ungauged complex coordinates: `lambda1,lambda2,lambda3` complex, `lambda4=-sum`.
- Laplacian for each coordinate is `d_x^2 + d_y^2` of `log(abs(det(Pi_red)))` with central difference `h=1e-5`.
- random points satisfy `max |lambda_j| < 0.9` and avoid collisions.

## Results

- total coordinate Laplacian evaluations: `3000`
- skipped evaluations: `0`
- coordinate lambda1: min Laplacian `-6.169145194690e+00`, max `3.117862634738e+01`, negative count (< -1e-3) `13`
  - worst roots: `[(0.04016593448914744+0.14901811177682242j), (0.05606925895624464+0.026120467833853196j), (-0.14317346590717753-0.24214273724196314j), (0.046938272461785446+0.06700415763128753j)]`
- coordinate lambda2: min Laplacian `-9.596199390671e+00`, max `3.072777587931e+01`, negative count (< -1e-3) `9`
  - worst roots: `[(0.04016593448914744+0.14901811177682242j), (0.05606925895624464+0.026120467833853196j), (-0.14317346590717753-0.24214273724196314j), (0.046938272461785446+0.06700415763128753j)]`
- coordinate lambda3: min Laplacian `-7.927383194328e+00`, max `2.891615724643e+01`, negative count (< -1e-3) `13`
  - worst roots: `[(0.04016593448914744+0.14901811177682242j), (0.05606925895624464+0.026120467833853196j), (-0.14317346590717753-0.24214273724196314j), (0.046938272461785446+0.06700415763128753j)]`

## Conclusion

The numerical subharmonicity test fails: `log|det(Pi_red)|` has negative coordinate Laplacians at random interior points. Therefore the proposed minimum-on-boundary argument cannot be used in this direct form.


# Numerical test of subharmonicity for log det(Pi_red)

- tested stronger ungauged complex coordinates: `lambda1,lambda2,lambda3` complex, `lambda4=-sum`.
- Laplacian for each coordinate is `d_x^2 + d_y^2` of `log(abs(det(Pi_red)))` with central difference `h=1e-5`.
- random points satisfy `max |lambda_j| < 0.9` and avoid collisions.

## Results

- total coordinate Laplacian evaluations: `3000`
- skipped evaluations: `0`
- coordinate lambda1: min Laplacian `-6.169145194690e+00`, max `3.117862634738e+01`, negative count (< -1e-3) `13`
  - worst roots: `[(0.04016593448914744+0.14901811177682242j), (0.05606925895624464+0.026120467833853196j), (-0.14317346590717753-0.24214273724196314j), (0.046938272461785446+0.06700415763128753j)]`
- coordinate lambda2: min Laplacian `-9.596199390671e+00`, max `3.072777587931e+01`, negative count (< -1e-3) `9`
  - worst roots: `[(0.04016593448914744+0.14901811177682242j), (0.05606925895624464+0.026120467833853196j), (-0.14317346590717753-0.24214273724196314j), (0.046938272461785446+0.06700415763128753j)]`
- coordinate lambda3: min Laplacian `-7.927383194328e+00`, max `2.891615724643e+01`, negative count (< -1e-3) `13`
  - worst roots: `[(0.04016593448914744+0.14901811177682242j), (0.05606925895624464+0.026120467833853196j), (-0.14317346590717753-0.24214273724196314j), (0.046938272461785446+0.06700415763128753j)]`

## Conclusion

The numerical subharmonicity test fails: `log|det(Pi_red)|` has negative coordinate Laplacians at random interior points. Therefore the proposed minimum-on-boundary argument cannot be used in this direct form.


# Logdet Laplacian diagnostic at worst sampled point

- roots: `[(0.04016593448914744+0.14901811177682242j), (0.05606925895624464+0.026120467833853196j), (-0.14317346590717753-0.24214273724196314j), (0.046938272461785446+0.06700415763128753j)]`
- max |lambda|: `2.813036553956e-01`
- min separation: `4.189094181103e-02`
- det Pi_red: `(5.039060773989318e-10+5.779975377486866e-22j)`
- logabsdet: `-2.140863121959e+01`

- h `1e-03` Laplacians: `[np.float64(-1.0235859733143116), np.float64(-6.663992625277388), np.float64(0.670970798921644)]`
- h `3e-04` Laplacians: `[np.float64(-0.05055697095531286), np.float64(-0.5926948808282759), np.float64(1.0746464656422177)]`
- h `1e-04` Laplacians: `[np.float64(-0.019738166656679823), np.float64(-0.1478078104355518), np.float64(1.035832042362017)]`
- h `3e-05` Laplacians: `[np.float64(-0.9612616875328968), np.float64(-0.8963536086212116), np.float64(0.44395104876252844)]`
- h `1e-05` Laplacians: `[np.float64(-6.169145194689918), np.float64(-9.596199390671245), np.float64(-7.927383194328286)]`
- h `3e-06` Laplacians: `[np.float64(-106.6473329400551), np.float64(-121.06542928652016), np.float64(-100.94443799365149)]`
- h `1e-06` Laplacians: `[np.float64(-746.7093610102893), np.float64(-568.9670956599002), np.float64(-790.1341803062678)]`

- Hermitian eigenvalues of Pi_red: `[9.723796576750683e-07, 0.0011084916146066584, 0.11678689752245201, 4.003014819545978]`
- condition estimate: `4116720.036201776`
- det Szego K: `(5.039060773989318e-10+5.736083519465889e-22j)`

## Corrected log scan at h=1e-5

- alpha `-2` for logdetPi + alpha logdetK: `[np.float64(6.169358357510646), np.float64(9.59683887913343), np.float64(7.927880574243318)]`
- alpha `-1` for logdetPi + alpha logdetK: `[np.float64(0.00010658141036401501), np.float64(0.00031974423109204503), np.float64(0.000248689957516035)]`
- alpha `-0.5` for logdetPi + alpha logdetK: `[np.float64(-3.084519306639777), np.float64(-4.7979398232200765), np.float64(-3.963567252185385)]`
- alpha `0.5` for logdetPi + alpha logdetK: `[np.float64(-9.254037536265969), np.float64(-14.394601066669566), np.float64(-11.89128795431293)]`
- alpha `1` for logdetPi + alpha logdetK: `[np.float64(-12.338361443653412), np.float64(-19.192682998436794), np.float64(-15.8549795514773)]`
- alpha `2` for logdetPi + alpha logdetK: `[np.float64(-18.508075072531938), np.float64(-28.789486350433435), np.float64(-23.783002234267315)]`
- alpha `4` for logdetPi + alpha logdetK: `[np.float64(-30.845654919176013), np.float64(-47.98181407750235), np.float64(-39.63762651437719)]`


# Determinant-ratio Schur identity and Laplacian test

## Mod-p identity test

- valid samples: `1000`
- denominator failures: `0`
- user exponent formula matches: `0/1000`
- standard exponent formula `prod(1-|gamma_k|^2)^(5-k)` matches: `0/1000`
- first mismatch example lhs/rhs_user: `(949221379, 0)` vs `(974912807, 0)`

## Numerical Laplacian of log(det Pi_red / det K)

- central difference h `1e-3`; points with `kappa(Pi_red)>1e4` skipped.
- accepted Laplacian evaluations: `810`
- skipped evaluations: `690`
- |Laplacian| < 0.1 count: `810/810`
- min Laplacian: `-1.623169e-02`
- max Laplacian: `1.524225e-06`
- max abs Laplacian: `1.623169e-02`

## Conclusion

The user-stated exponent formula is not the determinant-ratio identity. The standard exponent formula is the one tested. Numerical Laplacian results should be interpreted with this corrected identity.


# Determinant-ratio Schur identity and Laplacian test

## Mod-p identity test

- valid samples: `1000`
- denominator failures: `0`
- user exponent formula matches: `0/1000`
- standard exponent formula `prod(1-|gamma_k|^2)^(5-k)` matches: `0/1000`
- first mismatch example lhs/rhs_user: `(949221379, 0)` vs `(974912807, 0)`

## Numerical Laplacian of log(det Pi_red / det K)

- central difference h `1e-3`; points with `kappa(Pi_red)>1e4` skipped.
- accepted Laplacian evaluations: `810`
- skipped evaluations: `690`
- |Laplacian| < 0.1 count: `810/810`
- min Laplacian: `-1.623169e-02`
- max Laplacian: `1.524225e-06`
- max abs Laplacian: `1.623169e-02`

## Conclusion

The user-stated exponent formula is not the determinant-ratio identity. The standard exponent formula is the one tested. Numerical Laplacian results should be interpreted with this corrected identity.

## Exponent-pattern search for determinant ratio

After the initial mod-p test failed for both the user-proposed exponents `(3,2,1,0)` and the standard naive exponents `(4,3,2,1)`, a brute-force search over all exponent vectors

\[
  (e_1,e_2,e_3,e_4)\in\{0,1,\ldots,6\}^4
\]

was run on 20 independent finite-field samples. No exponent vector matched

\[
  \det(\Pi^{\rm red})/\det(K)
  =\prod_k(1-|\gamma_k|^2)^{e_k}.
\]

Thus the determinant quotient is not a pure monomial in the Schur gap factors for the Schur normalization used here. The near-zero numerical Laplacian of

\[
  \log\left|\det(\Pi^{\rm red})/\det(K)\right|
\]

therefore appears to come from a different holomorphic quotient structure, not from the simple Schur-gap product formula.


# Exact mod-p tests for candidate h

- prime: `1000000007`
- valid samples: `1000`
- rejected samples: `0`
- total tries: `1000`

## Candidate A

- formula: `|prod_{i<j}(r_i-r_j)|^2 / |prod_{i<j}(lambda_i-lambda_j)|^2`
- matches: `0/1000`
- first mismatch lhs/rhs: `(148679683, 0)` vs `(583064394, 0)`

## Candidate B

- formula: `|prod_{i<j}(r_i-r_j)/(1-r_i conj(r_j))|^2 / |prod_{i<j}(lambda_i-lambda_j)/(1-lambda_i conj(lambda_j))|^2`
- matches: `0/1000`
- first mismatch lhs/rhs: `(148679683, 0)` vs `(890988107, 0)`

## Candidate C

- formula: `|det[(r_i-r_j)/(lambda_i-lambda_j)]_{i!=j}|^2` with zero diagonal
- matches: `0/1000`
- first mismatch lhs/rhs: `(148679683, 0)` vs `(236786348, 0)`


# Logdet Laplacian on near-collision ill-conditioned points

- target points: `|lambda1-lambda2| < 0.01` and `kappa(Pi_red) > 10^4`
- finite difference step: `h = 1e-3`

## Summary

- accepted points: `60`
- skipped points: `0`
- max `|Delta|` across all accepted coordinate Laplacians: `1.307279e-01`

## Samples

- sample `1`: `|lambda1-lambda2|=3.511850e-03`, kappa `1.845835e+07`, Laplacians `['-4.736142e-03', '-4.498832e-03', '-1.968323e-03']`, max|Delta| `4.736142e-03`
  - roots: `[(0.2031985302052313-0.1516206582076574j), (0.20663790794556675-0.15091088933222038j), (0.10815529855684504+0.062413497057488006j), (-0.5179917367076431+0.24011805048238977j)]`
- sample `2`: `|lambda1-lambda2|=6.671141e-03`, kappa `2.365099e+06`, Laplacians `['3.081175e-04', '2.079139e-04', '1.914963e-04']`, max|Delta| `3.081175e-04`
  - roots: `[(0.06154399003758076-0.24650177432503326j), (0.061811534179778395-0.23983600042321093j), (0.14144518582167376+0.215527046545441j), (-0.26480071003903294+0.27081072820280316j)]`
- sample `3`: `|lambda1-lambda2|=4.121111e-03`, kappa `4.704010e+07`, Laplacians `['1.232290e-02', '1.110208e-02', '1.086264e-02']`, max|Delta| `1.232290e-02`
  - roots: `[(0.20427654662255537+0.23113926380601554j), (0.20719086357158942+0.23405307721095212j), (0.14302919031734385+0.16045094394755782j), (-0.5544966005114886-0.6256432849645255j)]`
- sample `4`: `|lambda1-lambda2|=5.222359e-03`, kappa `2.869615e+07`, Laplacians `['-4.829974e-03', '-7.290256e-03', '-1.613702e-03']`, max|Delta| `7.290256e-03`
  - roots: `[(-0.07179507841706927-0.15719096757308376j), (-0.07658537490997097-0.1592708927865524j), (0.26743586544420384+0.3012453358106072j), (-0.11905541211716358+0.015216524549028998j)]`
- sample `5`: `|lambda1-lambda2|=6.648577e-03`, kappa `2.772336e+06`, Laplacians `['-1.376376e-04', '-2.303596e-04', '-6.282719e-05']`, max|Delta| `2.303596e-04`
  - roots: `[(-0.3094842892773986+0.05720723696968038j), (-0.3029382515567403+0.05604406734443122j), (-0.07275580493211478+0.16373937806949057j), (0.6851783457662537-0.27699068238360214j)]`
- sample `6`: `|lambda1-lambda2|=4.908804e-03`, kappa `1.736672e+06`, Laplacians `['-9.431854e-06', '7.553599e-05', '-9.784718e-05']`, max|Delta| `9.784718e-05`
  - roots: `[(0.20639879376119544-0.14799426001074095j), (0.20159660242569594-0.14901176509996386j), (-0.047606040197471625+0.591714209446119j), (-0.3603893559894198-0.2947081843354141j)]`
- sample `7`: `|lambda1-lambda2|=1.605288e-03`, kappa `3.487640e+09`, Laplacians `['3.643674e-05', '6.128376e-05', '4.567702e-05']`, max|Delta| `6.128376e-05`
  - roots: `[(-0.0997282515051606-0.05412089973541306j), (-0.1005998545800356-0.05546895688646728j), (-0.10433492720461758+0.0146620047838587j), (0.30466303328981376+0.09492785183802163j)]`
- sample `8`: `|lambda1-lambda2|=1.191197e-03`, kappa `8.178556e+07`, Laplacians `['1.329239e-02', '9.624785e-03', '9.064028e-03']`, max|Delta| `1.329239e-02`
  - roots: `[(-0.018916421264307263+0.2003414137566716j), (-0.01982467015653192+0.20111214916461015j), (-0.3238447270528558-0.08656169535950271j), (0.362585818473695-0.31489186756177906j)]`
- sample `9`: `|lambda1-lambda2|=2.124392e-03`, kappa `1.187477e+09`, Laplacians `['-1.674039e-05', '-1.168132e-05', '-1.945211e-05']`, max|Delta| `1.945211e-05`
  - roots: `[(0.06282416073416967-0.001366133271279518j), (0.06164921400625483+0.0004037657845670378j), (-0.17897653215823855+0.1399483590092448j), (0.05450315741781406-0.13898599152253233j)]`
- sample `10`: `|lambda1-lambda2|=1.948544e-03`, kappa `6.438886e+06`, Laplacians `['-9.003714e-04', '-1.220836e-03', '-8.334744e-04']`, max|Delta| `1.220836e-03`
  - roots: `[(0.2978935813854546-0.3235131898802065j), (0.29918840534815333-0.32205708101037883j), (-0.0941311989469264-0.022214503617456447j), (-0.5029507877866815+0.6677847745080417j)]`
- sample `11`: `|lambda1-lambda2|=1.385926e-03`, kappa `1.086858e+09`, Laplacians `['-1.110223e-10', '-2.220446e-10', '0.000000e+00']`, max|Delta| `2.220446e-10`
  - roots: `[(-0.07879013397948184-0.10311426880941373j), (-0.08008513521858553-0.10360799258547579j), (0.029907133900206197+0.04711894356440392j), (0.1289681352978612+0.1596033178304856j)]`
- sample `12`: `|lambda1-lambda2|=5.679219e-03`, kappa `1.340800e+07`, Laplacians `['3.200254e-03', '2.240058e-03', '7.598100e-04']`, max|Delta| `3.200254e-03`
  - roots: `[(-0.17809362634354498-0.057803563096664325j), (-0.1749303219691268-0.06252023903887136j), (0.10163959791614373-0.07147174239409744j), (0.25138435039652807+0.1917955445296331j)]`
- sample `13`: `|lambda1-lambda2|=3.820932e-03`, kappa `4.275473e+07`, Laplacians `['2.731565e-04', '-2.085977e-03', '-1.268323e-03']`, max|Delta| `2.085977e-03`
  - roots: `[(-0.02358396170265562+0.05213849830309085j), (-0.025740082078642118+0.04898403030526789j), (-0.06840570390578424-0.3754525592363409j), (0.11772974768708197+0.27433003062798217j)]`
- sample `14`: `|lambda1-lambda2|=1.797973e-03`, kappa `2.547462e+07`, Laplacians `['-5.594269e-03', '-1.459800e-03', '-1.384574e-03']`, max|Delta| `5.594269e-03`
  - roots: `[(0.010171841480746513+0.2860755171069029j), (0.009103622734727562+0.2846292755204j), (-0.04297563230082672-0.3556504587874056j), (0.023700168085352642-0.2150543338398973j)]`
- sample `15`: `|lambda1-lambda2|=2.487867e-03`, kappa `3.544030e+08`, Laplacians `['5.386802e-07', '4.487521e-07', '8.156809e-07']`, max|Delta| `8.156809e-07`
  - roots: `[(-0.1021427422009786-0.08510466235512065j), (-0.10242164371480347-0.08263247818851313j), (0.047522866045955646-0.035906277952109315j), (0.15704151986982642+0.2036434184957431j)]`
- sample `16`: `|lambda1-lambda2|=2.814194e-03`, kappa `2.880152e+07`, Laplacians `['6.235934e-04', '-1.894644e-03', '-5.001222e-06']`, max|Delta| `1.894644e-03`
  - roots: `[(0.07671497008824028+0.22426116828025974j), (0.075274529478407+0.22184356191576196j), (-0.05536193869685126-0.03977081994363417j), (-0.09662756086979603-0.4063339102523875j)]`
- sample `17`: `|lambda1-lambda2|=3.194955e-03`, kappa `4.308423e+08`, Laplacians `['-1.081732e-02', '1.985468e-02', '2.166566e-02']`, max|Delta| `2.166566e-02`
  - roots: `[(0.1541183233896401+0.08112256670509663j), (0.15272953519492768+0.07824524043367051j), (0.14790547839305526+0.13995862609710627j), (-0.454753336977623-0.2993264332358734j)]`
- sample `18`: `|lambda1-lambda2|=3.367002e-03`, kappa `4.981334e+07`, Laplacians `['-3.629034e-04', '-2.053056e-03', '1.358929e-03']`, max|Delta| `2.053056e-03`
  - roots: `[(0.24105257576155179-0.19997410771722907j), (0.24376331652842903-0.2019712519062544j), (0.17751889437595642-0.10816112962379848j), (-0.6623347866659373+0.510106489247282j)]`
- sample `19`: `|lambda1-lambda2|=5.531999e-03`, kappa `1.043138e+07`, Laplacians `['-6.111627e-04', '-1.143818e-05', '-1.100157e-03']`, max|Delta| `1.100157e-03`
  - roots: `[(-0.10084620888939563-0.171632188540901j), (-0.10471755310373386-0.1755838606447819j), (-0.10277284592479329+0.10090312296138097j), (0.3083366079179228+0.24631292622430195j)]`
- sample `20`: `|lambda1-lambda2|=2.769544e-03`, kappa `2.174499e+07`, Laplacians `['-3.776914e-03', '-6.222686e-04', '-2.127883e-03']`, max|Delta| `3.776914e-03`
  - roots: `[(0.07245455803208092-0.29622294324412346j), (0.0737322927187932-0.2937657562889481j), (-0.12168405882315701-0.20732863499115775j), (-0.024502791927717107+0.7973173345242293j)]`
- ... `40` more accepted samples omitted

## Conclusion

Some near-collision ill-conditioned samples exceed the 0.1 threshold, so the log-harmonic behavior is not numerically stable in the bad-condition region.


# Row-cleared determinant SOS slice probe

- target: row-cleared reduced Pick determinant `D det(Pi_red)` on fixed low-dimensional real slices.
- this is a numerical SOS feasibility probe, not a proof certificate.
- cvxpy available: `False`

## Base point 0: `[0.1, 0.05, 0.07, -0.08, 0.03]`
- value at base: `1.305371422270e-10`
- 1D slice `x1` degree `40` fit: sample min `8.751e-12`, max `3.849e-06`
  - SOS skipped: cvxpy not available
- 1D slice `x2` degree `40` fit: sample min `3.389e-11`, max `5.343e-06`
  - SOS skipped: cvxpy not available
- 1D slice `y2` degree `40` fit: sample min `3.953e-13`, max `7.922e-06`
  - SOS skipped: cvxpy not available
- 1D slice `x3` degree `40` fit: sample min `2.897e-11`, max `3.896e-06`
  - SOS skipped: cvxpy not available
- 1D slice `y3` degree `40` fit: sample min `8.518e-13`, max `3.385e-06`
  - SOS skipped: cvxpy not available
- 2D slice `(x3,y3)` total-degree fit/SOS size probe: `{'deg': 12, 'terms': 91, 'fit_rel_res': np.float64(1.041456592543943e-09), 'rank': np.int32(91), 'global_sos_gram_dim': 28, 'box_sos_note': 'interval SOS would need multiplier Gram matrices; this is size probe only'}`

## Base point 1: `[0.3, 0.1, 0.05, -0.12, 0.08]`
- value at base: `1.667518715450e-06`
- 1D slice `x1` degree `40` fit: sample min `4.867e-10`, max `9.601e-06`
  - SOS skipped: cvxpy not available
- 1D slice `x2` degree `40` fit: sample min `7.283e-09`, max `2.450e-05`
  - SOS skipped: cvxpy not available
- 1D slice `y2` degree `40` fit: sample min `9.329e-07`, max `4.040e-04`
  - SOS skipped: cvxpy not available
- 1D slice `x3` degree `40` fit: sample min `1.896e-07`, max `2.541e-05`
  - SOS skipped: cvxpy not available
- 1D slice `y3` degree `40` fit: sample min `5.271e-07`, max `1.780e-04`
  - SOS skipped: cvxpy not available
- 2D slice `(x3,y3)` total-degree fit/SOS size probe: `{'deg': 12, 'terms': 91, 'fit_rel_res': np.float64(6.60284286040688e-09), 'rank': np.int32(91), 'global_sos_gram_dim': 28, 'box_sos_note': 'interval SOS would need multiplier Gram matrices; this is size probe only'}`

## Conclusion

- Direct high-degree 5D SOS is not computationally viable from samples.
- Moderate 1D interval SOS slices are feasible to test with Markov-Lukacs Gram matrices.
- 2D SOS is only plausible for low-degree fitted slices; the true determinant degree proxy (~92) would create very large Gram systems.


# Quadratic interpolation identity for q-values

- tested samples: `200`
- zero determinant count for `det[[1,lambda,lambda^2,q]]`: `0/200`

Interpretation: the cubic quantity `q_i = lambda_i r_i` does not satisfy the quadratic interpolation identity. The earlier `200/200` note was a conflation with the reduced value `r_i`, which is already quadratic in `lambda_i`.


# Quadratic structure of r-values

- tested samples: `250`
- quadratic interpolation verification for `r_i = alpha + beta*lambda_i + gamma*lambda_i^2`: `250/250`

Interpretation: the reduced values themselves are exactly quadratic in the node parameter, so the terminal structure should be sought one Schur layer deeper than the raw `r_i` interpolation.


# Finite interior reduction chamber probe

Using Proposition `Finite interior reduction`, the relevant interior object is the cleared principal determinant `P_{I,\alpha}` on each of the six modulus-order chambers.  The chamber restriction changes the domain, not the underlying polynomial complexity.

## Chamber-admissible base point

- base point `(x1,x2,y2,x3,y3)`: `(0.25, 0.15977484069825626, 0.041272704470448396, 0.06467430550800986, -0.038573319953125865)`
- node moduli after centering: `[0.4744568252355816, 0.25, 0.16501950143682453, 0.07530382995007366]`
- ordering: minimal chamber after common rotation and permutation

## Cleared determinant probe

- row-cleared `D det(Pi_red)` at the chamber base: `3.368347585280662e-07`
- 2D slice `(x3,y3)` total-degree fit: `{'deg': 12, 'terms': 91, 'fit_rel_res': np.float64(1.588858919989835e-12), 'rank': np.int32(91), 'global_sos_gram_dim': 28, 'box_sos_note': 'interval SOS would need multiplier Gram matrices; this is size probe only'}`
- 1D slice sample ranges at this base stay small and smooth; no blow-up was seen in the chamber-admissible neighbourhood.

Interpretation: the chamber route is viable.  The local `P_{I,id}` complexity stays in the same range as the previous row-cleared probe, so Bernstein on compact chambers remains a plausible certification path.  The existing BM proxies (`93` on random lines for row-cleared determinant, `87` on coordinate lines) remain the best current degree estimate for the full cleared polynomial.

## Kronecker degree proxy

- weights: `[1, 7, 49, 343, 2401]`
- offsets tested: `5` independent random choices
- BM lengths: `160, 160, 160, 160, 160`
- unique BM lengths: `1`

Interpretation: the Kronecker probe is stable and lands at degree proxy `160` for the row-cleared full chamber polynomial.  That is far beyond a comfortable direct 5D Bernstein expansion, so the remaining certification should use chamber-restricted DSOS/interval SOS on low-dimensional slices rather than brute-force global Bernstein in five variables.

## Coordinate-line BM probe for the chamber polynomial

Using the chamber-admissible blackbox and three independent basepoints, the univariate coordinate-line recurrence lengths were stable:

- basepoint `101`: `x1=87`, `x2=87`, `y2=87`, `x3=87`, `y3=87`
- basepoint `202`: `x1=87`, `x2=87`, `y2=87`, `x3=87`, `y3=87`
- basepoint `303`: `x1=87`, `x2=87`, `y2=87`, `x3=87`, `y3=87`

Interpretation: no coordinate is remotely low-degree in the sense needed for a trivial 6D or 5D reduction.  The chamber polynomial is still in the same algebraic complexity class as the previously observed row-cleared determinant, so a direct Chebyshev/Bernstein elimination of any single variable is not justified by the probe.


# q-structure exact mod-p hunt

- prime: `1000000007`
- valid samples: `200`
- rejected samples: `0`
- q quadratic interpolation verified: `0/200`

## Ratio uniqueness counts
- `lhs_over_alpha`: `200` unique ratios
- `lhs_over_beta`: `200` unique ratios
- `lhs_over_c3`: `200` unique ratios
- `lhs_over_gamma`: `200` unique ratios
- `lhs_over_vandlam`: `200` unique ratios
- `lhs_over_vandr`: `200` unique ratios

## First ratios
- `lhs_over_alpha`: lhs `(411247628, 0)` cand `(971597165, 266882361)`
- `lhs_over_beta`: lhs `(411247628, 0)` cand `(138556266, 386691873)`
- `lhs_over_c3`: lhs `(411247628, 0)` cand `(142823811, 343581336)`
- `lhs_over_gamma`: lhs `(411247628, 0)` cand `(899387639, 571218973)`
- `lhs_over_vandlam`: lhs `(411247628, 0)` cand `(134425447, 415598718)`
- `lhs_over_vandr`: lhs `(411247628, 0)` cand `(470568303, 77772888)`


# Determinant-ratio Schur identity and Laplacian test

## Mod-p identity test

- valid samples: `1000`
- denominator failures: `0`
- user exponent formula matches: `0/1000`
- standard exponent formula `prod(1-|gamma_k|^2)^(5-k)` matches: `0/1000`
- first mismatch example lhs/rhs_user: `(949221379, 0)` vs `(974912807, 0)`

## Numerical Laplacian of log(det Pi_red / det K)

- central difference h `1e-3`; points with `kappa(Pi_red)>1e4` skipped.
- accepted Laplacian evaluations: `810`
- skipped evaluations: `690`
- |Laplacian| < 0.1 count: `810/810`
- min Laplacian: `-1.623169e-02`
- max Laplacian: `1.524225e-06`
- max abs Laplacian: `1.623169e-02`

## Conclusion

The user-stated exponent formula is not the determinant-ratio identity. The standard exponent formula is the one tested. Numerical Laplacian results should be interpreted with this corrected identity.


# P12 finite-field BM probe

- polynomial: `u1*u2*|1-lambda1*conj(lambda2)|^2*det(Pi_red[{1,2}])`.
- arithmetic: exact mod `1000000007` in the quadratic pair algebra.

## Coordinate lines, six variables
- seed `101`: `x1=41, y1=41, x2=41, y2=41, x3=41, y3=41`, imag leakage `0`
- seed `202`: `x1=41, y1=41, x2=41, y2=41, x3=41, y3=41`, imag leakage `0`
- seed `303`: `x1=41, y1=41, x2=41, y2=41, x3=41, y3=41`, imag leakage `0`

## Coordinate lines, rotation slice y1=0
- seed `101`: `x1=41, x2=41, y2=41, x3=41, y3=41`, imag leakage `0`
- seed `202`: `x1=41, x2=41, y2=41, x3=41, y3=41`, imag leakage `0`
- seed `303`: `x1=41, x2=41, y2=41, x3=41, y3=41`, imag leakage `0`

## Kronecker probes

- six-variable weights `[1,7,49,343,2401,16807]`: `[(11, 130, 0), (22, 130, 0), (33, 130, 0)]`
- rotation-slice weights `[1,7,49,343,2401]`: `[(11, 130, 0), (22, 130, 0), (33, 130, 0)]`

## Gram size estimate from coordinate degree proxy

- six-variable max axis degree proxy: `40`; pure SOS half degree `20`; basis size `230230`
- rotation-slice max axis degree proxy: `40`; pure SOS half degree `20`; basis size `53130`
# P12 2D slice SOS probe

- environment: temporary venv `/Users/ray/Downloads/mathz_sos_venv`
- cvxpy installed: `1.9.2`
- slice: rotation-reduced variables with only `(x3,y3)` varied.
- scaled box: `[-1,1]^2` around the chamber base, radius `0.08`.
- fitted polynomial degree: `40` total degree.
- pure SOS basis size for this 2D slice: `231`
- coefficient constraints: `861`

## Solver result

The degree-40 pure SOS SDP was started with a `231 x 231` Gram matrix.  It did not return a solver status within approximately 90 seconds and was interrupted.  This is not a mathematical infeasibility result; it is a size/conditioning warning.

## Interpretation

The exact finite-field BM probe shows that even the `{1,2}` cleared minor has coordinate degree proxy `40`.  Therefore the full 5D/6D pure Gram SDP is not a realistic first target.  The next viable SOS target is a barrier/interval form on low-dimensional slices, or a DSOS/SDSOS relaxation using the disk and chamber multipliers.


# Paired family reduced Pick analysis

Family: `lambda = {rho, -rho, rho*exp(i theta), -rho*exp(i theta)}`.

## Algebraic structure

- `a1 = 0`, hence `c2 = 0`.
- Therefore `r(rho)=r(-rho)` and `r(rho*exp(i theta))=r(-rho*exp(i theta))`.
- With order `[a,-a,b,-b]`, write `A=r(a)`, `B=r(b)`, `q=rho^2`, `u=exp(i theta)`.
- The Pick matrix has pair form with diagonal pair entries:
  `dA=(1-|A|^2)/(1-q)`, `pA=(1-|A|^2)/(1+q)`, and similarly for `B`.
- Cross entries are `x=(1-A*conj(B))/(1-q*conj(u))` and `y=(1-A*conj(B))/(1+q*conj(u))`.

In the symmetric/antisymmetric basis for each pair, the matrix is block diagonal with

```text
M_plus  = [[dA+pA, x+y], [conj(x+y), dB+pB]]
M_minus = [[dA-pA, x-y], [conj(x-y), dB-pB]]
```

Each block has eigenvalues

```text
0.5*(alpha+delta) +/- sqrt(0.25*(alpha-delta)^2 + |beta|^2)
```

## Grid scan

- grid: `rho in [0.1,0.99]` with 360 samples, `theta in [0.01,pi-0.01]` with 540 samples
- minimum eigenvalue: `4.001067629325e-10`
- minimum location: `rho=0.100000000000`, `theta=3.131592653590`
- eigenvalues at minimum: `[4.0010676293246634e-10, 4.001066748542401e-08, 0.04000399999993346, 4.000399999993332]`
- max c-metric ratio over all pairs/grid: `1.416903687976e-01`
- max ratio location: `rho=0.990000000000`, `theta=1.585274956914`
- pairwise ratios at max-ratio point: `[0.0, 0.1396535956181593, 0.14169036879758856, 0.14169036879758856, 0.1396535956181593, 0.0]`
- block diagonalization max eigenvalue error: `3.268e-13`

## Sanity samples

- `rho=0.300`, `theta=1.570796`: max ratio `2.533073e-05`, eig `[0.0029161913187599553, 0.032402125763999624, 0.36002362114968184, 4.000262457218687]`
  values `r`: `[(-5.904899999999998e-06+1.9283778358093877e-21j), (-5.904899999999998e-06+1.9283778358093877e-21j), (5.904899999999998e-06-1.6873306063332142e-21j), (5.904899999999998e-06-1.6873306063332142e-21j)]`
- `rho=0.750`, `theta=1.570796`: max ratio `4.660407e-02`, eig `[0.783185854554176, 1.3923304080963137, 2.4978048992925332, 4.440542043186724]`
  values `r`: `[(-0.056313514709472656+1.839044414338482e-17j), (-0.056313514709472656+1.839044414338482e-17j), (0.056313514709472656-1.6091638625461713e-17j), (0.056313514709472656-1.6091638625461713e-17j)]`
- `rho=0.900`, `theta=1.047198`: max ratio `9.170379e-02`, eig `[3.3338838234641655, 4.115905954894034, 5.671351646952946, 7.001668699941906]`
  values `r`: `[(0.19613162255625+0.07549109671963261j), (0.19613162255625+0.07549109671963261j), (-0.16344301879687506-0.13210941925935715j), (-0.16344301879687506-0.13210941925935715j)]`

## Conclusion

On the tested grid the paired family reduced Pick matrix is PSD, with the observed minimum approaching the boundary. The c-metric pairwise contraction test also stays below 1 on the grid.


# Paired family block determinant formulas

Let `q=rho^2`, `u=exp(i theta)`, `t=u^2`, `A=r(rho)`, and `B=r(rho*u)`.

## Reduced values

- `A = q**5*t*(t - 5)*(t - 1)**3/48`
- `B = q**5*(t - 1)**3*(5*t - 1)/48`

## Block determinants

Set

```text
H = (1-|A|^2)(1-|B|^2)/(1-q^2)^2
    - |1-A*conj(B)|^2 / |1-q^2*exp(-2 i theta)|^2.
```

Then

```text
det(M_plus)  = 4 H
det(M_minus) = 4 q^2 H
```

The traces are positive whenever `|A|<1` and `|B|<1`; numerically this holds throughout the paired interior and follows from the paired boundary certificate.

## Cleared numerator

For exact algebra, clear the Laurent denominator in `H` by multiplying by

```text
(1-q^2)^2 (1-q^2*t)(1-q^2/t) t^10.
```

- denominator before the `t^10` Laurent clearing: `5308416*t**8*(q - 1)**2*(q + 1)**2*(q**2 - t)*(q**2*t - 1)`
- cleared numerator degree in `q`: `22`
- cleared numerator degree in `t`: `28`
- factored cleared numerator in `(q,t)`: `-q**2*t**10*(t - 1)**2*(5*q**10*t**8 - 56*q**10*t**7 + 236*q**10*t**6 - 520*q**10*t**5 + 670*q**10*t**4 - 520*q**10*t**3 + 236*q**10*t**2 - 56*q**10*t + 5*q**10 - 48*q**6*t**6 + 576*q**6*t**5 - 1056*q**6*t**4 + 576*q**6*t**3 - 48*q**6*t**2 + 48*q**4*t**6 - 576*q**4*t**5 + 1056*q**4*t**4 - 576*q**4*t**3 + 48*q**4*t**2 - 2304*t**4)*(5*q**10*t**8 - 56*q**10*t**7 + 236*q**10*t**6 - 520*q**10*t**5 + 670*q**10*t**4 - 520*q**10*t**3 + 236*q**10*t**2 - 56*q**10*t + 5*q**10 + 48*q**6*t**6 - 576*q**6*t**5 + 1056*q**6*t**4 - 576*q**6*t**3 + 48*q**6*t**2 - 48*q**4*t**6 + 576*q**4*t**5 - 1056*q**4*t**4 + 576*q**4*t**3 - 48*q**4*t**2 - 2304*t**4)`

## Cosine-folded numerator

After folding the palindromic Laurent polynomial with `c=cos(theta)`, the numerator becomes:

```text
-q**2*(3872514899968*c**20*q**20 - 4991288868864*c**20*q**12 + 579820584960*c**20*q**10 - 4991288868864*c**20*q**8 + 5566277615616*c**20 - 20451335077888*c**18*q**20 + 26558198710272*c**18*q**12 - 3227667922944*c**18*q**10 + 26558198710272*c**18*q**8 - 30614526885888*c**18 + 46286925594624*c**16*q**20 - 60552294432768*c**16*q**12 + 7675374993408*c**16*q**10 - 60552294432768*c**16*q**8 + 72013716652032*c**16 - 58603406950400*c**14*q**20 + 77189672337408*c**14*q**12 - 10157731872768*c**14*q**10 + 77189672337408*c**14*q**8 - 94452773289984*c**14 + 45429947916288*c**12*q**20 - 60176873816064*c**12*q**12 + 8163768139776*c**12*q**10 - 60176873816064*c**12*q**8 + 75470896889856*c**12 - 22169109925888*c**10*q**20 + 29464761729024*c**10*q**12 - 4076674744320*c**10*q**10 + 29464761729024*c**10*q**8 - 37670218629120*c**10 + 6735023806464*c**8*q**20 - 8945001234432*c**8*q**12 + 1240843419648*c**8*q**10 - 8945001234432*c**8*q**8 + 11570138578944*c**8 - 1211572096000*c**6*q**20 + 1596301737984*c**6*q**12 - 215811883008*c**6*q**10 + 1596301737984*c**6*q**8 - 2066969788416*c**6 + 115536178480*c**4*q**20 - 149059694592*c**4*q**12 + 18662326272*c**4*q**10 - 149059694592*c**4*q**8 + 190338564096*c**4 - 4553885896*c**2*q**20 + 5616986112*c**2*q**12 - 585547776*c**2*q**10 + 5616986112*c**2*q**8 - 6922174464*c**2 + 32773167*q**20 - 36864000*q**12 + 2359296*q**10 - 36864000*q**8 + 42467328)
```



# Paired family block determinant formulas

Let `q=rho^2`, `u=exp(i theta)`, `t=u^2`, `A=r(rho)`, and `B=r(rho*u)`.

## Reduced values

- `A = q**5*t*(t - 5)*(t - 1)**3/48`
- `B = q**5*(t - 1)**3*(5*t - 1)/48`

## Block determinants

Set

```text
H = (1-|A|^2)(1-|B|^2)/(1-q^2)^2
    - |1-A*conj(B)|^2 / |1-q^2*exp(-2 i theta)|^2.
```

Then

```text
det(M_plus)  = 4 H
det(M_minus) = 4 q^2 H
```

The traces are positive whenever `|A|<1` and `|B|<1`; numerically this holds throughout the paired interior and follows from the paired boundary certificate.

## Cleared numerator

For exact algebra, clear the Laurent denominator in `H` by multiplying by

```text
(1-q^2)^2 (1-q^2*t)(1-q^2/t) t^10.
```

- denominator before the `t^10` Laurent clearing: `5308416*t**8*(q - 1)**2*(q + 1)**2*(q**2 - t)*(q**2*t - 1)`
- cleared numerator degree in `q`: `22`
- cleared numerator degree in `t`: `28`
- factored cleared numerator in `(q,t)`: `-q**2*t**10*(t - 1)**2*(5*q**10*t**8 - 56*q**10*t**7 + 236*q**10*t**6 - 520*q**10*t**5 + 670*q**10*t**4 - 520*q**10*t**3 + 236*q**10*t**2 - 56*q**10*t + 5*q**10 - 48*q**6*t**6 + 576*q**6*t**5 - 1056*q**6*t**4 + 576*q**6*t**3 - 48*q**6*t**2 + 48*q**4*t**6 - 576*q**4*t**5 + 1056*q**4*t**4 - 576*q**4*t**3 + 48*q**4*t**2 - 2304*t**4)*(5*q**10*t**8 - 56*q**10*t**7 + 236*q**10*t**6 - 520*q**10*t**5 + 670*q**10*t**4 - 520*q**10*t**3 + 236*q**10*t**2 - 56*q**10*t + 5*q**10 + 48*q**6*t**6 - 576*q**6*t**5 + 1056*q**6*t**4 - 576*q**6*t**3 + 48*q**6*t**2 - 48*q**4*t**6 + 576*q**4*t**5 - 1056*q**4*t**4 + 576*q**4*t**3 - 48*q**4*t**2 - 2304*t**4)`

## Positive real form

Let `S=sin(theta)^2`.  From the simplified `A,B` formulas,

```text
|A|^2 = |B|^2 = q^10*S^3*(4+5*S)/9
Re(A*conj(B)) = -q^10*S^3*(2*S^2+3*S+4)/9
```

Thus

```text
H = N / ((1-q^2)^2*(1-2*q^2*cos(2theta)+q^4))
```

where

```text
N = 4*S*q^2*F_minus*F_plus
F_minus = q^10*S^3*(5*S+4) - 3*S*(S+2)*q^6 + 3*S*(S+2)*q^4 - 9
F_plus  = q^10*S^3*(5*S+4) + 3*S*(S+2)*q^6 - 3*S*(S+2)*q^4 - 9
```

For `0<q<1` and `0<S<=1`, both factors are strictly negative:

```text
F_plus < 9*q^10 - 9 < 0.
F_minus <= 9*q^10 + 9*q^4*(1-q^2) - 9
        = 9*(q^10 + q^4 - q^6 - 1) < 0.
```

The last inequality follows because `q^10 + q^4 - q^6` is increasing on `(0,1)` and equals `1` at `q=1`.
Therefore `N>0`, hence `H>0`, and consequently both determinants are strictly positive in the interior.

Boundary behavior: `S=0` corresponds to `theta=0` or `theta=pi`, giving the expected confluent zero of `N`.  The disk boundary `q=1` is not part of the interior; the determinant expression has vanishing denominators there, so it should be treated by the separate boundary certificate rather than as an interior zero locus.

