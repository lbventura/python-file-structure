import random

from .random_parameters import LENGTH_OF_RANDOM_LIST


def create_random_integer() -> int:
    random_list = [random.randint(3, 5) for _ in range(LENGTH_OF_RANDOM_LIST)]
    return random_list[random.randint(0, len(random_list) - 1)]
