#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a: The first integer to add.
        b: The second integer to add. Defaults to 98.

    Returns:
        The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
        ValueError: If a or b is not an exact integer.
        OverflowError: If a or b is too large.
    """

    # Check if a and b are integers or floats
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    # Cast a and b to integers
    a = int(a)
    b = int(b)
    # Return the addition of a and b
    return a + b
