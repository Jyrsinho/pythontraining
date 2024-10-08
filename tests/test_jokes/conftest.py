import csv
from turtledemo.clock import setup
from types import new_class

import pytest
from _pytest.tmpdir import tmp_path

from source.jokes.jokes import JokeService, Joke


# 1. single_joke_csv_filepath — a fixture that returns the path to a temporary csv file containing a single joke 
# (the fixture may create the file or the file can be created in another fixture)
@pytest.fixture
def single_joke_csv_filepath(tmp_path):
    temporary_csv_file = tmp_path / "test_joke_file.csv"
    data = [
        ["setup", "punchline"],  # Headers
        ["Can February March?", "No, but April May."]  # Single joke as a row
        ]
    
    with open(temporary_csv_file, "w", newline='') as temp_file:
        writer = csv.writer(temp_file)
        writer.writerows(data)
    
    return temporary_csv_file


# 2. single_joke — a fixture that returns the joke from the temporary single joke csv file
@pytest.fixture
def single_joke(single_joke_csv_filepath):
    # Read the contents of the CSV file
    with open(single_joke_csv_filepath, mode='r') as file:
        reader = csv.DictReader(file)
        content = [row for row in reader]  # content will be a list of dictionaries

    # Debug print the content read from the CSV file
    print("Content read from CSV:", content)

    # Ensure there is at least one joke to return
    assert len(content) > 0, "No jokes found in CSV file."

    # Return the first joke as a Joke object
    row = content[0]  # Get the first joke
    return Joke(setup=row['setup'], punchline=row['punchline'])  # Return an instance of the Joke class
    
    

# 3 jokes_csv_filepath — a fixture that returns the path to a temporary csv file containing multiple jokes 
# (the fixture may create the file or the file can be created in another fixture)
@pytest.fixture
def jokes_csv_filepath(tmp_path):
    temporary_csv_file = tmp_path / "test_jokes_file.csv"
    return temporary_csv_file

#4. jokes — a fixture that returns the jokes from the temporary jokes csv file
@pytest.fixture
def jokes(jokes_csv_filepath):
    pass



