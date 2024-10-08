
def test_conftest_returns_a_csv_filepath(single_joke_csv_filepath):
    assert single_joke_csv_filepath.exists(), "The CSV file does not exist"
    assert single_joke_csv_filepath.suffix == ".csv"
    