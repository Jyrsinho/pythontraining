"""
Kirjoita ohjelma, joka toteuttaa pino-operaatiot push, pop, isEmpty, size ja top pinolle, jonka 
alkiot ovat kokonaislukuja.

Toteuta pino-operaatiot itse. (Älä käytä ohjelmakoodien valmiita rutiineja kuten "length"/"count", "append"/
"add"/"insert" tai "remove", "pop", "delete".)
"""
from inspect import stack


class Stack:
    
    
    def __init__(self, capacity):
        self.size = 0
        self.capacity = capacity
        self.elements = [0] * capacity
        
    
    
    def push(self, item):
        self.size += 1
        self.elements[0] = item
        
        
    
    def top(self):
        """
        returns the top element of the stack
        :return: top element of the stack
        """
        return self.elements[0]


def main():
    
    print ("Testing push- function")
    

if __name__ == "__main__":
    main()