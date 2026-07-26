import matplotlib.pyplot as plt
import numpy as np

# Sactter Graph --> Shows the relationship B/W two variables
#                   it Helps to identify a correlation (+, -, None)
#                   E.g: Study hours vs. Test scores


x1 = np.array([0, 1, 1, 2, 3, 4, 5, 6, 7, 7, 8]) # hours studied
y1 = np.array([55, 60, 65, 62, 70, 75, 78, 82, 85, 87, 90]) # Grades


x2 = np.array([0, 1, 1, 2, 3, 4, 4, 6, 7, 8, 8]) # hours studied
y2 = np.array([50, 70, 69, 72, 60, 55, 88, 92, 80, 87, 70]) # Grades

plt.scatter(x1,y1, color = "red",
                alpha = 0.5,
                s = 100,
                label = "Class A")

plt.scatter(x2,y2, color = "blue",
                alpha = 0.5,
                s = 100,
                label = "Class B")

plt.title("Test Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Grade")

plt.show()