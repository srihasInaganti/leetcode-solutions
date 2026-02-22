# Approach: Track cumulative altitude while iterating and keep the maximum value reached.
# Time Complexity: O(n), n = length of gain.
# Space Complexity: O(1), constant extra variables.
# Edge Cases: empty gain list, all negative gains, single element, altitude never increases above 0.
from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr = 0
        out = 0
        for i in gain:
            curr += i
            if curr > out:
                out = curr
        return out
