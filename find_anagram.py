from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
       Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
        """
        res = []
        if len(s) < len(p):
            return res
        p_count = [0] * 26
        s_count = [0] * 26
        for i in range(len(p)):
            p_count[ord(p[i]) - ord('a')] += 1
            s_count[ord(s[i]) - ord('a')] += 1
        if p_count == s_count:
            res.append(0)
        for i in range(len(p), len(s)):
            s_count[ord(s[i]) - ord('a')] += 1
            s_count[ord(s[i - len(p)]) - ord('a')] -= 1
            if p_count == s_count:
                res.append(i - len(p) + 1)
        return res

# Time complexity: O(N)
# Space complexity: O(1)

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_findAnagrams(self):
        self.assertEqual(self.solution.findAnagrams("cbaebabacd", "abc"), [0,6])
        self.assertEqual(self.solution.findAnagrams("abab", "ab"), [0,1,2])

if __name__ == '__main__':
    unittest.main()
