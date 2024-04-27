from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
        """
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        root_index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:1+root_index], inorder[:root_index])
        root.right = self.buildTree(preorder[1+root_index:], inorder[root_index+1:])
        return root

# Time complexity: O(n)
# Space complexity: O(n)

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_buildTree(self):
        def inorder_traversal(node):
            if not node:
                return []
            return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)
        def preorder_traversal(node):
            if not node:
                return []
            return [node.val] + preorder_traversal(node.left) + preorder_traversal(node.right)
        root = self.solution.buildTree([3,9,20,15,7], [9,3,15,20,7])
        self.assertEqual(inorder_traversal(root), [9,3,15,20,7])
        self.assertEqual(preorder_traversal(root), [3,9,20,15,7])
        root = self.solution.buildTree([], [])
        self.assertEqual(inorder_traversal(root), [])
        self.assertEqual(preorder_traversal(root), [])

if __name__ == '__main__':
    unittest.main()
