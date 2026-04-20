from typing import List

# Approach: Track two smallest values and check for third greater
# Time Complexity: O(n)
# Space Complexity: O(1)
# Edge Cases: Length < 3, strictly decreasing array

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i = float('inf')
        j = float('inf')
        for n in nums:
            if n <= i:
                i = n
            elif n <= j:
                j = n
            else:
                return True

        return False
