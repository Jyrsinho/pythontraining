from time import sleep
from dataclasses import dataclass
import requests

API_URL = "https://official-joke-api.appspot.com/jokes/random"


@dataclass
class Joke:
    type: type
    id: int
    setup: str
    punchline: str


def get_random_joke() -> Joke:
    return Joke(**requests.get(API_URL).json())


def print_random_joke() -> None:
    joke = get_random_joke()
    print(joke.setup)
    sleep(2)
    print(joke.punchline)


if __name__ == "__main__":
    print_random_joke()

