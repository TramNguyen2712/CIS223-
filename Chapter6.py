"""R-6.1 What values are returned during the following series of stack operations, if
executed upon an initially empty stack? push(5), push(3), pop(), push(2),
push(8), pop(), pop(), push(9), push(1), pop(), push(7), push(6), pop(),
pop(), push(4), pop(), pop()."""
import collections
import math


class Empty(Exception):
    pass
class Stack():
    """Last In First Out"""
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == []

    def push(self,e):
        self._data.append(e)

    def top(self):
        """Return the element at the top of the stack"""
        """The last element is pushed"""
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]

    def pop(self):
        """Remove the element at the top of stack"""
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()

# if __name__ == "__main__":
#     S = Stack()
#     print(S.push(5))
#     print(S.push(3))
#     print(S.pop())
#     print(S.push(2))
#     print(S.push(8))
#     print(S.pop())
#     print(S.pop())
#     print(S.push(8))
#     print(S.push(1))
#     print(S.pop())
#     print(S.push(7))
#     print(S.push(6))
#     print(S.pop())
#     print(S.push(4))
#     print(S.pop())
#     print(S.pop())
#     print(len(S))

"""R-6.2 Suppose an initially empty stack S has executed a total of 25 push operations, 12 top operations, and 10 pop operations, 3 of which raised Empty
errors that were caught and ignored. What is the current size of S?"""
#25 push operations: S has 25 element
#12 top operations: top operation does not affect the length of S
#10 popoperations, 3 of which raiseed Empty errors that were caught and ignored: only 7 operations was excecuted
# successfully, so S has 18 element left

"""R-6.3 Implement a function with signature transfer(S, T) that transfers all elements from stack S onto stack T, so that the element that starts at the top
of S is the first to be inserted onto T, and the element at the bottom of S
ends up at the top of T."""

def transfer(S,T):
    if len(S) == 0:
        return T.top()
    else:
        a = S.pop()
        T.push(a)
        return transfer(S,T)

# S = Stack()
# T = Stack()
# S.push(2)
# S.push(5)
# print(S._data)
# transfer(S,T)
# print(T._data)

"""R-6.4 Give a recursive method for removing all the elements from a stack"""

def remove_ele_stack(S):
    if len(S) == 0:
        return "Stack is Empty"
    else:
        S.pop()
        return remove_ele_stack(S)

# S = Stack()
# S.push(2)
# S.push(3)
# S.push(5)
# print(S._data)
# remove_ele_stack(S)
# print(len(S))
# print(S.__data)

"""R-6.5 Implement a function that reverses a list of elements by pushing them onto
a stack in one order, and writing them back to the list in reversed order"""

def reverse_lst(list):
    S = Stack()
    result = []
    for i in range(0,len(list)):
        S.push(list[i])
    for i in range(0, len(list)):
        result.append(S.pop())
    return result

# list = [1,2,3,4,5]
# print(reverse_lst(list))

"""R-6.6 Give a precise and complete definition of the concept of matching for
grouping symbols in an arithmetic expression. Your definition may be
recursive."""

def matching_symbol(expre,i,S=Stack()):
    left = '({['
    right = ')}]'
    if len(S) == 0 and S.is_empty(): #when all symbols matched
        return True
    elif expre[i] in left:
        #push left delimiter on stack
        S.push(expre[i])
        return matching_symbol(expre[1:len(expre)],i,S) #recur on the rest
    elif expre[i] in right:
        #compare the element in expre to the last element of S
        c = S.pop()
        if expre[i] != c:
            return False #mismatched
        elif expre[i] == c:
            return matching_symbol(expre[1:len(expre)],i,S) #recur on the rest if matching
    # if element in expre is not in left and right, continue to run the recursive operation
    return matching_symbol(expre[1:len(expre)], i,S)

expre = '[(5+x)-y+z)]'
# print(matching_symbol(expre,0))

"""R-6.7 What values are returned during the following sequence of queue operations, if executed on an initially empty queue? enqueue(5), enqueue(3),
dequeue(), enqueue(2), enqueue(8), dequeue(), dequeue(), enqueue(9),
enqueue(1), dequeue(), enqueue(7), enqueue(6), dequeue(), dequeue(),
enqueue(4), dequeue(), dequeue()."""

