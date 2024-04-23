from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Given a reference of a node in a connected undirected graph.

        Return a deep copy (clone) of the graph.

        Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
        """
        if not node:
            return None
        visited = {}
        def dfs(node):
            if node in visited:
                return visited[node]
            clone = Node(node.val)
            visited[node] = clone
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone
        return dfs(node)

# Time complexity: O(N)
# Space complexity: O(N) where n is the number of nodes in the graph.

import unittest

class TestCloneGraph(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_clone_graph(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node1.neighbors = [node2, node4]
        node2.neighbors = [node1, node3]
        node3.neighbors = [node2, node4]
        node4.neighbors = [node1, node3]
        clone = self.solution.cloneGraph(node1)
        self.assertEqual(clone.val, node1.val)
        self.assertEqual(len(clone.neighbors), len(node1.neighbors))


if __name__ == '__main__':
    unittest.main()
