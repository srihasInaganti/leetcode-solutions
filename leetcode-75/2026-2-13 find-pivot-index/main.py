# Approach: Maintain running left sum and right sum (initialized to total sum), updating per index to find where they match.
# Time Complexity: O(n), n = length of nums.
# Space Complexity: O(1), constant extra variables.
# Edge Cases: empty list, single-element list, no pivot exists, pivot at first or last index.
from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = 0
        r = sum(nums)
        for i in range(len(nums)):
            r -= nums[i]
            if l == r:
                return i
            l += nums[i]
        return -1