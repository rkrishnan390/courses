
import os
from rahulk_LinkedList import LinkedList

def clear():
    os.system('clear')

def printList(linked_list):
    for position in range(linked_list.length()):
        value = linked_list.getEntry(position)
        print("Value at %s is %s" % (position, value))
    print(''.join(['*']*23))

def testInsertAtBeginning(ll):
    # Add values 2, 4, 6
    ll.insert(2)
    ll.insert(4)
    ll.insert(6)
    print("After adding values '2, 4, 6'")
    printList(ll)


def testInsertAtN(ll):
    # Insert value 3 into position
    ll.insert(3,1)
    print("After inserting value 3 into position 1")
    printList(ll)

    # Insert value 5 at position 3, and 1 at position 0
    ll.insert(5,3)
    ll.insert(1,0)
    print("After inserting value 5 at position 3, and value 1 at position 0")
    printList(ll)

    # Insert values 7, 8, and 10; then insert value 9 at position 8
    ll.insert(7)
    ll.insert(8)
    ll.insert(10)
    ll.insert(9,8)
    print("After inserting values 7, 8, and 10; then inserting value 9 at position 8")
    printList(ll)

    print("Final list.")
    printList(ll)

    ll.delete()
    print("After deleting last element.")
    printList(ll)


def testDelete(ll):
    ll.delete(0)
    print("After deleting first element.")
    printList(ll)

    ll.delete(4)
    print("After deleting fourth element.")
    printList(ll)


def initialTest():
    # Instantiate the list
    ll = LinkedList()

    # Some beginning inserts
    testInsertAtBeginning(ll)

    # Some arbitrary inserts
    testInsertAtN(ll)

    # Some Deletions
    testDelete(ll)


def reverseTest():
    ll = LinkedList()

    for i in range(1,11):
        ll.insert(i)

    print("Initial list before reversing.")
    printList(ll)
    ll.reverse()
    print("List after reversing.")
    printList(ll)

    return ll

print("Initial test.")
initialTest()

print("Reverse test.")
reverseTest()



