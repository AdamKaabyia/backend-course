import logging
from functools import wraps

def log_decorator(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__}")
        result = await func(*args, **kwargs)
        logging.info(f"{func.__name__} completed")
        return result
    return wrapper
