#!/usr/bin/python3
"""Defines classes of Node and SinglyLinkedList"""


class Node:
    """Class that defines Node"""
    def __init__(self, data, next_node=None):
        """Initializes instance of Node
        args:
            data (int): integer data
            next_node: Node object
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets data"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """Sets data
        Raises:
            TypeError: if data is not integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Gets next_node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Sets next_node
        Raises:
            TypeError: if next_node is not Node object
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Class that defines SinglyLinkedList."""
    def __init__(self):
        """Initializes instance of SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts, in a sorted order, new Node in a linked list.
        args:
            value: Node object.
        """
        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node
            return

        if value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        cur = self.__head
        tmp = self.__head
        while cur.next_node and value > cur.data:
            tmp = tmp.next_node
            if value < tmp.data or value == tmp.data:
                new_node.next_node = tmp
                cur.next_node = new_node
                return
            cur = cur.next_node

        if cur.next_node:
            pass
        else:
            cur.next_node = new_node

    def __str__(self):
        """Returns string of node"""
        node = self.__head
        node_list = []
        while node:
            node_list.append(node.data)
            node = node.next_node
        res = "\n".join(str(itm)for itm in node_list)
        return f"{[res]}"
    
sll = SinglyLinkedList()
sll.sorted_insert(2)
sll.sorted_insert(5)
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
sll.sorted_insert(5)
sll.sorted_insert(12)
sll.sorted_insert(3)
print(sll)
