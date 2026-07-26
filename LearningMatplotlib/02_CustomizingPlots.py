import matplotlib.pyplot as plt
import numpy as np

x = np.array([2022, 2023, 2024, 2025, 2026])
y1 = np.array([14, 50, 60, 70, 80])
y2 = np.array([24, 40, 65, 73, 90])
y3 = np.array([4, 30, 6, 79, 99])


line_style = dict(marker=".",
         markerfacecolor="red",
         markeredgecolor="#1cd3fc",
         markersize=20,
         linestyle="dashed",
         linewidth=2)

plt.plot(x, y1, color="#1c5bfc", **line_style)
plt.plot(x, y2, color="#1cfc45", **line_style)
plt.plot(x, y3, color="#fc1c1c", **line_style)
plt.show()