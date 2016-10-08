# -*- coding: utf-8 -*-
"""
Created on Sat Oct 08 22:44:54 2016

@author: 2014301020016
"""

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

class nuclei:
    def __init__(self, name,number_of_nuclei, time_constant):
        # unit of time is second
        self.name=name
        self.n = number_of_nuclei
        self.tau = time_constant
    def getnumber(self):
        print self.name, "=", self.n
    def decay(self, others):
        self.newvalue=self.n+(others.n/others.tau-self.n/self.tau)*0.01
    def update(self):
        self.n = self.newnumber
A = nuclei('A', 100, 1)
B = nuclei('B', 0, 1)
ti = 0
def decay(w, t, a):
    x, y=w
    return np.array([y/a-x/a, x/a-y/a])
t = np.arange(0, 5, 0.01)
track = odeint(decay, (100, 0), t, (1,))
plt.plot(t,track[:,0], label='Value of A', color="red",linewidth=2)
plt.plot(t,track[:,1], label='Value of B', color="blue",linewidth=2)
plt.xlabel("Time(s)")
plt.ylabel("Values")
plt.legend()
plt.show()
while ti==5:
    ti+=0.01
    print "After 0.01 seconds, %f seconds have passed" %ti
    A.decay(B)
    B.decay(A)
    A.update()
    B.update()
    A.getnumber()
    B.getnumber()