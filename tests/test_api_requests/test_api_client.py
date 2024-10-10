import pytest

from source.api_requests.api_client import APIClient



@pytest.fixture
def api_client():
    api_client = APIClient()
    return api_client

#TODO this need to use Mock instead of connecting to API
def test_should_create_new_country_from_api_data(api_client):
    country_name = "suomi"
    country = api_client.get_country_by_name( country_name= country_name)
    assert country.name == "suomi"
    assert country.common_name == "Finland"
    assert country.capital == "Helsinki"
