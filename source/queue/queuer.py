from dataclasses import dataclass


@dataclass
class Queuer:
    """A class to represent a person in queue."""
    id: int
    position: int

    def update_position(self, new_position: int):
        """Update the position of a queuer in the queue."""
        self.position = new_position
        # Update the user about the change
        print(f'Queuer {self.id} is now at position {self.position}.')