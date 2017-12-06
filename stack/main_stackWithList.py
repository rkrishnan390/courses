
from StackWithList import Stack

s = Stack()

for i in range(5):
    s.push(i)

assert s.top() == 4, ["top() did not return 4"]
assert s.pop() == 4, ["pop() did not return 4"]
assert s.pop() == 3, ["pop() did not return 3"]
s.push(3)
assert s.top() == 3
s.pop()
assert s.pop() == 2, ["pop() did not return 2"]
assert s.pop() == 1, ["pop() did not return 1"]
assert s.top() == 0, ["top() did not return 0"]
assert s.isEmpty() == False, ["Stack is empty when it shouldn't be"]

print("Stack is correct!")
