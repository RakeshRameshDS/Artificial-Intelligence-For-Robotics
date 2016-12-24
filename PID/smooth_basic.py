# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 16:51:49 2016

@author: rakes_000
"""

# -----------
# User Instructions
#
# Define a function smooth that takes a path as its input
# (with optional parameters for weight_data, weight_smooth,
# and tolerance) and returns a smooth path. The first and 
# last points should remain unchanged.
#
# Smoothing should be implemented by iteratively updating
# each entry in newpath until some desired level of accuracy
# is reached. The update should be done according to the
# gradient descent equations given in the instructor's note
# below (the equations given in the video are not quite 
# correct).
# -----------

from copy import deepcopy
from matplotlib import pyplot as plt

# thank you to EnTerr for posting this on our discussion forum
def printpaths(path,newpath):
    for old,new in zip(path,newpath):
        print('['+ ', '.join('%.3f'%x for x in old) + \
               '] -> ['+ ', '.join('%.3f'%x for x in new) +']')

# Don't modify path inside your function.
path = [[0, 0],
        [0, 1],
        [0, 2],
        [1, 2],
        [2, 2],
        [3, 2],
        [4, 2],
        [4, 3],
        [4, 4]]

def smooth(path, weight_data = 0.5, weight_smooth = 0.1, tolerance = 0.000001):

    # Make a deep copy of path into newpath
    new_path = deepcopy(path)
    length = len(new_path)-1
    change = tolerance
    while change>=tolerance:
        change = 0.0
        for i in range(1,length):
            temp = new_path[i]
            new_path[i] = [new_path[i][0]+weight_data*(path[i][0]-new_path[i][0]),new_path[i][1]+weight_data*(path[i][1]-new_path[i][1])]
            new_path[i] = [new_path[i][0]+weight_smooth*(new_path[i+1][0]+new_path[i-1][0]-2*new_path[i][0]),new_path[i][1]+weight_smooth*(new_path[i+1][1]+new_path[i-1][1]-2*new_path[i][1])]
            change += abs(temp[0] - new_path[i][0]) + abs(temp[1] - new_path[i][1])
    #######################
    ### ENTER CODE HERE ###
    #######################
    return new_path # Leave this line for the grader!

printpaths(path,smooth(path))
print()
np = smooth(path)
p = path
plt.plot([np[i][0] for i in range(len(np))],[np[i][1] for i in range(len(np))],'r-')
plt.plot([p[i][0] for i in range(len(p))],[p[i][1] for i in range(len(p))],'b-')
plt.xlim([-1,6])
plt.ylim([-1,6])
plt.legend('SN')
