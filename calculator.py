import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

history = []


def validate_numbers(*args):
    """Raise an error if any input is not a number."""
    for value in args:
        if not isinstance(value, (int, float)):
            raise TypeError(f"Invalid input: {value} is not a number")


def add(a, b):
    validate_numbers(a, b)
    logger.info("Adding %s + %s", a, b)
    result = a + b
    history.append(f"add({a}, {b}) = {result}")
    return a + b


def subtract(a, b):
    validate_numbers(a, b)
    logger.info("Subtracting %s - %s", a, b)
    result = a - b
    history.append(f"subtract({a}, {b}) = {result}")
    return a - b


def multiply(a, b):
    validate_numbers(a, b)
    logger.info("Multiplying %s * %s", a, b)
    result = a * b
    history.append(f"multiply({a}, {b}) = {result}")
    return a * b


def divide(a, b):
    validate_numbers(a, b)
    if b == 0:
        raise ValueError("Cannot divide by zero")
    logger.info("Dividing %s / %s", a, b)
    result = a / b
    history.append(f"divide({a}, {b}) = {result}")
    return a / b


def square_root(a):
    validate_numbers(a)
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")
    logger.info("Square root of %s", a)
    result = a**0.5
    history.append(f"square_root({a}) = {result}")
    return a**0.5


def power(base, exponent):
    validate_numbers(base, exponent)
    logger.info("Power %s ^ %s", base, exponent)
    result = base**exponent
    history.append(f"power({base}, {exponent}) = {result}")
    return result


def average(*numbers):
    validate_numbers(*numbers)
    if len(numbers) == 0:
        raise ValueError("Cannot take average of no numbers")
    logger.info("Average of %s", numbers)
    result = sum(numbers) / len(numbers)
    history.append(f"average{numbers} = {result}")
    return result


def get_history():
    """Return the list of all calculations performed."""
    return history


if __name__ == "__main__":
    print("add:", add(4, 2))
    print("subtract:", subtract(4, 2))
    print("multiply:", multiply(4, 2))
    print("divide:", divide(4, 2))
    print("sqrt:", square_root(4))
    print("history:", get_history())
