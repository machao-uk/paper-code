# Gamma3 hard-corner certificate output

## Lowest corner face

- order: `11`
- lead/C: `v**9*(u - 4*v)**2`

## Inner tube

- c00: `24480747847196240787800064`
- tail bound positive: `True`
- relative margin: `0.1134235068699399217319812498264692476821`

## Annulus

- region: `16v < |z| < 1/4`, hence `v < 1/64`
- main lower bound: `C(z^2+64v+32vz-320v^2) >= 55 C v`
- remainder/C: `4.0242699693795626990770705309229990531464891981352`
- remainder < 5C: `True`
- final margin `55C-rem > 50C`: `True`

## Fixed-z Bernstein

- z `[-4,-2]`: degree `(62, 51)`, neg `0`, zeros `0`, loc `(62, 51)`
- z `[-2,-1]`: degree `(62, 51)`, neg `0`, zeros `0`, loc `(62, 0)`
- z `[-1,-1/2]`: degree `(62, 51)`, neg `0`, zeros `0`, loc `(62, 0)`
- z `[-1/2,-1/4]`: degree `(62, 51)`, neg `0`, zeros `0`, loc `(62, 0)`
- z `[1/4,1/2]`: degree `(62, 51)`, neg `0`, zeros `0`, loc `(0, 0)`
- z `[1/2,1]`: degree `(62, 51)`, neg `0`, zeros `0`, loc `(0, 0)`
- z `[1,2]`: degree `(62, 51)`, neg `0`, zeros `0`, loc `(0, 0)`
- z `[2,4]`: degree `(62, 51)`, neg `0`, zeros `0`, loc `(0, 0)`
- z `[4,8]`: degree `(62, 51)`, neg `0`, zeros `0`, loc `(0, 0)`
- z `[8,16]`: degree `(62, 51)`, neg `0`, zeros `0`, loc `(0, 0)`
- z `[16,32]`: degree `(62, 51)`, neg `0`, zeros `0`, loc `(0, 0)`

## Reciprocal tail

- chart: `H(r,u)=Q(u,ru)`
- box: `0 <= r <= 1/36`, `0 <= u <= 1/16`
- degree: `(28, 62)`
- neg: `0`
- zeros: `367`
- min loc: `(0, 0)`

## Verdict

- hard corner closed: `True`
