class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Given a string s, return the longest palindromic substring in s.
        """
        if len(s) == 0:
            return ""
        start = 0
        end = 0
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i + 1)
            length = max(len1, len2)
            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2
        return s[start: end + 1]

    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

# Time complexity: O(n^2) where n is the length of s
# Space complexity: O(1)

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_longestPalindrome(self):
        self.assertEqual(self.solution.longestPalindrome("babad"), "aba")
        self.assertEqual(self.solution.longestPalindrome("cbbd"), "bb")
        self.assertEqual(self.solution.longestPalindrome("a"), "a")
        self.assertEqual(self.solution.longestPalindrome("bb"), "bb")
        self.assertEqual(self.solution.longestPalindrome("ccc"), "ccc")


if __name__ == '__main__':
    unittest.main()
