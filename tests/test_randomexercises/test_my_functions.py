from lib2to3.pgen2.tokenize import String

from source.random_exercises.my_functions import is_min_length


def test_is_min_length_should_return_false_when_string_less_than_eight():
    s = "kissani"
    expected = False
    result = is_min_length(s)
    assert result == expected
    
def test_should_return_true_when_strings_lenght_is_ten():
    s = "1234567890"
    expected = True
    result = is_min_length(s)
    assert result == expected
    