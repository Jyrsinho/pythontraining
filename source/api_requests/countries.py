"""
Dictionary of all the country objects
"""


class Countries:

    def __init__(self):
        self.countries = dict()

    def add_country(self, country):
        "adds given country to the dictionary"
        self.countries[country.name] = country


    def get_length(self):
        return len(self.countries)