# Approach: Use XOR across all numbers since duplicates cancel out, leaving the single number.
# Time Complexity: O(n), n = length of nums.
# Space Complexity: O(1), constant extra variable.
# Edge Cases: single-element array, negative numbers, large values.
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        out = 0
        for i in nums:
            out = out ^ i
        return out
