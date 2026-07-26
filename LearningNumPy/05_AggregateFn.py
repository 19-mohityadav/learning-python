import numpy as np

# Aggregate functions -> summarize data and return a single value

array = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10]])

# print(np.sum(array))
# print(np.mean(array))
# print(np.std(array))
# print(np.var(array))
# print(np.median(array))
# print(np.min(array))
# print(np.max(array))
# print(np.argmin(array)) # position of the min val
# print(np.argmax(array))  # index of greatest val

print(np.sum(array, axis=0)) # col sum -> [7 9 11 13 15]
print(np.sum(array, axis=1)) # row sum -> [15 40]