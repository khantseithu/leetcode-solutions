from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Given a list of integers, return all possible subsets.
        """
        def backtrack(start = 0, path = []):
            output.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        output = []
        backtrack()
        return output

# Time complexity: O(N * 2^N) where N is the number of elements in the list.
# Space complexity: O(N * 2^N) where N is the number of elements in the list.

import unittest

class TestSubsets(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_subsets(self) -> None:
        self.assertEqual(self.solution.subsets([1, 2, 3]), [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]])
        self.assertEqual(self.solution.subsets([0]), [[], [0]])

if __name__ == '__main__':
    unittest.main()
