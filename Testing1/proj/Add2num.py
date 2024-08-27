# Add2num

def add2num(x, y):
    """
    Adds 2 given numbers and returns the sum.
    >>> add2num(6, 7)
    13
    >>> add2num(-8.5, 7)
    -1.5
    >>> add2num(7, 'hello')
    Traceback (most recent call last):
    ValueError: unsupported operand type(s) for +: 'int' and 'str'
    """
    return x + y
