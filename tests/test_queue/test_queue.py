"""
In this exercise, you have the code and tests for a Queue class similar to previous examples in this part.

Here, the class has a new untested method, remove_first(), which removes the first in line from the queue.

Add three tests for the remove_first() method.

The first test should check that the method removes the first element and not for example the last.
The second test should check that the method returns the removed element.
The third test should check that the method raises a RuntimeError when the queue is empty.

Each test should be in a separate function and should be named so that pytest can automatically locate them. 
"""
import pytest

from source.queue.queue import Queue
from source.queue.queuer import Queuer


def test_add_one():
    # Arrange
    queue = Queue()
    # Act
    queue.add()
    # Assert
    assert queue.queue == [Queuer(id=1, position=1)]


def test_add_two():
    # Arrange
    queue = Queue()
    # Act
    queue.add()
    queue.add()
    # Assert
    assert queue.queue == [Queuer(id=1, position=1), Queuer(id=2, position=2)]


def test_remove_first():
    # Arrange
    queue = Queue()
    queue.queue = [Queuer(id=1, position=1), Queuer(id=2, position=2)]
    # Act
    queue.remove(1)
    # Assert
    assert queue.queue == [Queuer(id=2, position=1)]


def test_remove_from_middle():
    # Arrange
    queue = Queue()
    queue.queue = [Queuer(id=1, position=1), Queuer(
        id=2, position=2), Queuer(id=3, position=3)]
    # Act
    queue.remove(1)
    # Assert
    assert queue.queue == [Queuer(id=2, position=1), Queuer(id=3, position=2)]


def test_remove_last():
    # Arrange
    queue = Queue()
    queue.queue = [Queuer(id=1, position=1), Queuer(id=2, position=2)]
    # Act
    queue.remove(2)
    # Assert
    assert queue.queue == [Queuer(id=1, position=1)]


def test_remove_first_until_empty():
    # Arrange
    queue = Queue()
    queue.queue = [Queuer(id=1, position=1), Queuer(id=2, position=2)]
    # Act
    queue.remove(1)
    queue.remove(1)
    # Assert
    assert queue.queue == []


def test_remove_from_empty():
    # Arrange
    queue = Queue()

    with pytest.raises(IndexError):  # Assert
        queue.remove(1)  # Act


def test_remove_out_of_range():
    # Arrange
    queue = Queue()
    queue.queue = [Queuer(id=1, position=1)]

    with pytest.raises(IndexError):  # Assert
        queue.remove(3)  # Act


