import pytest
from Testing.basic4 import add_sub_div_mul


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        add_sub_div_mul(10, 0, '/')


def test_unsupported_operation():
    with pytest.raises(ValueError):
        add_sub_div_mul(10, 5, '%')


def test_add():
    assert add_sub_div_mul(2, 3, '+') == 5


def test_subtract():
    assert add_sub_div_mul(5, 2, '-') == 3


def test_divide():
    assert add_sub_div_mul(6, 2, '/') == 3


def test_multiply():
    assert add_sub_div_mul(3, 4, '*') == 12
