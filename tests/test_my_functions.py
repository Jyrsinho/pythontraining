import pytest
import source.my_functions as my_functions
import time

def test_add():
    result = my_functions.add(1,4)
    assert result == 5
    
def test_divide():
    result = my_functions.divide(4,2)
    assert result == 2
    result = my_functions.divide(2,2)
    assert result == 1
    result = my_functions.divide(10, 5)
    assert result == 2
    
@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = my_functions.divide(10, 5)
    assert result == 2
    

@pytest.mark.skip(reason="This feature is currently broken")
def test_add():
    assert my_functions.add(1,2) == 3
    

@pytest.mark.xfail(reason= "We know we cannot divide by zero")
def test_divide_zero_broken():
    assert my_functions.divide(4,0)