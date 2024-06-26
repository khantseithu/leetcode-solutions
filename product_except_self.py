from typing import List
import unittest

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
        """
        n = len(nums)
        left = [1] * n
        right = [1] * n
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        return [left[i] * right[i] for i in range(n)]

# Time complexity: O(n)
# Space complexity: O(n)

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_productExceptSelf(self):
        self.assertEqual(self.solution.productExceptSelf([1,2,3,4]), [24,12,8,6])
        self.assertEqual(self.solution.productExceptSelf([-1,1,0,-3,3]), [0,0,9,0,0])


if __name__ == '__main__':
    unittest.main()
