# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 22:40:51 2016

@author: rakes_000
"""

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

default = 99;
init = [0,0]
goal = [len(grid[0])-1,len(grid)-1]

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]]
delta_name = ['^', '<', 'v', '>']

def print_list(list_to_be_printed):
    for i in range(len(list_to_be_printed)):
        print(list_to_be_printed[i]) 

def create_dynamic_grid(grid,init,goal):
    closed_grid = grid;
    closed_grid[goal[0]][goal[1]]=1;
    flag = 0;
    g = 0;
    open_list = []
    dynamic_grid = [[default for i in range(len(grid[0]))] for j in range(len(grid))]
    nav_grid = [['B' if grid[j][i]==1 else ' ' for i in range(len(grid[0]))] for j in range(len(grid))]
    path_map = [[default for i in range(len(grid[0]))] for j in range(len(grid))]
    path_map[goal[0]][goal[1]] = '*'
    nav_grid[goal[0]][goal[1]] = '*';
    dynamic_grid[goal[0]][goal[1]] = 0;
    pos = [0,goal[0],goal[1]];
    while(True):
        val_inc_counter=1;
        sum_closed_grid = sum([sum(closed_grid[i]) for i in range(len(grid))])
        if(sum_closed_grid==len(grid[0])*len(grid)):
            flag = 1;
            break;
        for i in range(len(delta)):
            x2 = pos[1] + delta[i][0];
            y2 = pos[2] + delta[i][1];
            if x2>=0 and x2<len(grid) and y2>=0 and y2<len(grid[0]) and closed_grid[x2][y2]==0:
                if val_inc_counter==1:
                    val_inc_counter=0;
                    g = g+1;
                dynamic_grid[x2][y2]=g;
                path_map[x2][y2] = (i+2)%4 #(i+2)%4 gives the opposite action - For up its down and vice versa
                nav_grid[x2][y2]=delta_name[(i+2)%4]
                open_list.append([g,x2,y2])
                closed_grid[x2][y2] = 1;
        if open_list ==[]:
            break;
        pos = min(open_list)
        g = pos[0]
        open_list.remove(pos)
    return [flag,dynamic_grid,nav_grid,path_map];

def path_from_src_to_goal(path_map,src,goal):
    pos = src;
    path = [src];
    success = 0;
    road_map = [['B' if path_map[j][i]==99 else ' ' for i in range(len(path_map[0]))] for j in range(len(path_map))]
    road_map[goal[0]][goal[1]] = '*'    
    while(True):
        if pos==goal:
            success = 1;
            break;
        if path_map[pos[0]][pos[1]] == 99:
            success = 0;
            break;
        road_map[pos[0]][pos[1]] = delta_name[path_map[pos[0]][pos[1]]]
        x2 = pos[0]+delta[path_map[pos[0]][pos[1]]][0]
        y2 = pos[1]+delta[path_map[pos[0]][pos[1]]][1]
        pos = [x2,y2]
        path.append(pos)
    return [success,path,road_map]

[flag,dynamic_grid,nav_grid,path_map] = create_dynamic_grid(grid,init,goal)
if flag==0:
    print('Failure - Mapping Incomplete')
    print_list(dynamic_grid)
    print()
    print_list(nav_grid)
else:
    print_list(dynamic_grid)
    print()
    print_list(nav_grid)

[success,path,road_map] = path_from_src_to_goal(path_map,[2,1],goal)
if success==1:
    print()
    print_list(road_map)
    print()
    print(path)
else:
    print('Failure');