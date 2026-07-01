import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def add(a, b):
    logger.info("Adding %s + %s", a, b)
    return a + b


def subtract(a, b):
    logger.info("Subtracting %s - %s", a, b)
    return a - b


def multiply(a, b):
    logger.info("Multiplying %s * %s", a, b)
    return a * b


def divide(a, b):
    logger.info("Dividing %s / %s", a, b)
    return a / b


def square_root(a):
    logger.info("Square root of %s", a)
    return a**0.5


if __name__ == "__main__":
    print("add:", add(4, 2))
    print("subtract:", subtract(4, 2))
    print("multiply:", multiply(4, 2))
    print("divide:", divide(4, 2))
    print("sqrt:", square_root(4))
