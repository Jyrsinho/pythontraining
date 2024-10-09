"""
Exercise to get data from an API
Data is about countries

Let's try at least create country objects from the API.
And let's mock the API connection.

API 
"""
from tkinter.font import names

import requests

from source.api_requests.country import Country

base_url = "https://restcountries.com/v3.1/"

def get_country_info(country_name):
    url = f"{base_url}name/{country_name}"
    print(url)
    response = requests.get(url)
    
    if response.status_code == 200:
        print("Data retrieved successfully")
        country_data = response.json()
        return country_data
    else: 
        print(f"Failed to retrieve data for {country_name} {response.status_code}")

country_name = "suomi"
country_info = get_country_info(country_name)

if country_info:
    country_data = country_info[0]
    print(f"{country_data["name"]["common"]}")
    print(f"{country_data["capital"]}")
