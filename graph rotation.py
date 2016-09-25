# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 09:06:06 2016

@author: 2014301020016
"""

import matplotlib.pyplot as plt   
import numpy as np  
import math  
def roseline0():  
    t = np.linspace(0, math.pi)  
    x = np.sin(t*3)*np.cos(t)*30
    y = np.sin(t*3)*np.sin(t)*30
    plt.plot(x,y, color='blue', linewidth=2, label='h')   
    plt.ylim(-40, 40)  
    plt.xlim(-40, 40)    
    plt.show()  
def roseline1():  
    t = np.linspace(0, math.pi)  
    x = np.sin(t*3)*np.cos(t)*30
    y = np.sin(t*3)*np.sin(t)*30
    plt.plot(y,x, color='blue', linewidth=2, label='h')  
    plt.ylim(-40, 40)  
    plt.xlim(-40, 40)   
    plt.show() 
def roseline2():  
    t = np.linspace(0, math.pi)  
    x = np.sin(t*3)*np.cos(t)*30
    y = np.sin(t*3)*np.sin(t)*30
    plt.plot(x,-y, color='blue', linewidth=2, label='h')   
    plt.ylim(-40, 40)  
    plt.xlim(-40, 40)  
    plt.show()  
def roseline3():  
    t = np.linspace(0, math.pi)  
    x = np.sin(t*3)*np.cos(t)*30
    y = np.sin(t*3)*np.sin(t)*30
    plt.plot(-y,x, color='blue', linewidth=2, label='h')   
    plt.ylim(-40, 40)  
    plt.xlim(-40, 40)  
    plt.show()
for b in range(20):
    t=b%4
    if t==0:
        roseline0()
        import os
        i = os.system('cls')
        import time
        time.sleep(0.1)
    else:
        if t==1:
            roseline1()
            import os
            i = os.system('cls')
            import time
            time.sleep(0.1)
        else:
            if t==2:
                roseline2()
                import os
                i = os.system('cls')
                import time
                time.sleep(0.1)
            else:
                roseline3()
                import os
                i = os.system('cls')
                import time
                time.sleep(0.1)