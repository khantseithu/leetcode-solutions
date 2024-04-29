from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_map = [0] * 26
        for task in tasks:
            task_map[ord(task) - ord('A')] += 1
        task_map.sort()
        max_val = task_map[25] - 1
        idle_slots = max_val * n
        for i in range(24, -1, -1):
            idle_slots -= min(task_map[i], max_val)
        return len(tasks) + max(idle_slots, 0)

# Time complexity: O(n)
# Space complexity: O(1)

import unittest

class TestLeastInterval(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_least_interval(self) -> None:
        self.assertEqual(self.solution.leastInterval(["A","A","A","B","B","B"], 2), 8)
        self.assertEqual(self.solution.leastInterval(["A","A","A","B","B","B"], 0), 6)
        self.assertEqual(self.solution.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2), 16)

if __name__ == '__main__':
    unittest.main()
