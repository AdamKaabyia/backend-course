from decorators.log import log_operation, safe_divide


@log_operation
def multiply(x, y):
    return x * y


@log_operation
@safe_divide
def divide(x, y):
    return x / y
