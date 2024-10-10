import pytest

from source.api_requests.country import Country


def test_should_create_new_country_with_given_name():
    country = Country(name="Finland")
    assert country.name == "Finland"
    
    
def test_should_create_new_country_with_given_name_commonname_and_capital():
    country = Country( name="Suomi", common_name="Finland", capital="Helsinki")
    assert country.name == "Suomi"
    assert country.common_name == "Finland"
    assert country.capital == "Helsinki"
    


