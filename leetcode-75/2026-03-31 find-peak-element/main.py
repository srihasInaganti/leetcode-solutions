from typing import List

# Approach: Binary search comparing mid with mid+1
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Edge Cases: Single element, strictly increasing/decreasing

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[m + 1]:
                r = m
            else:
                l = m + 1
        
        return l
