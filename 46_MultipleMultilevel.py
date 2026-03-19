# Multiple inheritance --> Inherit from more than one parent class
#                          C(A, B)

# Multilevel inheritance --> Inherit from a parent which inherits from another parent
#                            C(B) <-- B(A) <-- A

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is Eating")

    def sleep(self):
        print(f"{self.name} Sleeping")




class Prey(Animal):
    def flee(self):
        print("This Animal is fleeing")

class Predator(Animal):
    def hunt(self):
        print("This Animal is hunting")


class Rabbit(Prey):
    pass

class Fox(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bugo")
fox = Fox("Lomri")
fish = Fish("Machli")

rabbit.flee()
fox.hunt()
fish.flee()
fish.hunt()
rabbit.sleep()
print(rabbit.name)