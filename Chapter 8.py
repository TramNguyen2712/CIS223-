class Tree:
    """Abstract base class representng a tree structure"""

    #-----------------nested Position class ---------

    class Position:
        """An abstraction representing the location of a single element"""
        def element(self):
            """Return the element stored at this Position"""
            raise NotImplementedError('must be implemented by subclass')
        def __eq__(self, other):
            """Return True if other Position represents the same location"""
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            """Return True if other does not represent the same location"""
            return not(self==other)

    #----------- abstract methods that concrete subclass must support ------
    def root(self):
        """Return Position representing the tree's root (or None if empty)"""
        raise NotImplementedError('must be implemented by subclass')

    def parent(self,p):
        """Return Position representing p's parent (or None ifp is root)"""
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self,p):
        """Return the number of children that Position p has"""

    def children(self,p):
        """Generate an iteration of Positions representing p's children"""
        raise NotImplementedError('must be implement by subclass')

    def __len__(self):
        """Return the total number of elements in the tree"""
        raise NotImplementedError('must be implement by subclass')

    def is_root(self,p):
        """Return True if Position p presents the root of the tree"""
        return self.root() == p

    def is_leaf(self,p):
        """Return True of Position p does not have any children"""

    def is_empty(self):
        """Return True if the tree is empty"""
        return len(self) == 0

    def depth(self,p):
        """Return the number of levels separating Position p from the root"""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    #Running Complexity: O(n)

    def _height1(self):
        """Return the height of the tree"""
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self,p):
        """Return the height of the subtree rooted at Poition p"""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self,p = None):
        """Return the height of the subtree rooted at Position p

        If p is None, return the height of the entire tree
        """
        if p is None:
            p = self.root()
        return self._height2(p)


class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure. """

    #----------------------------additional abstract methods-----------
    def left(self,p):
        """Return a Position representing p's left child.
        Return None if p does not have a left child
        """
        raise NotImplementedError('must be implemented by subclass')

    def right(self,p):
        """Return a Position representing p's right child.
        Return None if p does not have a right child"""

        raise NotImplementedError('must be implemented by subclass')

    #------concrete methods implemented in this class-----
    def sibling(self,p):
        """Return a Position representing p's sibling (or None if no sibling)"""
        parent = self.parent(p)
        if parent is None: #p must be the root
            return None   #root has no sibling
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.right(parent)

    def children(self,p):
        """Generate an iteration of Postions representing p's children"""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)


class LinkedBinaryTree(BinaryTree):
    """Linked representation of a binary tree structure"""

    class _Node:  # Lightweight, nonpublic class for storing a node
        __slots__ = '_element', '_parent', '_left','_right'
        def __init__(self,element,parent=None, left=None,right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

        class Position(BinaryTree.Position):
            """An abstraction representing the location of a single element"""

            def __init__(self,container,node):
                """Constructor the element stored at this Position."""
                self._container = container
                self._node = node

            def element(self):
                """Return the element stored at this Position"""
                return self._node._element

            def __eq__(self, other):
                """Return True if other is a Position representing the same location"""
                return type(other) is type(self) and other._node is self._node

        def _validate(self,p):
            """Return associated node, if position is valid"""
            if not isinstance(p,self.Position):
                raise TypeError('p must be proper Position type')
            if p._container is not self:
                raise ValueError('p does not belong to this container')
            if p._node._parent is p._node:
                raise ValueError('p is no longer valid')
            return p._node

        def _make_position(self,node):
            """Return Position instance for given node (or None if no code)"""
            return self.Position(self,node) if node is not None else None

