from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Given a collection of intervals, merge all overlapping intervals.
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else:
                merged.append(intervals[i])
        return merged

# Time complexity: O(n log n)
# Space complexity: O(n)

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_merge(self):
        self.assertEqual(self.solution.merge([[1,3],[2,6],[8,10],[15,18]]), [[1,6],[8,10],[15,18]])
        self.assertEqual(self.solution.merge([[1,4],[4,5]]), [[1,5]])
        self.assertEqual(self.solution.merge([[1,4],[0,4]]), [[0,4]])
        self.assertEqual(self.solution.merge([[1,4],[2,3]]), [[1,4]])
        self.assertEqual(self.solution.merge([[1,4],[0,0]]), [[0,0],[1,4]])
        self.assertEqual(self.solution.merge([[1,4],[0,1]]), [[0,4]])
        self.assertEqual(self.solution.merge([[1,4],[0,2],[3,5]]), [[0,5]])


if __name__ == '__main__':
    unittest.main()
