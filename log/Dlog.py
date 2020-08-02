from functools import wraps
import logging

# TODO:: 改logging的root name


def Error_Log(func):
    """Decorator for raise with Exception."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.critical(f'{func.__name__}:{e}')
    return wrapper
