# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 08:57:44 2016

@author: rakes_000
"""

# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's 
# optimal path to the position specified in goal; 
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a 
# right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right
                
goal = [2, 0] # given in the form [row,col]

cost = [2, 1, 20] # cost has 3 values, corresponding to making 
                  # a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------


def print_list(list_to_be_printed):
    for i in range(len(list_to_be_printed)):
        print(list_to_be_printed[i]) 

def optimum_policy2D(grid,init,goal,cost):
    closed_list = grid
    map_grid = [[[0,0,0] for i in range(len(grid[0]))] for j in range(len(grid))]
    open_list = []
    pos = [0,0,init[0],init[1]]
    # pos = [g,orientation,x,y]
    g = 0;
    for i in range(10):
        temp_cnt = 0;
        for i in range(len(action)):
            new_d = pos[1]+action[i];
            x2 = pos[2]+forward[new_d][0];
            y2 = pos[3]+forward[new_d][1];
            if x2>=0 and x2<len(grid) and y2>=0 and y2<len(grid[0]) and closed_list[x2][y2]==0:
                new_g = g+cost[i]
                open_list.append([new_g,new_d,x2,y2])
                map_grid[x2][y2] = [new_g,pos[2],pos[3]]
                temp_cnt+=1;
        if temp_cnt <= 1:
            closed_list[pos[2]][pos[3]] = 1;
        if temp_cnt>1:
            map_grid[pos[2]][pos[3]] = [10,'J']
        pos = min(open_list);
        open_list.remove(pos)
        g = pos[0]
    print_list(closed_list)
    print()
    print_list(map_grid)
    print()
    print(open_list)
    pass
    #return policy2D

optimum_policy2D(grid,init,goal,cost)