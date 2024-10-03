from __future__ import annotations
import datetime
from tokenize import String


class Person:
    def __init__(self, name: str, birth_date: datetime.date):
        self.name = name
        self.birth_date = birth_date

    @staticmethod
    def calculate_age(person: Person) -> int:
        today = datetime.date.today()
        age = today.year - person.birth_date.year
        if today < datetime.date(today.year, person.birth_date.month, person.birth_date.day):
            age -= 1
        return age

    def get_age(self) -> int:
        return Person.calculate_age(self)

    def is_adult(self) -> bool:
        return self.get_age() >= 18



