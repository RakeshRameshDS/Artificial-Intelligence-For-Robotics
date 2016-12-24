# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 14:43:16 2016

@author: rakes_000
"""

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
"""grid = [[0, 0, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0]]"""
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right
                
goal = [2, 0] # given in the form [row,col]

cost = [2, 1, 20] # cost has 3 values, corresponding to making 
                  # a right turn, no turn, and a left turn
def print_list(list_to_be_printed):
    for i in range(len(list_to_be_printed)):
        print(list_to_be_printed[i]) 

def optimum_policy2D(grid,init,goal,cost):
    g = 0;
    pos = [g,init[2],init[0],init[1]]
    open_list = []
    policy = [['B' if grid[i][j]==1 else ' ' for j in range(len(grid[0]))] for i in range(len(grid))]
    junction_list = []
    g_grid = [[99 for i in range(len(grid[0]))] for j in range(len(grid))]
    g_grid[init[0]][init[1]] = 0
    pos_grid = [[[0,0] for j in range(len(grid[0]))] for i in range(len(grid))]
    while [pos[2],pos[3]]!=goal:
        tmp_lst = [];
        open_list_extract = [[x,y] for a,b,x,y in open_list]
        for j in range(len(action)):
            act = (pos[1]+action[j])%len(forward)
            x2 = pos[2]+forward[act][0]
            y2 = pos[3]+forward[act][1]
            if x2>=0 and x2<len(grid) and y2>=0 and y2<len(grid[0]) and grid[x2][y2]==0:               
                g_new = g+cost[j];
                if(g_grid[x2][y2]>g_new):
                    if [x2,y2] in open_list_extract:
                        idx = open_list_extract.index([x2,y2])
                        open_list.pop(idx)
                        x3=x2;
                        y3=y2;
                        while [x3,y3] not in junction_list:
                            g_grid[x3][y3] = 99;
                            [x3,y3] = pos_grid[x3][y3]
                    g_grid[x2][y2] = g_new
                    pos_grid[x2][y2] = [pos[2],pos[3]]
                    policy[pos[2]][pos[3]] = action_name[j]
                    open_list.append([g_new,act,x2,y2])
                    tmp_lst.append([g_new,act,x2,y2])
        if len(tmp_lst)>1:
            junction_list.append([pos[2],pos[3]])
            g_grid[pos[2]][pos[3]] = max(tmp_lst)[0]           
        if open_list==[]:
            break;
        pos = min(open_list)
        open_list.remove(pos)
        g = pos[0]
    policy[goal[0]][goal[1]] = '*'
    print_list(g_grid)
    print()
    print_list(pos_grid)  
    print()
    print_list(policy)
    pass    

optimum_policy2D(grid,init,goal,cost)