# 2D List = [list1, list2, list3]

# fruits =     ["apple", "banana", "cherry"]
# vegetables = ["potatoes", "carrots", "onions"]
# meats =      ["chicken", "fish", "turkey"]

# groceries = [fruits, vegetables, meats]

groceries = [
    ["apple", "banana", "cherry"],
    ["potatoes", "carrots", "onions"],
    ["chicken", "fish", "turkey"]
]


print(groceries[0][0]) # apple
print(groceries[1][1]) # carrots
print(groceries[2][2]) # turkey

for collection in groceries:
    for item in collection:
        print(item, end=" ")
    print()


print("########################################")

num_pad = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()
