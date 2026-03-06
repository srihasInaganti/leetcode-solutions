
# Approach: Use a sliding window of size k, update the window sum by removing the left element and adding the next element.
# Time Complexity: O(n)
# Space Complexity: O(1)
# Edge Cases: k = 1, k = len(nums), all negative numbers

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = sum(nums[:k])
        out = curr

        for i in range(len(nums) - k):
            curr = curr - nums[i] + nums[i + k]
            out = max(curr, out)
        return out / k
