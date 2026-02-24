import pytest

from cicd_demo.calculator import add, divide, multiply, subtract


def test_add() -> None:
    assert add(2, 3) == 5


def test_subtract() -> None:
    assert subtract(10, 4) == 6


def test_multiply() -> None:
    assert multiply(6, 7) == 42


def test_divide() -> None:
    assert divide(12, 4) == 3


def test_divide_by_zero() -> None:
    with pytest.raises(ValueError):
        divide(1, 0)
