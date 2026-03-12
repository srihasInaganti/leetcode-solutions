import math

# Approach: Use the combinatorics formula: total moves = m+n-2 and choose (m-1) downward moves.
# Time Complexity: O(m + n)
# Space Complexity: O(1)
# Edge Cases: m = 1, n = 1, very long narrow grids

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.factorial(m + n - 2) // (math.factorial(m - 1) * math.factorial(n - 1))
