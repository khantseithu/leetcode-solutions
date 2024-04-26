from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of the largest rectangle in the histogram.
        """
        n = len(heights)
        if n == 0:
            return 0
        stack = []
        max_area = 0
        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        while stack:
            height = heights[stack.pop()]
            width = n if not stack else n - stack[-1] - 1
            max_area = max(max_area, height * width)
        return max_area

# Time complexity: O(n) where n is the length of the heights
# Space complexity: O(n) where n is the length of the heights

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_largestRectangleArea(self):
        self.assertEqual(self.solution.largestRectangleArea([2, 1, 5, 6, 2, 3]), 10)
        self.assertEqual(self.solution.largestRectangleArea([2, 4]), 4)
        self.assertEqual(self.solution.largestRectangleArea([2, 1, 2]), 3)

if __name__ == '__main__':
    unittest.main()
