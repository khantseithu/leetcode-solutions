from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        You are given an m x n grid where each cell can have one of three values:

        0 representing an empty cell,
        1 representing a fresh orange, or
        2 representing a rotten orange.
        Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

        Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
        """
        m, n = len(grid), len(grid[0])
        q = []
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        minutes = 0
        while q:
            minutes += 1
            for _ in range(len(q)):
                i, j = q.pop(0)
                for x, y in directions:
                    if 0 <= i + x < m and 0 <= j + y < n and grid[i + x][j + y] == 1:
                        grid[i + x][j + y] = 2
                        fresh -= 1
                        q.append((i + x, j + y))
        return minutes - 1 if fresh == 0 else -1

# Time complexity: O(m * n) where m is the number of rows and n is the number of columns
# Space complexity: O(m * n)

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_oranges_rotting(self) -> None:
        grid = [[2,1,1],[1,1,0],[0,1,1]]
        self.assertEqual(self.solution.orangesRotting(grid), 4)
        grid = [[2,1,1],[0,1,1],[1,0,1]]
        self.assertEqual(self.solution.orangesRotting(grid), -1)
        grid = [[0,2]]
        self.assertEqual(self.solution.orangesRotting(grid), 0)

if __name__ == '__main__':
    unittest.main()
