import pytest
from robot.utils.asserts import assert_true, assert_false

from source.stack.stack import Stack

"""
Kirjoita ohjelma, joka toteuttaa pino-operaatiot push, pop, isEmpty, size ja top pinolle, jonka 
alkiot ovat kokonaislukuja.

Toteuta pino-operaatiot itse. (Älä käytä ohjelmakoodien valmiita rutiineja kuten "length"/"count", "append"/
"add"/"insert" tai "remove", "pop", "delete".)
"""

@pytest.fixture
def setup_stack():
    test_stack = Stack(5)
    return test_stack

def test_push_should_increase_the_size_of_the_stack(setup_stack):
    test_stack = setup_stack
    test_stack.push(1)
    assert test_stack.size == 1
    
    
def test_should_add_an_element_to_stack():
    
    test_stack = Stack(5)
    test_stack.push(1)
    assert test_stack.top() == 1
    
    
def test_should_add_two_elements_to_stack():
    test_stack = Stack(5)
    test_stack.push(1)
    test_stack.push(2)
    
    assert test_stack.pop() == 2
    assert test_stack.pop() == 1
    
    
def test_should_create_larger_stack_when_array_size_is_exceeded():
    test_stack = Stack(3)
    test_stack.push(1)
    test_stack.push(2)
    test_stack.push(3)
    test_stack.push(4)
    
    assert test_stack.size == 4
    
    
def test_should_be_able_to_add_values_to_a_stack_that_has_been_expanded():
    test_stack = Stack(1)
    test_stack.push(1)
    test_stack.push(2)
    test_stack.push(3)
    
    assert test_stack.top() == 3
    
    
def test_should_return_true_for_is_empty_when_stack_is_empty():
    test_stack = Stack(5)
    assert_true(test_stack.is_empty())
    
    
def test_should_return_false_when_stack_has_an_element():
    test_stack = Stack(5)
    test_stack.push(1)
    assert_false(test_stack.is_empty())
    