from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Given an array nums of size n, return the majority element.
        The majority element is the element that appears more than ⌊n / 2⌋ times.
        You may assume that the majority element always exists in the array.
        """
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate

# Time complexity: O(n)
# Space complexity: O(1)

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_majorityElement(self) -> None:
        self.assertEqual(self.solution.majorityElement([3,2,3]), 3)
        self.assertEqual(self.solution.majorityElement([2,2,1,1,1,2,2]), 2)
        self.assertEqual(self.solution.majorityElement([1]), 1)

if __name__ == '__main__':
    unittest.main()
