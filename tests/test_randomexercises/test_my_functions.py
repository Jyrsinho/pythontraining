from source.random_exercises.my_functions import is_min_length


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
    