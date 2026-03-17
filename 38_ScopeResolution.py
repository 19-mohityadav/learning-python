# Variable Scope --> Where a variable is visible and accessible
# scope resolution --> (LEGB) Local -> Enclosed -> Global -> Built-in


# Variable Scope
# def func1():
#     a =1
#     print(a) # print(b) --> Name error
#
# def func2():
#     b = 5
#     print(b) # print(a) --> Name error
#
# func1()
# func2()

def func1():
    x = 1

    def func2():
        # x = 5
        print(x)
    func2()

x = 3 # Global
func1()


print("##############################################################")

# if __name__ == __main__: (this script can be imported OR run standalone)
# Function and classes in this module can be reused without the main block of code executing
# Good practice (code is modular,
#                Helps readability,
#                leaves no global variables,
#                Avoid unintended execution

#                Ex.. library = import library for functionality
#                     When running library directly, display a help page
