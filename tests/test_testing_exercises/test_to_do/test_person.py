import datetime
import pytest
from source.testing_exercises.person import Person


class MockDatetime(datetime.date):
    @classmethod
    def today(cls):  # type: ignore
        return datetime.date(2018, 1, 1)


@pytest.mark.parametrize(
    'birth_year, birth_month, birth_day, expected', [
        (1900, 1, 1, True),
        (2000, 1, 1, True),
        (2000, 1, 2, False),
        (2010, 1, 1, False),
    ])
def test_is_adult(monkeypatch, birth_year, birth_month, birth_day, expected):
    monkeypatch.setattr(datetime, "date", MockDatetime)

    over_18_years_old_person = Person(
        name="John Doe",
        birth_date=datetime.date(birth_year, birth_month, birth_day),
    )

    assert over_18_years_old_person.is_adult() == expected
