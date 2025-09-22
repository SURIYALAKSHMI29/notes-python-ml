"""

Question:
Test twttr.py using pytest

"""

import sys
from pathlib import Path

# add project root to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from week_2.twttr import shorten


def test_lower_case():
    assert shorten("hello") == "hll", "hello is not returned as hll"
    assert shorten("suriya") == "sry", "suriya is not returned as sry"


def test_upper_case():
    assert shorten("HELLO") == "HLL", "HELLO is not returned as HLL"
    assert shorten("SURIYA") == "SRY", "SURIYA is not returned as SRY"


def test_combined_case():
    assert shorten("hellO") == "hll", "hellO is not returned as hll"
    assert shorten("SuriyA") == "Sry", "SuriyA is not returned as Sry"
