from typing import List

# Approach: DP tracking hold and cash states
# Time Complexity: O(n)
# Space Complexity: O(1)
# Edge Cases: Single price, no profitable transactions

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold = -prices[0]
        cash = 0

        for price in prices[1:]:
            prevCash = cash

            cash = max(cash, hold + price - fee)
            hold = max(hold, prevCash - price)

        return cash
