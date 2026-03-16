# keyword argument --> an argument preceded by an identifier
#                       helps with readability
#                       order of arguments doesn't matter

def hello(greeting, title, first_name, last_name):
    print(f"{greeting} {title} {first_name} {last_name}")
    print()

hello("Hello", title="Mr.", last_name="Yadav", first_name="Mohit")

for x in range(1, 11):
    print(x, end=" ")  # end = .... keyword args

print()
print("1", "2", "3", "4", "5", "6", "7", "8", "9", sep="-")


def get_phone_number(country_code, first_digit, last_digit):
    return f"{country_code} {first_digit} {last_digit}"

phone_number = get_phone_number(country_code="+91", first_digit="12345", last_digit="67891")
print(phone_number)


