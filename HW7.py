class SLinkedList(object):
    """Non-circular Linked List with head and tail"""

    class _Node:
        """Lightweight private class for storing a linked node"""
        __slots__ = '_element', '_link'  # for memory efficiency; google it

        def __init__(self, element, link):
            self._element = element
            self._link = link

        def __repr__(self):
            return '[{0}, {1}]'.format(self._element, self._link)

    class Empty(Exception):
        pass

    def __init__(self):
        self._head = None
        self._tail = self._head
        self._size = 0

    def __len__(self):
        return self._size

    def __repr__(self):
        # idea: traverse through the nodes, extracting each element and print the elements
        return "Yay, there a list here"

    def is_empty(self):
        return len(self) == 0

    def head(self):
        if self._size == 0:
            return None
        return self._head._element

    def tail(self):
        if self._size == 0:
            return None
        return self._tail._element

    def insert_tail(self, e):
        # Create a new node N
        # Set element of node N to e
        # Set next link of N to None
        # Set next link of tail to N
        # Set list tail to N

        new_tail = self._Node(e, None)
        if self._size == 0:
            self._head = new_tail
        else:
            self._tail._link = new_tail
        self._tail = new_tail
        self._size += 1

    def remove_head(self):  # :(
        if self.is_empty():
            raise self.Empty("Linked List is empty")
        temp = self._head
        self._head = self._head._link
        self._size -= 1
        temp._link = None  # help with garbage collection
        return temp._element

    def insert_head(self, e):
        # 1. Create a node N
        # 2. Set element of node N to e
        # 3. Set next link of N to current list head
        # 4. Set List head to point to N

        new_head = self._Node(e, None)
        temp = self._head
        self._head = new_head
        self._head._link = temp
        self._size += 1

    def remove_tail(self):
        if len(self) == 0:
            raise Exception('List is empty')
        # Case size = 1
        # set temp variable to hold the tail element
        # update head and tail pointers to None
        # return temp variable

        temp = self.tail()

        if len(self) == 1:
            self._head = None
            self._tail = None

        # Case size > 1
        # set temp variable to hold tail element
        # traverse linked list starting at head up to size-2, keeping track of current node
        #      point current node's next link to None
        #      update tail pointer of list to current node

        if len(self) > 1:
            current = self._head
            for i in range(len(self) - 1):
                current = current._link
            current._link = None
            self._tail = current

        return temp
        # typically we do not implement remove_tail due to its O(n) complexity

class _DoublyLinkedBase(object):
    """Base class for a doubly linked list with header and trailer sentinels."""

    class _Node:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, previous, next):
            self._element = element
            self._next = next
            self._prev = previous

    class Empty(Exception):
        pass

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        new_node = self._Node(e, predecessor, successor)
        predecessor._next = new_node
        successor._prev = new_node
        self._size += 1
        return new_node

    def _delete_node(self, a_node):
        """WARNING: Should not delete sentinels."""
        prev_ = a_node._prev
        next_ = a_node._next
        prev_._next = next_
        next_._prev = prev_
        self._size -= 1
        temp = a_node._element
        a_node._prev = a_node._next = a_node._element = None
        return temp

