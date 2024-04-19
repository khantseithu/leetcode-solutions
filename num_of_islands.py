from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
        An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
        """
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    islands += 1
                    self.dfs(grid, i, j)
        return islands

    def dfs(self, grid: List[List[str]], i: int, j: int) -> None:
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0":
            return
        grid[i][j] = "0"
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)

# Time complexity: O(m * n) where m is the number of rows and n is the number of columns
# Space complexity: O(m * n) where m is the number of rows and n is the number of columns

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_numIslands(self):
        self.assertEqual(self.solution.numIslands([
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]), 1)
        self.assertEqual(self.solution.numIslands([
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]), 3)
        self.assertEqual(self.solution.numIslands([
            ["1","0","1","1","0","1","1"]
        ]), 3)


if __name__ == '__main__':
    unittest.main()
