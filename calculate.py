class Solution:
    def calculate(self, s: str) -> int:
        """
        Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

        Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
        """
        stack = []
        num = 0
        sign = 1
        result = 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '+':
                result += sign * num
                num = 0
                sign = 1
            elif c == '-':
                result += sign * num
                num = 0
                sign = -1
            elif c == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif c == ')':
                result += sign * num
                num = 0
                result *= stack.pop()
                result += stack.pop()
        result += sign * num
        return result

# Time complexity: O(N) where N is the length of the string s.
# Space complexity: O(N) where N is the length of the string s.

import unittest

class TestCalculate(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_calculate(self) -> None:
        self.assertEqual(self.solution.calculate("1 + 1"), 2)
        self.assertEqual(self.solution.calculate(" 2-1 + 2 "), 3)
        self.assertEqual(self.solution.calculate("(1+(4+5+2)-3)+(6+8)"), 23)

if __name__ == '__main__':
    unittest.main()
