import functools
from datetime import datetime

def log_operation(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[{datetime.now().isoformat()}] Calling '{func.__name__}'")
        result = func(*args, **kwargs)
        print(f"[{datetime.now().isoformat()}] Finished '{func.__name__}'")
        return result
    return wrapper