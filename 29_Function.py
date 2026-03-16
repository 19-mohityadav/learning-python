# Function --> A block of reusable code
#              place() after the function name to invoke it
# Position of parameter and arguments matters



def happy_birthday(name, age):
    print(f"Happy Birthday {name}")
    print(f"You are {age} years old")
    print()

happy_birthday("Mohit", 20)
happy_birthday("Bob", 13)
happy_birthday("Mohit", 20)


def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ₹{amount} is due: {due_date}")
    print()

display_invoice("Mohit", 20, "08/02/2026")
display_invoice("Bob", 13, "08/02/2026")


# return --> statement used to end a Fn
#             & send a result back to the caller

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print(add(10, 20))
print(subtract(10, 20))


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return f"{first} {last}"  # first + " " + last

full_name = create_name("Mohit", "Yadav")
print(full_name)