import csv

import pytest
from _pytest.tmpdir import tmp_path


# 1. single_joke_csv_filepath — a fixture that returns the path to a temporary csv file containing a single joke 
# (the fixture may create the file or the file can be created in another fixture)
@pytest.fixture
def single_joke_csv_filepath(tmp_path):
    temporary_csv_file = tmp_path / "test_joke_file.csv"
    data = [
        "Can February March?","No, but April May."
    ]
    
    with open(temporary_csv_file, "w") as temp_file:
        writer = csv.writer(temp_file)
        writer.writerow(data)
    
    return temporary_csv_file


#2. single_joke — a fixture that returns the joke from the temporary single joke csv file
@pytest.fixture
def single_joke(single_joke_csv_filepath):
    # Read the contents of the CSV file back into a list
    with open(single_joke_csv_filepath, mode='r') as file:
        reader = csv.reader(file)
        content = [row for row in reader]

    # Return the content of the CSV file
    return  content

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



