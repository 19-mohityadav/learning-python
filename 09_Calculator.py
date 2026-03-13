# Basic Python Calculator

operator = input("Please enter your operator (+ - * /): ")
num1 = float(input("Please enter your first number: "))
num2 = float(input("Please enter your second number: "))

if operator == "+":
    print(round(num1 + num2))
elif operator == "-":
    print(round(num1 - num2))
elif operator == "*":
    print(round(num1 * num2))
elif operator == "/":
    print(round(num1 / num2))
else:
    print("Please enter a valid operator")

