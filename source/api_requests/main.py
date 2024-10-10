"""
Exercise to get data from an API
Data is about countries

Let's try at least create country objects from the API.
And let's mock the API connection.

API 
"""

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
        return None
        
        
        
def create_country_by_name(country_name):
    country_info = get_country_info(country_name)
    
    if country_info:
        country_data = country_info[0]
        country_name_common = country_data["name"]["common"]
        country_capital = country_data["capital"][0]
    
    country = Country(name =country_name, common_name=country_name_common,capital= country_capital)
    return country
    

    


    
country_name = "suomi"
country_info = get_country_info(country_name)

if country_info:
    country_data = country_info[0]
    print(f"{country_data["name"]["common"]}")
    print(f"{country_data["capital"]}")
