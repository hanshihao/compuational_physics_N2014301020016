# -*- coding: utf-8 -*-
"""
Created on Sun Nov 06 20:50:53 2016

@author: 27373
"""

import pylab as pl
import math
class oscillatory:
    def __init__(self, intial_theta=0.5,intial_omega=0,time_of_duration=10000):
        self.theta=[intial_theta]
        self.t=[0]
        self.omega=[intial_omega]
        self.dt=0.01
        self.q=0.5        
        self.F_D=1.2
        self.omega_D=float(2)/3
        self.nsteps = int(time_of_duration // self.dt + 1)
        self.tmp_omega=[0]
        self.tmp_theta=[0]
    def calculate(self):
        for i in range(self.nsteps):#set an arbitrary time limit of the plot
            tmp_omega=self.omega[i]-(math.sin(self.theta[i])+self.q*self.omega[i]-self.F_D*math.sin(self.omega_D*self.t[i]))*self.dt
            self.omega.append(tmp_omega)  
            tmp_theta=self.theta[i]+self.omega[i+1]*self.dt                        
            self.theta.append(tmp_theta)
            while self.theta[-1]>1*math.pi:
                self.theta[-1]=self.theta[-1]-2*math.pi
            while  self.theta[-1]<-1*math.pi:
                self.theta[-1]=self.theta[-1]+2*math.pi 
            self.t.append(self.t[i]+self.dt)
        for i in range(self.nsteps):           
           if (self.t[i]-math.pi/2)%(2*math.pi/self.omega_D)<0.005:
                self.tmp_omega.append(self.omega[i])
                self.tmp_theta.append(self.theta[i])
    def show(self):
        pl.plot(self.tmp_theta, self.tmp_omega,'.',label='$F_{D}$=%.2f'%self.F_D)
        pl.xlabel('$\\theta$ (radians)')
        pl.ylabel('$\\omega$(radius/s)')
        pl.title('$w$ versus $\\theta$')
        pl.grid(True)        
        pl.show()
a=oscillatory()
a.calculate()
a.show()