# Abstract Data Type: Double Ended Queue
# Underlying Data structure is a Doubly Linked List
# Implement as an extension of _DoublyLinkedBase

# Recall
# Deque D (pronounced deck) supports
# len(D)
# D.is_empty()
# D.first(): Returns a reference to the first element of D
# D.last(): Returns a reference to the last element of D
# D.insert_first(e): add element e to the front of D
# D.insert_last(e): add element e to the back of D
# D.delete_first(): Remove and return a reference to the first element of D
# D.delete_last(): Remove and return a reference to the last element of D

from DoublyLinkedList import _DoublyLinkedBase

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

# Exercise: Test it
pl = LinkedDeque()
pl.insert_first("A")
pl.insert_first("B")
print(pl._header._next._element)

