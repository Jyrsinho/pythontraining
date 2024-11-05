import pytest

def testShouldReturnZeroForArrayWithUnEvenValuesAndTwo():
    testnumbers = {1,3,5,7}
    expected = 0
    result = dividedBy(testnumbers, 2)
    assert expected == result