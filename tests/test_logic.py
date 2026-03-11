import pytest
from unittest.mock import patch
from validation import validation_float

def test_validation_float_ok():
    # We simulate that the user has typed "100.5"
    with patch('builtins.input', side_effect=["100.5", "q"]):
        assert validation_float("Zadej částku: ") == 100.5

def test_validation_float_comma():
    # We simulate the entry with a comma "50.2"
    with patch('builtins.input', return_value="50,2"):
        # If your function returns a float, the test passes.
        assert validation_float("Zadej částku: ") == 50.2

def test_validation_float_quit():
    # We simulate that the user wants to end with the letter "q"
    with patch('builtins.input', side_effect=["q"]):
        assert validation_float("Zadej částku: ") is None