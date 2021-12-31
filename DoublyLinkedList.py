# Abstract Data Type: Doubly Linked List
# A Doubly Linked List DLL supports
# DLL.is_empty()
# len(DLL)
# DLL._insert_between(e, predecessor, successor)
# DLL._delete_node(a_node)

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


if __name__ == "__main__":
    dll = _DoublyLinkedBase()

    def func1():
        length = len(dll)
        temp = dll._header
        print(length)
        for i in range(length + 2):    # to include header and sentinel nodes
            print("ELEMENT: " + str(temp._element))
            print("ADDRESS: " + str(temp))
            print("NEXT ADDRESS: " + str(temp._next))
            print("PREVIOUS ADDRESS: " + str(temp._prev))
            print("-"*10)
            temp = temp._next
        print()

    func1()
    a = dll._insert_between("A", dll._header, dll._trailer)
    func1()
    b = dll._insert_between("B", a, a._next)
    func1()
    c = dll._insert_between("C", b, b._next)
    func1()
    element = dll._delete_node(b)
    func1()
    print("Item removed from list: " + str(element))










