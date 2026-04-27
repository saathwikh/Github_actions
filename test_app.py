import pytest
from app import add, divide, average


def test_add():
    assert add(2, 3) == 5


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


def test_average():
    assert average([1, 2, 3, 4]) == 2.5


def test_average_empty():
    with pytest.raises(ValueError):
        average([])