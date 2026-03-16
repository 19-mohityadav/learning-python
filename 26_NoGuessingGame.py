# import random
# # print(help(random))
#
# low = 1
# high = 100
#
# number = random.randint(low,high)
# print(number)
#
# floatNumber = random.random()
# print(floatNumber)
#
# options = ("rock", "paper", "scissors")
# option = random.choice(options)
# print(option)
#
# cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
# random.shuffle(cards)
# print(cards)


print("#######################################")
import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = (input("Guess a number: "))
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("That number is out of range!")
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low! Try again")
        elif guess > answer:
            print("Too high! Try again")
        else:
            print("You guessed correctly! answer: ", answer)
            print(f"Number of guesses: {guesses}")
            is_running = False
    else:
        print("Invalid Guess")
        print(f"Please select a number between {lowest_num} and {highest_num}")


