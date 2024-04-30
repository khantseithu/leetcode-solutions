from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.
        """
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[target]

# Time complexity: O(N * M) where N is the length of the nums array and M is the target.
# Space complexity: O(M) where M is the target.

import unittest

class TestCanPartition(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_can_partition(self) -> None:
        self.assertEqual(self.solution.canPartition([1, 5, 11, 5]), True)
        self.assertEqual(self.solution.canPartition([1, 2, 3, 5]), False)

if __name__ == '__main__':
    unittest.main()
