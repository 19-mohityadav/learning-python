# @property --> Decorator used to define a method as a property (it can be accessed like an attributes)
#               Benefit--> Add additional logic when read, write or delete attributes
#               Gives you getter, setter and deleter method


class Rectangle:

    def __init__(self, length, breadth):
        self._length = length
        self._breadth = breadth

    @property
    def length(self):
        return f"{self._length :.1f}cm"

    @property
    def breadth(self):
        return f"{self._breadth :.1f}cm"


    @length.setter
    def length(self, new_length):
        if new_length > 0:
            self._length = new_length
        else:
            print("Please enter a positive Length")

    @breadth.setter
    def breadth(self, new_breadth):
        if new_breadth > 0:
            self._breadth = new_breadth
        else:
            print("Please enter a positive Height")

    @length.deleter
    def length(self):
        del self._length
        print("Length is deleted")

    @breadth.deleter
    def breadth(self):
        del self._breadth
        print("Breadth is deleted")


rectangle = Rectangle(100, 200)

rectangle.length = 200
rectangle.breadth = 300


print(rectangle.length)
print(rectangle.breadth)