class PositionalList(_DoublyLinkedBase):
    # --------------- nested Position class ---------------------------------
    class Position:
        def __init__(self, container, node):
            self._container = container   # reference to linked list that contains the node at this position
            self._node = node             # reference to the node pointed to by this position

        def element(self):
            return self._node._element

        # Comparisons
        def __eq__(self, other):
            """Returns True if other is a Position pointing to the same node."""
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """Return True if other does not represent the same location"""
            return not (self == other)

    # --------------- nested Position class ---------------------------------

    # Validation
    # possible errors: p is not a Position, p is not in the current list,
    # p is no longer valid
    # purpose of the following method: return the node pointed to by a position p
    # if p is a valid position
    # self in this scope represents a doubly linked list....
    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError("p must be of type Position")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._next is None or p._node._prev is None:
            raise ValueError("p is no longer valid")
        return p._node

    # Create a position
    def _make_position(self, node):
        """Return a Position instance for a given node, None if pointing to a Sentinel."""
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    # Accessor methods
    def first(self):
        """Return position of first element"""
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        """Forward iterator of list elements"""
        # Allows the use of next()
        # Allows to embed Positional Lists in for loops
        pointer = self.first()
        while pointer is not None:
            yield pointer.element()    # returns element stored at this position
            pointer = self.after(pointer)

    # Mutator methods
    # Override the _insert_between() method from parent to return a position after new node is inserted
    def _insert_between(self, e, predecessor, successor):
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """Insert new element in front and return a position"""
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p:Position, e:object):
        node = self._validate(p)
        return self._insert_between(e, node._prev, node)

    def add_after(self, p:Position, e:object):
        node = self._validate(p)
        return self._insert_between(e, node, node._next)

    def delete(self, p):
        """Remove and return element at position p."""
        node = self._validate(p)
        return self._delete_node(node)  # the position is invalidated since the Node _next and _prev are set to None

    def replace(self, p:Position, e:object):
        """Replace and return element that was replaced"""
        node = self._validate(p)
        old_element = node._element
        node._element = e
        return old_element

class LinkedDeque(_DoublyLinkedBase):
    # __init__, len(), is_empty() are inherited

    def first(self):
        if self.is_empty():
            raise self.Empty("Deque is empty.")
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise self.Empty("Deque is empty.")
        return self._trailer._prev._element

    def insert_first(self, e):
        # is always inserting between header and header._next
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        # is always inserting between trailer and trailer._prev
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        if self.is_empty():
            raise self.Empty("Deque is empty.")
        return self._delete_node(self._header._next)

    def delete_last(self):
        if self.is_empty():
            raise self.Empty("Deque is empty.")
        return self._delete_node(self._trailer._prev)


"""•Problem R-7.2 Describe a good algorithm for concatenating two singly linked lists L and
M, given only references to the first node of each list, into a single list L
that contains all the nodes of L followed by all the nodes of M."""


def concatenate_SLL(L, M):
    n = L._head
    # find the tail of L
    while n._link is not None:
        # if n is not tail of M
        # keep moving n until n._link is None
        n = n._link
    # when n is a tail of M, change n._link from None to L._head
    # in other words, point the tail of M to the head of L
    n._link = M._head
    # print M
    return L._head


print("Problem R-7.2")
L = SLinkedList()
L.insert_head("D")
L.insert_head("C")
L.insert_head("B")
L.insert_head("A")
print('L: ', L._head)

M = SLinkedList()
M.insert_head(1)
M.insert_head(2)
M.insert_head(3)
M.insert_head(4)
print('M: ', M._head)

print('L after concatenating with M: ', concatenate_SLL(L, M))
print()

"""•Problem R-7.3 Describe a recursive algorithm that counts the number of nodes in a singly
linked list"""


def count_node(L, n):
    # To count number of nodes in SLL
    # we have to traverse from first node to last node in the list.
    if n is None:
        # if SLL is empty, return 0
        # or if n is L._tail._link, stop recursive process and plus 0
        return 0
    else:
        # counting the first node already
        # number of nodes will be returned
        return 1 + count_node(L, n._link)


print("Problem R-7.3")
L = SLinkedList()
L.insert_head("F")
L.insert_head("C")
L.insert_head("B")
L.insert_head("A")
L.remove_head()
print('L: ', L._head)
print('Number of nodes is: ', count_node(L, L._head))
print()

"""•Problem R-7.8 Describe a non recursive method for finding, by link hopping, the middle
node of a doubly linked list with header and trailer sentinels. In the case
of an even number of nodes, report the node slightly left of center as the
“middle.” (Note: This method must only use link hopping; it cannot use a
counter.) What is the running time of this method? """
#IDEA: traverse both from header and trailer by using 2 nodes (1 node from header, 1 node from trailer)
#From header, move node 1 step forward
#From trailer, back node 1 step backward
#when two nodes meet together at point M, M is the middle

