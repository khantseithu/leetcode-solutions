class Solution:
    def myAtoi(self, s: str) -> int:
        """
        Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

        The algorithm for myAtoi(string s) is as follows:

        Read in and ignore any leading whitespace.
        Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
        Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
        Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
        If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
        Return the integer as the final result.
        Note:

        Only the space character ' ' is considered a whitespace character.
        Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
        """
        s = s.strip()
        if not s:
            return 0
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        res = 0
        for i in range(len(s)):
            if not s[i].isdigit():
                break
            res = res * 10 + int(s[i])
        res = sign * res
        return max(min(res, 2**31 - 1), -2**31)


# Time complexity: O(N)
# Space complexity: O(1)

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()


    def test_myAtoi(self):
        solution = Solution()
        self.assertEqual(solution.myAtoi("42"), 42)
        self.assertEqual(solution.myAtoi("   -42"), -42)
        self.assertEqual(solution.myAtoi("4193 with words"), 4193)
        self.assertEqual(solution.myAtoi("words and 987"), 0)
        self.assertEqual(solution.myAtoi("-91283472332"), -2147483648)

if __name__ == '__main__':
    unittest.main()
