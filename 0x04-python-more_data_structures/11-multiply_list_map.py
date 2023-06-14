#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    # use the map function to apply a lambda function that,
    # multiplies each element by number.
    # use the list function to convert the map object to a list.
    return list(map(lambda x: x * number, my_list))
