from methode import meine_methode
import pytest

def test_array_empty():
    assert meine_methode([]) == "array empty!"