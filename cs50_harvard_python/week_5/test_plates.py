"""

Question:
Test plates.py from week_2 using pytest

"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from week_2.plates import is_valid


def test_starts_with_alpha():
    assert is_valid("W36789") == False, "W36789 should return False"
    assert is_valid("WE6789") == True, "WE6789 should return True"


def test_char_count():
    assert is_valid("W6789") == False, "W6789 should return False"
    assert is_valid("WE72189") == False, "WE72189 should return False"
    assert is_valid("WE6789") == True, "WE6789 should return True"


def test_not_starts_with_zero():
    assert is_valid("WM06789") == False, "WM06789 should return False"
    assert is_valid("WERHL0") == False, "WERHL0 should return False"
    assert is_valid("WERHL1") == True, "WE6789 should return True"


def test_ends_with_digits():
    assert is_valid("WM0678E") == False, "WM0678E should return False"
    assert is_valid("WET87V") == False, "WET87V should return False"
    assert is_valid("WERHL1") == True, "WERHL1 should return True"
