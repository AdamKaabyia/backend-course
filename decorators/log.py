import functools
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')


def log_operation(func):
    """Decorator to log function operation."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            logging.info(f"{func.__name__.capitalize()} operation with {args}: {result}")
            return result
        except Exception as e:
            logging.error(f"Error during {func.__name__} operation with {args}: {e}")
            return None

    return wrapper


def safe_divide(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError:
            logging.error("Division by zero error.")
            return None

    return wrapper
