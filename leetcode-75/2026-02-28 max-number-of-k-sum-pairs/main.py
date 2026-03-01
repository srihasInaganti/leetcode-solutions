# Approach: Sort the array and use two pointers from both ends to count pairs summing to k.
# Time Complexity: O(n log n), due to sorting.
# Space Complexity: O(1), sorting in-place (ignoring Python's internal sort space).
# Edge Cases: empty list, no valid pairs, multiple duplicate values, negative numbers.
from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        l, r = 0, len(nums) - 1
        nums.sort()
        count = 0
        while l < r:
            if nums[l] + nums[r] == k:
                count += 1
                l += 1
                r -= 1
            elif nums[l] + nums[r] > k:
                r -= 1
            else:
                l += 1
        return count
