import matplotlib.pyplot as plt
import numpy as np

# Figure --> The entire canvas
# Ax --> A single plot in the canvas -> subplot

# print(plt.subplots(2, 2))
'''
(<Figure size 640x480 with 4 Axes>, array([[<Axes: >, <Axes: >],
       [<Axes: >, <Axes: >]], dtype=object))
'''
x = np.array([1, 2, 3, 4, 5])

figure, axes = plt.subplots(2, 2)

axes[0, 0].plot(x, x*2, color='red')
axes[0,0].set_title("x*2")

axes[0, 1].plot(x, x**2, color='blue')
axes[0,1].set_title("x**2")

axes[1, 0].plot(x, x**3, color='green')
axes[1,0].set_title("x**3")
axes[1, 1].plot(x, x**4, color='yellow')
axes[1,1].set_title("x**4")

plt.tight_layout()

plt.show()