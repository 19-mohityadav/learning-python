import matplotlib.pyplot as plt
import numpy as np

# Bar Chart --> compare categories of data by representing each category with a bar

# x = [1, 2, 3, 4, 5]
# y = [10, 20, 30, 40, 50]
#
# plt.bar(x, y)
# plt.show()

categories = np.array(["Grains", "Fruits", "Vegetables", "Protein", "Dairy", "Sweets"])
values = np.array([4, 2, 3, 4, 4, 1])

plt.bar(categories, values, color="skyblue")

plt.title("Daily Consumption", fontsize=20)
plt.xlabel("Food")
plt.ylabel("Consumption")

plt.show()
