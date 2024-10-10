from unittest.mock import patch

import pytest

from source.api_requests.api_client import APIClient


@pytest.fixture
def api_client():
    api_client = APIClient()
    return api_client



def test_should_get_new_country_from_api_data(api_client):
    mock_response = [{
        "name": {
            "common": "United States"
        },
        "capital": ["Washington"]
    }]
    
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response
        
        result = api_client.get_country_by_name("Usa")
        
        assert result.name == "Usa"
        assert result.capital == "Washington"
        assert result.common_name == "United States"
        
        mock_get.assert_called_with("https://restcountries.com/v3.1/name/Usa" )
