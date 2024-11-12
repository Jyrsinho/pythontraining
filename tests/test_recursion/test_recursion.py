from numpy.ma.core import equal

from source.recursion.recursion import factorial, fibonacci, recursive_sum


def test_factorial_should_return_one_for_one() :
    assert factorial(1) == 1;
    
    
def test_factorial_should_return_two_for_two() :
    assert factorial(2) == 2;

def test_factorial_should_return_six_for_three() :
    assert factorial(3) == 6;
    
def test_fibonacci_should_return_fibonacci_sequence():
    assert fibonacci(0) == 0;
    
def test_fibonacci_should_return_one_for_one():
    assert fibonacci(1) == 1;
    
def test_fibonacci_should_return_five_for_five():
    assert fibonacci(5) == 5
        
def test_fibonacci_should_return_fiftyfive_for_ten():
    assert fibonacci(10) == 55
    
def test_recursivesum_should_return_zero_for_zero():
    assert recursive_sum(0) == 0
    
def test_recursivesum_should_return_one_for_one():
    assert recursive_sum(1) == 1
    
def test_recursivesum_should_return_three_for_two():
    assert recursive_sum(2) == 3
    
def test_recursivesum_should_return_fifteen_for_five():
    assert recursive_sum(5) == 15