# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 15:39:07 2016

@author: rakes_000
"""
from gaussian import Gaussian
import math

def GS(mean,variance,X):
    return ((1/math.sqrt(2*math.pi*variance))*math.pow(math.e,((-1/2)*(X-mean)**2/variance)))

measurements = [5.,6.,7.,9.,10.]
motion = [1.,1.,2.,1.,1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0.
sig = 10000
#sig = 0.0000001
measurement_Gaussian = [Gaussian('ME'+str(i),measurements[i],measurement_sig) for i in range(len(measurements))]
motion_Gaussian = [Gaussian('MO'+str(i),motion[i],motion_sig) for i in range(len(motion))]
base = Gaussian('Base',mu,sig)
for i in range(len(measurements)):
    base = base*measurement_Gaussian[i]
    base = base + motion_Gaussian[i]
    print(base)