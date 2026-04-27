def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def average(numbers):
    if len(numbers) == 0:
        raise ValueError("List is empty")
    return sum(numbers) / len(numbers)