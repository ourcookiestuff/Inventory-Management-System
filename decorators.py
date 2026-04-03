import functools
import time
from datetime import datetime

def log_operation(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Calling {func.__name__}...")
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {func.__name__} completed in {elapsed:.4f}s")
        return result
    return wrapper