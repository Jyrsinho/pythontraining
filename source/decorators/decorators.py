
import functools
import time


def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__}() in {run_time:.4f} secs")
        return value
    return wrapper_timer


def decorator_example(func):
    @functools.wraps(func)
    def wrapper_decorator_example(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator_example


def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):      # The wrapper_do_twice() inner function now accepts any number of arguments 
        func(*args, **kwargs)                   # and passes them on to the function that it decorates.
        return func(*args, **kwargs)
    return wrapper_do_twice


