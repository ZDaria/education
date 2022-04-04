# examle 1

def named(**kwargs):
    print(kwargs)


named(name="Bob", age=25)

# example 2


def named2(name, age):
    print(name, age)


details = {'name': 'Bob', 'age': 25}
named2(**details)

# example 3


def print_nicely(**kwargs):
    named(**kwargs)
    for arge, values in kwargs.items():
        print(f"{arge}: {values}")


print_nicely(name="Bob", age=25)

# example 4


def both(*args, **kwargs):
    print(args)
    print(kwargs)


both(1, 2, 5, name="Bob", age=25)

# example 5


def myfunction(**kwargs):
    print(kwargs)


myfunction(**"Bob")  # Error, mast by mapping
myfunction(**None)  # Error
