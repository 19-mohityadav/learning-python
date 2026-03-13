# Conditional expression = A one line shortcut for the if-else statement (ternary operator)
#                          Print/Assign one of two value based on a condition (true --> first, false --> second)
#                          x if condition_true else y

num = 6

print("Positive" if num > 0 else "Negative")

result = "Even" if num % 2 == 0 else "Odd"
print(result)

a = 6
b = 7
max_num = a if a > b else b
min_num = a if a < b else b

print(f"Maximum of {a} and {b} is {max_num}")
print(f"Minimum of {a} and {b} is {min_num}")



age = 25
status = "Adult" if age >= 18 else "Minor"
print(f"Status of {age} is {status}")

user_role = "admin"
access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(access_level)