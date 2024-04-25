class LRUCache:
    """
    Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

    Implement the LRUCache class:

    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    int get(int key) Return the value of the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
    The functions get and put must each run in O(1) average time complexity.
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.order = []


    def get(self, key: int) -> int:
        if key in self.cache:
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) == self.capacity:
            del self.cache[self.order.pop(0)]
        self.cache[key] = value
        self.order.append(key)


# Time complexity: O(1) for both get and put operations.
# Space complexity: O(N) where N is the capacity of the cache.



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

import unittest

class TestLRUCache(unittest.TestCase):
    def setUp(self) -> None:
        self.cache = LRUCache(2)

    def test_lru_cache(self) -> None:
        self.cache.put(1, 1)
        self.cache.put(2, 2)
        self.assertEqual(self.cache.get(1), 1)
        self.cache.put(3, 3)
        self.assertEqual(self.cache.get(2), -1)
        self.cache.put(4, 4)
        self.assertEqual(self.cache.get(1), -1)
        self.assertEqual(self.cache.get(3), 3)
        self.assertEqual(self.cache.get(4), 4)

if __name__ == '__main__':
    unittest.main()
