# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 19:30:21 2016

@author: rakes_000
"""

grid = [[0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']


def AStar_search(grid,init,goal,cost):
    path = [goal];
    grid_len = len(grid)+len(grid[0])-2
    heuristic = [[grid_len-i-j for j in range(len(grid[0]))] for i in range(len(grid))]
    road_traced = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
    road_map = [[' ' for i in range(len(grid[0]))] for j in range(len(grid))]
    path_traversed = [[-1 for i in range(len(grid[0]))] for j in range(len(grid))]
    open_list = [];
    g = 0;
    counter = 0;
    f = 0;
    flag = 0;
    closed_list = grid;
    pos = [heuristic[init[0]][init[1]],0,init[0],init[1]];
    while(True):
        counter += 1;
        var_inc_g = 1;
        open_extract = [[x,y] for [a,b,x,y] in open_list]
        for j in range(len(delta)):
            x2 = pos[2]+delta[j][0];
            y2 = pos[3]+delta[j][1];
            if x2>=0 and x2<len(grid) and y2>=0 and y2<len(grid[0]) and closed_list[x2][y2]==0 and [x2,y2] not in open_extract:
                if(var_inc_g==1):
                    g += 1;
                    var_inc_g = 0;
                f = g+heuristic[x2][y2];
                road_traced[x2][y2] = j;
                open_list.append([f,g,x2,y2])
        path_traversed[pos[2]][pos[3]] = counter;
        closed_list[pos[2]][pos[3]] = 1; 
        if [pos[2],pos[3]]==goal:
            flag = 1;
            break;
        if open_list != []:
            pos = min(open_list)
            open_list.remove(pos)
            g = pos[1]
        else:
            break;

    x2 = goal[0]
    y2 = goal[1]
    road_map[x2][y2] = '*'
    for i in range(g):
        rt = road_traced[x2][y2]
        x2 = x2-delta[rt][0]
        y2 = y2-delta[rt][1]
        path.append([x2,y2])
        road_map[x2][y2] = delta_name[rt]

    print_list(closed_list)
    print()
    print_list(path_traversed)
    print()
    print_list(road_map)
    print()
    path.reverse();
    return path;

def print_list(list_to_be_printed):
    for i in range(len(list_to_be_printed)):
        print(list_to_be_printed[i]) 
        
print(AStar_search(grid,init,goal,cost));