# Membership operator --> used to test whether a value or variable is found in a sequence
#                         (string, list, tuple, set or dictionary
#                          1. in & 2. not in

word = "APPLE"

# letter = input("Guess a letter in the secret word: ")
#
# if letter in word:
#     print(f"There is a {letter} in the secret word")
# else:
#     print(f"{letter} not found!")
#
#
# if letter not in word:
#     print(f"{letter} not found!")
# else:
#     print(f"There is a {letter} in the secret word")




students = {"Mohit", "Rohit", "Piyush"}

# student = input("Enter student name: ")
#
# if student in students:
#     print(f"{student} is a Student")
# else:
#     print(f"{student} is not a Student")
#
# if student not in students:
#     print(f"{student} is not a Student")
# else:
#     print(f"{student} is a Student")




marks = {
    "Math": 80,
    "English": 70,
    "Science": 60,
    "Geography": 90,
    "History": 70
}

# subject = input("Please enter your subject: ")
#
# if subject in marks:
#     print(f"{subject} has a marks {marks[subject]}")
# else:
#     print(f"{subject} has no marks")


email = "mohit@gmail.com"

if "@" in email and "." in email:
    print("Email address is valid")
else:
    print("Email address is invalid")
    
