# Approach: Maintain an insert pointer and swap non-zero elements forward while preserving order.
# Time Complexity: O(n), n = length of nums.
# Space Complexity: O(1), in-place modification.
# Edge Cases: empty list, all zeros, no zeros, zeros at beginning or end.
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        insert = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert], nums[i] = nums[i], nums[insert]
                insert += 1
