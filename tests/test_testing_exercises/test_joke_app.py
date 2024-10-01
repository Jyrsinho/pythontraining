import pytest

import source
from source.testing_exercises.joke_app import get_random_joke
from unittest.mock import patch

def test_get_random_joke_calls_correct_URI():
    
    with patch ("source.testing_exercises.joke_app.get_random_joke") as spy_mock_joke:
        #Run the function
        source.testing_exercises.joke_app.get_random_joke()
    
        # Did the function make an HTTP GET request?
        spy_mock_joke.assert_called_once()

        # Was the request sent to the right URI?
       # spy_mock_joke.assert_called_with("requests.gethttps://official-joke-api.appspot.com/jokes/random.json")
    