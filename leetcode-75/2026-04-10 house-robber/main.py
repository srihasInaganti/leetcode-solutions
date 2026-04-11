from typing import List

# Approach: Top-down DP with memoization choosing rob or skip
# Time Complexity: O(n)
# Space Complexity: O(n)
# Edge Cases: Empty list, single house, all zeros

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        
        def dp(curr):
            if curr >= len(nums):
                return 0
            if curr in memo:
                return memo[curr]

            rob = nums[curr] + dp(curr + 2)
            noRob = dp(curr + 1)
            memo[curr] = max(rob, noRob)
            return memo[curr]
        return dp(0)
