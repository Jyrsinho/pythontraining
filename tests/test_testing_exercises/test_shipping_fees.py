import pytest
from source.testing_exercises.shipping_fees import calculate_shipping_fee

@pytest.mark.parametrize(
    'total_price, total_weight, expected', [
        (0,          0,         4.99),         
        (49, 	    0.9, 	    4.99),
        (49,        1.1,        9.99),
        (49,        4.99,       9.99),      
        (49,        5.0,       14.99),
        (49,        5.1,       14.99),
        (50,        0.9,        4.99),
        (50,        1.0,        9.99),
        (51,        1.0,        4.99),
        (100,       1.0,        4.99),
        (101,       1.0,            0),
        (101,       5.1,            0),
    ])


def test_calculate_shipping_fee(total_price, total_weight, expected):
    assert calculate_shipping_fee(total_price, total_weight) == expected
    
def test_should_throw_ValueError_for_negative_price():
    with pytest.raises(ValueError):
        calculate_shipping_fee(-1, 4.99)
    
#Raise error for negative total_weight
def test_should_throw_ValueError_for_weight_less_than_zero():
    with pytest.raises(ValueError):
        calculate_shipping_fee(0, -1)