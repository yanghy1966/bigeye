# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import

""" 练习matplotlib绘图工具
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

fig = plt.figure()
l1 = [0,10]
l2 = [5,8]
line1 = Line2D([0,1],[10,1], transform=fig.transFigure, figure=fig, color="r")
line2 = Line2D([3,1],[4,1], transform=fig.transFigure, figure=fig, color="r")

fig.lines.extend([line1, line2])

fig.show()

"""

plt.show()
for i in range(10):
    plt.figure(1)
    r1 = np.random.rand() * 10
    r2 = np.random.rand() * 10
    print([r1,r2])
    plt.plot([r1,r2])
    #plt.draw()

plt.show()
#plt.show()
x = np.linspace(0,3,100)
y = np.sin(x)

plt.plot([1,2,3])

#plt.plot(x,y)

#plt.show()

"""

"""

plt.figure(1) # 创建图表1
plt.figure(2) # 创建图表2
ax1 = plt.subplot(211) # 在图表2中创建子图1
ax2 = plt.subplot(212) # 在图表2中创建子图2
x = np.linspace(0, 3, 100)

for i in xrange(5):
    plt.figure(1)  #❶ # 选择图表1
    plt.plot(x, np.exp(i*x/3))
    plt.sca(ax1)   #❷ # 选择图表2的子图1
    plt.plot(x, np.sin(i*x))
    plt.sca(ax2)  # 选择图表2的子图2
    plt.plot(x, np.cos(i*x))
plt.show()


hl, = plt.plot([], [])

def update_line(hl, new_data):
    hl.set_xdata(np.append(hl.get_xdata(), new_data))
    hl.set_ydata(np.append(hl.get_ydata(), new_data))
    plt.draw()

update_line(hl,[1,2])
update_line(hl,[2,3])
#plt.show()
"""
