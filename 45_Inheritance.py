# Inheritance --> Allows a class to inherit attributes and methods from another class
#                 Helps with code reusability and extensibility
#                 class Child(Parent)


class Animal:

    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} eating")

    def sleep(self):
        print(f"{self.name} sleeping")

class Dog(Animal):
    def speak(self):
        print("BARK")


class Cat(Animal):
    def speak(self):
        print("MEOW")


class Mouse(Animal):
    pass


class Student(Animal):
    pass

dog = Dog("Kutta")
cat = Cat("Kitti")
mouse = Mouse("Chuha")

print(dog.name)
print(dog.is_alive)
print(cat.name)
print(cat.eat())
dog.sleep()
cat.speak()
mouse.eat()

