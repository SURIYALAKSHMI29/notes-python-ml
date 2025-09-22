"""

Question:
Test bank.py from week 1 using pytest

"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))


from week_1.bank import dollars_earned


def test_starts_with_hello():
    assert dollars_earned("HELLO") == 0, "HELLO should return 0 dollars"
    assert dollars_earned("hello") == 0, "hello should return 0 dollars"
    assert dollars_earned("HeLLo") == 0, "HeLLo should return 0 dollars"


def test_starts_with_h():
    assert dollars_earned("hiii") == 20, "hiii should return 20 dollars"
    assert dollars_earned("HIII") == 20, "HIII should return 20 dollars"
    assert dollars_earned("hEY") == 20, "hEY should return 20 dollars"


def test_others():
    assert dollars_earned("vanakam") == 100, "vanakam should return 100 dollars"
    assert dollars_earned("VANAKAM") == 100, "VANAKAM should return 100 dollars"
    assert dollars_earned("Vanakam") == 100, "Vanakam should return 100 dollars"
