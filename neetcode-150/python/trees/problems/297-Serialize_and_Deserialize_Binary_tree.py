# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        
        queue = deque([root])
        result = []
        
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("N")  # Marker for null nodes

        return ",".join(result)

    def deserialize(self, data: str):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        values = data.split(",")

        root = TreeNode(data[0])
        # since 0 is processed already as root, we will start by processing index 1.
        index = 1
        queue = collections.deque()

        while queue:
            node = queue.popleft()

            if values[index] != "N": # this is tree node.
                new_node = TreeNode(values[index])
                node.left = new_node
                queue.append(new_node)
            index += 1

            if values[index] != "N":
                new_node = TreeNode(values[index])
                node.right = new_node
                queue.append(new_node)
            index += 1

        return root

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
