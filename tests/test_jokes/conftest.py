import os

import pytest
from _pytest.tmpdir import tmp_path


# 1. single_joke_csv_filepath — a fixture that returns the path to a temporary csv file containing a single joke 
# (the fixture may create the file or the file can be created in another fixture)
def single_joke_csv_filepath(tmp_path):
    temporary_csv_file = tmp_path / "test_file.csv"
    return temporary_csv_file

#2. single_joke — a fixture that returns the joke from the temporary single joke csv file
#3. jokes_csv_filepath — a fixture that returns the path to a temporary csv file containing multiple jokes (the fixture may create the file or the file can be created in another fixture)
#4. jokes — a fixture that returns the jokes from the temporary jokes csv file


@pytest.fixture
def single_joke_csv_filepath() -> str:
    return "source.jokes.jokes.csv"
