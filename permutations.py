from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Given a list of distinct integers, return all possible permutations.
        """
        def backtrack(first = 0):
            if first == n:
                output.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]
        n = len(nums)
        output = []
        backtrack()
        return output

# Time complexity: O(N!) where N is the number of elements in the list.
# Space complexity: O(N!) where N is the number of elements in the list.

import unittest

class TestPermutations(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_permute(self) -> None:
        self.assertEqual(self.solution.permute([1, 2, 3]), [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]])
        self.assertEqual(self.solution.permute([0, 1]), [[0, 1], [1, 0]])
        self.assertEqual(self.solution.permute([1]), [[1]])

if __name__ == '__main__':
    unittest.main()
