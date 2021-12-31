# ADT: Priority Queue
# A priority queue PQ supports
# PQ.add(k, y ): Insert and itiem with key k and value v into priority queue PQ
# PQ.min(): Returns a tuple (k,v) , representing the key and the value of an item in PQ
# with minimal key; error if PQ is empty
# PQ.remove_min(): Remove item with minumum key and return tuple (k,v); error if PQ is empty
# PQ.len(p), PQ.is_empty()

from PositionalLists import PositionalList


class Empty(Exception):
    pass


class PriorityQueueBase(object):
    class _Item:
        __slots__ = '_key', '_value'

        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __lt__(self, other):
            return self._key < other.getKey()

        def getKey(self):
            return self._key

        def getValue(self):
            return self._value

    def is_empty(self):
        return len(self) == 0


# Implementation of Priority Queue with an Unsorted List
# IDEA: Store key-value pair _Item instances in a PositionalList
# Since PositionalList is implemented with a doubly-linked list, all operations
# are O(1)
# To remove the minimum element (or to find the minimum element), we must traverse
# the underlying list until we find the positionof the item with the minimum key
# in the worst case we check all elements, thus operations of min() and remove_min() run at
# O(n)

class UnsortedPriorityQueue(PriorityQueueBase):

    def __init__(self):
        self._data = PositionalList()

    def _find_min(self):
        """Return Position of item with minimum key."""
        if self.is_empty():
            raise Empty("Priority queue is empty.")

        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small
        # O(n)

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        """Add the key-value pair"""
        self._data.add_last(self._Item(key, value))

    def min(self):
        """Return (k,v) tuple with the minimum key. """
        if self.is_empty():
            raise Empty("Priority queue is empty. ")
        p = self._find_min()
        item = p.element()
        return item.getKey(), item.getValue()

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key."""
        if self.is_empty():
            raise Empty("Priority queue is empty. ")

        p = self._find_min()
        item = self._data.delete(p)
        return item.getKey(), item.getValue()


# Exercise: Test this object

# Implementation of Priority Queue with s sorted list
# IDEA: Using PositionalList, make sure that you add elements so that their relative
# positions before and after are smaller and larger respectively
# Thus, remove_min() and min() will only cost O(1)
# However, adding will require O(n) in the worst case

class SortedPriorityQueue(PriorityQueueBase):
    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        newest = self._Item(key, value)
        walk = self._data.last()   # walk backwards looking for smaller key
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)
        else:
            self._data.add_after(walk, newest)

    def min(self):
        if self.is_empty():
            raise Empty("Priority queue is empty.")

        p = self._data.first()
        item = p.element()
        return item.getKey(), item.getValue()

    def remove_min(self):
        if self.is_empty():
            raise Empty("Priority queue is empty")

        item = self._data.delete(self._data.first())
        return item.getKey(), item.getValue()

# Exercise: test this object


