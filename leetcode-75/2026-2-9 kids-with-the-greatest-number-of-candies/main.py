# Approach: Find the max candy count, then check if each kid with extraCandies reaches it.
# Time Complexity: O(n), n = number of kids.
# Space Complexity: O(n) for the output list.
# Edge Cases: empty list, all kids have same candies, extraCandies = 0, single kid.
from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        curr = 0
        for i in candies:
            curr = max(i, curr)
        out = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= curr:
                out.append(True)
            else:
                out.append(False)
        return out