from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

        Find two lines that together with the x-axis form a container, such that the container contains the most water.

        Return the maximum amount of water a container can store.

        Notice that you may not slant the container.
        """
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

# Time complexity: O(n)
# Space complexity: O(1)

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_maxArea(self):
        self.assertEqual(self.solution.maxArea([1,8,6,2,5,4,8,3,7]), 49)
        self.assertEqual(self.solution.maxArea([1,1]), 1)
        self.assertEqual(self.solution.maxArea([4,3,2,1,4]), 16)
        self.assertEqual(self.solution.maxArea([1,2,1]), 2)


if __name__ == '__main__':
    unittest.main()
