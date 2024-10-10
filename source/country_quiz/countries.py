"""
Dictionary of all the country objects
"""


class Countries:

    def __init__(self):
        self.countries = dict()

    def add_country(self, country):
        "adds given country to the dictionary"
        self.countries[country.common_name] = country


    def get_country(self, name):
        "returns the country with the given name"
        return self.countries[name]


    def get_length(self):
        return len(self.countries)