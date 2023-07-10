#!/usr/bin/python3
"""
This a script that checks if the object is an instance of class that inherited
(directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class
    """

    return isinstance(obj, a_class)
