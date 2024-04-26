from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
        """
        n = len(s)
        if n == 0:
            return False
        word_set = set(wordDict)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[n]

# Time complexity: O(n^2)
# Space complexity: O(n)

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_wordBreak(self):
        self.assertTrue(self.solution.wordBreak("leetcode", ["leet", "code"]))
        self.assertTrue(self.solution.wordBreak("applepenapple", ["apple", "pen"]))
        self.assertFalse(self.solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))

if __name__ == '__main__':
    unittest.main()
