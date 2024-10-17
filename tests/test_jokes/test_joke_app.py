from source.jokes.joke_app import print_random_joke
import io
import sys
from unittest.mock import patch
import requests
import pytest

def test_should_print_the_joke_in_correct_order(monkeypatch):

    mocked_stdout = io.StringIO()
    monkeypatch.setattr(sys, 'stdout', mocked_stdout)

    with patch("source.jokes.joke_app.sleep", return_value=None) as mocked_sleep:
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

    assert printed_lines == expected_lines
    
    
def test_should_call_sleep_between_prints(monkeypatch):
    calls = []

    
    with patch.object(requests, 'get') as mocked_get:
         mocked_get.return_value.json.return_value = {
             "id": 1,
             "setup": "setup",
             "punchline": "punchline",   
         }
         with patch("builtins.print", side_effect=lambda x: calls.append(f"print")) as mocked_print:
            with patch("source.jokes.joke_app.sleep", side_effect=lambda _: calls.append("sleep")) as mocked_sleep:
                print_random_joke()
                
            assert calls == ["print", "sleep", "print"]
                
                
             

               