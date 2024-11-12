
import pandas as pd

"""
Let's do here some recursion assignments
"""


def factorial(x):

    if (x == 1):
        return x
    else: return x * factorial(x-1)
    
"""
    Tehtävä: Fibonaccin lukujono
    Tehtävänanto: Kirjoita rekursiivinen funktio, joka laskee ja palauttaa Fibonaccin lukujonon nn
    alkion. Fibonaccin lukujono määritellään seuraavasti:
    F(0)=0F(0)=0
    F(1)=1F(1)=1
    F(n)=F(n−1)+F(n−2)F(n)=F(n−1)+F(n−2) (kun n>1n>1)
"""
    
def fibonacci(x):
    
    if (x <= 1):
        return x
    else: return fibonacci(x-1) + fibonacci(x-2)
    
    
def recursive_sum(x):
    
    if (x <= 1):
        return x
    else: return recursive_sum(x-1) + x                                    
    

def pandas():
    data = pd.Series([1, 3, 0.5, 2, 5])
    sorted_data = data.sort_values(ascending=True)
    print(sorted_data)
    
pandas()