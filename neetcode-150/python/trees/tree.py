class Node:

    def __init__(self, data, left, right):
        self.left = left
        self.right = right
        self.value = data


class Tree:

    def __init__(self):
        self.root = Node(None, None, None)

    def _populate(self, node: Node):
        is_left = input("Do you want to input data to the left")
        if is_left is True:
            data = input(f"Enter the data left to {node.value}")
            new_node = Node(int(data), None, None)
            node.left = new_node
            self._populate(node.left)

        is_right = input("Do you want to input data to the right")
        if is_right is True:
            data = input(f"Enter the data right to {node.value}")
            node.right = Node(int(data), None, None)
            self._populate(node.right)

    def populate(self):
        print("Populating tree \n")
        data = input("Enter the data of root node")
        self.root = Node(data, None, None)
        self._populate(self.root)

    def display(self):
        self._display(self.root, "")

    def _display(self, node, indent):
        if node is None:
            return
        print(indent + str(node.value))
        self._display(node.left, indent + "\t")
        self._display(node.right, indent + "\t")

    def pretty_display(self):
        self._pretty_display(self.root, 0)

    def _pretty_display(self, node, level):
        if node is None:
            return

        self._pretty_display(node.right, level + 1)
        if level != 0:
            print("|" + "\t\t" * (level - 1) + "|------->" + str(node.value))
        else:
            print(node.value)
        self._pretty_display(node.left, level + 1)


if __name__ == "__main__":
    tree = Tree()
    tree.populate()
    print("\nTree Display:\n")
    tree.display()
    print("\nPretty Display:\n")
    tree.pretty_display()
    print("\nPre-order Traversal:")