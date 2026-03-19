# Duck Typing --> Another way to achieve polymorphism besides inheritance
#                 Object must have the minimum necessary attributes/methods
#                  "If it looks like a duck and quacks like a duck, It must be a duck."

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("I am dog. and I BARK")

class Cat(Animal):
    def speak(self):
        print("I am cat. and I MEOW")

class Car:
    alive = False

    def speak(self):
        print("PEEE PEEE")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)

