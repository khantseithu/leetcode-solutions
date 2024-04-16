from typing import List
import unittest


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
        Find all unique triplets in the array which gives the sum of zero.
        """
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result

# Time complexity: O(n^2)
# Space complexity: O(n)

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_threeSum(self):
        self.assertEqual(self.solution.threeSum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])
        self.assertEqual(self.solution.threeSum([]), [])
        self.assertEqual(self.solution.threeSum([0]), [])
        self.assertEqual(self.solution.threeSum([0, 0, 0]), [[0, 0, 0]])
        self.assertEqual(self.solution.threeSum([0, 0, 0, 0]), [[0, 0, 0]])

if __name__ == '__main__':
    unittest.main()
