import pytest

from source.random_exercises.mode import create_histogram
from source.random_exercises.temperature_converter import fahrenheit_to_celsius


@pytest.mark.parametrize(
    "temperature, expected", [
        (212,)
    ]
)

def test_temperature_converter():
    #Arrange
    fahrenheit = 212
    expected = 100
    #Act
    fahrenheit_to_celsius(fahrenheit)
    #Assert
    assert fahrenheit_to_celsius(fahrenheit) == expected
    
    
    
    
    
    
    
# assert result == approx(expected)    

# Create parameterized test with expected value using approximation