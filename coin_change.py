from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

        Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

        You may assume that you have an infinite number of each kind of coin.
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

# Time complexity: O(N * M) where N is the length of the coins array and M is the amount.
# Space complexity: O(M) where M is the amount.

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_coin_change(self) -> None:
        self.assertEqual(self.solution.coinChange([1, 2, 5], 11), 3)
        self.assertEqual(self.solution.coinChange([2], 3), -1)
        self.assertEqual(self.solution.coinChange([1], 0), 0)
        self.assertEqual(self.solution.coinChange([1], 1), 1)
        self.assertEqual(self.solution.coinChange([1], 2), 2)

if __name__ == '__main__':
    unittest.main()
