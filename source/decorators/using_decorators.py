from source.decorators.decorators import do_twice, timer


@do_twice
def say_hello(*args, **kwargs):
    if len(args) == 1 and isinstance(args[0], str):
        print(f"Hello: {args[0]}")
    if len(args) == 2:
        print(f"Hello: {args[0]} and {args[1]}")
    else: print("hello")


@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


@timer
def waste_some_time(num_times):
    for i in range(num_times):
        sum([number**2 for number in range(10_000)])




say_hello()
say_hello("Timo")
say_hello("Bob", "Timo")

print()
print("--------********-------------")
print()

hi_adam = return_greeting("Adam")

print(hi_adam)

print(say_hello.__name__)

print()
print("--------********-------------")
print()

waste_some_time(100)
waste_some_time(1)
waste_some_time(10000)