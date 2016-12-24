# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 16:21:46 2015

@author: rakes_000
"""
"""
n = 5
z = [float(1.0/n) for i in range(n)]
print(z)
pHit = 0.6
pMiss = 0.2
x = [z[i]*pHit if (i==1 or i==2) else z[i]*pMiss for i in range(len(z))]
print([x[i]/sum(x) for i in range(len(x))])
"""
p = [0.2,0.2,0.2,0.2,0.2]
world = ['green','red','red','green','green']
Z = 'green'
measurements = ['red','red']
motions = [1,1]
pHit = 0.6
pMiss = 0.2

def sense(p, Z, world, pHit=0.6, pMiss=0.2):
    q = [p[i]*pHit if world[i]==Z else p[i]*pMiss for i in range(len(p))]
    q = [q[i]/sum(q) for i in range(len(q))]
    return q

def move(p,U):
    q = [p[(i-U)%len(p)] for i in range(len(p))]
    return q
    
def moveInaccurate(p,U,pHit=0.8,pMiss=0.1):
    q = move(p,U)
    x = [q[(i+1)%len(q)]*pMiss+q[(i-1)%len(q)]*pMiss+q[i]*pHit for i in range(len(q))]
    return x

T = sense(p,Z,world,pHit,pMiss)
T = moveInaccurate(T,1)

for i in range(len(measurements)):
    p = sense(p,measurements[i],world)
    p = moveInaccurate(p,motions[i])

print(p)

