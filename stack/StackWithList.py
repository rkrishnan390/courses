
class Stack(object):
    def __init__(self):
        self._stack = list()
        self._head = -1

    @property
    def stack (self) -> list:
        return self._stack

    @property
    def head(self) -> int:
        return self._head

    @head.setter
    def head(self, value: int):
        self._head = value

    def push(self, value: int):
        # Increment pointer
        self.head += 1

        # Not enough room in the stack, so append
        if self.head >= len(self.stack):
            self.stack.append(value)

        # Sufficient room in the stack, overwrite
        else:
            self.stack[self.head] = value

    def pop(self):
        if self.isEmpty():
            print("Nothing in stack.")
            return None
        val = self.stack[self.head]
        self.head -= 1
        return val

    def top(self):
        if self.isEmpty():
            print("Nothing in stack.")
            return None
        return self.stack[self.head]

    def isEmpty(self):
        return self.head == -1
