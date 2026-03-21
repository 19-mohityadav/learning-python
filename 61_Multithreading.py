# multithreading --> Used to perform multiple tasks concurrently (multitasking)
#                    Good for I/O bound tasks like reading files or fetching data from APIs
#                    threading.Tread(target= my_function)

import threading
import time

def walk_dog(first):
    time.sleep(8)
    print(f"You Finished walking the {first} dog")

def take_picture():
    time.sleep(4)
    print("You clicked the Photos")

def take_screenshot():
    time.sleep(2)
    print("You took the SS")

# walk_dog()
# take_picture()
# take_screenshot()
# print("All Chores are completed!")


chore1 = threading.Thread(target=walk_dog, args=("Kutta",)) # Comma is Important
chore1.start()

chore2 = threading.Thread(target=take_picture)
chore2.start()

chore3 = threading.Thread(target=take_screenshot)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All Chores are completed!")