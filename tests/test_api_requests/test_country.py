import pytest
from platformdirs.android import Android

from source.api_requests.countries import Countries
from source.api_requests.country import Country
from source.api_requests.main import country_name, create_country_by_name


def test_should_create_new_country_with_given_name():
    country = Country(name="Finland")
    assert country.name == "Finland"
    
    
def test_should_create_new_country_with_given_name_commonname_and_capital():
    country = Country( name="Suomi", common_name="Finland", capital="Helsinki")
    assert country.name == "Suomi"
    assert country.common_name == "Finland"
    assert country.capital == "Helsinki"
    

#TODO this need to use Mock instead of connecting to API
def testshouldcreatenewcountryfromapidata():
    country_name = "suomi"
    country = create_country_by_name( country_name= country_name)
    assert country.name == "suomi"
    assert country.common_name == "Finland"
    assert country.capital == "Helsinki"