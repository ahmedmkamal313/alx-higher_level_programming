#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    # check if idx is valid
    if 0 <= idx < len(my_list):
        # loop through the list from idx to the end
        for i in range(idx, len(my_list) - 1):
            # shift the elements to the left by one position
            my_list[i] = my_list[i + 1]
        # create a new list without the last element using slicing
        new_list = my_list[:-1]
        # assign the new list back to the original list
        my_list = new_list
    # return the modified list
    return my_list
