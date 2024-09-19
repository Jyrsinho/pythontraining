
from source.queue.queuer import Queuer
from dataclasses import dataclass


@dataclass
class Queue:
    '''A class to represent a list of queuers.'''

    def __init__(self):
        self.queue = []

    def add(self):
        '''Add a new queuer to the queue.'''
        self.queue.append(Queuer(len(self.queue) + 1, len(self.queue) + 1))

    def remove(self, index: int):
        """Remove a queuer from the queue by its index."""
        leaving_queuer = self.queue[index - 1]
        del self.queue[index - 1]
        for i, queuer in enumerate(self.queue):
            if queuer.position > index:
                queuer.update_position(i + 1)
        return leaving_queuer

    def remove_first(self) -> Queuer:
        """Remove the first queuer from the queue."""
        if len(self.queue) == 0:
            raise RuntimeError('The queue is empty.')
        return self.remove(1)



queue = Queue()
queue.add()
queue.add()
queue.add()
print(queue.remove_first())
