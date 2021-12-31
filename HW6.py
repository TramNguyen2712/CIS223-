class Empty(Exception):
    pass
#Stack Operation
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
#Queue Operation
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
#implements our queue ADT while using a collections.deque instance for storage
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
"""
•Problem R-6.2 Suppose an initially empty stack S has executed a total of 25 push operations, 12 top operations, and 10 pop operations, 3 of which raised Empty
errors that were caught and ignored. What is the current size of S?
"""
#25 push operations: S has 25 element
#12 top operations: top operation does not affect the length of S
#10 popoperations, 3 of which raiseed Empty errors that were caught and ignored: only 7 operations was excecuted
# successfully, so S has 18 element left
"""
•Problem R-6.3 Implement a function with signature transfer(S, T) that transfers all elements from stack S onto stack T, so that the element that starts at the top
of S is the first to be inserted onto T, and the element at the bottom of S
ends up at the top of T. 
"""
def transfer(S,T):
    if len(S) == 0:
        return T.top()
    else:
        a = S.pop()
        T.push(a)
        return transfer(S,T)

S = Stack()
T = Stack()
S.push(2)
S.push(5)
print('Problem R-6.3: ')
print('S before transferring:',S._data)
transfer(S,T)
print('T after transferring: ',T._data)
print()
"""
•Problem R-6.5 Implement a function that reverses a list of elements by pushing them onto
a stack in one order, and writing them back to the list in reversed order
"""
def reverse_lst(list):
    #create empty stack
    S = Stack()
    # copy elements from list to stack
    for i in range(0,len(list)):
        S.push(list[i])
    # add elements from stack to list at the end of list
    for i in range(0, len(list)):
        list.append(S.pop())
        #remove the first element after appending
        list.pop(0)
    #now list is in reversed order
    return list

list = [1,2,3,4,5]
print('Problem R-6.5: ')
print('list: ',list)
print('list after reversing',reverse_lst(list))
print()
"""
•Problem R-6.13 Suppose you have a deque D containing the numbers (1,2,3,4,5,6,7,8),
in this order. Suppose further that you have an initially empty queue Q.
Give a code fragment that uses only D and Q (and no other variables) and
results in D storing the elements in the order (1,2,3,5,4,6,7,8).
"""
print('Problem R-6.13: ')
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
print()
"""
•Problem R-6.14  Repeat the previous problem using the deque D and an initially empty
stack S.
"""
print('Problem R-6.14: ')
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
print()
"""
•Problem C-6.15 Suppose Alice has picked three distinct integers and placed them into a
stack S in random order. Write a short, straight-line piece of pseudo-code
(with no loops or recursion) that uses only one comparison and only one
variable x, yet that results in variable x storing the largest of Alice’s three
integers with probability 2/3. Argue why your method is correct.
"""
print('Problem C-6.15: ')
S = Stack()
S.push(6)
S.push(8)
S.push(9)
print('S: ',S._data)
x = S.pop()
if x < S.top(): #comparison
    x = S.pop()
print('Maximum of S: ',x)
print()
#Assume three integers S has are C,A,B
#Explain: x = S.pop() means point x to one of three elements in S.
#Example: When x = C, comparing C and A.If C < A, x will be A

#Probability = (Number of favourable outcomes)/ (Total number of possible outcome)
#Total number of possible outcome is 3 because S contains three distinct integers
#Number of getting wrong answer is 1 if B is maximum of Stack)
#Probability of getting wrong largest number is 1/3
#So, probability of getting right largest number is 1 - 1/3 = 2/3
"""
•Problem C-6.18 Show how to use the transfer function, described in Exercise R-6.3, and
two temporary stacks, to replace the contents of a given stack S with those
same elements, but in reversed order
"""
print('Problem C-6.18: ')
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
print()
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
"""
•Problem C-6.29 In certain applications of the queue ADT, it is common to repeatedly
dequeue an element, process it in some way, and then immediately enqueue the same element. 
Modify the ArrayQueue implementation to include a rotate( ) method that has semantics identical to the combination, 
Q.enqueue(Q.dequeue( )). However, your implementation should
be more efficient than making two separate calls (for example, because
there is no need to modify size)
"""

class Queue1 (Queue):
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

print('Problem C-6.29: ')
Q = Queue1(4)
Q.enqueue(3)
Q.enqueue(5)
Q.enqueue(7)
Q.enqueue(8)

print('Q before rotating',Q._data)
Q.rotate()
print('Q after rotating',Q._data)