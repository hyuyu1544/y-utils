from functools import wraps

import time


# TODO:: 打包給pip install可用
# TODO:: 確定好結構，及每個func名稱，說明文件


def Counter(func):
    """Decorator for counting timer."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        pass


def Timer(func):
    """Decorator for timming timer."""
    pass


def Retry_timer(func):
    """Decorator for retry func."""
    pass
