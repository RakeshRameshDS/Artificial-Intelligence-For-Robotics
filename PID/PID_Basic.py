# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 09:37:48 2016

@author: rakes_000
"""

# -----------
# User Instructions
#
# Implement a P controller by running 100 iterations
# of robot motion. The desired trajectory for the 
# robot is the x-axis. The steering angle should be set
# by the parameter tau so that:
#
# steering = -tau * crosstrack_error
#
# Note that tau is called "param" in the function
# below.
#
# Your code should print output that looks like
# the output shown in the video. That is, at each step:
# print myrobot, steering
#
# Only modify code at the bottom!
# ------------
 
from math import *
import random
from matplotlib import pyplot as plt

# ------------------------------------------------
# 
# this is the robot class
#

class robot:

    # --------
    # init: 
    #    creates robot and initializes location/orientation to 0, 0, 0
    #

    def __init__(self, length = 20.0):
        self.x = 0.0
        self.y = 0.0
        self.orientation = 0.0
        self.length = length
        self.steering_noise = 0.0
        self.distance_noise = 0.0
        self.steering_drift = 0.0

    # --------
    # set: 
    #	sets a robot coordinate
    #

    def set(self, new_x, new_y, new_orientation):

        self.x = float(new_x)
        self.y = float(new_y)
        self.orientation = float(new_orientation) % (2.0 * pi)


    # --------
    # set_noise: 
    #	sets the noise parameters
    #

    def set_noise(self, new_s_noise, new_d_noise):
        # makes it possible to change the noise parameters
        # this is often useful in particle filters
        self.steering_noise = float(new_s_noise)
        self.distance_noise = float(new_d_noise)

    # --------
    # set_steering_drift: 
    #	sets the systematical steering drift parameter
    #

    def set_steering_drift(self, drift):
        self.steering_drift = drift
        
    # --------
    # move: 
    #    steering = front wheel steering angle, limited by max_steering_angle
    #    distance = total distance driven, most be non-negative

    def move(self, steering, distance, 
             tolerance = 0.001, max_steering_angle = pi / 4.0):

        if steering > max_steering_angle:
            steering = max_steering_angle
        if steering < -max_steering_angle:
            steering = -max_steering_angle
        if distance < 0.0:
            distance = 0.0


        # make a new copy
        res = robot()
        res.length         = self.length
        res.steering_noise = self.steering_noise
        res.distance_noise = self.distance_noise
        res.steering_drift = self.steering_drift

        # apply noise
        steering2 = random.gauss(steering, self.steering_noise)
        distance2 = random.gauss(distance, self.distance_noise)

        # apply steering drift
        steering2 += self.steering_drift

        # Execute motion
        turn = tan(steering2) * distance2 / res.length

        if abs(turn) < tolerance:

            # approximate by straight line motion

            res.x = self.x + (distance2 * cos(self.orientation))
            res.y = self.y + (distance2 * sin(self.orientation))
            res.orientation = (self.orientation + turn) % (2.0 * pi)

        else:

            # approximate bicycle model for motion

            radius = distance2 / turn
            cx = self.x - (sin(self.orientation) * radius)
            cy = self.y + (cos(self.orientation) * radius)
            res.orientation = (self.orientation + turn) % (2.0 * pi)
            res.x = cx + (sin(res.orientation) * radius)
            res.y = cy - (cos(res.orientation) * radius)

        return res

    def __repr__(self):
        return '[x=%.5f y=%.5f orient=%.5f]'  % (self.x, self.y, self.orientation)

############## ADD / MODIFY CODE BELOW ####################
    
# ------------------------------------------------------------------------
#
# run - does a single control run


def run_P(param):
    pos_list = []
    myrobot = robot()
    myrobot.set(0.0, 1.0, 0.0)
    myrobot.set_steering_drift(10.0/180.0*pi)
    speed = 1.0 # motion distance is equal to speed (we assume time = 1)
    N = 200
    #
    for i in range(N):
        alpha = -param*(myrobot.y-0.0)
        myrobot = myrobot.move(alpha,speed);
        pos_list.append([myrobot.x,myrobot.y])
    # 
    #print(pos_list)
    plt.plot([pos_list[i][0] for i in range(len(pos_list))],[pos_list[i][1] for i in range(len(pos_list))])
    plt.plot([0,N],[0,0],'r-')
    plt.xlim([0,N])
    plt.ylim([-5,5])
    plt.show()


def run_PD(param1,param2):
    pos_list = []
    myrobot = robot()
    myrobot.set(0.0,1.0,0.0)
    myrobot.set_steering_drift(10.0/180.0*pi)
    speed = 1.0
    N = 200
    CTE_old = 0.0
    for i in range(N):
        CTE_new = myrobot.y
        alpha = -param1*CTE_new - param2*(CTE_new-CTE_old)
        CTE_old = CTE_new
        myrobot = myrobot.move(alpha,speed)
        pos_list.append([myrobot.x,myrobot.y])
    # 
    #print(pos_list)
    plt.plot([pos_list[i][0] for i in range(len(pos_list))],[pos_list[i][1] for i in range(len(pos_list))])
    plt.plot([0,N],[0,0],'r-')
    plt.xlim([0,N])
    plt.ylim([-5,5])
    plt.show()

def run_PID(param1,param2,param3):
    pos_list = []
    myrobot = robot()
    myrobot.set(0.0,1.0,0.0)
    myrobot.set_steering_drift(10.0/180.0*pi)
    speed = 1.0
    N = 200
    CTE_old = 0.0
    CTE_sum = 0.0
    for i in range(N):
        CTE_new = myrobot.y
        CTE_sum += CTE_new
        alpha = -param1*CTE_new - param2*(CTE_new-CTE_old) - param3*(CTE_sum)
        CTE_old = CTE_new
        myrobot = myrobot.move(alpha,speed)
        pos_list.append([myrobot.x,myrobot.y])
    # 
    #print(pos_list)
    plt.plot([pos_list[i][0] for i in range(len(pos_list))],[pos_list[i][1] for i in range(len(pos_list))])
    plt.plot([0,N],[0,0],'r-')
    plt.xlim([0,N])
    plt.ylim([-5,5])
    plt.show()

run_P(0.1) # call function with parameter tau of 0.1 and print results
run_PD(0.2,3.0)
run_PID(0.2,3.0,0.005)