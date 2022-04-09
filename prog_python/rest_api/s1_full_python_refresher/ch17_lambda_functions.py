# example 1
def add(x, y):
    return x + y


print(add(3, 2))

# or
add2 = lambda x, y: x + y
print(add2(3, 2))

# example 2
def double(x):
    return x * 2


sequence = [1, 2, 3, 5, 9]
doubled1 = [double(x) for x in sequence]
print(doubled1)
doubled2 = list(map(double, sequence))
print(doubled2)

doubled3 = list(map(lambda x: x * 2, sequence))
print(doubled3)
