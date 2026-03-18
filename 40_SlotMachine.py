# Python Slot machine

import random

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '⭐', '🔔']

    # results = []
    # for symbol in range(3):
    #     results.append(random.choice(symbols))
    # return results

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("**************")
    print(" | ".join(row))
    print("**************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet*1.2
        elif row[0] == '🍉':
            return bet*3
        elif row[0] == '🍋':
            return bet*1.5
        elif row[0] == '⭐':
            return bet*5
        elif row[0] == '🔔':
            return bet*2
    return 0

def main():
    balance = 100
    print("--------------------------------------------------")
    print("|             Welcome to Slot Machine            |")
    print("|             Symbols: 🍒 🍉 🍋 ⭐ 🔔           |")
    print("--------------------------------------------------")

    while balance > 0:
        print(f"Current balance: ₹{balance}")

        bet = input("Enter your bet: ")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue
        bet = int(bet)

        if bet > balance:
            print("Insufficient Balance")
            continue

        if bet <= 0:
            print("Bet must be greater than Zero")
            continue

        balance -= bet

        row = spin_row()
        print("\nSpinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"\nYou have won ₹{payout}!")
        else:
            print("Sorry, you lost this round!")
            print("Try again!")

        balance += payout

        play_again = input("Do you want to play again? (y/n): ").lower()

        if play_again != 'y':
            break
    print("**************************************")
    print(f"Game Over! Current balance: {balance}")
    print("**************************************")




if __name__ == "__main__":
    main()