# Python Temperature Converter

unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C" or unit == "c":
    temp = round(temp * 9 / 5 + 32, 1)
    print(f"{temp} F")
elif unit == "F" or unit == "f":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"{temp} C")
else:
    print("Sorry, please enter C or F")