from source.queue.queue import Queue
from source.queue.queuer import Queuer

"""
def test_add_one():
    # Arrange
    queue = Queue()
    # Act
    queue.add()
    # Assert
    expected = [Queuer(id=1, position=1)]
    assert queue.queue == expected



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
    try:
        # Act
        queue.remove(1)
    except IndexError:  # Assert
        pass
    else:
        assert False, 'Expected IndexError'


def test_remove_out_of_range():
    # Arrange
    queue = Queue()
    queue.queue = [Queuer(id=1, position=1)]

    try:
        # Act
        queue.remove(3)
    except IndexError:  # Assert
        pass
    else:
        assert False, 'Expected IndexError'
        
        """


