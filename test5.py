from methode import meine_methode
import pytest

def test_array_negative_numbers():
    assert meine_methode([-69, -69, -3, -8, -3, -25, -25]) == -8