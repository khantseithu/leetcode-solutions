class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Given a string s, find the length of the longest substring without repeating characters.
        """
        n = len(s)
        if n == 0:
            return 0
        start = 0
        max_length = 0
        char_index = {}
        for i in range(n):
            if s[i] in char_index and char_index[s[i]] >= start:
                start = char_index[s[i]] + 1
            char_index[s[i]] = i
            max_length = max(max_length, i - start + 1)
        return max_length

# Time complexity: O(n)
# Space complexity: O(min(n, m)), where m is the size of the character set

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_lengthOfLongestSubstring(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(self.solution.lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(self.solution.lengthOfLongestSubstring("pwwkew"), 3)
        self.assertEqual(self.solution.lengthOfLongestSubstring(""), 0)


if __name__ == '__main__':
    unittest.main()
