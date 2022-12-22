#!/usr/bin/python3
"""Class Define SinglyLinkedList"""


class Node:
    """Represent of node"""
    def __init__(self, data, next_n=None):
        self.__data = data
        self.__next_n = next_n

    @property
    def data(self):
        """Specail method for retrive data"""
        return self.__data

    @data.setter
    def data(self, value):
        """special setter for data"""
        if isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_n(self):
        """Special getter for next node"""
        return self.__next_n

    @next_n.setter
    def next_n(self, value):
        """special setter of next node with constraint
            Args:
                value (Node): Represnt Node
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_n = value


class SinglyLinkedList:
    """Creating the list"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """method for insert node into list
            Args:
                value (Node) : instance of Node
        """
        new = Node(value)
        if self.__head is None:
            self.__head = new
        else:
            current = self.__head
            while current is not None:
                if current.next_n is None:
                    current.next_n = new
                    break
                elif value <= current.data:
                    new.next_n = current
                    self.__head = new
                    break
                elif value <= (current.next_n).data:
                    new.next_n = current.next_n
                    current.next_n = new
                    break
                current = current.next_n

    def __str__(self):
        """overriddin __str__ method from object class"""
        current = self.__head
        ans = ""
        while current is not None:
            ans =  ans + str(current.data) + '\n'
            current = current.next_n
        return ans[:-1]
