#!/usr/bin/python3
""" text_indentation returns "text" in the specified format:
2 newlines after each ['.', '?', ':']
"""


# Define a function that takes one parameter: a text string
def text_indentation(text):
    """ prints "text" with 2 newlines after each of these char: ['.', '?', ':']
    checks if "text" is a str
    first loop removes spaces after each required chars
    second loop adds 2 newlines after each required chars
    """

    # Raise a TypeError if text is not a string
    if type(text) != str:
        raise TypeError("text must be a string")

    # Define a list of characters that trigger a new line
    special_chars = ['.', '?', ':']

    # Removes the space after special chars
    index = 0
    for char in text:
        if char in special_chars:
            if text[index + 1] == " ":
                # Slice the text to remove the space
                text = text[:index + 1] + text[index + 2:]
        else:
            index += 1

    # Cats '\n\n' after the special char with removed space
    index = 0
    for char in text:
        if char in special_chars:
            # Slice the text to insert two new lines
            text = text[:index + 1] + '\n\n' + text[index + 1:]
            index += 3
        else:
            index += 1

    # Print the formatted text without an extra new line at the end
    print(text, end='')
