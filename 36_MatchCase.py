# match-Case statement (switch): An alternative to using many 'elif' statements
#                                Execute some code if a value matches a 'case'
#                                Benefits: cleaner and syntax is more readable

# def day_of_week(day):
#     if day == 0:
#         return "Monday"
#     elif day == 1:
#         return "Tuesday"
#     elif day == 2:
#         return "Wednesday"
#     elif day == 3:
#         return "Thursday"
#     elif day == 4:
#         return "Friday"
#     elif day == 5:
#         return "Saturday"
#     elif day == 6:
#         return "Sunday"
#     else:
#         return "Invalid Day"
# print(day_of_week(5))

def day_of_week(day):
    match day:
        case 1:
            return 'Monday'
        case 2:
            return 'Tuesday'
        case 3:
            return 'Wednesday'
        case 4:
            return 'Thursday'
        case 5:
            return 'Friday'
        case 6:
            return 'Saturday'
        case 7:
            return 'Sunday'
        case _:
            return 'Invalid Day'

print(day_of_week(5))
print(day_of_week(1))
print(day_of_week(7))
print()

def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return False, "Invalid Day"

print(is_weekend("Monday"))