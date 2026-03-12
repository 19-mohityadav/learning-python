# input() = A Fn that prompts the user to enter data
#            Returns the entered data as string

name = input("What is your name?: ")
age = int(input("What is your age?: "))

# age = int(age)  # needed TC
age = age + 1

print(f"Hello {name}!")
print("HAPPY BIRTHDAY")
print(f"You are {age} years old.")


