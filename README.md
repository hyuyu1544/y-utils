# yutils: provide some python tools which often used
<br>
All tools are be provided as decorators.

## Installation

Not provide using `pip` install yet.

## Usage

```
from yutils import *
```

All functions:

### Counter

A decorator to count the number of times the function is called.

### Timer

A decorator to calculate function execution time.

### Retry_timer

A decorator to help if function execution fail, how many times will retry and what is the retry interval.

Use ```functools.partial```to change parameters.
<br>
example:
```
from functools import partial
My_retry_timer = partial(Retry_timer, interval=1, retry_times=5)

@My_retry_timer
def foo(*arg,**kwargs):
    pass
```

### Schedule

A decorator to schedule the function execution time.

Use ```functools.partial```to change parameters.
<br>
example:
```
from functools import partial
My_schedule = partial(Schedule, interval=60)

@My_schedule
def foo(*arg,**kwargs):
    pass
```

### Error_Log

A decorator for logging Exception but not stop the program.

### TypePrints

A decorator for print func.__doc__ like type prints.
