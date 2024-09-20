import pytest
from source.testing_exercises.is_adult import is_adult
@pytest.mark.parametrize(
    'age, expected', [
        (0, False),
        (1, False),
        (10, False),
        (17, False),
        (18, True),
        (19, True),
        (50, True),
        (155, True)
        
    ])

def test_is_adult(age, expected):
    assert is_adult(age) == expected
    
def test_should_raise_ValueError_when_age_less_than_zero():
    with pytest.raises(ValueError):
        is_adult(-1)

        