def is_int(x):
    return isinstance(x, int)


def each2d(test, matrix):
    inner_matrix = (x for x in matrix)
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    return all(test(a) for a in inner_matrix)


def test_01():
    assert each2d(is_int, [
        [1, 2, 3],
        [4, 0, 'BOOM'],  # your code should stop at 0
        [7, 8, 9],
    ]) is False
