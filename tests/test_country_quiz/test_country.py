import pytest

from source.country_quiz.country import Country


def test_should_create_new_country_with_given_name():
    country = Country(official_name = "Finland")
    assert country.official_name == "Finland"
    
    
def test_should_create_new_country_with_given_name_commonname_and_capital():
    country = Country( official_name = "Republic of Finland", common_name="Finland", capital="Helsinki")
    assert country.official_name == "Republic of Finland"
    assert country.common_name == "Finland"
    assert country.capital == "Helsinki"
    


