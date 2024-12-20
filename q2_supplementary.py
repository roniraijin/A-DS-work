from dataclasses import dataclass

@dataclass
class Node:
    """Implements a (singly) linked-list node 

    For a Node n:
        n.data holds an integer value
        n.next refers to the next Node in the linked list, or None

    You must not modify this code.
    """
    data: int
    next: 'Node' = None

@dataclass
class LinkedList:
    """Implements a (singly) linked-list 

    For a LinkedList ll:
        ll.head refers to a Node that is the head of the linked list, or None
        ll.size is the size of the linked list

    You must not modify this code.
    """
    head: Node = None
    size: int = 0

@dataclass
class LinkedListWithTail:
    """Implements a (singly) linked-list 

    For a LinkedList ll:
        ll.head refers to a Node that is the head of the linked list, or None
        ll.tail refers to a Node that is the tail of the linked list, or None
        ll.size is the size of the linked list

    You must not modify this code.
    """
    head: Node = None
    tail: Node = None
    size: int = 0


def show(linked_list):
    """Prints values in the order they appear in the linked list.

    Each value should be separated by a newline and no other character. 
    """
    bob = linked_list.head
    while True:
        if bob == None:
            break
        else:                
            print(bob.data)
            bob = bob.next
            
        
            


def cat(linked_list_a, linked_list_b):
    """Concatenates two linked lists.

    Returns a LinkedList which contains all the nodes of linked_list_a followed
    by all the nodes of linked_list_b.
    """
    bob = linked_list_a.head
    while True:        
        if bob.next == None:          
            bob.next = linked_list_b.head
            break
        
        else:
            bob = bob.next
            linked_list_a.next = bob



def smart_cat(linked_list_a, linked_list_b):
    """Concatenates two linked lists, both with tail references.

    Returns a LinkedListWithTail which contains all the nodes of linked_list_a followed
    by all the nodes of linked_list_b.
    """
    bob = linked_list_a        
    if bob.tail == None:   
        bob.head = linked_list_b.head
    else:
        bob.tail.next = linked_list_b.head
        bob.tail = linked_list_b.tail
            
    return(bob)

def make_queue():
    """Creates a linked list with the required structure.

    Returns a LinkedListWithTail containing the contents of Q as described in the 
    question.
    """
    N1 = Node(4)
    N2 = Node(9)
    N3 = Node(18)
    N4 = Node(3)
    N5 = Node(21)
    bob = LinkedListWithTail()
    bob.head = N1
    bob.head.next = N2
    bob.head.next.next = N3
    bob.head.next.next.next = N4
    bob.head.tail = N5
    return(bob)


def enqueue(ll_queue, value):
    """Returns a linked list representing a queue, after a new value has been
    enqueued.

    Returns a LinkedListWithTail containing the contents of a queue held in the
    LinkedListWithTail ll_queue, after a new value has been enqueued.
    """
    return(ll_queue)
    bob = ll_queue.head
    new_node = Node(value)
    print(new_node)
    print(ll_queue)
    if ll_queue.head:
        while True:
            if bob == None:
                ll_queue.tail.next = new_node
                ll_queue.tail = new_node
                ll_queue.size += 1
                break
            else:
                bob = bob.next
    return(ll_queue)

def convert_to_array_queue(ll_queue):
    """
    "Converts" a LinkedList to an array-backed queue.

    Given a LinkedList ll_queue containing a tuple (A, f, r) where: 

    A is a list of length 10, backing the queue
    f is an int with a value facilitating access to the front of the queue
    r is an int with a value facilitating access to the rear of the queue.
    """
    arRay = []
    bob = ll_queue.head
    counter = 0
    for x in range(0,10,1):
        if bob == None:
            arRay.append(None)
        else:
            arRay.append(bob)
            bob = bob.next
            counter += 1
    Linkedin = [arRay,0,counter]
    return(Linkedin)
    


# test data
N1 = Node(3)
N2 = Node(7)
N1.next = N2
N2.next = None
LL1 = LinkedList()
LL1.head = N1

N3 = Node(2)
N4 = Node(8)
N3.next = N4
N4.next = None
LL2 = LinkedList()
LL2.head = N3

N5 = Node(1)
N6 = Node(9)
N5.next = N2
N6.next = None
LLWT1 = LinkedListWithTail(head=N5, tail=N6, size=2)

N7 = Node(0)
N8 = Node(4)
N7.next = N4
N8.next = None
LLWT2 = LinkedListWithTail(head=N7, tail=N8, size=2)

Lcat = cat(LL1, LL2)
assert(Lcat.head == N1)
assert(Lcat.head.next.next== N3)

Lsmcat = smart_cat(LLWT1, LLWT2)
assert(Lsmcat.head == N5)
assert(Lsmcat.tail == N8)

assert(make_queue().head.next.next.data == 18)

# there is no simple test for convert_to_array_queue(ll_queue)

assert(enqueue(make_queue(), 3).size > make_queue().size)
print(convert_to_array_queue(ll_queue))