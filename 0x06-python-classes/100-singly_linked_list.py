#!/usr/bin/python3
"""
Singly Linked Lists Module

This module defines two classes: Node and SinglyLinkedList, representing
a node of a singly linked list and the singly linked list itself.
"""


class Node():
    """
    Defines a node of a singly linked list.

    Attributes:
        data (int): The value stored in the node.
        next_node (Node): The reference to the next node in the list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a Node object with the given data and next node.

        Args:
            data (int): The value of the node.
            next_node (Node): The next node in the list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get or set the data value of a node."""
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data value of a node.

        Args:
            value (int): The value to set.

        Raises:
            TypeError: If the value is not an integer.
        """
        if type(value) is int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """Get or set the next node of the current node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node of the current node.

        Args:
            value (Node or None): The next node or None.

        Raises:
            TypeError: If the value is not a Node object or None.
        """
        if type(value) is Node or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object or None")


class SinglyLinkedList():
    """
    Defines a singly linked list.

    Attributes:
        __head (Node): The head node of the list.
    """

    def __init__(self):
        """Initializes an empty singly linked list."""
        self.__head = None

    def __str__(self):
        """
        Returns a string representation of the singly linked list.

        Returns:
            str: The string representation of the list.
        """
        sll_str = ""
        node = self.__head

        while node is not None:
            sll_str += str(node.data) + '\n'
            node = node.next_node

        return sll_str[:-1]

    def sorted_insert(self, value):
        """
        Inserts a new node with the given value into the list in sorted order.

        Args:
            value (int): The value to insert.
        """
        if self.__head is None or self.__head.data >= value:
            self.__head = Node(value, self.__head)
        else:
            current = self.__head
            while (current.next_node is not None
                    and current.next_node.data < value):
                current = current.next_node

            current.next_node = Node(value, current.next_node)
