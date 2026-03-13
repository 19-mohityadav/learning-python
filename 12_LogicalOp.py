# logical operators = evaluate multiple conditions (or, and, not)
#                      or = at least one condition must be true
#                      and = both conditions must be true
#                      not = inverts the condition (not False, not True)

temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")



temp2 = 25
is_sunny = True

if temp2 >= 28 and is_sunny:
    print("It is HOT outside 🥵")
    print("It is SUNNY")
elif temp2 <= 0 and is_sunny:
    print("It is cold Outside")
    print("It is SUNNY")
elif 28 > temp2 > 0 and is_sunny:
    print("It is Warm Outside")
    print("It is SUNNY")
elif temp2 >= 28 and not is_sunny:
    print("It is HOT outside")
    print("It is CLOUDY")
elif temp2 <= 0 and not is_sunny:
    print("It is cold Outside")
    print("It is CLOUDY")
elif 28 > temp2 > 0 and not is_sunny:
    print("It is Warm Outside")
    print("It is CLOUDY")




