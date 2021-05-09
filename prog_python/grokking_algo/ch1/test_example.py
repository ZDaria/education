from education.prog_python.grokking_algo.ch1.example import binary_search
import pytest


def test_list_contains_var():
    my_list = [1, 3, 5, 7, 9]
    assert 1 == binary_search(my_list, 3)


def test_list_wo_var():
    my_list = [1, 3, 5, 7, 9]
    assert binary_search(my_list, -1) is None
