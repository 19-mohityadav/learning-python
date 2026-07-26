import numpy as np

# Scaler Arithmetic -> single data val like integers and floats
# rather than multi element struct like lists or matrices

array = np.array([1,2,3])
print(array + 1)
print(array - 1)
print(array * 2)
print(array / 2)
print(array // 2)
print(array % 2)
print(array ** 2)


# Vectorised maths Fn ->

array2 = np.array([1,2,3])

print(np.sqrt(array2))
print(np.round(array2)) # Floor to round down , ceil to round Up and diff math fn
print(np.pi) # built in constants

# Question array2 have radius of circle find area for each
print(np.pi * array2 ** 2) # i.e. pi*r^2

# Element wise arithmetic

array3 = np.array([1,2,3])
array4 = np.array([4,5,6])

print(array3 + array4) # [5 7 9]
print(array3 - array4) # [-3 -3 -3] and *,/,//,%,** all same pattern


# Comparison Operators
scores = np.array([91, 55, 100, 73, 82, 64])
print(scores == 100) # [False False True False False False]
print(scores >= 60)  # [True False True True True True]

scores[scores < 60] = 0
print(scores) #[91 0 100 73 82 64]






























