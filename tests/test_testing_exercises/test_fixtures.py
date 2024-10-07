import pytest


@pytest.fixture
def test_data() -> list[str]:
    return ['a', 'b']

@pytest.fixture
def test_user():
    return {
        "name": "Tester",
        "email": "testing@testers.qa",
        "password": "tester1?P*ssword"
    }


@pytest.fixture
def extended_test_data(test_data) -> list[str]:
    test_data = test_data +["c"]
    return test_data



def test_data_should_be_list_of_a_and_b(test_data):
    assert test_data == ['a', 'b']
    

def test_extended_data_should_be_list_of_a_b_and_c(extended_test_data):
    assert extended_test_data == ['a', 'b', 'c']

def test_should_use_two_fixtures(test_data: list[str], extended_test_data: list[str]):
    assert  extended_test_data == test_data + ["c"]