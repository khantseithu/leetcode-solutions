class MedianFinder:

    def __init__(self):
        self.nums = []
        self.length = 0

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.length += 1
        self.nums.sort()

    def findMedian(self) -> float:
        if self.length % 2 == 0:
            return (self.nums[self.length // 2] + self.nums[self.length // 2 - 1]) / 2
        else:
            return self.nums[self.length // 2]

# Time Complexity: O(nlogn)
# Space Complexity: O(n)

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

import unittest

class TestMedianFinder(unittest.TestCase):
    def setUp(self) -> None:
        self.median_finder = MedianFinder()

    def test_median_finder(self) -> None:
        self.median_finder.addNum(1)
        self.median_finder.addNum(2)
        self.assertEqual(self.median_finder.findMedian(), 1.5)
        self.median_finder.addNum(3)
        self.assertEqual(self.median_finder.findMedian(), 2)

if __name__ == '__main__':
    unittest.main()
