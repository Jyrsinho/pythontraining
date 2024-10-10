"""
Creates a Country object.
Should get attributes from an API.

Sample API URL:

https://randomuser.me/api/

"""


class Country:
    def __init__(self, **kwargs):
        self.common_name = kwargs.get('common_name')
        self.official_name = kwargs.get('official_name')
        self.capital = kwargs.get('capital')
        
        
    
        
        
    
     

    
    