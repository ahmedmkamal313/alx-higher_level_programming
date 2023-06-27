#!/usr/bin/python3
"""This module defines a class Node and a class SinglyLinkedList"""


class Node:
    """This class represents a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """This method initializes he node with the given data and next_node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """This method returns the data of the node"""
        return self.__data

    @data.setter
    def data(self, value):
        """This method sets the data of the node"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """This method returns the next_node of the node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """This method sets the next_node of the node"""
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """This class represents a singly linked list"""

    def __init__(self):
        """This method initializes the linked list with an empty head"""
        self.__head = None

    def sorted_insert(self, value):
        """
        This method inserts a new Node into the correct
        sorted position in the list (increasing order)
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while (current.next_node is not None and
                    current.next_node.data < value):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """This method returns a string representation of the linked list"""
        result = ""
        current = self.__head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result[:-1]
