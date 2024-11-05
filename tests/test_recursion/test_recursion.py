from numpy.ma.core import equal

from source.recursion.recursion import  factorial


def test_factorial_should_return_one_for_one() :
    assert factorial(1) == 1;
    
    
def test_factorial_should_return_two_for_two() :
    assert factorial(2) == 2;

def test_factorial_should_return_six_for_three() :
    assert factorial(3) == 6;