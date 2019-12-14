"""Home work after ch. 1"""


def test_in_fail():
    assert 1 in [2, 3, 4]


def test_in_pass():
    assert 1 in [2, 3, 1]


def test_less_than_pass():
    a = 5
    b = 6
    assert a < b


def test_st_in_str_fail():
    assert 'fizz' not in 'fizzbuzz'
