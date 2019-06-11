import sys


def divide(a:int, b:int, bDIVIDEa:bool) -> int:
    """divide function. if b is 0, then error"""
    if bDIVIDEa:
        a, b = b, a
    try:
        return a / b
    except ZeroDivisionError as e:
        sys.exit(e)