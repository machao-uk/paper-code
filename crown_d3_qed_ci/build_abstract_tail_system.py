#!/usr/bin/env python3
from sympy.polys.rings import ring
from sympy.polys.domains import QQ, GF
import sys, time, os

start=int(sys.argv[1]); N=int(sys.argv[2]); char=int(sys.argv[3]); chart=int(sys.argv[4]); out=sys.argv[5]
base=['A','B','C','D']
tails=[f'c{r}_{d}' for d in range(start,N+1) for r in range(7)]
names=base+tails+['S']
R,*gens=ring(','.join(names), GF(char) if char else QQ)
g=dict(zip(names,gens)); Z=R.zero; O=R.one
A,B,C,D=[g[x] for x in base]; slopes=[Z,O,A,B,C,D]

def hadd(P,Q):
    n=max(len(P),len(Q)); return [(P[i] if i<len(P) else Z)+(Q[i] if i<len(Q) else Z) for i in range(n)]
def hscale(P,c): return [c*x for x in P]
def hmul(P,Q):
    z=[Z]*(len(P)+len(Q)-1)
    for i,a in enumerate(P):
        if a:
            for j,b in enumerate(Q):
                if b: z[i+j]+=a*b
    return z
def smul(P,Q):
    z=[[] for _ in range(N+1)]
    for n in range(N+1):
        a=[]
        for i in range(n+1):
            if P[i] and Q[n-i]: a=hadd(a,hmul(P[i],Q[n-i]))
        z[n]=a
    return z

def endpoint():
    X=[[] for _ in range(N+1)]; Y=[[] for _ in range(N+1)]
    X[1]=[O,Z]; Y[1]=[Z,O]
    forms=[(O,z) for z in slopes]+[(Z,O)]
    for r,(a,b) in enumerate(forms):
        L=[[] for _ in range(N+1)]
        for n in range(1,N+1):
            if X[n] or Y[n]: L[n]=hadd(hscale(X[n],a),hscale(Y[n],b))
        powers=[[[] for _ in range(N+1)] for _ in range(N+1)]
        powers[0][0]=[O]
        for d in range(1,N+1): powers[d]=smul(powers[d-1],L)
        F=[[] for _ in range(N+1)]
        for d in range(start,N+1):
            c=g[f'c{r}_{d}']
            for n in range(d,N+1):
                if powers[d][n]: F[n]=hadd(F[n],hscale(powers[d][n],c))
        for n in range(start,N+1):
            if F[n]:
                X[n]=hadd(X[n],hscale(F[n],b)); Y[n]=hadd(Y[n],hscale(F[n],-a))
        print('factor',r,'maxterms',max([len(q.terms()) for n in range(start,N+1) for q in (X[n]+Y[n]) if q] or [0]),flush=True)
    return X,Y

def expr(f):
    parts=[]
    for m,c in f.terms():
        if char:
            ci=int(c)%char
            if ci>char//2: ci-=char
            if not ci: continue
            cs=str(ci)
        else:
            cs=str(c)
        mono=[]
        for nm,e in zip(names,m):
            if e: mono.append(nm+(f'^{e}' if e!=1 else ''))
        mm='*'.join(mono)
        if not mm: t=cs
        elif cs=='1': t=mm
        elif cs=='-1': t='-'+mm
        else: t=cs+'*'+mm
        if parts and not t.startswith('-'): t='+'+t
        parts.append(t)
    return ''.join(parts) or '0'

st=time.time(); X,Y=endpoint(); eq=[]
for d in range(start,N+1):
    for f in X[d]+Y[d]:
        if f: eq.append(f)
Delta=O
for i in range(6):
    for j in range(i): Delta*=slopes[i]-slopes[j]
# Distinct-direction saturation and a projective chart for the first nonzero layer.
eq=[g['S']*Delta-O, g[f'c{chart}_{start}']-O]+eq
os.makedirs(os.path.dirname(out),exist_ok=True)
with open(out,'w') as f:
    f.write(','.join(names)+'\n'+str(char)+'\n')
    for i,q in enumerate(eq): f.write(expr(q)+(',\n' if i+1<len(eq) else '\n'))
print('vars',len(names),'eq',len(eq),'maxterms',max(len(f.terms()) for f in eq),'bytes',os.path.getsize(out),'sec',round(time.time()-st,3),flush=True)
