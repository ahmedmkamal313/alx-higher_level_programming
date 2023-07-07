#!/usr/bin/python3
"""This module contains a function that multiplies two matrices using NumPy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy

    Args:
        m_a (list of lists): the first matrix
        m_b (list of lists): the second matrix

    Returns:
        numpy.ndarray: the product of m_a and m_b

    Raises:
        TypeError: if m_a or m_b is not a list, a list of lists,
        or contains non-numbers
        ValueError: if m_a or m_b is empty or if their shapes are incompatible
    """
    # Convert the inputs to numpy arrays
    try:
        a = np.array(m_a)
        b = np.array(m_b)
    except Exception:
        raise TypeError("m_a and m_b must be a list of lists")

    # Check if the arrays are empty
    if a.size == 0 or b.size == 0:
        raise ValueError("m_a or m_b can't be empty")

    # Check if the arrays contain only numbers
    if not (np.issubdtype(a.dtype, np.number) and
            np.issubdtype(b.dtype, np.number)):
        raise TypeError("m_a and m_b should contain only integers or floats")

    # Check if the arrays are 2D
    if len(a.shape) != 2 or len(b.shape) != 2:
        raise TypeError("m_a and m_b must be a list of lists")

    # Check if the arrays have the same inner dimensions
    if a.shape[1] != b.shape[0]:
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform the multiplication using numpy.dot
    return np.dot(a, b)
