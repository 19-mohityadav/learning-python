# Super() --> Function used in a child class (subclass) to call methods from a parent class (superClass).
#             Allows you to extend the Functionality of the inherited methods

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")


class Circle(Shape):
    def __init__(self,color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self): #method overriding
        print(f"It is Circle and area is {self.radius * self.radius}")
        super().describe()


class Square(Shape):
    def __init__(self, color, is_filled, side):
        super().__init__(color, is_filled)
        self.side = side

class Triangle(Shape):
    def __init__(self, color, is_filled, base, height):
        super().__init__(color, is_filled)
        self.base = base
        self.height = height


circle = Circle("red", True, 5)
square = Square("blue", True, 5)
triangle = Triangle("green", True, 5, 10)

# print(circle.color)
# print(square.is_filled)
# print(triangle.base)
print(circle.describe())