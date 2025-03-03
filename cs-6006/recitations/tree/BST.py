from binary_tree import BinaryNode, BinaryTree

class BST_Node(BinaryNode):
    def subtree_find(self, A):
        """
        If A is self.item return it.
        If A is greater than self.item then go to the right
        subtree, else go to the left subtree.
        """
        if A < self.item.key:
            if self.left:
                return self.left.subtree_find(A)
        elif A > self.item.key:
            if self.right:
                return self.right.subtree_find(A)
        else: return A
        return None

    def subtree_find_next(self, A):
        """
        If A is found, return first item in the right subtree.
        If A is not found, return item itself.
        """
        if self.item.key <= A:
            if self.right:
                return self.right.subtree_find_next(A)
            else: return None
        elif self.left:
            B = self.left.subtree_find_next(A)
            if B: return B
        return self

    def subtree_find_prev(self, A):
        if self.item.key >= A:
            if self.left: return self.left.subtree_find_prev(A)
            # end of the tree.
            else: return None
        elif self.right:
            return self.right.subtree_find_prev(A)
        return self

    def subtree_insert(self, A):
        pass


class Set_Binary_Tree(BinaryTree):
    """
    Top level Data structure for holding a Set Binary Tree
    """
    def __init__(self): super().__init__(BST_Node)

    def build_tree(self, X):
        pass

    def find_min(self):
        pass

    def find_max(self):
        pass

    def find(self, k):
        pass

    def find_next(self, k):
        pass

    def find_prev(self, k):
        pass

    def insert(self, x):
        pass

    def delete(self, k):
        pass
