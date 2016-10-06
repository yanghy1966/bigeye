====================================
如何在Matplotlib中绘制交互式动画？
====================================

也就是一边计算，一边绘制，而不是计算完之后再进行绘制。

::

	import matplotlib.pyplot as plt
	import numpy as np

	plt.ion() # 交互模式
	plt.figure()
	for i in range(100):
	    plt.clf() # 清空图
	    j = np.random.rand() * 10
	    print j
	    plt.plot([j,j+2], [j,j+8], 'o')
	    plt.draw() # 绘制图像
	    plt.pause(0.05)
	raw_input("done >>")
