#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): First operand.
        b (int or float): Second operand (default is 98).

    Returns:
        int: The addition of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.

    Example:
        >>> add_integer(1, 2)
        3
        >>> add_integer(100, -2)
        98
        >>> add_integer(2)
        100
        >>> add_integer(100.3, -2)
        98
        >>> add_integer(4, "School")
        Traceback (most recent call last):
            ...
        TypeError: b must be an integer
        >>> add_integer(None)
        Traceback (most recent call last):
            ...
        TypeError: a must be an integer
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    return int(a) + int(b)
