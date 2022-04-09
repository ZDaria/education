def divide(divided, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor can not be 0!")
    return divided/divisor


students = [{"name": "Bob", "grades": [75, 91]},
            {"name": "Rolf", "grades": []},
            {"name": "Jen", "grades": [75, 91]}]

try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divide(sum(grades), len(grades))
        print(f"{name} averaged {average}.")
except ZeroDivisionError as e:
    print(f"ERROR: {name} has no grades!")
else:
    print("-- All student averages calculated --")
finally:
    print("-- End of student average calculation --")
