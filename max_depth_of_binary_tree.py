from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Given the root of a binary tree, return its maximum depth.

        A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Time complexity: O(n)
# Space complexity: O(n)

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_maxDepth(self):
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        self.assertEqual(self.solution.maxDepth(root), 3)

        root = TreeNode(1, None, TreeNode(2))
        self.assertEqual(self.solution.maxDepth(root), 2)

        root = None
        self.assertEqual(self.solution.maxDepth(root), 0)

        root = TreeNode(0)
        self.assertEqual(self.solution.maxDepth(root), 1)

if __name__ == '__main__':
    unittest.main()
