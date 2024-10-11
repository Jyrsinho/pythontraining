from time import sleep

from source.country_quiz.api_client import APIClient


class Countryquiz:
    
    
    def __init__(self):
        self.api_client = APIClient()
    
    def create_a_question(self):
        
        country = self.api_client.get_country_by_name("finland")
    
        print(f"Let's quizz you about {country.official_name}!")
        sleep(1)
        print(f"What is the capital of {country.common_name}?")
        sleep(2)
        print(f"It is obviously {country.capital}.")
        
        
countryquiz = Countryquiz()   
countryquiz.create_a_question()
    
    



    
    