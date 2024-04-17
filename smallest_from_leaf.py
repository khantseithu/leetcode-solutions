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
        def dfs(node, path, result):
            if not node:
                return
            path.append(chr(node.val + ord('a')))
            if not node.left and not node.right:
                result.append(''.join(path[::-1]))
            dfs(node.left, path, result)
            dfs(node.right, path, result)
            path.pop()

        result = []
        dfs(root, [], result)
        return min(result) if result else ''


# Time complexity: O(n)
# Space complexity: O(n)

import unittest

class TestSmallestFromLeaf(unittest.TestCase):
    def test_example_1(self):
        root = TreeNode(0)
        root.left = TreeNode(1)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(4)
        self.assertEqual(Solution().smallestFromLeaf(root), 'dba')

if __name__ == '__main__':
    unittest.main()
