# example 1

def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total *= arg
    return total


print(multiply(1, 3, 5))

# example 2


def add(x, y):
    return x + y


nums = [3, 5]
print(add(*nums))
nums2 = {'x': 3, 'y': 5}
print(add(**nums2))


# example 3

def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator to apply()."


print(apply(1, 3, 6, 7, operator="*"))
