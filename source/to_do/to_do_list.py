class TodoList:
    """
    A class to manage a todo list.

    The todo items in the todo list are dictionaries, each containing an id, a description, and a completed status.

    Example:
    {
        "id": 1,
        "description": "Buy groceries",
        "completed": False
    }
    
    The id is a unique identifier for the todo task that also tells at which index in the list the task is located.
    The todo list is 1-indexed, meaning the first task has an id of 1, the second has an id of 2, and so on.
    Thus, the index of a task in the list is its id minus 1.

    Managing the index and ids works similarly to managing a serial id in a database.
    Creating a new task increments the id counter by 1 (the id counter is equivalent to the list length),
    and deleting a task does not change the ids of other tasks or their position in the list.
    """

    def __init__(self):
        self.todos: list[dict | None] = [
            {"id": 1, "description": "Test todo", "completed": False},
            {"id": 2, "description": "Another test todo", "completed": True},
            {"id": 3, "description": "Yet another test todo", "completed": False},
        ]

    def get_todo(self, todo_id: int):
        """Returns a todo by its id."""
        if todo_id > 0 and todo_id <= len(self.todos):
            return self.todos[todo_id - 1]  # This may return None
        else:
            raise ValueError(f"todo with id {todo_id} does not exist.")

    def add_todo(self, task: str) -> dict:
        """
        Adds a new task to the todo list. 

        Args:
            task (str): The task to add.
        """
        todo = {
            "id": len(self.todos) + 1,
            "descritpion": task,
            "completed": False
        }
        self.todos.append(todo)
        return todo

    def complete_todo(self, todo_id: int) -> None:
        """
        Marks a task as completed. If the task is not found, raises ValueError.

        Args:
            todo_id (int): The task to mark as completed.
        Raises:
            ValueError: If the task is not found in the todo list.
        """
        if (todo := self.get_todo(todo_id)) is not None:
            todo["completed"] = True

    def delete_todo(self, todo_id: int) -> dict:
        """
        Deletes a task. If the task is not found, raises ValueError.

        Args:
            todo_id (int): The task to delete.
        Raises:
            ValueError: If the task is not found in the todo list.
        """
        if (todo := self.get_todo(todo_id)) is not None:
            self.todos.remove(todo) # This approach to deleting items can cause duplicate ids in todos
            return todo
        else:
            raise ValueError("Task does not exist.")

    def get_all_todos(self) -> list[dict]:
        """Returns a list of all existing tasks."""
        return [todo for todo in self.todos if todo is not None]
