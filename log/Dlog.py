from functools import wraps
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s:[%(asctime)s]:%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)


def Error_Log(func):
    """Decorator for logging Exception but not stop the program."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.debug(f'{func.__name__}:{e}', exc_info=True)
    return wrapper
