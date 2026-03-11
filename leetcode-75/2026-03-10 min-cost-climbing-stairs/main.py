from typing import List

# Approach: Use DP with two variables storing the minimum cost to reach the previous two steps.
# Time Complexity: O(n)
# Space Complexity: O(1)
# Edge Cases: cost length = 2, all costs equal, large cost values

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev = cost[0]
        prev1 = cost[1]

        for i in range(2, len(cost)):
            curr = cost[i] + min(prev, prev1)
            prev = prev1
            prev1 = curr

        return min(prev, prev1)
