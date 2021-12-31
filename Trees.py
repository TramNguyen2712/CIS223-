# Abstract data type : Tree
# Tree uses position abstraction to determine node in tree
# Positions will contain elements, positions are comparable and must
# satisfy parent-child relationship
# We will code a tree as an "abstract" class with no mutator methods
# Mutator methods should be implemented by concrete classes that inherit
# the Tree object

# Tree T supports (and checks positions are valid)
# p.element() : Return element at p
# T.root() : Return position at root
# T.is_root() : Returns True if p is root
# T.parent(p) : Return position p' of parent of p; None if p is the root
# T.num_children(p) : Return the number of children of p
# T.children(p) : Generate the children of p; else we have an empty iterator if p is a leaf
# T.is_leaf(p) : Return True if p is a leaf
# len(T) : Number of position of T
# T.is_empty()
# T.positions() : Generate an iterator of all positions of T; empty if T is empty
# iter(T) : Generate iteration of all element stored in T; empty if T is empty
# height(p) : return the height as an integer of the node p
# depth(p) : return number of ancestors of p, excluding p itself

from Queues import ArrayQueue as aq
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

    def parent(self,p):
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
    def _subtree_preorder(self,p):
        # root first
        yield p # visit p, when p is a leaf we are in the base case
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

    def _subtree_postorder(self,p):
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p  # root last

    # Breadthfirst
    def breadthfirst(self):
        # using array queue
        if not self.is_empty():
            Q = aq() #empty queue....probably better if we used a Queue implemented with
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


















