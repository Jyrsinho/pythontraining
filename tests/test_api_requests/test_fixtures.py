import pytest

from source.api_requests.country import Country


@pytest.fixture
def test_country_finland():
    name = "Suomi"
    common_name = "Finland"
    capital = "Helsinki"
    finland = Country(name=name, common_name=common_name, capital=capital)
    return finland