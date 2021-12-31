# Abstract Data Type: Queue
# Queue Q supports
# Q.enqueue(e): add element to the "back" of the queue Q
# Q.dequeue(): Removes and returns a reference to the first element of the queue Q
# Q.first(): Returns a reference to the fist element of Q
# Q.is_empty(): Returns True if Q does not contain any elements
# len(Q): Return number of elements of Q

# We will use a Python list to implement a Queue circularly my using modulo arithmetic to avoid
# unnecessary waste of space and unnecessary shifts of data withing the list

class Empty(Exception):
    pass

class ArrayQueue(object):
    """Circularly defined FIFO Queue"""
    def __init__(self, capacity):
        self._data = [None]*capacity
        self._size = 0                 # actual number of elements stored in queue
        self._front = 0                # reference to the index of the first element in queue

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty.")
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty.")
        element_to_dequeue = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % (len(self._data))
        self._size -= 1
        return element_to_dequeue

    def enqueue(self, e):
        if self._size == len(self._data):    #queue is full
            self._resize(2*len(self._data))  # twice the capacity

        idx_to_enqueue = (self._front + self._size) % len(self._data)  # (f+size)%capacity
        self._data[idx_to_enqueue] = e
        self._size += 1

    def _resize(self, capacity):
        temp = self._data
        self._data = [None]*capacity
        step = self._front
        self._front = 0
        for k in range(self._size):
            self._data[k] = temp[step]
            step = (step + 1) % len(temp)



# Analysis:
# enqueue(), dequeue() -> O(1) ... when we resize this will be ammortized
# first(), is_empty(), len() -> O(1)


if __name__ == "__main__":
    Q1 = ArrayQueue(3)

    print(Q1.is_empty())

    Q1.enqueue("a")
    print(Q1.first())

    Q1.enqueue(70)
    print(Q1._data)
    print(len(Q1))

    print(Q1.dequeue())
    print(Q1.first())
    print(Q1._data)

    print(Q1.enqueue(4))
    print(Q1._data)
    print(Q1.enqueue(6))
    print(Q1._data)

    #print(Q1.dequeue())
    Q1.enqueue(8)
    print(Q1.first())
    print(Q1._data)
    print(Q1.first())






