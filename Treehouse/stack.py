""" A Python stack module."""


class Node:
    """ A node for building a singly-linked list."""
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, next_node):
        self.next_node = next_node


class LinkedList:
    """ A simple linked list."""
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        new_node = Node(value)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        place = self.head
        node_count = 0
        while place:
            node_count += 1
            place = place.get_next()
        return node_count

    def delete_last(self):
        if self.head is not None:
            self.head = self.head.get_next()
