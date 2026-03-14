# While loop = execute some code WHILE some condition remains true

name = input("Enter your name: ")

while name == "":
    print("Please enter a valid name")
    name = input("Enter your name: ")
print(f"Hello {name}")



age = int(input("Enter your age: "))
while age < 0 or age > 100:
    print("Please enter a valid age")
    age = int(input("Enter your age: "))

print(f"You  are {age} years old")


food = input("Enter a food you like (q to quit): ")
while not food == "q" or food == "Q":
    print(f"You  like: {food}")
    food = input("Enter a food you like (q to quit): ")

print("bye")


num = int(input("Enter a number between 1 and 10: "))

while num < 1 or num > 10:
    print(f"{num} is not between 1 and 10")
    num = int(input("Enter a number between 1 and 10: "))
print(f"GOOD! You  entered: {num}")


print("###############################")
# Compound Interest Calculator


principle = float(input("Enter principle: "))
while principle <= 0:
    print("Principle cannot be negative or zero")
    principle = float(input("Enter principle: "))

rate = float(input("Enter rate: "))
while rate <= 0:
    print("Rate cannot be negative or zero")
    rate = float(input("Enter rate: "))

time = int(input("Enter time: "))
while time <= 0:
    print("Time cannot be negative or zero")
    time = float(input("Enter time: "))

total = principle * pow((1+rate/100), time)
print(f"Balance after {time} year/s: ${total:,.2f}")


