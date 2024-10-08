from idlelib.run import StdOutputFile
from tkinter.ttk import Button
from unittest import expectedFailure

from source.jokes.jokes import Joke


def test_conftest_returns_a_csv_filepath(single_joke_csv_filepath):
    assert single_joke_csv_filepath.exists(), "The CSV file does not exist"
    assert single_joke_csv_filepath.suffix == ".csv"
    
    
def test_conftest_returns_a_single_joke(single_joke):
    print(single_joke)
    assert single_joke is not None
    

