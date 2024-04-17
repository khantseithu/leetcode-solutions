from typing import List
import unittest

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        i = 0
        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            else:
                i += 1

# Time complexity: O(n)
# Space complexity: O(1)

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_sortColors(self):
        nums = [2,0,2,1,1,0]
        self.solution.sortColors(nums)
        self.assertEqual(nums, [0,0,1,1,2,2])

        nums = [2,0,1]
        self.solution.sortColors(nums)
        self.assertEqual(nums, [0,1,2])

        nums = [0]
        self.solution.sortColors(nums)
        self.assertEqual(nums, [0])

        nums = [1]
        self.solution.sortColors(nums)
        self.assertEqual(nums, [1])

        nums = [2]
        self.solution.sortColors(nums)
        self.assertEqual(nums, [2])

        nums = [1,2,0]
        self.solution.sortColors(nums)
        self.assertEqual(nums, [0,1,2])

        nums = [1,0,2]
        self.solution.sortColors(nums)
        self.assertEqual(nums, [0,1,2])

        nums = [0,2,1]
        self.solution.sortColors(nums)
        self.assertEqual(nums, [0,1,2])

        nums = [0,1,2]
        self.solution.sortColors(nums)
        self.assertEqual(nums, [0,1,2])

        nums = [2,1,0]
        self.solution.sortColors(nums)
        self.assertEqual(nums, [0,1,2])

        nums = [2,0,1,2,1,0]
        self.solution.sortColors(nums)
        self.assertEqual(nums, [0,0,1,1,2,2])

if __name__ == '__main__':
    unittest.main()
