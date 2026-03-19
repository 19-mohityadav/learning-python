# Static Method --> A method that belong to a class rather than any object from that class(instance)
#                   Usually used for general utility Fns

# Instance Methods --> Best for operations on instance of the class (objects)
# Static Methods --> Best for utility functions that do not need access to class data

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name}: {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_position = ["Manager", "Cashier", "Cook", "Cook", "Developer"]
        return position in valid_position


employee1 = Employee("Mohit", "Manager")
employee2 = Employee("Mohit Yadav", "Developer")


print(employee1.get_info())
print(employee2.get_info())

print(Employee.is_valid_position("Manager"))