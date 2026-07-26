import numpy as np

rng = np.random.default_rng() # we can use here seed to reproduce same value again(seed =1)

print(rng.integers(1, 7)) # (low, high) -> 1 to 6

print(rng.integers(low=1, high=100, size=10)) # 10 rnd no, we can make it 2 d array by passing two arg in size

print(np.random.uniform(low=-1, high=1, size=10))

# Shuffle an array
array = np.array([1, 2, 3, 4, 5])
rng.shuffle(array)
print(array) # array will be shuffled

# Random choice
fruits = ['apple', 'banana', 'cherry', 'coconut', 'grape', 'mango']
fruit = rng.choice(fruits, size= 3)
print(fruit) # random fruits
