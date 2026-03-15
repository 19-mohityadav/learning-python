# collection --> Single "variable" used to store multiple values
#       LIST --> [] ordered and changeable (using index we can assign the val). Duplicates OK
#       SET --> {} unordered and immutable, but Add/Remove OK. No duplicates
#       TUPLE --> () ordered and unchangeable. Duplicates OK. FASTER
#  ......
#  dir(collection)
#  help(collection)

fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[0])
print(fruits[-1])
print(fruits[0:3:2]) #returns new list
print(fruits[0:])

for fruit in fruits:
    print(fruit, end=" ")

print(len(fruits))
# print(dir(fruits))
# print(help(fruits))
fruits.append("pineapple") # Add at last
print(fruits)
fruits.remove("apple")
print(fruits)
fruits.insert(0, "orange")
print(fruits)

print("orange" in fruits)

fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)

fruits2 = {"apple", "banana", "cherry"}
print(dir(fruits2))
print(fruits2)
fruits2.add("orange")
print(fruits2)
fruits2.remove("orange")


fruits3 = ("apple", "banana", "cherry")
print(dir(fruits3))
print(fruits3)