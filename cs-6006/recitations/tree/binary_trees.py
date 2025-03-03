from __future__ import annotations

class BinaryNode:
    def __init__(self, x):
        self.item = x
        self.left: BinaryNode | None = None
        self.right: BinaryNode | None = None
        self.parent: BinaryNode | None = None

    def subtree_iter(self):
        """
        In order traversal of the Tree
        """
        if self.left:
            yield from self.left.subtree_iter()
        yield self
        if self.right:
            yield from self.right.subtree_iter()

    def subtree_first(self) -> BinaryNode:
        """
        keep going down the left child, until you can't
        """
        if self.left:
            return self.left.subtree_first()
        else:
            return self

    def subtree_last(self) -> BinaryNode:
        """
        keep going down the right subtree, until you can't
        """
        if self.right:
            return self.right.subtree_last()
        else:
            return self

    def successor(self):
        """
        if node has a right child, return the first item in the right subtree as successor.

        if not, go up the tree, as long as the node has a parent and node itself, is the right
        child of it's parent, else return node parent.
        """
        if self.right:
            return self.right.subtree_first()
        node = self
        while node.parent and (node is node.parent.right):
            node = node.parent
        return node.parent

    def predecessor(self):
        """
        if node has a left child, return the last item in the left subtree as predecessor.
        if not, go up the tree, as long as the node has a parent and node itself is the left child of the parent.
        """
        if self.left:
            return self.left.subtree_last()
        node = self
        while node.parent and (node is node.parent.left):
            node = node.parent
        return node.parent

    def subtree_insert_before(self, X: BinaryNode):
        """
        if A does not have a left child, insert the new node there.

        If A has a left child, go down the left subtree, till you find the last item there. insert
        the new node as the right child of that last node because last node will not have a right child.
        """
        if not self.left:
            self.left = X
            X.parent = self
            return
        else:
            prev = self.left.subtree_last()
            prev.right = X
            X.parent = prev

    def subtree_insert_after(self, X: BinaryNode) -> bool:
        """
        if node does not have a right child, put the new node as it's right child.

        if it does, put the new node as the left child of the first item, in the right subtree.
        """
        if not self.right:
            self.right = X
            X.parent = self
        else:
            node = self.right.subtree_first()
            node.left = X
            X.parent = node
        return True

    def subtree_delete(self):
        """
        We can only delete leaf nodes.
        if A has a left or a right child, we switch it with either it's predecessor, or successor, till
        it has no children.

        Once it has no children, we remove it's connection with it's parent, hence deleting it and returning
        the deleted node.
        """
        if self.left or self.right:
            if self.left:
                B = self.predecessor()
            else:
                B = self.successor()
            self.item, B.item = B.item, self.item
            return B.subtree_delete()
        if self.parent:
            if self.parent.left is self:
                self.parent.left = None
            else:
                self.parent.right = None
        return self


class BinaryTree:
    """
    Top level Data structure for holding a Binary Tree.
    """
    def __init__(self, Node_Type=BinaryNode) -> None:
        self.root: BinaryNode | None = None
        self.size = 0
        self.Node_Type = Node_Type

    def __len__(self):
        return self.size

    def __iter__(self):
        if self.root:
            for node in self.root.subtree_iter():
                yield node.item

    def build_tree(self, X):
        def build_tree_recur(start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            node = self.Node_Type(X[mid])
            node.left = build_tree_recur(start, mid - 1)
            if node.left:
                node.left.parent = node
            node.right = build_tree_recur(mid + 1, end)
            if node.right:
                node.right.parent = node
            return node
        self.root = build_tree_recur(0, len(X) - 1)
        self.size = len(X)
