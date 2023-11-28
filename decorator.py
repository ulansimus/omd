from functools import wraps
from random import randint


def log(message_sample: str):
    """возвращает функцию декоратор."""
    def decorator(func):
        """декоратор, выводящий действие и время действия."""

        @wraps(func)
        def wrapper(*args, **kwargs):
            p = randint(10, 30)
            print(f' {message_sample} {p}мин ')
        return wrapper

    return decorator
