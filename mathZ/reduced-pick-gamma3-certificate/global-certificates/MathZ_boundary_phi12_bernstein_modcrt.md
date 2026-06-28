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