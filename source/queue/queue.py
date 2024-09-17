from source.queue.queuer import Queuer


class Queue:
    """a class to represent a queue"""
    
    def __init__(self):
        self.queue = []
        self.id_counter = 1
        
    def add(self):
        """Add a new queuer to the queue"""
        self.queue.append(Queuer(self.id_counter, len(self.queue) +1 ))
        self.id_counter += 1
    
    def remove(self, index: int):
        """Remove a queuer from the queue by its index."""
        del self.queue[index - 1]
        for i, queuer in enumerate(self.queue):
            if queuer.position > index:
                queuer.update_position(i - 1)