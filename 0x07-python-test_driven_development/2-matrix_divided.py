#!/usr/bin/python3
"""

This module is composed by a function that divides the numbers of a matrix

"""


def matrix_divided(matrix, divisor):
    """ Function that divides the integer/float numbers of a matrix

    Args:
        matrix: list of a lists of integers/floats
        divisor: number which divides the matrix

    Returns:
        A new matrix with the result of the division

    Raises:
        TypeError: If the elements of the matrix aren't lists
                   If the elemetns of the lists aren't integers/floats
                   If divisor is not an integer/float number
                   If the lists of the matrix don't have the same size

        ZeroDivisionError: If divisor is zero


    """

    # Check if divisor is a valid number
    if not isinstance(divisor, (int, float)):
        raise TypeError("divisor must be a number")

    # Check if divisor is zero
    if divisor == 0:
        raise ZeroDivisionError("division by zero")

    # Define the error message for invalid matrix elements
    msg_type = "matrix must be a matrix (list of lists) of integers/floats"

    # Check if matrix is a valid list
    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg_type)

    # Initialize the variable to store the length of each row
    row_length = 0

    # Define the error message for inconsistent row sizes
    msg_size = "Each row of the matrix must have the same size"

    # Loop through each row in the matrix
    for row in matrix:
        # Check if row is a valid list
        if not row or not isinstance(row, list):
            raise TypeError(msg_type)

        # Check if row length is consistent with previous rows
        if row_length != 0 and len(row) != row_length:
            raise TypeError(msg_size)

        # Loop through each element in the row
        for element in row:
            # Check if element is a valid number
            if not isinstance(element, (int, float)):
                raise TypeError(msg_type)

        # Update the row length variable
        row_length = len(row)

    # Create an empty list to store the new matrix
    new_matrix = []

    # Loop through each row in the matrix
    for row in matrix:
        # Create a new row by dividing each element
        # by the divisor and rounding to two decimals
        new_row = [round(element / divisor, 2) for element in row]

        # Append the new row to the new matrix
        new_matrix.append(new_row)

    # Return the new matrix
    return (new_matrix)
