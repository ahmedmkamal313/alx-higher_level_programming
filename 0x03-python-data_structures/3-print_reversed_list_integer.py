#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    # loop through my_list using negative idexing.
    for i in range(len(my_list) - 1, -1, -1):
        # print the current element using str.format()
        print("{:d}".format(my_list[i]))
