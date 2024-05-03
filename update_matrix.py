from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

        The distance between two adjacent cells is 1.
        """
        m, n = len(mat), len(mat[0])
        q = []
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = float('inf')
        while q:
            i, j = q.pop(0)
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and mat[x][y] > mat[i][j] + 1:
                    mat[x][y] = mat[i][j] + 1
                    q.append((x, y))
        return mat

# Time complexity: O(m * n)
# Space complexity: O(m * n)

import unittest

class TestUpdateMatrix(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_update_matrix(self) -> None:
        mat = [[0,0,0],[0,1,0],[0,0,0]]
        self.assertListEqual(self.solution.updateMatrix(mat), [[0,0,0],[0,1,0],[0,0,0]])
        mat = [[0,0,0],[0,1,0],[1,1,1]]
        self.assertListEqual(self.solution.updateMatrix(mat), [[0,0,0],[0,1,0],[1,2,1]])

if __name__ == '__main__':
    unittest.main()
