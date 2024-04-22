from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Given an m x n matrix, return all elements of the matrix in spiral order.
        """
        if not matrix:
            return []
        rows, cols = len(matrix), len(matrix[0])
        left, right, top, bottom = 0, cols - 1, 0, rows - 1
        res = []
        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            for i in range(top + 1, bottom + 1):
                res.append(matrix[i][right])
            if left < right and top < bottom:
                for i in range(right - 1, left, -1):
                    res.append(matrix[bottom][i])
                for i in range(bottom, top, -1):
                    res.append(matrix[i][left])
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return res

# Time complexity: O(N)
# Space complexity: O(1)

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_spiralOrder(self):
        self.assertEqual(self.solution.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]), [1,2,3,6,9,8,7,4,5])
        self.assertEqual(self.solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]), [1,2,3,4,8,12,11,10,9,5,6,7])

if __name__ == '__main__':
    unittest.main()
