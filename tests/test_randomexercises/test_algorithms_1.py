import pytest

from source.random_exercises.algorithms_1 import divided_by


def testShouldReturnZeroForArrayWithUnEvenValuesAndTwo():
    testnumbers = [1,3,5,7]
    expected = 0
    result = divided_by(testnumbers, 2)
    assert expected == result
    
def testShouldReturnOneForOneEvenValueInset():
    testnumbers = [2]
    expected = 1
    result = divided_by(testnumbers, 1)
    assert expected == result
    
def testShouldReturnThreeForEvenValuedInSet():
    testnumbers = [1,2,3,4,6]
    expected = 3
    result = divided_by(testnumbers, 2)
    assert expected == result
    
def testShouldReturnTwoForDividedByThree():
    testnumbers = [1,2,3,4,6]
    expected = 2
    result = divided_by(testnumbers, 3)
    assert expected == result