#!/usr/bin/env python3
from pathlib import Path
CAS=Path('crown_d4_qed_ci/work/cas')
for i in range(4):
 src=CAS/f'd4_saturated_outside_Jstd_{i}_Q.ms'
 lines=src.read_text().splitlines()
 variables=lines[0]
 polys='\n'.join(lines[2:])
 out=CAS/f'd4_saturated_outside_Jstd_{i}_Q.sing'
 out.write_text(f'''option(redSB);\nring r=0,({variables}),dp;\nideal I={polys};\nideal G=std(I);\nif (size(G)==1) {{\n  if (G[1]==1) {{ print("SINGULAR UNIT IDEAL PASS {i}"); }}\n  else {{ print("FAIL: singleton is not 1"); exit(1); }}\n}}\nelse {{ print("FAIL: basis size",size(G)); exit(1); }}\n''')
print('SINGULAR INPUT EXPORT: PASS')
