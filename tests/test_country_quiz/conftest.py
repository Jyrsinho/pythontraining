import pytest

from source.country_quiz.countries import Countries
from source.country_quiz.country import Country


@pytest.fixture
def test_country_finland():
    official_name = "Republic of Finland"
    common_name = "Finland"
    capital = "Helsinki"
    finland = Country(official_name = official_name, common_name=common_name, capital=capital)
    return finland

@pytest.fixture
def test_country_sweden():
    official_name = "Kingdom of Sweden"
    common_name = "Sweden"
    capital = "Stockholm"
    sweden = Country(official_name=official_name, common_name=common_name, capital=capital)
    return sweden

@pytest.fixture
def test_country_denmark():
    official_name = "Kingdom of Denmark"
    common_name = "Denmark"
    capital = "Copenhagen"
    denmark = Country(official_name= official_name, common_name=common_name, capital=capital)
    return denmark

@pytest.fixture
def test_country_norway():
    official_name = "Kingdom of Norway"
    common_name = "Norway"
    capital = "Oslo"
    norway = Country(official_name=official_name, common_name=common_name, capital=capital)
    return norway


@pytest.fixture
def test_nordic_countries(test_country_finland, test_country_sweden, test_country_norway, test_country_denmark):
    nordic_countries = Countries()
    nordic_countries.add_country(test_country_finland)
    nordic_countries.add_country(test_country_sweden)
    nordic_countries.add_country(test_country_norway)
    nordic_countries.add_country(test_country_denmark)
    return nordic_countries
    

