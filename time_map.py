class TimeMap:
    """
    Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

    Implement the TimeMap class:

    TimeMap() Initializes the object of the data structure.
    void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
    String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        values = self.map[key]
        left = 0
        right = len(values) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid - 1
        return values[right][1] if right >= 0 else ""



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

import unittest

class TestTimeMap(unittest.TestCase):
    def setUp(self) -> None:
        self.time_map = TimeMap()

    def test_time_map(self):
        self.time_map.set("foo", "bar", 1)
        self.assertEqual(self.time_map.get("foo", 1), "bar")
        self.assertEqual(self.time_map.get("foo", 3), "bar")
        self.time_map.set("foo", "bar2", 4)
        self.assertEqual(self.time_map.get("foo", 4), "bar2")
        self.assertEqual(self.time_map.get("foo", 5), "bar2")
        self.assertEqual(self.time_map.get("foo", 0), "")
        self.assertEqual(self.time_map.get("foo", 6), "bar2")

if __name__ == '__main__':
    unittest.main()
