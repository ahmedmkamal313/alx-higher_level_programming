#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    # check if idx is valid
    if 0 <= idx < len(my_list):
        # loop through the list from idx to the end
        for i in range(idx, len(my_list) - 1):
            # shift the elements to the left by one position
            my_list[i] = my_list[i + 1]
        # remove the last element of the list
        my_list.pop()
    # return the modified list
    return my_list
