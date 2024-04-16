from typing import List
import unittest

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """"
        Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
        """
        start, end = newInterval
        left, right = [], []
        for interval in intervals:
            if interval[1] < start:
                left += [interval]
            elif interval[0] > end:
                right += [interval]
            else:
                start = min(start, interval[0])
                end = max(end, interval[1])
        return left + [[start, end]] + right


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_insert(self):
        self.assertEqual(self.solution.insert([[1,3],[6,9]], [2,5]), [[1,5],[6,9]])
        self.assertEqual(self.solution.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]), [[1,2],[3,10],[12,16]])
        self.assertEqual(self.solution.insert([], [5,7]), [[5,7]])
        self.assertEqual(self.solution.insert([[1,5]], [2,3]), [[1,5]])

if __name__ == '__main__':
    unittest.main()
