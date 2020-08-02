from functools import wraps
import logging
import time


# TODO:: 打包給pip install可用
# TODO:: 確定好結構，及每個func名稱，說明文件


def Counter(func):
    """Decorator for counting timer."""
    pass


def Timer(func):
    """Decorator for timming timer."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        ans = func(*args, **kwargs)
        end_time = time.time()
        running_time = end_time-start_time
        logging.debug(f'{func.__name__} running in {running_time} sec.')
        return ans
    return wrapper


def Retry_timer(func):
    """Decorator for retry func."""
    pass
