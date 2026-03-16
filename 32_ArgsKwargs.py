############## Arbitrary Arguments #######################
# *args --> allows you to pass multiple non-key arguments
# **kwargs --> allows you to pass multiple keyword-arguments
#              * unpacking operator

# *args --> It is tuple we can iterate over it
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(5,5,3,4,1))


def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Mr.","Mohit", "Yadav", "1st", "Eng..")
print()


# **kwargs --> Dictionary --> type(kwargs)
def print_address(**kwargs):
    print("My Address: ", end="\n")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_address(street="New Road",
              city="Asansol",
              state="West Bengal",
              zip_code="123459",
              country="India"
              )

print()
print()


def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    print("MY SHIPPING LABEL: ", end=" ")

    # for key, value in kwargs.items():
    #     print(f"{key}: {value}")

    # print(f"{kwargs['apt']} {kwargs['street']} {kwargs['city']} {kwargs['state']} {kwargs['zip_code']}")

    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip_code')}")

shipping_label("Dr.", "Mohit", "Yadav", "1st", "Eng..",
               apt = "#100",
               street="New Road",
               city="Asansol",
               state="West Bengal",
               zip_code="123459",
               country="India"
               )

