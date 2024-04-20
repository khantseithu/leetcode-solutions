from typing import List
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        """
        You are given a 0-indexed m x n binary matrix land where a 0 represents a hectare of forested land and a 1 represents a hectare of farmland.

        To keep the land organized, there are designated rectangular areas of hectares that consist entirely of farmland. These rectangular areas are called groups. No two groups are adjacent, meaning farmland in one group is not four-directionally adjacent to another farmland in a different group.

        land can be represented by a coordinate system where the top left corner of land is (0, 0) and the bottom right corner of land is (m-1, n-1). Find the coordinates of the top left and bottom right corner of each group of farmland. A group of farmland with a top left corner at (r1, c1) and a bottom right corner at (r2, c2) is represented by the 4-length array [r1, c1, r2, c2].

        Return a 2D array containing the 4-length arrays described above for each group of farmland in land. If there are no groups of farmland, return an empty array. You may return the answer in any order.
        """
        rows = len(land)
        cols = len(land[0])
        farmlands = []
        for i in range(rows):
            for j in range(cols):
                if land[i][j] == 1:
                    top_left = [i, j]
                    bottom_right = [i, j]
                    self.dfs(land, i, j, top_left, bottom_right)
                    farmlands.append([top_left[0], top_left[1], bottom_right[0], bottom_right[1]])
        return farmlands

    def dfs(self, land: List[List[int]], i: int, j: int, top_left: List[int], bottom_right: List[int]) -> None:
        if i < 0 or i >= len(land) or j < 0 or j >= len(land[0]) or land[i][j] == 0:
            return
        land[i][j] = 0
        top_left[0] = min(top_left[0], i)
        top_left[1] = min(top_left[1], j)
        bottom_right[0] = max(bottom_right[0], i)
        bottom_right[1] = max(bottom_right[1], j)
        self.dfs(land, i + 1, j, top_left, bottom_right)
        self.dfs(land, i - 1, j, top_left, bottom_right)
        self.dfs(land, i, j + 1, top_left, bottom_right)
        self.dfs(land, i, j - 1, top_left, bottom_right)

# Time complexity: O(m * n) where m is the number of rows and n is the number of columns
# Space complexity: O(m * n) where m is the number of rows and n is the number of columns

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_findFarmland(self):
        self.assertEqual(self.solution.findFarmland([
            [1,0,0],
            [0,1,1],
            [0,1,1]
        ]), [[0,0,0,0],[1,1,2,2]])
        self.assertEqual(self.solution.findFarmland([
            [1,1],
            [1,1]
        ]), [[0,0,1,1]])
        self.assertEqual(self.solution.findFarmland([
            [0,0],
            [0,0]
        ]), [])


if __name__ == '__main__':
    unittest.main()
