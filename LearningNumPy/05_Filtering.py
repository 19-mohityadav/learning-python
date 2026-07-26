import numpy as np

# Filtering -> Selecting elements from an array that match a given condition

ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65],
                 [39, 22, 15, 99, 18, 19, 20, 21]])

teenagers = ages[ ages < 18]
print(teenagers) # [17 16 15]

adults = ages[ages >= 18 & ages >= 65]
print(adults) # all ages which are greater than = 18

seniors = ages[ages >= 65]
print(seniors)

evens = ages[ages % 2 == 0]
print(evens) # All even ages
odds = ages[ages % 2 == 1]
print(odds)  # all odd ages

adults = np.where(ages >= 18, adults, -1)
print(adults) 