class Queue(object):
    """First In, First Out"""
    def __init__(self,capacity):
        self._data = [None] * capacity
        self._size = 0
        self._front = 0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size == 0
    def first(self):
        """Return (but do not remove) the element at the front of the queue.

        Raise Empty exception if the queue is empty
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        """Remove and return the first element of the queue(i.e.,FIFO).
        Raise Empty exception if the queue is empty
        """

        answer = self._data[self._front]
        self._data[self._front] = None #help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self,e):
        """Add an element to the back of queue"""
        if self._size == len(self._data):
            self._resize(2*len(self._data))   #double the array size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize (self,cap):  # we assume cap >= len(self)
        """Resize to a new list of capacity >= len(self)"""
        old = self._data   #keep track of existing list
        self._data = [None]*cap  #allocate list with new capacity
        walk = self._front
        for k in range(self._size): #only consider existing elements
            self._data[k] = old[walk] #intentionally shift indices
            walk = (1+walk)%len(old) #use old size as modulus
        self._front = 0 #front has been realigned

# S = Queue(3)
# S.enqueue(5)
# print(S._data)
# S.enqueue(3)
# print(S._data)
# S.dequeue()
# print(S._data)
# S.enqueue(2)
# print(S._data)
# S.enqueue(8)
# print(S._data)
# S.dequeue()
# print(S._data)
# S.dequeue()
# print(S._data)
# S.enqueue(9)
# print(S._data)
# S.enqueue(1)
# print(S._data)
# S.dequeue()
# print(S._data)
# S.enqueue(7)
# print(S._data)
# S.enqueue(6)
# print(S._data)
# S.dequeue()
# print(S._data)
# S.dequeue()
# print(S._data)
# S.enqueue(4)
# print(S._data)
# S.dequeue()
# print(S._data)
# S.dequeue()
# print(S._data)
# print()

"""R-6.8 Suppose an initially empty queue Q has executed a total of 32 enqueue
operations, 10 first operations, and 15 dequeue operations, 5 of which
raised Empty errors that were caught and ignored. What is the current
size of Q?"""

#32 enqueue: 32 elements. size is 32
#10 first operations: do not affect the size
#15 dequeue operations, 5 of which raised Empty errors that were caught and ignord:
#just 10 dequeue operations which run successfully, so size is 22 (32-10)

"""R-6.9 Had the queue of the previous problem been an instance of ArrayQueue
that used an initial array of capacity 30, and had its size never been greater
than 30, what would be the final value of the front instance variable?"""

"""R-6.10 Consider what happens if the loop in the ArrayQueue. resize method at
lines 53–55 of Code Fragment 6.7 had been implemented as:
for k in range(self. size):
self. data[k] = old[k]"""

class Queue1(Queue):
    def __init__(self, capacity):

        super().__init__(capacity)

    def enqueue1(self,e):
        """Add an element to the back of queue"""
        if self._size == len(self._data):
            self._resize1(2*len(self._data))   #double the array size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize1 (self,cap):  # we assume cap >= len(self)
        """Resize to a new list of capacity >= len(self)"""
        old = self._data   #keep track of existing list
        self._data = [None]*cap  #allocate list with new capacity
        #walk = self._front
        for k in range(self._size): #only consider existing elements
            self._data[k] = old[k] # old[k] instead of old[walk]
            #walk = (1+walk)%len(old) #remove
        self._front = 0 #front has been realigned

# D = Queue1(3)
# D.enqueue1(5)
# print(D._data)
# D.enqueue1(3)
# print(D._data)
# D.dequeue()
# print(D._data)
# D.enqueue1(2)
# print(D._data)
# D.enqueue1(8)
# print(D._data)
# D.dequeue()
# print(D._data)
# D.dequeue()
# print(D._data)
# D.enqueue1(9)
# print(D._data)
# D.enqueue1(1)
# print(D._data)
# D.dequeue()
# print(D._data)
# D.enqueue1(7)
# print(D._data)
# D.enqueue1(6)
# print(D._data)
# D.dequeue()
# print(D._data)
# D.dequeue()
# print(D._data)
# D.enqueue1(4)
# print(D._data)
# D.dequeue()
# print(D._data)
# D.dequeue()
# print(D._data)

#difference: after transfer the elements from the olf array to the new one,
#the element will be in the reverse order

"""R-6.11 Give a simple adapter that implements our queue ADT while using a
collections.deque instance for storage."""
from collections import deque
class Deque():
    def __init__(self):
        self._data = deque()

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def add_first(self,e):
        self._data.appendleft(e)
        return self._data[0]

    def add_last(self,e):
        self._data.append(e)
        return self._data[-1]

    def delete_first(self):
        first = self._data[0]
        self._data.popleft()
        return first

    def delete_last(self):
        last = self._data[-1]
        self._data.pop()
        return last

    def first(self):
        return self._data[0]

    def last(self):
        return self._data[-1]

# C = Deque()
# C.add_last(5)
# print(C._data)
# C.add_first(3)
# print(C._data)
# C.add_first(7)
# print(C._data)
# print(C.first())
# C.delete_last()
# print(C._data)
# print(len(C))
# C.delete_last()
# print(C._data)
# C.delete_last()
# print(C._data)
# C.add_first(6)
# print(C._data)
# print(C.last())
# C.add_first(8)
# print(C._data)
# print(C.is_empty())
# print(C.last())

"""R-6.12 What values are returned during the following sequence of deque ADT operations, on initially empty deque? add first(4), add last(8), add last(9),
add first(5), back( ), delete first( ), delete last( ), add last(7), first( ),
last( ), add last(6), delete first( ), delete first( )."""

class Deque2(object):
    def __init__(self,capacity):
        self._data = [None]*capacity
        self._size = 0
        self._front = 0
        self._back = (self._front + self._size -1) % len(self._data)

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty ("Queue is empty")
        return self._data[self._front]

    def last(self):
        if self.is_empty():
            raise Empty ("Queue is empty")
        return self._data[self._back]

    def add_fisrt(self,e):
        raise NotImplementedError
    def delete_last(self):
        raise NotImplementedError

    def add_last(self,e):
        if self._size == len(self._data):
            self._resize(len(self._data)*2)
        last = (self._front + self._size) % len(self._data)
        self._data[last] =  e
        self._back = last
        self._size += 1
        return last

    def delete_first(self):
        if self.is_empty():
            raise Empty ("Queue is empty")
        first = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front -1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data) //4:
            self._resize(len(self._data)//2)
        return first

    def _resize(self,cap):
        old = self._data
        self._data = [None]*cap
        step = self._front
        for k in range(self._size):
            self._data[k] = old[step]
            step = (1+step) % len(old)
        self._front = 0
        self._back = len(old) - 1

# C = Deque2(1)
# C.add_last(5)
# print(C._data)
# C.add_last(3)
# print(C._data)
# C.add_last(7)
# print(C._data)
# print(C.first())
# C.delete_first()
# print(C._data)
# print(len(C))
# C.delete_first()
# print(C._data)
# C.delete_first()
# print(C._data)
# C.add_last(6)
# print(C._data)
# print(C.last())
# C.add_last(8)
# print(C._data)
# print(C.is_empty())
# print(C.last())

"""R-6.13 Suppose you have a deque D containing the numbers (1,2,3,4,5,6,7,8),
in this order. Suppose further that you have an initially empty queue Q.
Give a code fragment that uses only D and Q (and no other variables) and
results in D storing the elements in the order (1,2,3,5,4,6,7,8)."""
print('* Queue')
#Create D contains ((1,2,3,4,5,6,7,8))
D = Deque()
D.add_last(1)
D.add_last(2)
D.add_last(3)
D.add_last(4)
D.add_last(5)
D.add_last(6)
D.add_last(7)
D.add_last(8)
print('Before: ',D._data)
#Create the emty queue Q
Q = Queue(8)
#add 8,7,6 to queue Q
#Q will be (8,7,6)
Q.enqueue(D.delete_last())
Q.enqueue(D.delete_last())
Q.enqueue(D.delete_last())
#Move 5 to the beginning of deque
#D will be (5,1,2,3,4)
D.add_first(D.delete_last())
#Add 4 to Queue
Q.enqueue(D.delete_last())
#Add 5 to Queue
#Q will be (8,7,6,4,5)
Q.enqueue(D.delete_first())
#Add 3,2,1 to Q
Q.enqueue(D.delete_last())
Q.enqueue(D.delete_last())
Q.enqueue(D.delete_last())
#Q = (8,7,6,4,5,3,2,1)
#D is empty now
#Dequeue Q and add to the first of D
D.add_first(Q.dequeue())
D.add_first(Q.dequeue())
D.add_first(Q.dequeue())
D.add_first(Q.dequeue())
D.add_first(Q.dequeue())
D.add_first(Q.dequeue())
D.add_first(Q.dequeue())
D.add_first(Q.dequeue())
#Result
print('After: ',D._data)

"""
•Problem R-6.14  Repeat the previous problem using the deque D and an initially empty
stack S.
"""
print('* Stack')
#Create D contains ((1,2,3,4,5,6,7,8))
D = Deque()
D.add_last(1)
D.add_last(2)
D.add_last(3)
D.add_last(4)
D.add_last(5)
D.add_last(6)
D.add_last(7)
D.add_last(8)
print('Before: ',D._data)
#Create empty stack
S = Stack()
#Add 1,2,3 to Stack
#Stack will be (3,2,1)
S.push(D.delete_first())
S.push(D.delete_first())
S.push(D.delete_first())
#Move 4 to the end of deque
D.add_last(D.delete_first())
#Add 5 to Stack
S.push(D.delete_first())
#Add 4 to Stack
S.push(D.delete_last())
#Add the rest numbers to Stack
#Stack will be (8,7,6,4,5,3,2,1)
S.push(D.delete_first())
S.push(D.delete_first())
S.push(D.delete_first())
#Pop the stack and add them to the first of deque
D.add_first(S.pop())
D.add_first(S.pop())
D.add_first(S.pop())
D.add_first(S.pop())
D.add_first(S.pop())
D.add_first(S.pop())
D.add_first(S.pop())
D.add_first(S.pop())
#Result
print('After: ',D._data)

"""C-6.15 Suppose Alice has picked three distinct integers and placed them into a
stack S in random order. Write a short, straight-line piece of pseudo-code
(with no loops or recursion) that uses only one comparison and only one
variable x, yet that results in variable x storing the largest of Alice’s three
integers with probability 2/3. Argue why your method is correct."""
S = Stack()
S.push(6)
S.push(8)
S.push(9)
x = S.pop()
if x < S.top(): #comparison
    x = S.pop()
print('Maximum of S: ',x)
#Assume three integers S has are C,A,B
#Explain: x = S.pop() means point x to one of three elements in S.
#Example: When x = C, comparing C and A.If C < A, x will be A

#Probability = (Number of favourable outcomes)/ (Total number of possible outcome)
#Total number of possible outcome is 3 because S contains three distinct integers
#Number of getting wrong answer is 1 if B is maximum of Stack)
#Probability of getting wrong largest number is 1/3
#So, probability of getting right largest number is 1 - 1/3 = 2/3

"""C-6.18 Show how to use the transfer function, described in Exercise R-6.3, and
two temporary stacks, to replace the contents of a given stack S with those
same elements, but in reversed order"""

#Code of problem R-6.3
def transfer(S,T):
    if len(S) == 0:
        return T.top()
    else:
        a = S.pop()
        T.push(a)
        return transfer(S,T)

S = Stack()
#1st temp stack
T1 = Stack()
#2nd temp stack
T2 = Stack()
S.push(2)
S.push(5)
print('S before 3 transfer calls: ',S._data)
transfer(S,T1)
transfer(T1,T2)
transfer(T2,S)
print('S after 3 transfer calls:',S._data)

#Explain:
# With S has 2 elements (2,5) and two temporary stacks, we have 3 transfer calls
# S : (2,5)
# T1 : ()
# T2 : ()
# First call: transfer elements from S to T1, the top element in S is the bottom in T1
# S : ()
# T1 : (5,2)
# T2 : ()
# Second call: transfer elements in T1 to T2, the top element in T1 is the bottom in T2
# now T2 is also S before the first call
# S : ()
# T1 : ()
# T2 : (2,5)
# Final call: transfer elements in T2 to S, the top element in T2 is the bottom in S
# now the elements of S are reserved
# S : (5,2)
# T1 : ()
# T2 : ()

"""C-6.29 In certain applications of the queue ADT, it is common to repeatedly
dequeue an element, process it in some way, and then immediately enqueue the same element. 
Modify the ArrayQueue implementation to include a rotate( ) method that has semantics identical to the combination, 
Q.enqueue(Q.dequeue( )). However, your implementation should
be more efficient than making two separate calls (for example, because
there is no need to modify size)"""


class Queue3 (Queue):
    def __init__(self, capacity):
        super().__init__(capacity)

    def rotate(self):
        if self.is_empty():
            raise Empty ('Queue is empty')
        else:
            # no allow to use enqueue, dequeue, and size does not change
            #set temp is the first element in queue
            temp = self._data[self._front]
            #move element up
            for i in range(self._front,len(self._data)-1):
                self._data[i] = self._data[i+1]
            # compute the location
            back = (self._front + self._size -1)
            #set next element is self._front
            self._front = (self._front+1)%len(self._data)
            #place the temp value at back index
            self._data[back] = temp


Q = Queue3(4)
Q.enqueue(3)
Q.enqueue(5)
Q.enqueue(7)
Q.enqueue(8)

print(Q._data)
print(Q._front)
Q.rotate()
print(Q._data)
















