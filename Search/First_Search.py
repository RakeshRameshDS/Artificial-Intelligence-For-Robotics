# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 15:17:05 2016

@author: rakes_000
"""

# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']


def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    closed_list = [];
    grid_map = [[[0,0] for i in range(len(grid[0]))] for j in range(len(grid))]
    open_list = [];
    pos = init;    
    road_map = [[' ' for i in range(len(grid[0]))] for j in range(len(grid))]
    val = 0;
    path = [];
    closed_list.append([pos,val]);
    while(True):
        combined_extract = [closed_list[i][0] for i in range(len(closed_list))] + [open_list[i][0] for i in range(len(open_list))]
        open_prospectives = [[pos[0]+delta[i][0],pos[1]+delta[i][1]] for i in range(len(delta))   if ((pos[0]+delta[i][0])>=0 and (pos[0]+delta[i][0])<len(grid) and (pos[1]+delta[i][1])>=0 and (pos[1]+delta[i][1])<len(grid[0]) and grid[pos[0]+delta[i][0]][pos[1]+delta[i][1]]==0)]
        val = val+cost;        
        open_prospectives = [[open_prospectives[j],val] for j in range(len(open_prospectives)) if open_prospectives[j] not in combined_extract]
        for i in range(len(open_prospectives)):
            grid_map[open_prospectives[i][0][0]][open_prospectives[i][0][1]] = pos     
        open_list += open_prospectives 
        tmp = [open_list[i][1] for i in range(len(open_list))]
        if open_list==[]:
            break;
        pos = open_list[tmp.index(min(tmp))][0]
        [x,ret] = open_list.pop(tmp.index(min(tmp)))
        val = ret;
        closed_list.append([pos,ret])
    if pos==goal:
        val = val-cost;
        path = [goal];
        print(val)
        g = goal;
        for i in range(val):
            g = grid_map[g[0]][g[1]]        
            path.append(g);
        path.reverse();
        for i in range(len(path)-1):
            road_map[path[i][0]][path[i][1]] = delta_name[delta.index([path[i+1][0]-path[i][0],path[i+1][1]-path[i][1]])]
        road_map[goal[0]][goal[1]]='*'
        for i in range(len(road_map)):
            print(road_map[i])
        return path
    else:
        return []

path = search(grid,init,goal,cost)
if path==[]: 
    print('fail')
else:
    print(path)