import pytest
from pytest import approx
from source.testing_exercises.temperature_converter import fahrenheit_to_celsius 

@pytest.mark.parametrize(
    'temperature, expected', [
        (212, 100),
        (98.6, 37),
        (70, 21.11111),
        (32, 0),
        (0, -17.77778),
        (-40, -40),
    ])



def test_temperature_converter(temperature,expected):
   assert fahrenheit_to_celsius(temperature) == approx(expected)

