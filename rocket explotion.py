# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 23:33:14 2016

@author: 27373
"""
line_0 = "     #    "  
line_1 = "    ###   "
line_2 = "   #####  "  
line_3 = "   #####  "  
line_4 = "   #####  "  
line_5 = "   #####  "  
line_6 = "   #####  "         
line_7 = "  ####### "  
line_8 = "    ###   "  
line_9 = "  ## # ## "  
   
ymax=50 
decelerationY=1                
for y in range(ymax*decelerationY,0,-1):    #上平移
    import os  
    i = os.system('cls')  
    y_deceleration = int(y/decelerationY)  
    for j in range(y_deceleration):  
        print " "  
    print line_0
    print line_1  
    print line_2 
    print line_3  
    print line_4  
    print line_5  
    print line_6 
    print line_7
    print line_8  
    print line_9
    decelerationY=decelerationY+0.2
    import time
    time.sleep(0.1)
import os  
i = os.system('cls')
print "          "
print "          "
print "          "
print "    ###   "
print "    ###   "
print "          "
print "          "
print "          "  
print "          "
import time
time.sleep(0.2)
import os  
i = os.system('cls')
print "          "
print "          "
print "   #   #  "
print "    ###   "
print "    ###   "
print "   #   #  "
print "          "
print "          "  
print "          "
import time
time.sleep(0.2)
import os  
i = os.system('cls') 
print "          "
print "          "
print "   # # #  "
print "  ##   ## "
print "  ##   ## "
print "   # # #  "
print "          "
print "          "  
print "          "
import time
time.sleep(0.2)
import os  
i = os.system('cls') 
print "          "
print "          "
print "    # #    "
print "  #     #  "
print " #       # "
print "  #     #  "
print "    # #    "
print "           "  
print "           "
import time
time.sleep(0.2)
import os  
i = os.system('cls') 