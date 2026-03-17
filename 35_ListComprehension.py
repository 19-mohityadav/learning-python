# List Comprehension --> A concise way to create lists in Python
#                        Compact and easier to read than traditional loops
#                        [expression for value in iterable if condition]

# doubles = []
# for x in range(1, 11):
#     doubles.append(x*2)
#
# print(doubles)



doubles = [x*2 for x in range(1,11)]
print(doubles)

triples = [x*3 for x in range(1,11)]
print(triples)

squares = [pow(x,2) for x in range(1,11) if x >= 0]
print(squares)


fruits = ["apple", "banana", "cherry"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)


numbers = [1,-2,3,-4,-5]
positive_numbers = [num for num in numbers if num >= 0]
negative_numbers = [num for num in numbers if num < 0]
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 == 1]

print(positive_numbers)
print(negative_numbers)
print(even_numbers)
print(odd_numbers)


marks = [85, 99, 68, 87, 95, 32]
passing_grades = [num for num in marks if num >= 33]
print(passing_grades)
