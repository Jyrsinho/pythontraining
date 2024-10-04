import io
import sys
from unittest.mock import patch
import requests
from source.testing_exercises.joke_app import get_random_joke, API_URL, print_random_joke

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
    
    with patch.object(requests, 'get') as mocked_get:
        mocked_get.return_value.json.return_value = {
            "id": 1,
            "setup": "Miksi joulupukki meni psykiatrille?",
            "punchline": "Hän ei uskonut enää itseensä."
        }
        
        get_random_joke()
        mocked_get.assert_called_once_with(API_URL)
        
        
def test_should_print_the_joke_in_correct_order(monkeypatch):

    mocked_stdout = io.StringIO()
    monkeypatch.setattr(sys, 'stdout', mocked_stdout)
    
    with patch("source.testing_exercises.joke_app.sleep", return_value=None) as mocked_sleep:
        with patch.object(requests, 'get') as mocked_get:
            mocked_get.return_value.json.return_value = {
                "id": 1,
                "setup": "Miksi joulupukki meni psykiatrille?",
                "punchline": "Hän ei uskonut enää itseensä."
            }
            print_random_joke()
    
    printed_output = mocked_stdout.getvalue()
    printed_lines = printed_output.strip().split("\n")
    expected_lines = ["Miksi joulupukki meni psykiatrille?", "Hän ei uskonut enää itseensä."]
    
    mocked_sleep.assert_called_once_with(2)
    assert printed_lines == expected_lines


def test_should_call_the_sleep_function_between_printing_setup_and_punchline():

    with patch("joke_app.sleep", return_value=None) as mocked_sleep:
        with patch.object(requests, 'get') as mocked_get:
            mocked_get.return_value.json.return_value = {
                "id": 1,
                "setup": "Miksi joulupukki meni psykiatrille?",
                "punchline": "Hän ei uskonut enää itseensä."
            }
            print_random_joke()

    mocked_sleep.assert_called_once_with(2)
    
       
    
