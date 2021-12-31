from abc import ABC
class Empty(Exception):
    pass
class LinkedQueue:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self,e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

class Trees(object):
    """Abstract base class for a tree structure"""

    # ----------------- Positional methods --------------------
    class Position:
        def element(self):
            raise NotImplementedError('Must be implemented by a sub-class')

        def __eq__(self, other):
            raise NotImplementedError('Must be implemented by a sub-class')

        def __ne__(self, other):
            return not (self == other)

    # ---------------------------------------------------------

    def root(self):
        raise NotImplementedError('Must be implemented by a sub-class')

    def parent(self, p):
        raise NotImplementedError('Must be implemented by a sub-class')

    def num_children(self, p):
        raise NotImplementedError('Must be implemented by a sub-class')

    def children(self, p):
        raise NotImplementedError('Must be implemented by a sub-class')

    def __len__(self):
        raise NotImplementedError('Must be implemented by a sub-class')

    # ----------------------------------------------------------

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    # Recursive definition of depth
    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    # By Proposition 8.4: Height of a non-empty tree T is the max depth of all leaves
    # Idea: Translate height into depth and use the depth function
    def _height1(self):
        """Height of the whole Tree"""
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

        # Analysis: We will see an implementation of positions that runs in O(n) time, for n positions
        # _height1() calls depth() for each leaf, and depth() is O(n)
        # So, the running time of _height1() will depend on the depth of each leaf
        # we will get a running time of O(n + sum(d+1)) for all leaves. In the worst-case scenario
        # depth could be n for n nodes, thus O(n²) complexity

    # Idea: Why don´t we then implement height recursively
    def _height2(self, p):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    # Analysis: Recursion calls all children at least once. We have not yet implemented
    # children(p), but if we assume that it takes O(cp + 1) where cp is the number of children of p, then
    # the overall running time of _height2 is
    # O(sum(cp + 1)) = O(n + sum(cp)). If there are n positions (including the root), there are n-1 children
    # of some position. Thus the running time is O(n)

    # We could wrap the _height2 method to allow us to calculate the height of sub-trees as well as the
    # entire tree
    def height(self, p=None):
        if p is None:
            p = self.root()
        return self._height2(p)

    # Tree Traversal algorithms are used to generate iterators (preorder, postorder, breadthfirst)

    def __iter__(self):
        for p in self.positions():
            yield p.element()

    # Preorder
    def preorder(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    # private method with a recursive implementation to traverse the tree
    # using pre-order traversal
    def _subtree_preorder(self, p):
        # root first
        yield p  # visit p, when p is a leaf we are in the base case
        # each child
        for c in self.children(p):
            # do pre-order on c subtree
            for other in self._subtree_preorder(c):
                yield other

    # Postorder
    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p  # root last

    # Breadthfirst
    def breadthfirst(self):
        # using array queue
        if not self.is_empty():
            Q = LinkedQueue()  # empty queue....probably better if we used a Queue implemented with
            Q.enqueue(self.root())
            while not Q.is_empty():
                p = Q.dequeue()
                yield p
                for c in self.children(p):
                    Q.enqueue(c)

    # Return iteration of positions
    def positions(self, mode="breadthfirst"):
        if mode == "preorder":
            return self.preorder()
        if mode == "postorder":
            return self.postorder()
        if mode == "breadthfirst":
            return self.breadthfirst()

class BinaryTree(Trees):
    def left(self, p):
        raise NotImplementedError("Must be implemented by subclass")

    def right(self, p):
        raise NotImplementedError("Must be implemented by subclass")

    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    def inorder(self):
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

                # exercise: consider a sample binary tree diagram and execute the inorder traversal

    def _subtree_inorder(self, p):
        # left to right
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p

        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other

    def position(self, mode="inorder"):
        if mode == "inorder":
            return self.inorder()
        else:
            super().positions(mode)

class LinkedBinaryTree(BinaryTree):
    """Linked representation of a binary tree structure"""

    # -----Node class
    class Node:
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    # ---------Postion class
    class Position(BinaryTree.Position):
        """Abstraction representing the location of a single element"""

        def __init__(self,container,node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(self) is type(other) and other._node is self._node

        def __ne__(self, other):
            return not self == other

    # Validate Position
    def _validate(self,p):
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._parent is p._node:   # convention used to deprecate nodes
            raise ValueError("p is no longer a valid position")
        return p._node

    def _make_position(self,node):
        return self.Position(self, node) if node is not None else None

    # ----------Binary tree method
    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def root(self):
        return self._make_position(self._root)

    def parent(self,p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def left (self,p):
        """Return the Position of p's left child"""
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self,p):
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        """Return the number of children of Position p"""
        """
        To calculate the number of children at node p
        : param p: a position object 
        : return number of children of p as an integer
        """
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1


"""Problem R-8.4 What is the running time of a call to T. height2(p) when called on a
position p distinct from the root of T? (See Code Fragment 8.5.)"""


class Tree_height2(Trees):
    def _height2(self, p):
        """Return the height of the subtree rooted at Position p"""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))


