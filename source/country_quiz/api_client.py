"""
Class that handles all the requests made to the API

API 
"""

import requests
from source.country_quiz.country import Country


class APIClient:
    base_url = "https://restcountries.com/v3.1/"


    def get_country_info(self, country_name):
        url = f"{self.base_url}name/{country_name}"
        response = requests.get(url)

        if response.status_code == 200:
            print("Data retrieved successfully")
            country_info = response.json()
            return country_info
        else:
            print(f"Failed to retrieve data for {country_name} {response.status_code}")
            return None


    def get_country_by_name(self, country_name):
        country_info = self.get_country_info(country_name)

        if country_info:
            country_data = country_info[0]
            country_name_official = country_data["name"]["official"]
            country_name_common = country_data["name"]["common"]
            country_capital = country_data["capital"][0]

        country = Country(official_name=country_name_official, common_name=country_name_common, capital=country_capital)
        return country


"""

api_client = APIClient()

country_name = "suomi"
country_info = api_client.get_country_info(country_name)

print(country_info)

if country_info:
    country_data = country_info[0]
    print(f"{country_data["name"]["common"]}")
    print(f"{country_data["capital"]}")

"""
