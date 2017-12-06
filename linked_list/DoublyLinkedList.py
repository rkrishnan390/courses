# Python implementation of a doubly Linked List

from typing import Union

class Node(object):
    def __init__(self, data: int=None, forward_link: 'Node'=None,
                 reverse_link: 'Node'=None):
        self._data = data
        self._forward_link = forward_link
        self._reverse_link = reverse_link

    @property
    def data(self) -> int:
        return self._data

    @data.setter
    def data(self, value: int):
        self._data = value

    @property
    def forward_link(self) -> 'Node':
        return self._forward_link

    @forward_link.setter
    def forward_link(self, value: 'Node'):
        self._forward_link = value

    @property
    def reverse_link(self) -> 'Node':
        return self._reverse_link

    @reverse_link.setter
    def reverse_link(self, value: 'Node'):
        self._reverse_link = value


class DoublyLinkedList(object):
    def __init__(self, head: Node=None):
        self._head = head

    @property
    def head(self) -> Node:
        return self._head

    @head.setter
    def head(self, value: Node):
        self._head = value

    def insert(self, value: int, position: int=None):
        # Init the new node
        new_node = Node(data=value, forward_link=None, reverse_link=None)

        # Empty list
        if (self.length() == 0) or (position == 0):
            # Head insert
            if self.length():
                # Get the first node
                first_node = self.head

                # Set the links
                new_node.forward_link = first_node
                first_node.reverse_link = new_node

            # Set the head anyways
            self.head = new_node

        # Add to the tail by default
        elif position is None:
            # Get the last node in the list
            last_node = self.getNodeRecursive(self.length()-1)

            # Forward link of last node is new node
            last_node.forward_link = new_node

            # Reverse link of new node is last node
            new_node.reverse_link = last_node

        # Arbitrary position
        else:
            # Get the node at the position and the node just before it
            left_node = self.getNodeRecursive(position-1)
            right_node = self.getNodeRecursive(position)

            # Set the links for the new node
            new_node.forward_link = right_node
            new_node.reverse_link = left_node

            # Fix the links for the old nodes
            left_node.forward_link = new_node
            right_node.reverse_link = new_node

    def delete(self, position: int=None):
        # If no position specified; remove from end
        if position is None:
            last_node = self.getNodeRecursive(self.length()-1)
            left_node = last_node.reverse_link

            last_node.reverse_link = None
            left_node.forward_link = None

        # If position 0, reset the head
        elif position == 0:
            first_node = self.head
            self.head = first_node.forward_link
            first_node.forward_link = None

        # Arbitrary position
        else:
            left_node = self.getNodeRecursive(position-1)
            current_node = left_node.forward_link
            right_node = left_node.forward_link.forward_link

            current_node.forward_link = None
            current_node.reverse_link = None
            left_node.forward_link = right_node
            right_node.reverse_link = left_node

    def reverseRecursively(self, current_node: Node=None):
        # Init
        if current_node is None:
            current_node = self.head

        # Stop condition
        if current_node.forward_link is None:
            self.head = current_node
            return 0
        else:
            self.reverseRecursively(current_node.forward_link)
            current_node.forward_link.forward_link = current_node
            current_node.reverse_link = current_node.forward_link
            current_node.forward_link = None

    def length(self) -> int:
        count = 1
        current_node = self.head

        if current_node is None:
            return 0

        while current_node.forward_link is not None:
            count += 1
            current_node = current_node.forward_link

        return count

    def getNode(self, position: int=0) -> Node:
        # Last node
        if position == -1:
            max_count = self.length() - 1
        else:
            max_count = position

        current_node = self.head
        for i in range(max_count):
            current_node = current_node.forward_link

        return current_node

    def getNodeRecursive(self, position: int, current_node: Node=None) -> Node:
        if current_node is None:
            current_node = self.head
        if position > self.length()-1:
            print("Out of bounds error.")
            return None

        if position == 0:
            return current_node
        else:
            position -= 1
            current_node = self.getNodeRecursive(position,
                                                 current_node.forward_link)
            return current_node

    def getEntry(self, position: int) -> int:
        return self.getNode(position).data

    def printBackwardRecursively(self, current_node: Node=None):
        if current_node is None:
            current_node = self.head

        if current_node.forward_link is None:
            print(current_node.data)
            return 0
        else:
            self.printBackwardRecursively(current_node.forward_link)
            print(current_node.data)

    def printForwardRecursively(self, current_node: Node=None):
        if current_node is None:
            current_node = self.head

        if current_node.forward_link is None:
            print(current_node.data)
            return 0
        else:
            print(current_node.data)
            self.printForwardRecursively(current_node.forward_link)





















