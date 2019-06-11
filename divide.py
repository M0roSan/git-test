import sys


def divide(a:int, b:int) -> int:
    """divide function. if b is 0, then error"""
    try:
        return a / b
    except ZeroDivisionError as e:
        sys.exit(e)