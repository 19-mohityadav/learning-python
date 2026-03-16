import random

options = ["rock", "paper", "scissors"]

playing = True

while playing:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter your choice (rock, paper, or scissors): ")

    print(f"You: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("Draw")
    elif player == "rock" and computer == "scissors":
        print("You win")
    elif player == "paper" and computer == "rock":
        print("You win")
    elif player == "scissors" and computer == "paper":
        print("You win")
    else:
        print("You lose")

    play_again = input("Do you want to play again? (y/n): ").lower()
    if not play_again == "y":
        playing = False

print("Thank you for playing yadav ji")




