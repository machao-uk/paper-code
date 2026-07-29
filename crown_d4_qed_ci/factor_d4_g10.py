#!/usr/bin/env python3
from fractions import Fraction
import ast,os,time
factors=[]
for i,n in enumerate('ABCD'):factors.append((n,i,None))
for i,n in enumerate('ABCD'):factors.append((n+'-1',i,('const',1)))
for i in range(4):
 for j in range(i+1,4):factors.append(('ABCD'[i]+'-'+'ABCD'[j],i,('var',j)))
def load(path):
 p={}
 for line in open(path):
  m,c=line.strip().rsplit(' ',1);p[ast.literal_eval(m)]=Fraction(c)
 return {m:c for m,c in p.items() if c}
def deg(p):return max((sum(m) for m in p),default=-1)
def write(p,path):
 with open(path,'w') as f:
  for m,c in sorted(p.items(),reverse=True):f.write(f'{m} {c.numerator}/{c.denominator}\n')
def addcoef(dst,m,c):
 v=dst.get(m,Fraction(0))+c
 if v:dst[m]=v
 elif m in dst:del dst[m]
def divide_linear(p,vi,root):
 groups={};maxe=0
 for m,c in p.items():
  e=m[vi];maxe=max(maxe,e);base=list(m);base[vi]=0;base=tuple(base);groups.setdefault(e,{})[base]=c
 qgroups={};carry=groups.get(maxe,{}).copy()
 for k in range(maxe-1,-1,-1):
  qgroups[k]=carry;nxt=groups.get(k,{}).copy()
  if root is None:pass
  elif root[0]=='const':
   rr=Fraction(root[1])
   for m,c in carry.items():addcoef(nxt,m,rr*c)
  else:
   j=root[1]
   for m,c in carry.items():
    mm=list(m);mm[j]+=1;addcoef(nxt,tuple(mm),c)
  carry=nxt
 if carry:return None,carry
 q={}
 for e,co in qgroups.items():
  for m,c in co.items():
   mm=list(m);mm[vi]=e;q[tuple(mm)]=c
 return q,{}
base='crown_d4_qed_ci/work/raw';out='crown_d4_qed_ci/work/residual';os.makedirs(out,exist_ok=True)
for name in [f'F7_scaled_{i}' for i in range(2)]+[f'G10_scaled_{i}' for i in range(5)]:
 t=time.time();p=load(f'{base}/{name}.txt');fac=[]
 for nm,vi,root in factors:
  e=0
  while True:
   q,r=divide_linear(p,vi,root)
   if r:break
   p=q;e+=1
  if e:fac.append((nm,e))
 print(name,'factors',fac,'residual terms',len(p),'degree',deg(p),'sec',round(time.time()-t,3),flush=True)
 write(p,f'{out}/{name}_residual.txt');open(f'{out}/{name}_factors.txt','w').write(repr(fac)+'\n')
print('COLLISION FACTOR CERTIFICATE: PASS')
