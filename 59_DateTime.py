# Date & Time in Python

import datetime

date = datetime.date(2026, 2, 9)

print(f"Date: {date}")

today = datetime.date.today()
print(f"Today's Date: {today}")

print()

time = datetime.time(12, 30, 0)
print(f"Time: {time}")

now = datetime.datetime.now()
print(f"Now: {now}")

now = now.strftime("%H:%M:%S %d/%m/%Y")


print(f"Now: Time & Date = {now} ")



print()
print()

target_datetime = datetime.datetime(2026, 2, 9, 12, 30)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target Date Has Passed")
else:
    print("Target Date Has Not passed")

