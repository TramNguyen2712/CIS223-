# Abtract Data Type : Circular Linked Lists
# A circular linked list CLL supports
# CLL.current(): return the element at the current node
# len(CLL)
# CLL.is_empty()
# CLL.insert(e): insert a new node containing the element e after the current node
# CLL.remove(): remove and return the element after current
# CLL.next(): updates the current node to the next node

class CircularLinkedList(object):
    """Circular Linked List"""

    class _Node:
        """Lightweight private class for storing a linked node"""
        __slots__ = '_element', '_link'  # for memory efficiency; google it

        def __init__(self, element, link):
            self._element = element
            self._link = link

    class Empty(Exception):
        pass

    def __init__(self):
        self._current = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return len(self) == 0

    def current(self):
        if self._current is not None:
            return self._current._element
        return None

    def insert(self, e):
        # Insert new node after current and update current
        if len(self) > 0:
            new_node = self._Node(e, self._current._link)
            self._current._link = new_node
            self._current = new_node
        else:
            new_node = self._Node(e, None)
            self._current = new_node
            new_node._link = self._current
        self._size += 1

    def remove(self):
        # Remove and return element stored in node after current
        if self.is_empty():
            raise self.Empty("Linked List is empty.")
        temp = self._current._link
        self._current._link = temp._link
        temp._link = None
        if len(self) == 1:
            self._current = None
        self._size -= 1
        return temp._element

    def next(self):
        # update the current node to the next node so that we can traverse the linked list
        if self.is_empty():
            raise self.Empty("Linked List is empty.")
        self._current = self._current._link


# Exercise: Test and argue about each method's complexity




