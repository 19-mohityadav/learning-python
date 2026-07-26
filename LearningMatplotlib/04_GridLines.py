import matplotlib.pyplot as plt
import numpy as np

# grid() --> Helps make plots easier to read by adding reference lines like graph.

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

plt.grid(axis='y',
         linewidth=2,
         color="lightgray",
         linestyle="dashdot", )
plt.plot(x, y)
plt.show()