# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 20:45:40 2016

@author: rakes_000

Class Car !!
"""

import random
from math import *
import matplotlib.pyplot as plt

world_size = 100.0

class Car:
    def __init__(self,length):
        self.length = float(length)
        self.x = random.random() * world_size
        self.y = random.random() * world_size
        self.orientation = random.random() * 2.0 * pi
        self.forward_noise = 0.0;
        self.turn_noise    = 0.0;
        self.sense_noise   = 0.0;
        self.bearing_noise  = 0.0;
        self.steering_noise = 0.0;
        self.distance_noise = 0.0;
    
    def set(self, new_x, new_y, new_orientation):
            
        self.x = float(new_x)
        self.y = float(new_y)
        self.orientation = float(new_orientation)
    
    
    def set_noise(self, new_f_noise, new_t_noise, new_s_noise):
        # makes it possible to change the noise parameters
        # this is often useful in particle filters
        self.forward_noise = float(new_f_noise);
        self.turn_noise    = float(new_t_noise);
        self.sense_noise   = float(new_s_noise);
        
    def set_car_noise(self, b_n, s_n, d_n):
        self.bearing_noise = float(b_n)
        self.distance_noise = float(d_n);
        self.steering_noise = float(s_n);
    
    def move(self,turn,forward):
        x_new = 0.0;
        y_new = 0.0;
        orientation_new = 0.0;
        turn = random.gauss(turn,self.steering_noise);
        forward = random.gauss(forward,self.distance_noise);
        beta = (forward/self.length)*tan(turn);
        #print(beta)
        if abs(beta)<0.001:
            x_new = self.x + forward*cos(self.orientation);
            y_new = self.y + forward*sin(self.orientation);
            orientation_new = (self.orientation + beta)%(2*pi);
        else:
            R = forward/beta;
            Cx = self.x - R*sin(self.orientation);
            Cy = self.y + R*cos(self.orientation);
            x_new = Cx + sin(self.orientation + beta)*R;
            y_new = Cy - cos(self.orientation + beta)*R;
            orientation_new = (self.orientation + beta)%(2*pi);
        car_new = Car(self.length)
        car_new.set(x_new,y_new,orientation_new);
        return car_new;
    
    def sense(self,landmarks,add_noise):
        sense_angles = [];
        for i in landmarks:
            dx = i[1] - self.x;
            dy = i[0] - self.y;
            angle = atan2(dy,dx)-self.orientation
            if add_noise==1:
                angle = angle + random.gauss(0.0,self.bearing_noise);
            angle = angle%(2*pi)
            sense_angles.append(angle);
        return sense_angles;
        
    def __repr__(self):
        return '[x=%.6s y=%.6s orient=%.6s]' % (str(self.x), str(self.y), str(self.orientation))

landmarks  = [[0.0, 100.0], [0.0, 0.0], [100.0, 0.0], [100.0, 100.0]] # position of 4 landmarks in (y, x) form.
world_size = 100.0 
#motions = [[0.0,10.0],[pi/6.0, 10],[0.0, 20.0]]
motions = [[-0.2,10] for i in range(10)];
my_car = Car(20)
my_car.set(30.0,20.0,pi/5.0);
print(my_car)
for i in range(len(motions)):
    my_car = my_car.move(motions[i][0],motions[i][1]);
    print(my_car);

