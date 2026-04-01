from typing import List

# Approach: Binary search on eating speed with feasibility check
# Time Complexity: O(n log m)
# Space Complexity: O(1)
# Edge Cases: Single pile, large h, all equal piles

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l < r:
            k = (l + r) // 2
            time = 0
            for p in piles:
                time += (p + k - 1) // k
            if time > h:
                l = k + 1
            elif time <= h:
                r = k
        return l
