# if = Do some code only IF some condition is TRUE
#       ELSE do something else

age = int(input("What is your age?: "))

if age >= 100:
    print("You are too Old to sign up!")
elif age >= 18:
    print("You are signed up!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You must be 18+ to sign up!")


response = input("Would you like Food? (y/n): ")
if response == "y":
    print("Welcome to Food!")
    print("Have a good day!")
else:
    print("No Food for You")
    print("Good bye!")


name = input("What is your name?: ")
if name == "":
    print("Name is required Please type the NAME")
else:
    print(f"Hello {name}!")


for_sale = True
if for_sale:
    print("This item is for sale!")
else:
    print("This item is not for sale!")