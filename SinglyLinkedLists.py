# Abstract Data type: singly linked list
# A singly linked liste SLL supports
# SLL.head(): returns a "private" pointer to the head of the list
# SLL.tail(): pointer to the tail of the list
# len(SLL)
# SLL.is_empty()
# SLL.insert_head(e): inserts a new node with element e at the head of the list, and update the head
# SLL.insert_tail(e): inserts a new node with element e at the tail and update tail
# SLL.remove_head(): updates head of list to next node and returns element of "old head"
# SLL.remove_tail(): update tail of list to second-to-last element of list (requires travesing the list
# twice)

class SLinkedList(object):
    """Non-circular Linked List with head and tail"""
    class _Node:
        """Lightweight private class for storing a linked node"""
        __slots__ = '_element', '_link'  # for memory efficiency; google it

        def __init__(self, element, link):
            self._element = element
            self._link = link

        def __repr__(self):
            return '[{0}, {1}]'.format(self._element, self._link)

    class Empty(Exception):
        pass

    def __init__(self):
        self._head = None
        self._tail = self._head
        self._size = 0

    def __len__(self):
        return self._size

    def __repr__(self):
        # idea: traverse through the nodes, extracting each element and print the elements
        return "Yay, there a list here"

    def is_empty(self):
        return len(self) == 0

    def head(self):
        if self._size == 0:
            return None
        return self._head._element

    def tail(self):
        if self._size == 0:
            return None
        return self._tail._element

    def insert_tail(self, e):
        # Create a new node N
        # Set element of node N to e
        # Set next link of N to None
        # Set next link of tail to N
        # Set list tail to N

        new_tail = self._Node(e, None)
        if self._size == 0:
            self._head = new_tail
        else:
            self._tail._link = new_tail
        self._tail = new_tail
        self._size += 1

    def remove_head(self):   # :(
        if self.is_empty():
            raise self.Empty("Linked List is empty")
        temp = self._head
        self._head = self._head._link
        self._size -= 1
        temp._link = None    # help with garbage collection
        return temp._element


    def insert_head(self, e):
        # 1. Create a node N
        # 2. Set element of node N to e
        # 3. Set next link of N to current list head
        # 4. Set List head to point to N

        new_head = self._Node(e, None)
        temp = self._head
        self._head = new_head
        self._head._link = temp
        self._size += 1

    def remove_tail(self):
        if len(self) == 0:
            raise Exception('List is empty')
        # Case size = 1
        # set temp variable to hold the tail element
        # update head and tail pointers to None
        # return temp variable

        temp = self.tail()

        if len(self) == 1:
            self._head = None
            self._tail = None

        # Case size > 1
        # set temp variable to hold tail element
        # traverse linked list starting at head up to size-2, keeping track of current node
        #      point current node's next link to None
        #      update tail pointer of list to current node 

        if len(self) > 1:
            current = self._head
            for i in range(len(self) - 1):
                current = current._link
            current._link = None
            self._tail = current

        return temp
        # typically we do not implement remove_tail due to its O(n) complexity



if __name__ == "__main__":
    SLL = SLinkedList()
    print(SLL.head())
    print(SLL.tail())
    print(SLL)
    print()

    SLL.insert_tail("A")
    print(SLL.head())
    print(SLL.tail())
    #print(SLL._tail)
    #print(SLL._head)

    SLL.insert_tail("B")
    print(SLL.head())
    print(SLL.tail())
    print(SLL._head)
    print(SLL._tail)

    SLL.insert_tail("C")
    print(SLL.head())
    print(SLL.tail())
    print(SLL._head)
    print(SLL._tail)





