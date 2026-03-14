# format specifiers = {value : flags} format a value based on what
#                                       flags are inserted

# .(number)f => round to that many decimal places (fixed point)
# :(number) => allocate that many spaces
# :03 => allocate and zero pad that many spaces
# :<  => left justify
# :>  => right justify
# :^  => center align
# :+  => use a plus sign to indicate positive value
# :=  => place sign to leftmost position
# :1space   => Insert a space before positive numbers
# :,  => Comma separator


price1 = 3.14159
price2 = -9874678.65
price3 = 12.34

# .(number)f
print(f"Price 1 is ${price1 : .2f}")
print(f"Price 2 is ${price2 : .1f}")
print(f"Price 3 is ${price3 : .3f}")

print("####################")
# : (number)
print(f"Price 1 is ${price1 : 14}")
print(f"Price 2 is ${price2 : 10}")
print(f"Price 3 is ${price3 : 8}")

print("####################")
# : (0number)
print(f"Price 1 is ${price1 : 014}")
print(f"Price 2 is ${price2 : 010}")
print(f"Price 3 is ${price3 : 08}")

print("####################")

# : (<number)
print(f"Price 1 is ${price1 : <14}")
print(f"Price 2 is ${price2 : <10}")
print(f"Price 3 is ${price3 : <8}")


print("####################")
# : (>number)
print(f"Price 1 is ${price1 : >14}")
print(f"Price 2 is ${price2 : >10}")
print(f"Price 3 is ${price3 : >8}")


print("####################")
# : (^number)
print(f"Price 1 is ${price1 : ^10}")
print(f"Price 2 is ${price2 : ^10}")
print(f"Price 3 is ${price3 : ^10}")

print("####################")
# :+
print(f"Price 1 is ${price1 :+}")
print(f"Price 2 is ${price2 :+}")
print(f"Price 3 is ${price3 :+}")

print("####################")
# :space
print(f"Price 1 is ${price1 : }")
print(f"Price 2 is ${price2 : }")
print(f"Price 3 is ${price3 : }")


print("####################")
# :,
print(f"Price 2 is ${price2 :,}")


print("####################")
# :,
print(f"Price 2 is ${price2 :+,.1f}")