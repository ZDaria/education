import pytest


def test_delete_last_elem():
    lifo = []
    lifo.append('one')
    lifo.append('two')

    assert lifo.pop() == 'two'


def test_delete_2_last_elem():
    lifo = []
    lifo.append('one')
    lifo.append('two')

    lifo.pop()
    assert lifo.pop() == 'one'


def test_emptiness():

    stack = []
    assert not stack

    stack.append('one')
    assert bool(stack)

    stack.pop()
    assert not stack


def test_pop_with_empty_stack():
    stack = []
    with pytest.raises(IndexError):
        stack.pop()
