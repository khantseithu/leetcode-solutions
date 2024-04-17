from typing import Optional
import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        """
        You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.

        Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

        As a reminder, any shorter prefix of a string is lexicographically smaller.

        For example, "ab" is lexicographically smaller than "aba".
        A leaf of a node is a node that has no children.
        """
        def dfs(node):
            if not node:
                return ''
            left = dfs(node.left)
            right = dfs(node.right)
            current_char = chr(node.val + ord('a'))
            if not left and not right:
                return current_char
            if not left:
                return right + current_char
            if not right:
                return left + current_char
            return  min(left, right) + current_char
        return dfs(root)



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_smallestFromLeaf(self):
        root = TreeNode(0)
        root.left = TreeNode(1)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(4)
        self.assertEqual(self.solution.smallestFromLeaf(root), 'dba')

        root = TreeNode(4)
        root.left = TreeNode(0)
        root.right = TreeNode(1)
        root.right.left = TreeNode(1)
        self.assertEqual(self.solution.smallestFromLeaf(root), 'bae')


if __name__ == '__main__':
    unittest.main()
