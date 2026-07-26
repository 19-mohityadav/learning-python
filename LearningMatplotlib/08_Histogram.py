import numpy as np
import matplotlib.pyplot as plt

# Histogram --> A visual representation of the distribution of quantitative data.
#               They group values into bins (intervals)
#               and counts how many fall in each range.

scores = np.random.normal(loc=80, scale= 50, size= 100)
scores = np.clip(scores, 0, 100)

plt.hist(scores, bins= 10,
         color= 'blue',
         edgecolor='black')
plt.title("Exam Scores Histogram")
plt.xlabel("Scores")
plt.ylabel("No of Students")

plt.show()