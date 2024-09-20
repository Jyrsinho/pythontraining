import pytest

from source.testing_exercises.to_do.to_do_list import TodoList


def test_should_add_todo():
    #Arrange
    tdList = TodoList()
    #Act
    tdList.add_todo("testaa")
    result = tdList.get_todo(1)
    expected = { "id": 1,
                 "description": "testaa",
                 "completed": False
                 }
    #Assert
    assert result == expected
    
def test_should_add_two_todos():
    tdList = TodoList()
    tdList.add_todo("testaa1")
    tdList.add_todo("testaa2")
    result = tdList.get_todo(2)
    expected = { "id": 2,
                 "description": "testaa2",
                 "completed": False}
    assert result == expected
    
def test_should_add_three_todos():
    tdList = TodoList()
    tdList.add_todo("testaa1")
    tdList.add_todo("testaa2")
    tdList.add_todo("testaa3")
    
    assert len(tdList.todos) == 3
    
def test_should_return_added_todo():
    tdList = TodoList()
    result = tdList.add_todo("testaa1")
    expected = { "id": 1,
                 "description": "testaa1",
                 "completed": False}
    assert result == expected
    
def test_should_mark_todo_completed():
    tdList = TodoList()
    tdList.add_todo("testi1")
    tdList.complete_todo(1)
    result = tdList.get_todo(1)
    expected = { "id": 1,
                 "description": "testi1",
                 "completed": True}
    assert result == expected
    
def test_should_throw_ValueError_when_completing_task_that_is_not_found():
    tdList = TodoList()
    tdList.add_todo("testaa1")
    tdList.delete_todo(1)
    with pytest.raises(ValueError):
        tdList.complete_todo(1)
    

def test_should_return_removed_todo():
    tdList = TodoList()
    tdList.add_todo("testaa")
    expected = { "id": 1,
                 "description": "testaa",
                 "completed": False
                 }
    result = tdList.delete_todo(1)
    assert result == expected
    
    
def test_should_raise_ValueError_when_trying_to_get_deleted_todo():
    tdList = TodoList()
    tdList.add_todo("testaa")
    tdList.delete_todo(1)

    with pytest.raises(ValueError): 
        tdList.get_todo(1)
        
def test_should_raise_ValueError_when_trying_to_delete_already_deleted_todo():
    tdList = TodoList()
    tdList.add_todo("testaa")
    tdList.delete_todo(1)
    with pytest.raises(ValueError):
        tdList.delete_todo(1)
        
        
def test_should_return_all_todos_when_list_has_one_todo():
    tdList = TodoList()
    tdList.add_todo("testaa")
    result = tdList.get_all_todos()
    expected = [{ "id": 1,
                 "description": "testaa",
                 "completed": False}]
    assert result == expected
    
def test_should_return_three_todos_when_list_has_three_todos():
    tdList = TodoList()
    tdList.add_todo("testaa1")
    tdList.add_todo("testaa2")
    tdList.add_todo("testaa3")
    result = tdList.get_all_todos()
    expected = [{ "id": 1,
                  "description": "testaa1",
                  "completed": False},
                { "id": 2,
                  "description": "testaa2",
                  "completed": False},
                { "id": 3,
                  "description": "testaa3",
                  "completed": False}
                ]
    assert result == expected
    
def test_should_return_empty_list_when_all_todos_are_deleted():
    tdList = TodoList()
    tdList.add_todo("testaa1")
    tdList.add_todo("testaa2")
    tdList.delete_todo(2)
    tdList.delete_todo(1)
    result = tdList.get_all_todos()
    expected = []
    assert result == expected