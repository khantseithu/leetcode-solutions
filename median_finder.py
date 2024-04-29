import heapq

class MedianFinder:

    def __init__(self):
        self.heaps = [], []

    def addNum(self, num: int) -> None:
        small, large = self.heaps
        heapq.heappush(small, -heapq.heappushpop(large, num))
        if len(large) < len(small):
            heapq.heappush(large, -heapq.heappop(small))

    def findMedian(self) -> float:
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0

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
