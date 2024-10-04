from functools import wraps
from turtledemo.clock import setup
from urllib.parse import urljoin

import pytest
import requests
import requests_mock

import source
from source.testing_exercises.joke_app import get_random_joke, API_URL
from unittest.mock import patch

mocked_joke = {
    "id": 123,
    "setup": "Why don't scientists trust atoms?",
    "punchline": "Because they make up everything!"
}

def test_should_mock_response_from_the_server(requests_mock):
    
    requests_mock.get(API_URL, json=mocked_joke)
    
    joke = get_random_joke()
    
    assert joke.id == 123
    assert joke.setup == "Why don't scientists trust atoms?"
    assert joke.punchline == "Because they make up everything!"
    
    
def test_should_call_the_api_once():
    
    with patch.object(requests, 'get', wraps=requests.get) as mocked_get:
        
        get_random_joke()
        mocked_get.assert_called_once_with(API_URL)
    
    
       
    
