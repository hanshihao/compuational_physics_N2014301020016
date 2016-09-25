# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 16:33:31 2016

@author: 27373
"""

import pylab as pl
y = [-20, -10,0,10,20,10,0,-10,-20]
x = [5,15,10,15,5,-10,-25,-10,5]
for i in range(200):
    pl.plot(y, x,"b*--")
    pl.xlim(-40.0, 40.0)
    pl.ylim(-40.0, 40.0)
    pl.show()
   