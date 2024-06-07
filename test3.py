from methode import meine_methode
import pytest

array = [1,2,3,4,5,6]

def test_array_even():
    assert meine_methode(array) == "array length even!"