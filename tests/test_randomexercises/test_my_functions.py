from pluggy import Result

from source.random_exercises.my_functions import is_min_length, non_negative


def test_is_min_length_should_return_false_when_string_less_than_eight():
    s = "kissani"
    expected = False
    result = is_min_length(s)
    assert result == expected
    
def test_should_return_true_when_strings_length_is_ten():
    s = "1234567890"
    expected = True
    result = is_min_length(s)
    assert result == expected
    
def test_should_return_true_when_strings_length_is_eight():
    s = "12345678"
    expected = True
    result = is_min_length(s)
    assert result == expected
    
def test_should_return_false_string_is_empty():
    s = ""
    expected = False
    result = is_min_length(s)
    assert result == expected
    
def test_should_return_all_the_positive_numbers():
    list = [2,4,7]
    expected = list
    result = non_negative(list)
    assert result == expected
    
def test_should_exclude_negative_numbers():
    list = [2,-4,7]
    expected = [2,7]
    result = non_negative(list)
    assert result == expected
    
def test_should_return_empty_list_when_all_numbers_are_negative():
    list = [-2,-4, -6]
    expected = []
    result = non_negative(list)
    assert result == expected
    
def test_should_return_empty_list_when_given_empty_list():
    list = []
    expected = []
    result = non_negative(list)
    assert result == expected
    