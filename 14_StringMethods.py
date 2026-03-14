# len(str) --> length of the string
# str.find("x") --> 1st occurrence's index
# str.rfind("x") --> last occurrence's index (if not -1 ans)
# str.capitalize() --> 1s Letter is Capi..
# str.upper() --> str will be in Upper case
# str.lower() --> str will be in lower case
# str.isdigit() --> If str only contains digits
# str.isalpha() --> If str only contains alphabet
# str.count("x") -->  count the no. of characters
# str.replace("x", "y") --> Replaces x with y


name = input("Enter your name: ")
result = len(name)
print(result)
result = name.find("o")
print(result)


phone_number = input("Enter your phone number: ")
result = phone_number.count("-")
print(result)
result = phone_number.replace("-", "")
print(result)


##########################################################################

# Qs1. Validate user input exercise
# -> username is no more than 12 characters
# -> username must not contain spaces
# -> username must not contain digits

user_name = input("Enter your name: ")



if len(user_name) > 12:
    print("Your name cannot exceed 12 characters")
elif not user_name.find(" ") == -1:
    print("Your name cannot contain spaces")
elif not user_name.isalpha():
    print("Your name cannot contain numbers")
else:
    print(f"Welcome {user_name}")
