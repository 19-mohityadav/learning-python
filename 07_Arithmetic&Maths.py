

friends = 10
# friends = friends + 1
friends += 1  #Augmented Assignment Operator
# friends = friends - 1
friends -= 1
# friends = friends * 3
friends *= 3
# friends = friends / 2
friends /= 2
# friends = friends ** 2 #Exponentiantion Ops
friends **= 2
remainder = friends % 3  #Modulus Ops
print(friends)

x = 3.14
y = 4
z = 5

result = round(x) # round() --> it round of the given value
print(result)

result = abs(y)  #abs() --> Gives the absolute value
print(result)

result = pow(z, 2) #pow(base, expo)
print(result)

result = max(x, y,z) #max() --> maximum value

################################################################################

import math

x1 = 3.4
print(math.pi)
print(math.e)
result2 = math.sqrt(x1)
print(result2)
result2 = math.pow(x1, 2)
print(result2)

result2 = math.ceil(x1)  # round a no. UP
print(result2)
result2 = math.floor(x1) # round a no. DOWN
print(result2)

# 1 Calculate Circumference of a Circle

radius = float(input("Enter a radius of a circle: "))
cicumference = 2 * math.pi * radius
print(f"The circumference of the circle is {round(cicumference, 2)}")


# 2 Calculate Area of the circle

area = math.pi * pow(radius, 2)
print(f"The area of the circle is {round(area, 2)} cm²")

# Find Hypotenuse of Triangle

length_of_a = float(input("Enter a length of SIDE A: "))
length_of_b = float(input("Enter a length of SIDE B: "))
length_of_c = math.sqrt(pow(length_of_a, 2) + pow(length_of_b, 2))

print(f"Length of Hypotenuse of {length_of_a} and {length_of_b} is {length_of_c}")