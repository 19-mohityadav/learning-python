# Exception --> An event that interrupts the flow of a program
#               (ZeroDivisionError, TypeError, ValueError)
#               1. try , 2. except, 3. finally

# Ex.. --> 1/0 , 1 + "1" , int(pizza)

try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("Division by zero is Not Possible BOKA!")
except ValueError:
    print("Enter only numbers Please!")
except Exception:
    print("Something went wrong!")
finally:
    print("\nClean the terminal!")





