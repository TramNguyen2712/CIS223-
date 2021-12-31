# A Stack - a data structure (a collection of data/objects) where objects are inserted and/or removed in a
# LIFO - last-in first-out ....
# Example - implement the behaviour of a printer ... we would not use a Stack
# Example - undo (ms word), back button web browser

# Notes:
# Could insert objects anywhere, but the intended behavious is for us to "only" access and/or remove
# elements from the top
# Fundamental operations "push", "pop"

# pop() on an empty stack, return and IndexError
# makes no sense to index stacks
# It maybe useful to have a model of a stack that has a fixed capacity (kind of like a compact array)
# Having fixed capacity means that our projected complexity for the methods will not be Ammortized
# Since we want the flexbility to grow/shink our stack depending on the capacity needs,
# we are stuck with Ammortization analysis of some of the methods

# IMPLEMENTATION
# Abstract Data Type: Stack
# Stack S supports
# S.push(e): add element e to the top of the stack S
# S.pop(): remove and and return the top element of the stack S
# S.top(): Returns a reference to the top element of the stack S
# S.is_empty(): Returns true if S does not contain any elements
# len(S): Return number of elements of the stack S


# We will use a Python list to implement a stack
# Stack S -> List L
# push() -> append()
# pop() -> remove(); pop()
# top() -> L[len(L) - 1]; L[-1]
# is_empty() -> len(L) == 0 or L == []
# len() -> len()

class Empty(Exception):
    """Simple Exception extension"""
    pass

class ArrayStack(object):
    """LIFO stack implementation using lists"""

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return self._data == []

    def push(self, e):
        self._data.append(e)

    def top(self):
        """Raise Exception if stack is empty"""
        if self.is_empty():
            raise Empty("Stack is empty.")
        return self._data[-1]

    def pop(self):
        """Raise Exception if stack is empty"""
        if self.is_empty():
            raise Empty("Stack is empty.")
        return self._data.pop()

# Analysis: based on running times of list methods
# push() and pop() -> O(1) ammortized  (mutating methods)
# top(), is_empty(), len() -> O(1)     (non-mutating methods)


if __name__ == "__main__":
    # Testing ArrayStack methods
    S = ArrayStack()
    S.push("dog")
    S.push(3)
    print(len(S))
    print(S.pop())
    print(S.is_empty())
    print(S.pop())
    print(S.is_empty())
    # S.pop()
    S.push("Hello World")
    print(S.top())
