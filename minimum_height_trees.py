from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

        The graph contains n nodes which are labeled from 0 to n - 1. You will be given an integer n and a list of undirected edges (each edge is a pair of labels).

        You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
        """
        if n == 1:
            return [0]
        adj = [set() for _ in range(n)]
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
        leaves = [i for i in range(n) if len(adj[i]) == 1]
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = adj[leaf].pop()
                adj[neighbor].remove(leaf)
                if len(adj[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves

# Time complexity: O(N) where N is the number of nodes in the graph.
# Space complexity: O(N) where N is the number of nodes in the graph.

import unittest

class TestMinimumHeightTrees(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_findMinHeightTrees(self) -> None:
        n = 4
        edges = [[1, 0], [1, 2], [1, 3]]
        self.assertEqual(self.solution.findMinHeightTrees(n, edges), [1])
        n = 6
        edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
        self.assertEqual(self.solution.findMinHeightTrees(n, edges), [3, 4])

if __name__ == '__main__':
    unittest.main()
