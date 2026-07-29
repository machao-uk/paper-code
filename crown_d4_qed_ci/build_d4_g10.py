#!/usr/bin/env python3
from sympy.polys.rings import ring
from sympy.polys.domains import QQ
from math import comb
import time, os
R,A,B,C,D=ring('A,B,C,D',QQ)
Z=R.zero; O=R.one; ss=[Z,O,A,B,C,D]

def req(c,m):
    if not c: raise RuntimeError(m)
def add(p,q):
    n=max(len(p),len(q)); return [(p[i] if i<len(p) else Z)+(q[i] if i<len(q) else Z) for i in range(n)]
def scale(p,c): return [c*x for x in p]
def mul(p,q):
    out=[Z]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        if not a: continue
        for j,b in enumerate(q):
            if b: out[i+j]+=a*b
    return out
def dx(p,n):
    o=[Z]*n
    for k,a in enumerate(p):
        if k:o[k-1]+=k*a
    return o
def dy(p,n):
    o=[Z]*n
    for k,a in enumerate(p):
        if n-k:o[k]+=(n-k)*a
    return o
def br(P,n,Q,m): return add(mul(dx(P,n),dy(Q,m)),scale(mul(dy(P,n),dx(Q,m)),-1))
def lp(s,n,inf=False):
    if inf:
        o=[Z]*(n+1);o[n]=O;return o
    o=[];pw=O
    for k in range(n+1):o.append(pw*comb(n,k));pw*=s
    return o
def pmul(a,b):
    out=[Z]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out
def pdeg(p): return max((sum(m) for m,c in p.terms()),default=-1)
def stats(x):return (len(x.terms()),pdeg(x))
def exact_div(x,y,msg):
    q,r=divmod(x,y);req(not r,msg);return q
def write_poly(p,path):
    with open(path,'w') as f:
        for m,c in p.terms():f.write(f'{m} {c}\n')

t=time.time();print('start',flush=True)
Delta=O
for i in range(6):
    for j in range(i):Delta*=ss[i]-ss[j]
print('Delta',stats(Delta),time.time()-t,flush=True)
Q=[O]
for z in ss:Q=pmul(Q,[-z,O])
di=[];cbar=[]
for i,z in enumerate(ss):
    d=O
    for j,w in enumerate(ss):
        if i!=j:d*=z-w
    di.append(d);cbar.append(exact_div(Delta,d,f'Delta/di {i}'))
Avec=[scale(lp(z,5),cbar[i]*QQ(1,5)) for i,z in enumerate(ss)]+[scale(lp(Z,5,True),-Delta*QQ(1,5))]
S0=[Z]*6
for x in Avec:S0=add(S0,x)
req(not any(S0),'quintic relation fail')
H=[Z]*9
for i in range(7):
    for j in range(i):H=add(H,scale(br(Avec[i],5,Avec[j],5),QQ(1,2)))
h=[H[k]*QQ(1,comb(8,k)) for k in range(9)]
F=[sum((Q[k]*h[k+r] for k in range(7)),Z) for r in range(2)]
print('F stats',[stats(x) for x in F],time.time()-t,flush=True)
beta=[]
for i,z in enumerate(ss):
    others=ss[:i]+ss[i+1:]
    e=[O]+[Z]*5
    for x in others:
        for j in range(5,0,-1):e[j]+=x*e[j-1]
    num=sum(((-1)**(5-k)*e[5-k]*(-h[k]) for k in range(6)),Z)
    beta.append(exact_div(num,di[i],f'beta division {i}'))
    print('beta',i,stats(beta[-1]),time.time()-t,flush=True)
binf=-h[8]-sum((beta[i]*ss[i]**8 for i in range(6)),Z)
print('binf',stats(binf),time.time()-t,flush=True)
Bvec=[scale(lp(z,8),beta[i]) for i,z in enumerate(ss)]+[scale(lp(Z,8,True),binf)]
S=[Z]*6;T=[Z]*9;U=[Z]*12
for idx,(Ai,Bi) in enumerate(zip(Avec,Bvec)):
    oldS,oldT,oldU=S,T,U
    term1=scale(add(br(Ai,5,oldT,8),br(Bi,8,oldS,5)),QQ(1,2))
    term2=scale(br(Ai,5,br(Ai,5,oldS,5),8),QQ(1,12))
    term3=scale(br(oldS,5,br(oldS,5,Ai,5),8),QQ(1,12))
    U=add(oldU,add(term1,add(term2,term3)))
    T=add(oldT,add(Bi,scale(br(Ai,5,oldS,5),QQ(1,2))))
    S=add(oldS,Ai)
    print('letter',idx,'Umax',max(stats(x)[0] for x in U),'Tmax',max(stats(x)[0] for x in T),'elapsed',time.time()-t,flush=True)
u=[U[k]*QQ(1,comb(11,k)) for k in range(12)]
G=[sum((Q[k]*u[k+r] for k in range(7)),Z) for r in range(5)]
print('G stats',[stats(x) for x in G],time.time()-t,flush=True)
out='crown_d4_qed_ci/work/raw';os.makedirs(out,exist_ok=True)
for i,x in enumerate(F):write_poly(x,f'{out}/F7_scaled_{i}.txt')
for i,x in enumerate(G):write_poly(x,f'{out}/G10_scaled_{i}.txt')
write_poly(Delta,f'{out}/Delta.txt')
print('done',time.time()-t,flush=True)
