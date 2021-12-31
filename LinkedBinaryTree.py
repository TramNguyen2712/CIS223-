# Abstract Data Type: Binary Tree
# Implemented as a linked Binary tree with supporting positional structure
# A linked binary tree LBB inherits from Binary Tree and supports
# LBB.add_root(e):: Create a root for an empty tree, store e, return position of the root
# error if the tree is non-empty
# LBB.add_left(p, e): Create a node storing the element e, link the node as left child
# of position p, and return a position
# LBB.add_right(p,e): Create a node storing the element e, link the node as right child
# of position p, and return a position
# LBB.replace(p,e): Replace the element at position p with e, return previous element
# LBB.delete(p): Remove node at position p; replace it with child (if any), return element
# error if p has two children
# LBB.attach(p, T1, T2): Attach the interna structure of trees T1 and T1 and left and right
# structures with p as the root; error if p is not a leaf

from BinaryTree import BinaryTree


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
        """Return the Postion of p's left child"""
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
        return count

    def _add_root(self,e):
        """Place element e at the root of an empty tree and return new Position

        Raise ValueError
        """
        if self._root is not None:
            raise ValueError('Root exist')
        self._size = 1
        self._root = self.Node(e)
        return self._make_position(self._root)

    def _add_left(self,p,e):
        """Create a new left shile for Position p, storing element e

        Return the Position of new node
        Raise ValueError if Postion p is invalid or p already has left child
        """
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('Left child exist')
        self._size += 1
        node._left = self.Node(e,parent=p)
        return self._make_position(node._left)

    def _add_right(self,p,e):
        """Create a new right chile for Position p, soring element e

        Return th Position of new node
        Raise ValueError if Postion p is invalid or p already has a right child
        """

        node = self._validate(p)
        if node._right is not None:
            raise ValueError('RIght child exists')
        self._size += 1
        node._right = self.Node(e,parent=p)
        return self._make_position(node._right)

    def _replace(self,p,e):
        """Replace the element at position p with e ,and return old element"""
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self,p):
        """Delete the node at Position p, and replace it with its child. if any

        Return the element that had been stored at Postion p
        Raise ValueError if Position p is invalid or p has two children
        """
        """
        Delete the node at position p, and replace it with its child, if any.
        Return the element at position p. Raise a ValueErorr if position p is invalid,
        or if there are two children. 
        """

        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('p had two children')

        if node._left:
            child = node._left
        else:
            child = node._right

        if child is not None:
            child._parent = node._parent

        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node # convention for deprecated node
        return node._element

    def _attach(self,p,t1,t2):
        """Attach trees t1 and t2, respectively, as the left and right
        subtrees od the extend position p.
        As a side effect, set t1 and t2 to None
        Raise a TypeError if trees t1 and t2 do not match self tree type.
        Raise a ValueError if position p is invalid or not external
        """
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError("Position must be a leaf.")

        if not type(self) is type(t1) is type(t2):
            raise TypeError("Trees must be of the same type")

        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0

        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0

# Exercise: Test this data structure

