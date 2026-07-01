def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b

def square_root(a):
    return a ** 0.5

if __name__ == "__main__":
    print("add:", add(4, 2))
    print("subtract:", subtract(4, 2))
    print("multiply:", multiply(4, 2))
    print("divide:", divide(4, 2))
    print("sqrt:", square_root(-4))
