from itertools import count
from unittest.mock import patch, MagicMock

import requests
import pytest
import pytest_mock
from source.country_quiz.api_client import APIClient


@pytest.fixture
def api_client():
    api_client = APIClient()
    return api_client

mock_response = [{
    "name": {
        "common": "Finland",
        "official": "Republic of Finland"
    },
    "capital": ["Helsinki"]
}]



def test_should_get_new_country_from_api_data(mocker, api_client):

    # Create a mock response object
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{
        "name": {
            "common": "Testimaa",
            "official": "Republic of Testimaa"
        },
        "capital": ["Testikaupunki"]
    }]

    # Patch requests.get to return the mock response
    mocker.patch('requests.get', return_value=mock_response)

    # Call the method that makes the request
    country = api_client.get_country_by_name("testimaa")

    # Verify the response based on the mocked status code and json data
    assert country.official_name == "Republic of Testimaa"
    assert country.capital == "Testikaupunki"
    
   
   
       
       
