import matplotlib.pyplot as plt
import numpy as np

# Pie Chart --> Circular chart divided into slices to show percentages of the total.
#               Good for visualizing distribution among categories

categories = np.array(["Freshman", "Sophomores", "Juniors", "Seniors"])
values = np.array([300, 250, 275, 400])
colors = ["red", "green", "blue", "yellow"]

plt.pie(values, labels=categories,
                autopct="%1.1f%%",
                shadow=True,
                colors=colors,
                explode=[0, 0, 0.2, 0])
plt.title("MY College")
plt.show()