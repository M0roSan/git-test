import sys


def divide(a:int, b:int) -> int:
    try:
        return a / b
    except ZeroDivisionError as e:
        sys.exit(e)