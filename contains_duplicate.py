from typing import List
import unittest
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
        """
        return len(nums) != len(set(nums))

# Time complexity: O(n)
# Space complexity: O(n)

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_containsDuplicate(self):
        self.assertEqual(self.solution.containsDuplicate([1,2,3,1]), True)
        self.assertEqual(self.solution.containsDuplicate([1,2,3,4]), False)
        self.assertEqual(self.solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]), True)

if __name__ == '__main__':
    unittest.main()