def middle_DLL(L):
    """Find the middle of DLL in case of an even number of node"""
    h = L._header
    t = L._trailer
    while h is not t._prev:
        # because the number of nodes is even,
        # the node slightly left of center is the middle
        h = h._next    # if h and t._prev does not meet together
        t = t._prev    # keep traversing
    return h._element  # return the "middle" element

if __name__ == "__main__":
    dll = _DoublyLinkedBase()
    def func1():
        length = len(dll)
        temp = dll._header
        print('Length of dll: ',length)
        for i in range(length + 2):    # to include header and sentinel nodes
            print("ELEMENT: " + str(temp._element))
            # print("ADDRESS: " + str(temp))
            # print("NEXT ADDRESS: " + str(temp._next))
            # print("PREVIOUS ADDRESS: " + str(temp._prev))
            print("-"*10)
            temp = temp._next
        print()

    print('Problem R-7.8')
    a = dll._insert_between("A", dll._header, dll._trailer)
    b = dll._insert_between("B", a, a._next)
    c = dll._insert_between("C", b, b._next)
    d = dll._insert_between("D", c, c._next)
    e = dll._insert_between("E", d, d._next)
    f = dll._insert_between("F", e, e._next)
    func1()
    print('Middle node of DLL is ',middle_DLL(dll))
    print()
# Analysis:
# Time complexity for finding middle Node is O(n)
# because we compare all node in ddl and n is the length of ddl
"""•Problem R-7.13 Update the PositionalList class to support an additional method find(e),
which returns the position of the (first occurrence of) element e in the list
(or None if not found)."""
class Update_PositionalList(PositionalList):
    def __init__(self):
        super().__init__()
        self._node = None

    def find(self,e):
        """Return position of element e"""
        m = self.first()
        #traverse from head to trailer to find position of e
        while m.element() is not e:
            if self.after(m) is not None:
                #if element at position m is not e, move m to next position
                m = self.after(m)
            else:
                #if not found, return None
                return None
        #if found, return position of e
        return self._make_position(m)

if __name__ == '__main__':
    pl = Update_PositionalList()

    # Add A, B, C so that they are in the order A, C, B
    pA = pl.add_first("A")
    pB = pl.add_after(pA, "B")
    pC = pl.add_before(pB, "C")
    print("Problem R-7.13: ")
    print('pl: ')
    # iterate through the list
    for e in pl:
        print(e)

    print('Find position C in pl. If not, return None: ',pl.find("C"))
    print('Find position D in pl. If not, return None: ', pl.find("D"))
    print()

"""•Problem R-7.15 Provide support for a reversed method of the PositionalList class that
is similar to the given iter , but that iterates the elements in reversed
order"""
class reverse_PL(PositionalList):
    def __init__(self):
        super().__init__()

    def __reversed__(self):
        """Backward iterator of list elements"""
        # Allows the use of prev()
        # Allows to embed Positional Lists in for loops
        pointer = self.last()
        while pointer is not None:
            yield pointer.element()  # returns element stored at this position
            pointer = self.before(pointer)

if __name__ == '__main__':
    pl = reverse_PL()

    # Add A, B, C so that they are in the order A, C, B
    pA = pl.add_first("A")
    pB = pl.add_after(pA, "B")
    pC = pl.add_before(pB, "C")
    pD = pl.add_after(pB,"D")
    pF = pl.add_first("E")
    print('Problem R-7.15')
    # print list
    print('List: ',[e for e in pl])
    # print all of the elements in reversed order
    print('Reversed List: ',[e for e in reversed(pl)])
    print()

"""•Problem C-7.26 Implement a method, concatenate(Q2) for the LinkedQueue class that
takes all elements of LinkedQueue Q2 and appends them to the end of the
original queue. The operation should run in O(1) time and should result"""

