import heapq
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        heap = []

        for i in range(len(lists)):
            if lists[i] is not None:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next

        while heap:
            val, i = heapq.heappop(heap)
            current.next = ListNode(val)
            current = current.next

            if lists[i] is not None:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next

        return dummy.next

# Time complexity: O(nlogk)
# Space complexity: O(1)

import unittest

class TestMergeKLists(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_merge_k_lists(self) -> None:
        l1 = ListNode(1)
        l1.next = ListNode(4)
        l1.next.next = ListNode(5)
        l2 = ListNode(1)
        l2.next = ListNode(3)
        l2.next.next = ListNode(4)
        l3 = ListNode(2)
        l3.next = ListNode(6)
        self.assertEqual(self.solution.mergeKLists([l1, l2, l3]).val, 1)
        self.assertEqual(self.solution.mergeKLists([l1, l2, l3]).next.val, 1)
        self.assertEqual(self.solution.mergeKLists([l1, l2, l3]).next.next.val, 2)
        self.assertEqual(self.solution.mergeKLists([l1, l2, l3]).next.next.next.val, 3)
        self.assertEqual(self.solution.mergeKLists([l1, l2, l3]).next.next.next.next.val, 4)
        self.assertEqual(self.solution.mergeKLists([l1, l2, l3]).next.next.next.next.next.val, 4)
        self.assertEqual(self.solution.mergeKLists([l1, l2, l3]).next.next.next.next.next.next.val, 5)
        self.assertEqual(self.solution.mergeKLists([l1, l2, l3]).next.next.next.next.next.next.next.val, 6)


if __name__ == "__main__":
    unittest.main()
