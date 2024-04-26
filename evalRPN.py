from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Evaluate the value of an arithmetic expression in Reverse Polish Notation.
        """
        stack = []
        for token in tokens:
            if token in "+-*/":
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        return stack[0]

# Time complexity: O(n)
# Space complexity: O(n)

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_evalRPN(self):
        self.assertEqual(self.solution.evalRPN(["2", "1", "+", "3", "*"]), 9)
        self.assertEqual(self.solution.evalRPN(["4", "13", "5", "/", "+"]), 6)
        self.assertEqual(self.solution.evalRPN(["10", "6", "9", "3", "/", "-11", "*", "/", "*", "17", "+", "5", "+"]), 22)

if __name__ == '__main__':
    unittest.main()
