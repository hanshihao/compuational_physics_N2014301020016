###第十一次作业###
####摘要####
####Study the behavior of our model for Hyperion for different initial conditions. Estimate the Lyapunov exponent from calculations of Δθ, such as those shown in Figure 4.19. Examine how this exponent varies as a function of the eccentricity of the orbit####
####背景####
#####三体问题是天体力学中的基本力学模型。它是指三个质量、初始位置和初始速度都是任意的可视为质点的天体，在相互之间万有引力的作用下的运动规律问题。现在已知，三体问题不能精确求解，即无法预测所有三体问题的数学情景，只有几种特殊情况已研究。三体问题（three-body problem）最简单的一个例子就是太阳系中太阳、地球和月球的运动。在浩瀚的宇宙中，星球的大小可以忽略不记，所以我们可以把它们看成质点。如果不计太阳系其他星球的影响，那么它们的运动就只是在引力的作用下产生的，所以我们就可以把它们的运动看成一个三体问题。#####
#####![enter image description here](https://github.com/hanshihao/compuational_physics_N2014301020016/blob/master/QQ%E6%88%AA%E5%9B%BE20161204204225.png)#####
#####![enter image description here](https://github.com/hanshihao/compuational_physics_N2014301020016/blob/master/QQ%E6%88%AA%E5%9B%BE20161204204726.png)#####
#####![enter image description here](https://github.com/hanshihao/compuational_physics_N2014301020016/blob/master/9f510fb30f2442a7244523d9d143ad4bd1130207.jpg)#####
#####天体力学中的基本力学模型。研究三个可视为质点的天体在相互之间万有引力作用下的运动规律问题。这三个天体的质量、初始位置和初始速度都是任意的。在一般三体问题中，每一个天体在其他两个天体的万有引力作用下的运动方程都可以表示成3个二阶的常微分方程，或6个一阶的常微分方程。因此，一般三体问题的运动方程为十八阶方程，必须得到18个积分才能得到完全解。然而，还只能得到三体问题的16个积分，因此还远不能解决三体问题。#####
#####研究方法：由于三体问题不能严格求解，在研究天体运动时，都只能根据实际情况采用各种近似的解法，研究三体问题的方法大致可分为3类：#####
#####第一类是分析方法，其基本原理是把天体的坐标和速度展开为时间或其他小参数的级数形式的近似分析表达式，从而讨论天体的坐标或轨道要素随时间的变化；#####
#####第二类是定性方法，采用微分方程的定性理论来研究长时间内三体运动的宏观规律和全局性质；#####
#####第三类是数值方法，这是直接根据微分方程的计算方法得出天体在某些时刻的具体位置和速度。#####
#####这三类方法各有利弊，对新积分的探索和各类方法的改进是研究三体问题中很重要的课题。#####
####正文####
#####改变vy0以改变偏心率，绘制不同vy0时的图像，[查看源代码](https://github.com/hanshihao/compuational_physics_N2014301020016/blob/master/orbits2.py)#####
#####轨道为圆时，即vy0=2π#####
#####![enter image description here](https://github.com/hanshihao/compuational_physics_N2014301020016/blob/master/QQ%E6%88%AA%E5%9B%BE20161211102055.png)#####
####以下分别为vy0=3，4，5，6，7，8时的图像####
#####![enter image description here](https://github.com/hanshihao/compuational_physics_N2014301020016/blob/master/QQ%E6%88%AA%E5%9B%BE20161211202233.png)#####
#####![enter image description here](https://github.com/hanshihao/compuational_physics_N2014301020016/blob/master/QQ%E6%88%AA%E5%9B%BE20161211202424.png)#####
#####![enter image description here](https://github.com/hanshihao/compuational_physics_N2014301020016/blob/master/QQ%E6%88%AA%E5%9B%BE20161211202457.png)#####
#####![enter image description here](https://github.com/hanshihao/compuational_physics_N2014301020016/blob/master/QQ%E6%88%AA%E5%9B%BE20161211202520.png)#####
#####![enter image description here](https://github.com/hanshihao/compuational_physics_N2014301020016/blob/master/QQ%E6%88%AA%E5%9B%BE20161211202542.png)#####
#####![enter image description here](https://github.com/hanshihao/compuational_physics_N2014301020016/blob/master/QQ%E6%88%AA%E5%9B%BE20161211202603.png)#####
