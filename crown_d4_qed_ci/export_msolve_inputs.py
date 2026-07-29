#!/usr/bin/env python3
from fractions import Fraction as F
from pathlib import Path
from math import gcd
import ast
DATA=Path('crown_d4_qed_ci/work/residual');OUT=Path('crown_d4_qed_ci/work/cas');OUT.mkdir(parents=True,exist_ok=True)
NAMES=[f'F7_scaled_{i}_residual' for i in range(2)]+[f'G10_scaled_{i}_residual' for i in range(5)]
VARS=('A','B','C','D')
def lcm(a,b):return abs(a*b)//gcd(a,b)
def load(name):
 p=[]
 for line in open(DATA/f'{name}.txt'):
  m,c=line.strip().rsplit(' ',1);p.append((ast.literal_eval(m),F(c)))
 return p
def primitive_integer(p):
 den=1
 for m,c in p:den=lcm(den,c.denominator)
 vals=[(m,c.numerator*(den//c.denominator)) for m,c in p];g=0
 for m,c in vals:g=gcd(g,abs(c))
 if g:vals=[(m,c//g) for m,c in vals]
 first=next((c for m,c in vals if c),1)
 if first<0:vals=[(m,-c) for m,c in vals]
 return vals
def term(m,c,mod=None):
 if mod is not None:
  c%=mod
  if c>mod//2:c-=mod
 if c==0:return ''
 mono='*'.join(v+(f'^{e}' if e!=1 else '') for v,e in zip(VARS,m) if e)
 if not mono:return str(c)
 if c==1:return mono
 if c==-1:return '-'+mono
 return f'{c}*{mono}'
def expr(p,mod=None):
 ss=[]
 for m,c in p:
  z=term(m,c,mod)
  if not z:continue
  if ss and not z.startswith('-'):z='+'+z
  ss.append(z)
 return ''.join(ss) or '0'
GENS=[primitive_integer(load(n)) for n in NAMES]
def write(path,variables,char,polys):
 with open(path,'w') as f:
  f.write(','.join(variables)+'\n'+str(char)+'\n')
  for i,p in enumerate(polys):f.write(p+(',\n' if i+1<len(polys) else '\n'))
for p in (13,17,19,23,29,31):write(OUT/f'd4_degree7_10_F{p}.ms',VARS,p,[expr(g,p) for g in GENS])
write(OUT/'d4_degree7_10_Q.ms',VARS,0,[expr(g) for g in GENS])
h=['A-B^2+B','C-B^2+1','D-B^2','B^3-B^2-2*B+1']
delta='A*B*C*D*(A-1)*(B-1)*(C-1)*(D-1)*(A-B)*(A-C)*(A-D)*(B-C)*(B-D)*(C-D)'
for char in (0,13,29,31):
 suffix='Q' if char==0 else f'F{char}';base=[expr(g,None if char==0 else char) for g in GENS]
 write(OUT/f'd4_saturated_{suffix}.ms',('S',)+VARS,char,base+[f'1-S*({delta})'])
 for i,hi in enumerate(h):
  write(OUT/f'd4_saturated_outside_Jstd_{i}_{suffix}.ms',('T','S')+VARS,char,base+[f'1-S*({delta})',f'1-T*({hi})'])
print('MSOLVE INPUT EXPORT: PASS')
print('generators:',[(n,len(g)) for n,g in zip(NAMES,GENS)])
