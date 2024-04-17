from typing import List
import unittest

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

        The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
        frequency
        of at least one of the chosen numbers is different.

        The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
        """
        result = []
        self.dfs(candidates, target, 0, [], result)
        return result

    def dfs(self, candidates: List[int], target: int, index: int, path: List[int], result: List[List[int]]) -> None:
        if target < 0:
            return
        if target == 0:
            result.append(path)
            return
        for i in range(index, len(candidates)):
            self.dfs(candidates, target - candidates[i], i, path + [candidates[i]], result)

# Time complexity: O(n^m) where n is the number of candidates and m is the target
# Space complexity: O(m) where m is the target


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_combinationSum(self):
        self.assertEqual(self.solution.combinationSum([2,3,6,7], 7), [[2,2,3],[7]])
        self.assertEqual(self.solution.combinationSum([2,3,5], 8), [[2,2,2,2],[2,3,3],[3,5]])
        self.assertEqual(self.solution.combinationSum([2], 1), [])
        self.assertEqual(self.solution.combinationSum([1], 1), [[1]])
        self.assertEqual(self.solution.combinationSum([1], 2), [[1,1]])
        self.assertEqual(self.solution.combinationSum([1], 3), [[1,1,1]])
        self.assertEqual(self.solution.combinationSum([1,2], 3), [[1,1,1],[1,2]])
        self.assertEqual(self.solution.combinationSum([1,2], 4), [[1,1,1,1],[1,1,2],[2,2]])
        self.assertEqual(self.solution.combinationSum([1,2], 5), [[1,1,1,1,1],[1,1,1,2],[1,2,2]])

if __name__ == '__main__':
    unittest.main()