class concate_LinkedQueue(LinkedDeque):
    def __init__(self):
        super(concate_LinkedQueue, self).__init__()
    def __iter__(self):
        """Forward iterator of list elements"""
        # Allows the use of ._next
        # Allows to embed Linked Deque in for loops
        m = self._header._next
        while m._next is not None:
            yield m._element # returns element stored at this position
            m = m._next

    def concatenate(self,other):
        """Append all elements of other to the end of linked queue"""
        #IDEA:
        # point the predecessor of trailer to the successor of other's header
        # point the successor of other's header back to the predecessor of trailer
        # set pointer of trailer and other's header is None
        if self.is_empty() or other.is_empty() :
            raise self.Empty ("Queue is empty")
        else:
            #point the last to other's first
            self._trailer._prev._next = other._header._next
            #point the first to back the other's last
            other._header._next._prev = self._trailer._prev
            #trailer and other's header point to None
            self._trailer._prev, other._header._next = None,None

print('Problem C-7.26')
Q1 = concate_LinkedQueue()
Q1.insert_first("A")
Q1.insert_first("B")
Q1.insert_first("C")
print ('Q1: ',[e for e in Q1])
Q2 = concate_LinkedQueue()
Q2.insert_first(1)
Q2.insert_first(2)
Q2.insert_first(3)
print ('Q2: ',[e for e in Q2])
Q1.concatenate(Q2)
print('Q1 after adding Q2 at the end: ',[e for e in Q1])
print()

"""•Problem C-7.29 Describe in detail an algorithm for reversing a singly linked list L using
only a constant amount of additional space and not using any recursion."""
#Algorithm for reversing a singly linked list:
#Challenge: do not take more space for this algorithm (do not use add() or create new linked list)
#IDEA: Relink all nodes include tail in SLL
#And then at the end, swaping head and tail

def reverse_SLL(L):
     prev = L._head
     curr = L._head._link
     next = L._head._link._link
     prev._link = None #it will be a tail at then end and point to None
     while next is not None:
         temp = next._link
         #relink all of nodes
         next._link = curr
         curr._link = prev
         prev,curr,next = curr,next,temp #move prev,curr and next 1 step forward
     L._head,L._tail = L._tail, L._head #swapping head and tail
     return L._head


#There will be roughly O(n) calls to reverse. However, those
#calls do not exist adding extra space,
#so it only needs O(1) space.

print('Problem C-7.29')
sll = SLinkedList()
sll.insert_tail("D")
sll.insert_head("A")
sll.insert_head("B")
sll.insert_head("C")
print('Single Linked List: ',sll._head)
print('Single Linked List after reversing: ',reverse_SLL(sll))
print()

"""•Problem C-7.34 Modify the PositionalList class to support a method swap(p, q) that causes
the underlying nodes referenced by positions p and q to be exchanged for
each other. Relink the existing nodes; do not create any new nodes.
"""
class SwapPositionalList(PositionalList):
    def __init__(self):
        super().__init__()

    def swap(self,p,q):
        #validate two positions
        node1 = self._validate(p)
        node2 = self._validate(q)
        #relink the previous and next of node 1 and node 2
        node1._prev._next,node1._next._prev = node2,node2
        node2._prev._next,node2._next._prev = node1,node1
        #relink the node 1 and node 2
        node1._prev,node2._prev = node2._prev,node1._prev
        node1._next, node2._next = node2._next,node1._next
        #return the list after swaping two position
        return [e for e in self]
print('Problem C-7.34')
pl = SwapPositionalList()
# Add A, B, C, D so that they are in the order A, C, B, D
pA = pl.add_first("A")
pB = pl.add_after(pA, "B")
pC = pl.add_before(pB, "C")
pD = pl.add_last("D")
print('List: ',[e for e in pl])
print('List after swapping A and B: ',pl.swap(pA,pB))


