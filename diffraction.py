# -*- coding: utf-8 -*-
"""
Created on Fri Jan 06 09:43:29 2017

@author: 27373
"""

import pylab as pl
import math  as m
import numpy as np

class Diffraction():
    def __init__(self,a=4e-6,d=4e-5,lamda=632.8e-9,N=8,theta=-0.015*m.pi):
        self.a=a
        self.d=d
        self.lamda=lamda
        self.N=N
        self.theta=[theta]
        self.s=[m.sin(theta)]
        self.steps=10000
        self.phi=[2*m.pi*self.d*m.sin(theta)/self.lamda]
        self.u=[m.pi*self.a*m.sin(theta)/self.lamda]
        self.I0=[(m.sin(self.u[-1])/(self.u[-1]))**2]
        self.Id=[(m.sin(self.phi[-1]*self.N/2)/m.sin(self.phi[-1]/2))**2]
        self.I=[self.I0[-1]*self.Id[-1]]
    def calculate(self):
        for i in range(self.steps):
            self.theta.append(self.theta[-1]+0.0000001*i)
            self.s.append(m.sin(self.theta[-1]))
            self.phi.append(2*m.pi*self.d*m.sin(self.theta[-1])/self.lamda)
            self.u.append(m.pi*self.a*m.sin(self.theta[-1])/self.lamda)
            self.I0.append((m.sin(self.u[-1])/self.u[-1])**2)
            self.Id.append((m.sin(self.N*self.phi[-1]/2)/m.sin(self.phi[-1]/2))**2)
            self.I.append(self.I0[-1]*self.Id[-1])
    def show(self):
        pl.plot(self.s,self.I0,'b')
c=Diffraction()
c.calculate()
c.show()