"""

Question:
Test fuel.p by using pytest

"""

import pytest
from fuel import convert, gauge


def test_convert_basic():
    assert convert("1/2") == 50
    assert convert("0/10") == 0
    assert convert("10/10") == 100


def test_convert_rounding():
    assert convert("1/3") == 33
    assert convert("2/3") == 67


def test_convert_value_error():
    with pytest.raises(ValueError):
        convert("5/2")  # X > Y
    with pytest.raises(ValueError):
        convert("a/2")  # X not int
    with pytest.raises(ValueError):
        convert("2/b")  # Y not int
    with pytest.raises(ValueError):
        convert("-1/5")  # X negative
    with pytest.raises(ValueError):
        convert("1/-5")  # Y negative


def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge_empty_and_full():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_gauge_normal():
    assert gauge(50) == "50%"
    assert gauge(33) == "33%"
    assert gauge(67) == "67%"
