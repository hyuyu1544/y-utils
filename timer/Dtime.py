from functools import wraps,partial
from settings import logging
import time

logger = logging.getLogger(__name__)



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
        logger.debug(f'{func.__name__} running in {running_time} sec.')
        return ans
    return wrapper
    

def Retry_timer(func,interval=3,retry_times=3):
    """Decorator for retry func."""
    # TODO:: add func for user to input interval and retry_times
    @wraps(func)
    def wrapper(count=1, interval=interval, retry_times=retry_times, *args, **kwargs):
        try:
            logger.debug(f'Try func:{func.__name__} {count} times.')
            return func(*args, **kwargs)
        except Exception as e:
            logger.warning(f'There have some error: {e}')
            count += 1
            if count <= retry_times:
                logger.debug(f'Will retry in {interval} sec.')
                time.sleep(interval)
                return wrapper(count=count,interval=interval, retry_times=retry_times,*args,**kwargs)
            else:
                logger.critical(f'Failed to execute func:{func.__name__}')
    return wrapper


