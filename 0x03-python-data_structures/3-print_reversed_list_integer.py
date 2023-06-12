#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    # loop through my_list using negative idexing.
    for i in reversed(my_list):
        # print the current element using str.format()
        print("{:d}".format(i))
