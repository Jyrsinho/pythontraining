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
    