# This function is computing the height of tree T
# Analysis:
# The algorithm is recursive. The recursion will be invoked on each of root's children
# which in turn invokes the recursion on each of their children and so on
# So, the running time of the height2 algorithm is O(n) where n is the number of position of T

"""•Problem R-8.10 Give a direct implementation of the num children method within the class
BinaryTree."""

class BinaryTree_numchildren(BinaryTree):
    def __init__(self):
        super(BinaryTree_numchildren, self).__init__()

    def num_children(self, p):
        if self.is_leaf(p):
            return 0
        else:
            count = 0
            if self.left(p) is not None:
                count +=1
            if self.right(p) is not None:
                count +=1
            return count


"""•Problem R-8.12 Draw an arithmetic expression tree that has four external nodes, storing
the numbers 1, 5, 6, and 7 (with each number stored in a distinct external
node, but not necessarily in this order), and has three internal nodes, each
storing an operator from the set {+,−,×, /}, so that the value of the root
is 21. The operators may return and act on fractions, and an operator may
be used more than once"""

# PDF File

""""•Problem R-8.13 Draw the binary tree representation of the following arithmetic expression: 
“(((5+2) ∗ (2−1))/((2+9) + ((7−2)−1)) ∗ 8)”"""
# PDF File


""""•Problem R-8.20 Draw a binary tree T that simultaneously satisfies the following:
• Each internal node of T stores a single character.
• A preorder traversal of T yields EXAMFUN.
• An inorder traversal of T yields MAFXUEN."""
# PDF File

"""•Problem R-8.25 Consider the example of a breadth-first traversal given in Figure 8.17.
Using the annotated numbers from that figure, describe the contents of
the queue before each pass of the while loop in Code Fragment 8.14. To
get started, the queue has contents {1} before the first pass, and contents
{2,3,4} before the second pass"""
# PDF File

"""•Problem C-8.34 [Use induction]For a tree T, let nI denote the number of its internal nodes, and let nE
denote the number of its external nodes. Show that if every internal node
in T has exactly 3 children, then nE = 2nI +1"""
# PDF File


"""•Problem C-8.35 Two ordered trees T' and T'' are said to be isomorphic if one of the following holds:
• Both T' and T'' are empty.
• The roots of T' and T'' have the same number k ≥ 0 of subtrees, and
the ith such subtree of T' is isomorphic to the ith such subtree of T''
for i = 1,...,k. Design an algorithm that tests whether two given ordered trees are isomorphic. 
What is the running time of your algorithm?"""

# Let assume:
# r1 is root of T'
# r2 is root of T''

# Algorithm test isomorphic (T', T''):
#   If r1 is None and r2 is None then
#       return True
#   If r1 is None or r2 is None then
#       return False
#   If value of r1 is not equal to value of r2 then
#       return False
#   Else:
#       Return isomorphic(r1.leftchild, r2.leftchild) and isomorphic(r1.rightchild, r2.rightchild)
#       or isomorphic(r1.leftchild, r2.rightchild) and isomorphic(r1.rightchild, r2.leftchild)

# Analysis:
# The algorithm is recursive, and it will scan all positions of two trees.
# However, two ordered trees may be same or different from the number of nodes.
# So, the running time of algorithm is O(2 * n) or O(n)
# where n is the minimum of number of nodes in two trees

