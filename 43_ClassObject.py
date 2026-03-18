# Object --> A "bundle" of related attributes (variables) and methods (functions)
#           Ex. phone, cup, book
#           You need a "class" to create many objects

# class --> (blueprint) used to design the structure and layout of an object
# constructor --> special Fn used to initialise the value
# dunder --> __ (double underscore)
# Methods --> are actions which objects perform

class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"You stop the {self.color} {self.model}")

    def describe(self):
        print(f"{self.color} {self.model} of {self.year}")

car1 = Car("Mustang", 2026, "Red", False)
# print(car1) # Address
# print(car1.model)
# print(car1.year)
# print(car1.color)

car2 = Car("Thar", 2026, "Black", True)
# print(car2.model)
# print(car2.year)
# print(car2.color)

car1.drive()
car1.describe()
car1.stop()
car2.drive()


