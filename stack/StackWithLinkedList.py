
from LinkedList import LinkedList

class Stack(object):
    def __init__(self):
        self._stack = LinkedList()

    @property
    def stack(self) -> LinkedList:
        return self._stack

    def push(self, value: int):
        # Add to the stack
        self.stack.insert(value)

    def pop(self):
        # Get the value and delete the node
        val = self.top()
        if val is None:
            return None
        else:
            self.stack.delete()
            return val

    def top(self):
        val = self.stack.getEntry(-1)
        if val is None:
            print("Stack is empty")
            return None
        else:
            return val

    def isEmpty(self):
        return self.stack.head is None