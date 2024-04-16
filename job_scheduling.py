from typing import List
import unittest

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
        We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

        You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

        If you choose a job that ends at time X you will be able to start another job that starts at time X.
        """
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        dp = [[0, 0]]
        for s, e, p in jobs:
            i = self.binary_search(dp, s)
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
        return dp[-1][1]

    def binary_search(self, dp, s):
        l, r = 0, len(dp) - 1
        while l < r:
            m = (l + r + 1) // 2
            if dp[m][0] <= s:
                l = m
            else:
                r = m - 1
        return l

# Time complexity: O(nlogn)
# Space complexity: O(n)

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_jobScheduling(self):
        self.assertEqual(self.solution.jobScheduling([1,2,3,3], [3,4,5,6], [50,10,40,70]), 120)
        self.assertEqual(self.solution.jobScheduling([1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60]), 150)
        self.assertEqual(self.solution.jobScheduling([1,1,1], [2,3,4], [5,6,4]), 6)

if __name__ == '__main__':
    unittest.main()
