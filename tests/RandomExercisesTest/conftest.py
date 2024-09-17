import pytest
import source.RandomExercises.shapes as shapes



@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(10, 20)

@pytest.fixture
def weird_rectangle():
    return shapes.Rectangle(5, 6)

@pytest.fixture
def integer_array1():
    integer_array1= [1,1,1,2,2,4,5]
    return integer_array1

@pytest.fixture
def integer_array2():
    integer_array2= [1,2,3,4]
    return integer_array2

@pytest.fixture
def integer_array3():
    integer_array3= [0,9,0,0,0,0,9,9,9,9]
    return integer_array3