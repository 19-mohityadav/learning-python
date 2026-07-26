import matplotlib.pyplot as plt
import numpy as np

x = np.array([2022, 2023, 2024, 2025, 2026])
y1 = np.array([14, 50, 60, 70, 80])
y2 = np.array([24, 40, 65, 73, 90])
y3 = np.array([4, 30, 6, 79, 99])

plt.title("Class Size", fontsize=25,
          fontweight='bold',
          family='Arial',
          color='blue')

plt.xlabel("Year", fontsize=20,
           fontweight='bold',
           family='Arial',
           color='#2dbefc'
           )
plt.ylabel("Students", fontsize=20)

plt.tick_params(axis='both')

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

plt.xticks(x)
plt.show()