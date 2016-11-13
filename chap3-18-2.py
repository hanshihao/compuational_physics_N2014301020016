# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 15:36:55 2016

@author: 27373
"""

import pylab as pl
import math
class bifurcation_diagram:
    def __init__(self,q=0.5,g=9.8,l=9.8,OmegaD=1.0/1.0,FD=1.20,theta=0.20):
        self.omega=[0]
        self.theta=[theta]
        self.q=q
        self.g=g
        self.l=l
        self.OmegaD=OmegaD
        self.FD=FD
        self.t=[0]
        self.dt=2*math.pi/(500*OmegaD)
        self.T=[]
        self.Theta=[]
        self.Omega=[]
        self.fd=[]
    def calculate(self):
        for i in range(7500):
            self.t.append(self.t[i] + self.dt)
            
            temp_omega=self.omega[-1]-(self.g/self.l)*\
            math.sin(self.theta[-1])*self.dt -self.q*self.omega[-1]*self.dt +\
            self.FD*math.sin(self.OmegaD*self.t[-1])*self.dt
            self.omega.append(temp_omega)            
            #这是omega（i+1）的算式
            temp_theta=self.theta[-1]+self.omega[-1]*self.dt
            #这是theta（i+1）
            while(temp_theta>=math.pi):
                 temp_theta-=2*math.pi
            while(temp_theta<=-math.pi):
                 temp_theta+=2*math.pi
            self.theta.append(temp_theta)#以上是第一个摆
            
        for i in range(8):
            self.Theta.append(self.theta[500*(i+7)])
            self.Omega.append(self.omega[500*(i+7)])
            self.fd.append(self.FD)
            
            
                
    def show_results(self):
        pl.plot(self.fd, self.Theta,'b.')
        pl.title('$Bifurcatioin$ $diagram$')
        pl.xlabel('$F_{D}$')
        pl.ylabel('$\\theta$(radians)')
        pl.show()
        

for i in range(140):
    a=bifurcation_diagram(FD=1.35+i/1000.0)
    a.calculate()
    a.show_results()