import pytest
from source.testing_exercises.is_adult import is_adult

@pytest.mark.parametrize(
    'age, expected', [
        (0, False),
        (1, False),
        (2, False),
        (10, False),
        (16, False),
        (17, False),
        (18, True),
        (19, True),
        (20, True),
        (30, True),
        (50, True),
        (100, True),
        (1000, True),
        (155, True),
        (999, True),
        (1999, True),
        (30000, True)
    ])

def test_is_adult(age, expected):
    assert is_adult(age) == expected

def test_should_raise_ValueError_when_age_less_than_zero():
    with pytest.raises(ValueError, match=r"Age must be a positive integer, but got -1"):
        is_adult(-1)

def test_should_raise_ValueError_when_age_less_than_zero4():
    with pytest.raises(ValueError):
        is_adult(-2)

def test_should_raise_ValueError_when_age_less_than_zero2():
    with pytest.raises(ValueError):
        is_adult(-1000)

def test_should_raise_ValueError_when_age_less_than_zero3():
    with pytest.raises(ValueError):
        is_adult(-100)
        

