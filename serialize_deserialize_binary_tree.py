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
        def build_string(node):
            if not node:
                return "None,"
            return str(node.val) + "," + build_string(node.left) + build_string(node.right)

        return build_string(root)



    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def build_tree(nodes):
            if nodes[0] == "None":
                nodes.pop(0)
                return None
            root = TreeNode(int(nodes[0]))
            nodes.pop(0)
            root.left = build_tree(nodes)
            root.right = build_tree(nodes)
            return root

        nodes = data.split(",")
        return build_tree(nodes)

# Time complexity: O(n)
# Space complexity: O(n)

import unittest

class TestSerializeDeserializeBinaryTree(unittest.TestCase):
    def setUp(self):
        self.codec = Codec()

    def test_serialize_deserialize(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)
        self.assertEqual(self.codec.deserialize(self.codec.serialize(root)).val, 1)
        self.assertEqual(self.codec.deserialize(self.codec.serialize(root)).left.val, 2)
        self.assertEqual(self.codec.deserialize(self.codec.serialize(root)).right.val, 3)
        self.assertEqual(self.codec.deserialize(self.codec.serialize(root)).right.left.val, 4)
        self.assertEqual(self.codec.deserialize(self.codec.serialize(root)).right.right.val, 5)

if __name__ == '__main__':
    unittest.main()
