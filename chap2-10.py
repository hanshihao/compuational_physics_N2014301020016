# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 23:04:52 2016

@author: 27373
"""

import pylab as pl
import math
initial_angle=math.pi*55/180
initial_v=569.83
class oblique_throw:
    def __init__(self,x=0,y=0,time_step=0.1,gravitational_constant=6.67*10**-11,
                 radius_of_earth=6371000,mass_of_earth=5.977*10**24,totle_time=120,
                 B=0.000045,mass=10,target_x=30000,target_y=1000,a=0.0065,
                 initial_vx=initial_v*math.cos(initial_angle),
                 initial_vy=initial_v*math.sin(initial_angle)):
        self.vx=[initial_vx]
        self.vy=[initial_vy]
        self.dt=time_step
        self.G=gravitational_constant
        self.R=radius_of_earth
        self.M=mass_of_earth
        self.m=mass
        self.a=a
        self.B=[B]
        self.x=[x]
        self.y=[y]
        self.t=[0]
        self.time=totle_time
        self.x0=target_x
        self.y0=target_y
    def trajectory(self):
        _time = 0
        while(_time < self.time and self.x[-1]<30000):
            self.x.append(self.x[-1]+\
                          self.vx[-1]* self.dt)
            self.vx.append(self.vx[-1]-self.B[-1]*math.sqrt((self.vx[-1])**2+\
                           (self.vy[-1])**2)*self.vx[-1]/self.m*self.dt)
            self.vy.append(self.vy[-1] -\
                          self.dt * self.G * self.M / (self.R + self.y[-1])**2-\
                          self.B[-1]*math.sqrt((self.vx[-1])**2+(self.vy[-1])**2)*\
                          self.vy[-1]/self.m*self.dt)
            self.y.append(self.y[-1] +\
                          self.vy[-1] * self.dt)
            self.B.append(self.B[-1]*(1-self.a*self.y[-1]/288)**2.5)
            self.t.append(_time)
            _time += self.dt    
    def show_results(self):
        font = {'family': 'serif',
                'color':  'darkblue',
                'weight': 'normal',
                'size': 16,
        }
        pl.plot(self.x, self.y)
        pl.plot(self.x0,self.y0,"r*")
        pl.title('Trajectory of cannon shell', fontdict = font)
        pl.xlabel('x ($m$)')
        pl.ylabel('y ($m$)')
        pl.xlim(0,40000)
        pl.ylim(0,20000)
        pl.show()
        print(self.y[-1])
        
a= oblique_throw()
a.trajectory()
a.show_results()