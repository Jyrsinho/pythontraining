import io
import sys
from unittest import expectedFailure
from unittest.mock import patch, call
from xml.sax.handler import property_interning_dict

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




def test_print_random_joke_calls_sleep_between_prints():
    
    with patch("source.testing_exercises.joke_app.sleep", return_value=None) as mocked_sleep:
        with patch.object(requests, 'get') as mocked_get:
            mocked_get.return_value.json.return_value = {
                "id": 1,
                "setup": "Miksi joulupukki meni psykiatrille?",
                "punchline": "Hän ei uskonut enää itseensä."
            }


            # Mock print to spy on print calls
            with patch("builtins.print") as mocked_print:
                # Call the function we are testing
                print_random_joke()

                # Create the expected sequence of calls
                expected_calls = [
                    call("Miksi joulupukki meni psykiatrille?"),  # First print (setup)
                    call(2),  # sleep(2) should be called here
                    call("Hän ei uskonut enää itseensä.")  # Second print (punchline)
                ]

                # Combine all the calls from mocked_print and mocked_sleep
                # Create a new list to track the order
                combined_calls = []

                # Add print calls
                combined_calls.extend(mocked_print.call_args_list)
                # Add sleep calls
                combined_calls.extend(mocked_sleep.call_args_list)

                # Check that the full sequence matches the expected order
                assert combined_calls == expected_calls

                # Verify that sleep was called exactly once with the argument 2
                mocked_sleep.assert_called_once_with(2)
            

    
       
    
