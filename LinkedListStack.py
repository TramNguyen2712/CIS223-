# Abstract data type : Stack
# Underlying data structure is a linked list using Adapted Design Pattern

from SinglyLinkedLists import SLinkedList as sll

# Stack  -> sll
# push()  ->
# pop() ->
# top() ->
# is_empty() ->
# len(S) ->


class SLLStack(object):
    def __init__(self):
        self._data = sll()

    def __len__(self):
        return len(self._data)

    def push(self,e):
        """Add element e to the top of stack"""
        self._data.insert_head(e)
    def is_empty(self):
        return self._data.is_empty()
    def top(self):
        if self.is_empty():
            raise self._data.Empty("empty")
        return self._data.head()

    def pop(self):
        if self.is_empty():
            raise self._data.Empty("empty")
        return self._data.remove_head()

