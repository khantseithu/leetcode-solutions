class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        def helper(s, k):
            n = len(s)
            dp = [[0] * 26 for _ in range(n)]
            for i in range(n):
                for j in range(26):
                    if i == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i - 1][j]
                        if abs(ord(s[i]) - ord('a') - j) <= k:
                            dp[i][j] = max(dp[i][j], 1 + (dp[i - 1][j] if j > 0 else 0))
            return max(max(dp[-1]), 0)

        return helper(s, k)

import unittest

class TestLongestIdealString(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_longest_ideal_string(self) -> None:
        self.assertEqual(self.solution.longestIdealString("acfgbd", 2), 4)
        self.assertEqual(self.solution.longestIdealString("abcd", 3), 4)
        self.assertEqual(self.solution.longestIdealString("acfgbd", 2), 4)


if __name__ == '__main__':
    unittest.main()
