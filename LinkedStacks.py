# Abstract data type : Stack
# Underlying data structure is a linked list using Adapted Design Pattern

from SinglyLinkedLists import SLinkedList as sll

# Stack  -> sll
# push()  -> insert_head()
# pop() -> remove_head()
# top() -> head()
# is_empty() -> is_empty()
# len(S) -> len(sll)


class SLLStack(object):
    def __init__(self):
        self._data = sll()

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return self._data.is_empty()

    def push(self, e):
        self._data.insert_head(e)

    def top(self):
        if self.is_empty():
            raise self._data.Empty("Data structure is empty.")
        return self._data.head()

    def pop(self):
        if self.is_empty():
            raise self._data.Empty("Data structure is empty.")
        return self._data.remove_head()


# Exercise: TEST IT





    

