# Approach: Use two pointers at both ends, compute area each step, and move the pointer at the shorter height inward.
# Time Complexity: O(n), each pointer moves at most n times.
# Space Complexity: O(1), constant extra space.
# Edge Cases: minimum size array (2 elements), all equal heights, strictly increasing/decreasing heights.
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0
        while l < r:
            vol = min(height[l], height[r]) * (r - l)
            if vol > max_area:
                max_area = vol
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area

