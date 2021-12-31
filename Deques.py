# Abstract data type: Double-ended Queue
# Deque D (pronuonced "deck") supports
# D.add_first(e): add element e to the front of D
# D.add_last(e): add element e to the back of D
# D.delete_first(): remove and return a reference to the first element of D
# D.delete_last(): remove and return a reference to the last element of D
# D.first(): return a reference to first element of D
# D.last(): return a reference to last element of D
# D.is_empty()
# len(D)

class Empty(Exception):
    pass

class ArrayDeque(object):
    """Circular Double-Ended Queue"""
    def __init__(self, capacity):
        self._data = [None]*capacity
        self._size = 0
        self._front = 0   # index of first element in Deque
        self._back = (self._front + self._size - 1) % len(self._data)

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._data[self._front]

    def last(self):
        # recall that (front + size - 1)%capacity
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._data[self._back]

    def delete_first(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        first = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data)//4:
            self._resize(len(self._data)//2)
        return first

    def add_last(self, e):
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        last = (self._front + self._size) % len(self._data)
        self._data[last] = e
        self._size += 1
        self._back = last

    def delete_last(self):
        raise NotImplementedError

    def add_first(self, e):
        raise NotImplementedError

    def _resize(self, capacity):
        temp = self._data
        self._data = [None]*capacity
        step = self._front
        for k in range(self._size):
            self._data[k] = temp[step]
            step = (1+step) % len(temp)
        self._front = 0
        self._back = len(temp) - 1