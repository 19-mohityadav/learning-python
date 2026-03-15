# Menu Card

menu = {
    "Pizza": 299,
    "nachos": 50,
    "popcorn": 150,
    "bread-jam": 80,
    "fries": 70,
    "chicken": 499,
    "soda": 90,
    "lemon": 50,
    "milk": 70
}

cart = []
total = 0

print("--------------MENU----------------")
print()
for key, value in menu.items():
    print(f"{key:15}:    ₹{value:.2f}")
print("----------------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print()
print("-------------YOUR ORDER----------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")
print()
print("--------------------------------")
print()

print("TOTAL: ₹", total)