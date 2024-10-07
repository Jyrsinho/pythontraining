from source.decorators.decorators import do_twice




@do_twice
def say_hello(*args, **kwargs):
    if len(args) == 1 and isinstance(args[0], str):
        print(f"Hello: {args[0]}")
    else: print("hello")


say_hello()
say_hello("Timo")
