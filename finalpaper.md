##**光栅衍射光强分布的研究**##


----------


#####**摘要：** 衍射和干涉是各种波动所特有的现象，波动能绕过障碍物传播。水波、声波、无线电波的波长较长，在日常生活中可以明显地觉察到这类现象。光波的波长很短，只有当障碍物很小时才能观察到。历史上，正是通过对光的干涉和衍射现象的研究而认识到光具有波动性。近代通过电子、中子等微观粒子的衍射实验，证明了微观粒子的波动性。 因此，研究光波的衍射也就是研究光波的传播规律，一切涉及光的传播问题中，衍射现象均存在并且有着重要的实际意义。本文着眼于用编程模拟的方式探究光栅衍射的光强分布。#####
#####**关键词：** 光强分布   光栅衍射   傅里叶变换法   计算机模拟#####
#####**Abstract：** Diffraction and interference are peculiar to all kinds of fluctuations, and fluctuations can bypass the propagation of obstacles. Water waves, sound waves, radio waves of a longer wavelength, in daily life can be clearly aware of this phenomenon. The wavelength of light is very short and can only be observed when the obstruction is small. Historically, it is through the interference of light and diffraction phenomena of the study and realize the light with volatility. In recent years, the microscopic particle's fluctuation is proved by the experiment of electron and neutron. Therefore, the study of light diffraction is to study the propagation of light waves, all involving the issue of light propagation, diffraction phenomena exist and has important practical significance. This paper focuses on exploring the light intensity distribution of grating diffraction by means of programming simulation.#####
#####**Key words：** Light Intensity Distribution   Diffraction grating   Fourier transform method   Computer simulation#####
####**1 引言**####
####		按照几何光学的传播规律，自点光源发出的光线，当其通过圆孔、圆屏或其它任意形状的孔和障碍物达到接收屏上时，在接受屏上应该呈现明晰的几何阴影。然而实际上，当孔和障碍物很小时，几何阴影失去了清晰的轮廓，在阴影边缘出现了一系列明暗相间的条纹，在离开边缘一定距离的阴影区内有光进入。这种光在传播过程中不遵从几何光学规律的现象，称为光的衍射。####
#####**1.1 光栅衍射基本概念**#####
#####		衍射光栅，通常简称为“光栅”，一种由密集﹑等间距平行刻线构成的非常重要的光学器件。分反射和透射两大类。它利用多缝衍射和干涉作用﹐将射到光栅上的光束按波长的不同进行色散﹐再经成像镜聚焦而形成光谱。天文仪器中应用较多的是反射光栅﹐它的基底是低膨胀系数的玻璃或熔石英﹐上面镀铝﹐然后把平行线刻在铝膜上。#####
#####		光栅色散可用方程m=c(sini +sinφ )描述﹐式中i为入射角﹐φ取正值﹐为衍射角。当衍射光与入射光在光栅法线同一侧i为正﹐反之为负﹔c为光栅常数﹐为一个整数。当入射角i 给定时﹐对于满足光栅方程的每个m值﹐都有相应的级光谱﹐每个波长的光能量分散在诸光谱级中。现代刻制光栅的技术﹐能使所有衍射光栅具有严格规定的形状和尺寸。选择适当入射角﹐可使所需的波长及其邻近波段的绝大部分(达70%)的光能量集中到预定的光谱级中。这种集中光能量的性质称为“闪耀”。起衍射作用的刻线槽面与光栅面的夹角β﹐称为闪耀角。具有这种性质的光栅称为闪耀光栅或定向光栅。另一方面﹐满足=……的不同光谱级次的谱线﹐在焦面上重叠。同所需谱线重叠的其他谱线﹐一般用有色玻璃隔去。光栅角色散﹐理论分辨本领R =λ /δλ =mN 。此处δλ 为可分辨的最小光谱单元宽度﹐N为刻线总数。#####
 