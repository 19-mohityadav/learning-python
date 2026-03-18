# Python Banking Program

def show_balance(balance):
    print(f"Your balance is ₹{balance:.2f}")

def deposit():
    amount = float(input("Enter amount to deposit: "))

    if amount < 0:
        print("Please enter a positive amount")
        return 0
    else:
        return amount


def withdraw(balance):
    if balance == 0:
        show_balance()
        print("Deposit First!")
        return 0
    amount = float(input("Enter amount to withdraw: "))
    if amount < 0:
        print("Please enter a positive amount")
        return 0
    elif amount > balance:
        print("Insufficient balance")
        return 0
    else:
        return amount


def main():

    balance = 0
    is_running = True

    while is_running:
        print("-----------------------------------------")
        print("         Welcome to Python's Bank        ")
        print("-----------------------------------------")
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = (input("Enter your choice (1-4): "))
        print("-----------------------------------------")
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("Please enter a valid choice")

    print("-----------------------------------------")
    print("-----------------------------------------")

    print("     Thank you for using Python's Bank   ")
    print("             Have a nice day!            ")

    print("-----------------------------------------")
    print("-----------------------------------------")
    print("-----------------------------------------")


if __name__ == '__main__':
    main()