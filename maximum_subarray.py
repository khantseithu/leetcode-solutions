from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
        """
        max_sum = current_sum = nums[0]
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)
        return max_sum

# Time complexity: O(n)
# Space complexity: O(1)
