class Node:
    def __init__(self, value):
       self.left = None
       self.value = value
       self.right = None

class BinarySearchTree:
    def __init__ (self, value):
        self.head = Node(value=value)

    def insert_left(self, new_node, node):
        if node.left is not None:
            self.insert_node(new_node.value, node.left)
        else:
            node.left = new_node

    def insert_right(self, new_node, node):
        if node.right is not None:
            self.insert_node(new_node.value, node.right)
        else:
            node.right = new_node

    def insert_node(self, value, node):
        new_node = Node(value=value)

        
        if node.value > value:
            self.insert_left(new_node, node)

        elif node.value < value:
            self.insert_right(new_node, node)

        return self.head
        
