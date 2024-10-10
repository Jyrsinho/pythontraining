from itertools import count
from unittest.mock import patch

import requests
import pytest

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


def test_should_get_new_country_from_api_data( mocker, api_client):
   
   pass
       
       
