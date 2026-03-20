# Decorator --> A Fn that extends the behaviour of another Fn
#               w/o modifying the base function
#               pass the base function as an argument to the decorator

#               @add_sprinkles
#               get_ice_cream("vanilla")


def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("*You added sprinkles")
        func(*args, **kwargs) #base Fn
    return wrapper


def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("*You added Chocolate")
        func(*args, **kwargs)
    return wrapper


@add_sprinkles
@add_fudge
def get_ice_cream(flavour):
    print(f"Here is your {flavour}Ice cream")

get_ice_cream("Vanilla")
get_ice_cream("Chocolate")