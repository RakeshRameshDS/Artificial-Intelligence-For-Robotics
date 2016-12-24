# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 11:52:13 2016

@author: rakes_000
"""

#colors = [['green','green','green'],['green','red','red'],['green','green','green']];
colors = [['red','green','green','red','red'],['red','red','green','red','red'],['red','red','green','green','red'],['red','red','red','red','red']]
measurements = ['green','green','green','green','green']
motion = [[0,0],[0,1],[1,0],[1,0],[0,1]]
sensor_right = 0.7
p_move = 0.8

tot = len(colors)*len(colors[0])
prob_uniform = [[1/tot for i in range(len(colors[0]))] for j in range(len(colors))]

def sense(p,measurement,sensor_right):
    p = [[sensor_right*p[i][j] if colors[i][j]==measurement else (1.0-sensor_right)*p[i][j] for j in range(len(colors[0]))] for i in range(len(colors))]
    total_sum = sum([sum(p[j]) for j in range(len(p))])
    return [[p[i][j]/float(total_sum) for j in range(len(colors[0]))] for i in range(len(colors))]

def move(p,motion,p_move):
    y = motion[0]
    x = motion[1]    
    p_orig = p
    p_new = [[p[(i-y)%len(p)][(j-x)%len(p[0])] for j in range(len(p[0]))] for i in range(len(p))]
    return [[(p_new[i][j]*p_move + p_orig[i][j]*(1-p_move)) for j in range(len(p[0]))] for i in range(len(p))]
    """    
    LRes = p
    if x>0:
        Lx = [[p[i][(j-1)%len(p)]*(1-p_move)+p[i][j]*p_move for j in range(len(p[0]))] for i in range(len(p))]
        LRes = Lx;
    if y>0:
        Ly = [[LRes[(i-1)%len(LRes)][j]*(1-p_move)+LRes[(i+1)%len(LRes)][j]*(1-p_move)+LRes[i][j]*p_move for j in range(len(LRes[0]))] for i in range(len(LRes))]
        LRes = Ly
    return [[LRes[i][j]/sum([sum(LRes[i]) for i in range(len(LRes))]) for j in range(len(LRes[0]))] for i in range(len(LRes))]
    """
    
p = prob_uniform
for i in range(len(motion)):
    p = move(p,motion[i],p_move)
    p = sense(p,measurements[i],sensor_right)
print(p)