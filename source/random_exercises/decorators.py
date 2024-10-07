
def parent():
    print("Printing from parent()")
    
    def first_child():
        print("Printing from first_child()")
    
    def second_child():
        print("Printing from second_child()")
    
    second_child()
    first_child()


def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")



say_whee = decorator(say_whee)

print(say_whee())

print("--------")

parent()
# This is uncallable because it is a local variable inside a parent function first_child()

print("-------")
decorated_parent = decorator(parent)
print(decorated_parent()) 
