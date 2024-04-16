
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        """
        Given the root of a binary tree, then value v and depth d, you need to add a row of nodes with value v at the given depth d. The root node is at depth 1.
        The adding rule is: given a positive integer depth d, for each NOT null tree nodes N in depth d-1, create two tree nodes with value v as N's left subtree root and right subtree root.
        """
        if depth == 1:
            return TreeNode(val, root)
        self.dfs(root, val, depth, 1)
        return root

    def dfs(self, node: Optional[TreeNode], val: int, depth: int, current_depth: int) -> None:
        if not node:
            return
        if current_depth == depth - 1:
            node.left = TreeNode(val, node.left)
            node.right = TreeNode(val, None, node.right)
        else:
            self.dfs(node.left, val, depth, current_depth + 1)
            self.dfs(node.right, val, depth, current_depth + 1)

# Time complexity: O(n)
# Space complexity: O(n)

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_addOneRow(self):
        root = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1)), TreeNode(6, TreeNode(5)))
        self.solution.addOneRow(root, 1, 2)
        root = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1)), TreeNode(6, TreeNode(5)))
        self.solution.addOneRow(root, 1, 1)

if __name__ == '__main__':
    unittest.main()
