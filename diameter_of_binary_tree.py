from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Given the root of a binary tree, return the length of the diameter of the tree.

        The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

        The length of a path between two nodes is represented by the number of edges between them.
        """
        self.diameter = 0
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)
        dfs(root)
        return self.diameter

# Time complexity: O(n)
# Space complexity: O(n)

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_diameterOfBinaryTree(self):
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 3)

        root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 3)

        root = TreeNode(1)
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 0)

        root = None
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 0)

if __name__ == '__main__':
    unittest.main()
