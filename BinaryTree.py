# Abstract Data Type: Binary Trees
# Abstract class, not providing complete implementations of left and right children
# A Binary Tree B inherits from Tree
# B.left(p): Returns the position to the left child of p, ot None
# B.right(p): Returns the position to the right child of p, or None
# B.sibling(p): Return th position that represents the sibling of P
# inorder(): traversal algorithm to go from bottom to top, left to right
# we will override the position method from parent to use inorder()
from abc import ABC

from Trees import Trees

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

    def position(self,mode="inorder"):
        if mode == "inorder":
            return self.inorder()
        else:
            super().positions(mode)

