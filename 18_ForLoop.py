# for loop = execute a block of code a fixed number of times.
#             You can iterate over a range, string, sequence, etc.

for x in range(1,11,3):
    print(x)
print("Happy New Year")

credit_card = "1234-5678-1234-5678"
for x in credit_card:
    print(x)


for x in range(1, 21):
    if x == 13:
        continue  #break will break the loop
    else:
        print(x)

print("#########################################COUNTDOWN TIMER####################################")

import time

my_time = int(input("Enter the amount of time in seconds: "))

# for x in reversed(range(0, my_time)):
for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("TIME'S UP")
