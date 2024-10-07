

def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):      # The wrapper_do_twice() inner function now accepts any number of arguments 
        func(*args, **kwargs)                   # and passes them on to the function that it decorates.
        func(*args, **kwargs)
    return wrapper_do_twice
