# python weight Converter

weight = float(input("Please enter your weight: "))
unit = (input("Please enter your unit (Kilogram or Pounds) --> K or L: "))

if unit == "k" or unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
    print(f"Your weight is {weight} {unit}")
elif unit == "l" or unit == "L":
    weight = weight/2.205
    unit = "Kgs"
    print(f"Your weight is {weight} {unit}")
else:
    print(f"{unit} is not a known unit")

