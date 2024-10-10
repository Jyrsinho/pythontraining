
import pytest

from source.api_requests.countries import Countries


def test_should_create_empty_countries_dictionary():
    countries = Countries()
    assert countries.countries == {}
    assert countries.get_length() == 0


def test_should_add_country_to_countries(test_country_finland):
    countries = Countries()
    countries.add_country(test_country_finland)
    assert countries.get_length() == 1
    
    
def test_should_return_the_country_with_given_name(test_nordic_countries):
    suomi = test_nordic_countries.get_country("Suomi")
    assert suomi.capital == "Helsinki"
    assert suomi.common_name == "Finland"
    
    
    