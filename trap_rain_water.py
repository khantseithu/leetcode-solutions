from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
        """
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        result = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    result += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    result += right_max - height[right]
                right -= 1
        return result

# Time complexity: O(N) where N is the length of the height list.
# Space complexity: O(1).

import unittest

class TestTrapRainWater(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_trap_rain_water(self) -> None:
        self.assertEqual(self.solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]), 6)
        self.assertEqual(self.solution.trap([4,2,0,3,2,5]), 9)

if __name__ == '__main__':
    unittest.main()
