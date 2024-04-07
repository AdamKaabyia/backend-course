import logging
import functools

logging.basicConfig(level=logging.INFO)

def log_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Executing: {func.__name__}")
        try:
            result = func(*args, **kwargs)
            logging.info(f"Success: {func.__name__}")
            return result
        except Exception as e:
            logging.error(f"Error in {func.__name__}: {e}")
            raise
    return wrapper
