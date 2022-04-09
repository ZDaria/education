from typing import List


def list_avg(sequence: List) -> float:
    return sum(sequence)/len(sequence)


list_avg(1234) # Expected type 'list', got 'int' instead
