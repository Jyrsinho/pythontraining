import pytest

from source.api_requests.countries import Countries
from source.api_requests.country import Country


@pytest.fixture
def test_country_finland():
    name = "Suomi"
    common_name = "Finland"
    capital = "Helsinki"
    finland = Country(name=name, common_name=common_name, capital=capital)
    return finland

@pytest.fixture
def test_country_sweden():
    name = "Sverige"
    common_name = "Sweden"
    capital = "Stockholm"
    sweden = Country(name=name, common_name=common_name, capital=capital)
    return sweden

@pytest.fixture
def test_country_denmark():
    name = "Danmark"
    common_name = "Denmark"
    capital = "Copenhagen"
    denmark = Country(name=name, common_name=common_name, capital=capital)
    return denmark

@pytest.fixture
def test_country_norway():
    name = "Norge"
    common_name = "Norway"
    capital = "Oslo"
    norway = Country(name=name, common_name=common_name, capital=capital)
    return norway


@pytest.fixture
def test_nordic_countries(test_country_finland, test_country_sweden, test_country_norway, test_country_denmark):
    nordic_countries = Countries()
    nordic_countries.add_country(test_country_finland)
    nordic_countries.add_country(test_country_sweden)
    nordic_countries.add_country(test_country_norway)
    nordic_countries.add_country(test_country_denmark)
    return nordic_countries
    

