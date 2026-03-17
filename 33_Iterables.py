# Iterables --> An object/collection that can return its elements one at a time,
#               allowing it to be iterated over

numbers = [1, 2, 3,4, 5]

# for number in numbers:
#     print(number, end=" ")
#
# print()
#
# for item in numbers:
#     print(item, end=" ")
#
# print()
# for number in reversed(numbers):
#     print(number, end=" ")

numbers2 = (1, 2, 3, 4, 5)

# for number in numbers:
#     print(number, end=" ")

fruits = {"apple", "orange", "pear", "banana"}

for fruit in fruits:
    print(fruit)


name = "Mohit Yadav"

for character in name:
    print(character, end=" ")
print()

my_dictionary = {"A":1, "B":2, "C":3, "D":4}

for key in my_dictionary:
    print(key, end=" ")

print()
for value in my_dictionary.values():
    print(value, end=" ")
print()

for key, value in my_dictionary.items():
    print(f"{key}: {value}")




