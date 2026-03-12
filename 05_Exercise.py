# 1 Calculate area of Rectangle

length_rectangle = float(input("What is your length of rectangle (in cm)?: ")) #TC because of arithmetic ops
breadth_rectangle = float(input("What is your breadth rectangle?: "))
area = length_rectangle * breadth_rectangle
print(f"Area of rectangle is {area} cm²")

# 2 Shopping Cart Program

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("What is the quantity?: "))
total_price = price * quantity
print(f"You have bought {quantity} x {item}/s")
print(f"Your total price is {total_price}")
