from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        return inorder(root)[k-1]

# Time complexity: O(N)
# Space complexity: O(N) where n is the number of nodes in the tree.

import unittest

class TestKthSmallest(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_kth_smallest(self):
        pass
