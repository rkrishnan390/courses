
import os
from rahulk_DoublyLinkedList import DoublyLinkedList

def clear():
    os.system('clear')

def printList(linked_list):
    for position in range(linked_list.length()):
        value = linked_list.getEntry(position)
        print("Value at %s is %s" % (position, value))
    print(''.join(['*']*23))

def testInsertAtBeginning(dll: DoublyLinkedList):
    # Add values 2, 4, 6
    dll.insert(2)
    dll.insert(4)
    dll.insert(6)
    print("After adding values '2, 4, 6'")
    printList(dll)


def testInsertAtN(dll: DoublyLinkedList):
    # Insert value 3 into position
    dll.insert(3, 1)
    print("After inserting value 3 into position 1")
    printList(dll)

    # Insert value 5 at position 3, and 1 at position 0
    dll.insert(5, 3)
    dll.insert(1, 0)
    print("After inserting value 5 at position 3, and value 1 at position 0")
    printList(dll)

    # Insert values 7, 8, and 10; then insert value 9 at position 8
    dll.insert(7)
    dll.insert(8)
    dll.insert(10)
    dll.insert(9, 8)
    print("After inserting values 7, 8, and 10; then inserting value 9 at position 8")
    printList(dll)

    print("Final list.")
    printList(dll)


def testDelete(dll: DoublyLinkedList):
    print("Test delete.")

    dll.delete()
    print("After deleting last element.")
    printList(dll)

    dll.delete(0)
    print("After deleting first element.")
    printList(dll)

    dll.delete(4)
    print("After deleting fourth element.")
    printList(dll)


def initialTest():
    # Instantiate the list
    dll = DoublyLinkedList()

    # Some beginning inserts
    testInsertAtBeginning(dll)

    # Some arbitrary inserts
    testInsertAtN(dll)

    # Some Deletions
    testDelete(dll)


def reverseTest():
    dll = DoublyLinkedList()

    for i in range(1,11):
        dll.insert(i)

    print("Initial list before reversing.")
    printList(dll)
    dll.reverseRecursively()
    print("List after reversing.")
    printList(dll)

    return dll


def printForwardRecursivelyTest():
    dll = DoublyLinkedList()
    for i in range(1,11):
        dll.insert(i)

    print("Initial list")
    printList(dll)

    print("Printing recursively forward.")
    dll.printForwardRecursively()


def printBackwardRecursivelyTest():
    dll = DoublyLinkedList()
    for i in range(1,11):
        dll.insert(i)

    print("Initial list")
    printList(dll)

    print("Printing recursively backward.")
    dll.printBackwardRecursively()


print("Initial test.")
initialTest()

print("Reverse test.")
reverseTest()

print("Print Forward Recursively test.")
printForwardRecursivelyTest()

print("Print Backward Recursively test.")
printBackwardRecursivelyTest()

