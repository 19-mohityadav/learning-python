
# This is my first python program

# print("I love coding")
# print("It is really good")
# print("I am a good Coder")

# Variable = A container for a value (string, integer, float, boolean)
#            A variable behaves as if it was the value it contains

a = 10          # int
b = 2.5         # float
c = "Python"    # string
d = True        # boolean
print(type(a))  #Check Type

# Dynamic Typing(Allowed) --> Same var, different value/type
x = 10
print(x)
x = "Ten"
print(x)

# 🧾 Variable Naming Rules
#
# ✔ Must start with letter or _
# ✔ Can contain letters, numbers, _
# ❌ Cannot start with number
# ❌ No spaces
# ❌ No keywords

# Valid:
user_name = "Alex"
_age = 25
total2 = 100

# Variables with User Input--> input() always returns string
name_input = input("Enter your name: ")
age_input = int(input("Enter your age: "))
print(name_input)
print(age_input)

# Constant Variables --> Python has no real constants, but we use UPPERCASE.
PI = 3.14159
MAX_USERS = 100

####################################################################3

# Strings --> A series of character
first_name = "Mohit"
food = "Doodh"
email = "mohit123@fake.com"

# print(f"Hello {first_name}!")
# print(f"You like {food}!")
# print(f"Your email is: {email}")

# Integers
age = 20
quantity = 4
num_of_students = 30

# print(f"You are {age} years old.")
# print(f"You are buying {quantity} items")
# print(f"You have {num_of_students} students")

# Float
price = 10.99
gpa = 9.07
run_dist = 4

# print(f"The price is: ${price}")
# print(f"Your GPA is: ${gpa}")
# print(f"You ran {run_dist}KM")

# Boolean
is_student = True

# print(f"Are you a student?: {is_student}")
if is_student:
    print("You are a Student")
else:
    print("You are NOT a Student")

for_sale = False

if for_sale:
    print("That item is for sale")
else:
    print("That item is not for sale")

# 📌 Summary
# Variables store data
# Python decides the type automatically
# Use clear, readable names
# Values can change anytime