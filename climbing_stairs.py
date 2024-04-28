class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        first = 1
        second = 2
        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third
        return second

# Time complexity: O(n)
# Space complexity: O(1)

import unittest

class TestClimbingStairs(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_climb_stairs(self) -> None:
        self.assertEqual(self.solution.climbStairs(2), 2)
        self.assertEqual(self.solution.climbStairs(3), 3)

if __name__ == '__main__':
    unittest.main()
