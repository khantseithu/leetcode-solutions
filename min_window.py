from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Given two strings s and t of lengths m and n respectively, return the minimum window  substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
        find an algorithm that runs in O(m + n) time
        """
        if not s or not t:
            return ""
        t_count = Counter(t)
        required = len(t_count)
        # left and right pointers to represent the window
        left = 0
        right = 0
        # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency
        formed = 0
        window_counts = {}
        # ans tuple of the form (window length, left, right)
        ans = float("inf"), None, None
        while right < len(s):
            character = s[right]
            window_counts[character] = window_counts.get(character, 0) + 1
            if character in t_count and window_counts[character] == t_count[character]:
                formed += 1
            while left <= right and formed == required:
                character = s[left]
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                window_counts[character] -= 1
                if character in t_count and window_counts[character] < t_count[character]:
                    formed -= 1
                left += 1
            right += 1
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]

# Time complexity: O(m + n) where m is the length of s and n is the length of t
# Space complexity: O(m + n) where m is the length of s and n is the length of t

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_minWindow(self):
        self.assertEqual(self.solution.minWindow("ADOBECODEBANC", "ABC"), "BANC")
        self.assertEqual(self.solution.minWindow("a", "a"), "a")
        self.assertEqual(self.solution.minWindow("a", "aa"), "")
        self.assertEqual(self.solution.minWindow("a", "b"), "")
        self.assertEqual(self.solution.minWindow("a", "aa"), "")
        self.assertEqual(self.solution.minWindow("aa", "aa"), "aa")
        self.assertEqual(self.solution.minWindow("aa", "aaa"), "")
        self.assertEqual(self.solution.minWindow("aa", "a"), "a")
        self.assertEqual(self.solution.minWindow("bba", "ab"), "ba")



if __name__ == '__main__':
    unittest.main()
