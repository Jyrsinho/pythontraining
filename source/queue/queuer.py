class Queuer:
    """A class to represent a person in a queue"""
    id: int
    position: int
    

    def __init__(self, id: int, position: int):
        self.id = id
        self.position = position
    
    
    def update_position(self, new_position: int):
        """Update the position of the person in the queue"""
        self.position = new_position
        "Update the user about the change"
        print(f'Queuer {self.id} is now at position {self.position}.')