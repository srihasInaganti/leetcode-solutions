# Approach: Build prefix products in one pass, then multiply by suffix products in a reverse pass without using division.
# Time Complexity: O(n), n = length of nums.
# Space Complexity: O(1) extra space (excluding output array).
# Edge Cases: contains zero(s), single-element array, negative numbers, all ones.
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        run = 1
        for i in nums:
            out.append(run)
            run *= i
        run = 1
        for i in range(len(nums) - 1, -1, -1):
            out[i] *= run
            run *= nums[i]
        return out

