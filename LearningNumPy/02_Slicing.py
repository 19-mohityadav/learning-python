import numpy as np

# Slicing --> array[start:end:step] (end index is exclusive)
array = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
])

# print(array)
# want first row in 2D arr
print("First row")
# print(array[0])

# by range
print("By range")
print(array[0:2])  # [st:end]

# select every 2nd row
print("Step")
print(array[0:4:2]) # or [: : 2] (negative step will reverse the row)

# column selection
print("Col E")
print(array[0,1]) #[rowI, colI]

print(array[:,1]) # selected second col
print("Last col")
print(array[:,-1]) # last col

print("First 3 columns")
print(array[:,0:3]) # Start is 0 and end is 3 so, (0 - 2) selected

print("Step")
print(array[:,::2])

print("Col reverse every two step")
print(array[:,::-2])

# First 2 rows but only first two cols elements
print("Both Selection")
print(array[0:2, 0:2]) # 1 2 5 6