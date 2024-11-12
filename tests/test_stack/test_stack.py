import pytest

from source.stack.stack import Stack

"""
Kirjoita ohjelma, joka toteuttaa pino-operaatiot push, pop, isEmpty, size ja top pinolle, jonka 
alkiot ovat kokonaislukuja.

Toteuta pino-operaatiot itse. (Älä käytä ohjelmakoodien valmiita rutiineja kuten "length"/"count", "append"/
"add"/"insert" tai "remove", "pop", "delete".)
"""

@pytest.fixture
def setup_stack():
    testStack = Stack(5)
    return testStack

def test_should_add_elements_to_stack(setup_stack):
    testStack = setup_stack
    testStack.push(1)
    assert testStack.size == 1
    
def test_should_add_elements_to_stack2():
    
    testStack = Stack(5)
    testStack.push(1)
    testStack.push(2)
    assert testStack.top() == 
