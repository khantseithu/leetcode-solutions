from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
        """
        if not root:
            return []
        result = []
        queue = [root]
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result

# Time complexity: O(n)
# Space complexity: O(n)

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_levelOrder(self):
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        self.assertEqual(self.solution.levelOrder(root), [[3],[9,20],[15,7]])
        root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
        self.assertEqual(self.solution.levelOrder(root), [[1],[2,3],[4]])

if __name__ == '__main__':
    unittest.main()
