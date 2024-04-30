class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

        Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

        The test cases are generated so that the answer will be less than or equal to 2 * 109.
        """
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

# Time complexity: O(N * M) where N is the length of the m and M is the length of n.
# Space complexity: O(N * M) where N is the length of the m and M is the length of n.

import unittest

class TestUniquePaths(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_unique_paths(self) -> None:
        self.assertEqual(self.solution.uniquePaths(3, 7), 28)
        self.assertEqual(self.solution.uniquePaths(3, 2), 3)
        self.assertEqual(self.solution.uniquePaths(7, 3), 28)
        self.assertEqual(self.solution.uniquePaths(3, 3), 6)

if __name__ == '__main__':
    unittest.main()
