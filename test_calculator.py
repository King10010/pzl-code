# test_calculator.py
import pytest
from calculator import add, sub, mul, div

# def test_add():
#     assert add(1, 2) == 3
def test_add_numeric_string():
    assert add("1", "2") == 3.0

def test_add_invalid_input():
    import pytest
    with pytest.raises(ValueError):
        add("abc", 1)
def test_sub():
    assert sub(5, 3) == 2

def test_mul():
    assert mul(3, 4) == 12

def test_div():
    assert div(10, 2) == 5

def test_div_zero():
    with pytest.raises(ValueError):
        div(10, 0)
