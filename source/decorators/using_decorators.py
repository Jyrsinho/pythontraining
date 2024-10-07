from source.decorators.decorators import do_twice




@do_twice
def say_hello(*args, **kwargs):
    if len(args) == 1 and isinstance(args[0], str):
        print(f"Hello: {args[0]}")
    if len(args) == 2:
        print(f"Hello: {args[0]} and {args[1]}")
    else: print("hello")


say_hello()
say_hello("Timo")
say_hello("Bob", "Timo")
