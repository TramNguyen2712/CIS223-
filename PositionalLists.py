# Abstract Data Type: Positional List
# Underlying Data Structure is a Doubly Linked List
# A Positional List PL supports
# PL.is_empty()
# len(PL)

# Accessor Methods
# iter(PL): Return a forward iterator (use yield)
# PL.first(), PL.last(): Return position of first (last) element, None if empty
# PL.before(p), PL.after(p): Return the position immediately before (after) p, None if p is first (last)

# Mutator Methods
# PL.add_first(e), PL.add_last(e): Insert new element in front (back) and return a position
# PL.add_before(p, e), PL.add_after(p, e): Insert new element e just before (after) position p, return a position
# L.delete(p): Remove and return element at position p. Invalidate position.
# L.replace(p, e): Replace and return element replaced

from DoublyLinkedList import _DoublyLinkedBase as dlb

class PositionalList(dlb):
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


# Insertion Sort using Positional List
# Uses m marker (position) for right most element of sorted portion of list
# p marker (position) for the next element to sort
# w marker (position) to traverse from right to left starting at m

def insertion_sort(pl:PositionalList):
    """Sort Positional list of comparable elements in a non-decreasing order"""
    if len(pl) > 1:    # at least two elements
        m = pl.first()
        w = m
        while m != pl.last():
            p = pl.after(m)
            # Case: element is correctly sorted
            if p.element() >= m.element():
                w = m = p
                continue

            # Case: w reached the beginning of the list
            if w == pl.first():
                pl.add_first(pl.delete(p))
                continue

            w = pl.before(w)   # move w to the left

            # Case: w is pointing to element smaller than p
            if p.element() > w.element():
                pl.add_after(w, pl.delete(p))
                w = m


if __name__ == '__main__':
    pl = PositionalList()

    # Add A, B, C so that they are in the order A, C, B
    pA = pl.add_first("A")
    pB = pl.add_after(pA, "B")
    pC = pl.add_before(pB, "C")

    # iterate through the list
    for e in pl:
        print(e)

    pFirst = pl.first()
    print(pFirst == pA)
    print(pFirst.element())
    print(pA.element())

    pLast = pl.last()
    print(pLast == pB)
    print(pLast.element())
    print(pB.element())

    pD = pl.add_last("F")
    print([e for e in pl])

    element = pl.replace(pD, "D")
    print([e for e in pl])

    element = pl.delete(pA)
    pFirst = pl.first()
    print(pFirst.element())
    print([e for e in pl])

    pl2 = PositionalList()
    for i in range(10):
        pl2.add_first(i)

    print([i for i in pl2])

    insertion_sort(pl2)

    print([i for i in pl2])

    print('pl2: ',pl2._header._next._element)


























