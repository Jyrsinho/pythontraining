import source.RandomExercises.mode as mode

# lista testeistä:
# 
# palauttaa numeron
# palauttaa moden taulukosta 1,1,2,3,4,5 == 1
# palauttaa modet taulukosta 1,1,2,2,3,5,0 == 1,2

def test_create_histogram_should_return_a_different_array(integer_array2):
    result = mode.create_histogram(integer_array2)
    assert result != integer_array2


def test_create_histogram_should_return_array_with_ones(integer_array2):
    result = mode.create_histogram(integer_array2)
    assert result == {0:0,1:1,2:1,3:1,4:1,5:0,6:0,7:0,8:0,9:0}
    
def test_create_histogram_should_return_array_with_varying_amounts(integer_array3):
    result = mode.create_histogram(integer_array3)
    assert result == {0:5,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0, 9:5}
    
def test_find_the_mode_should_return_mode_when_there_is_one_mode(integer_array1):
    result = mode.find_the_mode(integer_array1)
    assert result == [1]
    
def test_find_the_mode_should_return_negative_when_there_is_no_mode(integer_array2):
    result = mode.find_the_mode(integer_array2)
    assert result == -1

def test_find_the_mode_should_return_multiple_values_when_the_list_is_multimodal(integer_array3):
    result = mode.find_the_mode(integer_array3)
    assert result == [0,9]
