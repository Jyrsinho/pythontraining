import pytest
from platformdirs.android import Android

from source.api_requests.country import Country


def test_should_create_new_country_with_given_name():
    country = Country(name="Finland")
    assert country.name == "Finland"
    
