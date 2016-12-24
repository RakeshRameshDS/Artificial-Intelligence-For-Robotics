# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 16:16:13 2016

@author: rakes_000
"""

class Gaussian:
    def __init__(self,name,mean,variance):
        self.name = name
        self.mean = mean
        self.variance = variance

    def __mul__(self, other):
        if isinstance(other,Gaussian):
            me = (other.variance*self.mean + self.variance*other.mean)/(self.variance+other.variance)
            var = (other.variance*self.variance)/(self.variance+other.variance)
            return Gaussian(str(self.name+'*'+other.name),me,var)
            
    def __add__(self, other):
        if isinstance(other,Gaussian):
            me = other.mean + self.mean
            var = other.variance + self.variance
            return Gaussian(str(self.name+'+'+other.name),me,var)
    
    def __str__(self):
        return '===== '+str(self.name)+' ====='+'\nMean - '+str(self.mean)+'\nVariance - '+str(self.variance)