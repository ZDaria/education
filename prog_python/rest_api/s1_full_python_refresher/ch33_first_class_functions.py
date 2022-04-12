# example 1
def divide(divided, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor can not be 0.")
    return divided/divisor


def calculate(*values, operator):
    return operator(*values)


result = calculate(20, 4, operator=divide)
print(result)

# example 2
from operator import itemgetter


def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find the element with {expected}.")


friends = [
    {"name": "Tom", "age": 24},
    {"name": "Mary", "age": 30},
    {"name": "Allis", "age": 27}
]


def get_friend_name(friend):
    return friend["name"]


print(search(friends, "Mary", get_friend_name))
print(search(friends, "Tom", lambda friend: friend["name"]))
print(search(friends, "Allis", itemgetter("name")))
