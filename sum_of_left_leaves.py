from typing import Optional
import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        """
        Find the sum of all left leaves in a given binary tree.
        """
        def dfs(node, is_left):
            if not node:
                return 0
            if not node.left and not node.right:
                return node.val if is_left else 0
            return dfs(node.left, True) + dfs(node.right, False)
        return dfs(root, False)

# Time complexity: O(n)
# Space complexity: O(n)

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_sumOfLeftLeaves(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(self.solution.sumOfLeftLeaves(root), 24)

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right = TreeNode(3)
        self.assertEqual(self.solution.sumOfLeftLeaves(root), 4)

        root = TreeNode(1)
        self.assertEqual(self.solution.sumOfLeftLeaves(root), 0)


if __name__ == '__main__':
    unittest.main()
