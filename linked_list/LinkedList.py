# Python implementation of a singly Linked List

from typing import Union

class Node(object):
    def __init__(self, data: int=None, link: 'Node'=None):
        self._data = data
        self._link = link

    @property
    def data(self) -> int:
        return self._data

    @data.setter
    def data(self, value: int):
        self._data = value

    @property
    def link(self) -> 'Node':
        return self._link

    @link.setter
    def link(self, value: 'Node'):
        self._link = value


class LinkedList(object):
    def __init__(self, head: Node=None):
        self._head = head

    @property
    def head(self) -> Union['Node',None]:
        return self._head

    @head.setter
    def head(self, value: 'Node'):
        self._head = value

    def insert(self, value: int, position: int=None):
        # Init
        new_node = Node(value)

        # Add to the beginning
        if (position==0) or (self.length() == 0):
            new_node.link = self.head
            self.head = new_node

        # Add to the end
        elif position is None:
            # Get the last node
            current_node = self.getNode(-1)

            # Update the link of the last node
            current_node.link = new_node

        # Add to arbitrary position
        else:
            # Get the preceding node
            ith_node = self.getNode(position-1)

            # Set the link of new node to the link of preceding node
            new_node.link = ith_node.link

            # Update the link of preceding node to new node
            ith_node.link = new_node

    def delete(self, position: int=None):
        # Delete the first entry
        # Only 1 node
        if self.length() == 1:
            self.head = None
        elif position==0:
            # Get the 2nd node and set it as the new head
            ith_node = self.getNode(1)
            self.head = ith_node

        # Delete last entry
        elif position is None:
            # Reset link of second to last node
            ith_node = self.getNode(self.length()-2)
            ith_node.link = None

        # Delete arbitrary entry
        else:
            # Get the preceding node and current node
            ith_node = self.getNode(position-1)
            current_node = self.getNode(position)

            # Set the link of the preceding node to the link of the current node
            ith_node.link = current_node.link

    def reverse(self):
        # Get the last node
        last_node = self.getNode(-1)

        # Set the last node as the first prev_node
        prev_node = last_node
        for i in range(self.length()-2, -1, -1):
            # Get the current node starting with the 2nd to last
            current_node = self.getNode(i)

            # Address of prev node is now the current node
            prev_node.link = current_node

            # Set the prev node as the current node
            prev_node = current_node

        # At the first node, so set its link to null and the head to the last node
        prev_node.link = None
        self.head = last_node

    def reverseRecursively(self, node: 'Node'):
        if node.link is None:
            self.head = node
            return 0
        else:
            self.reverseRecursively(node.link)
            node.link.link = node
            node.link = None

    def forwardPrint(self, node: 'Node'):
        print(node.data)
        if node.link is None:
            return
        else:
            self.forwardPrint(node.link)

    def backwardPrint(self, node: 'Node'):
        if node.link is None:
            print(node.data)
            return
        else:
            self.backwardPrint(node.link)
            print(node.data)

    def getEntry(self, position: int=-1) -> int:
        try:
            return self.getNode(position).data
        except AttributeError as _:
            return None

    def getNode(self, position: int) -> Union['Node', None]:
        # Last node
        if position == -1:
            max_count = self.length() - 1
        else:
            max_count = position

        # Init
        current_node = self.head
        for count in range(max_count):
            current_node = current_node.link
        return current_node

    def length(self) -> int:
        count = 1
        current_node = self.head
        if current_node is None:
            count = 0
        else:
            while current_node.link is not None:
                current_node = current_node.link
                count += 1
        return count
