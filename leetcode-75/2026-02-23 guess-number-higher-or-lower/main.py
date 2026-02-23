# Approach: Use binary search between 1 and n, adjusting bounds based on the guess API response.
# Time Complexity: O(log n), binary search halves the range each step.
# Space Complexity: O(1), iterative approach with constant variables.
# Edge Cases: n = 1, picked number at boundaries (1 or n), large n.
class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            m = (l + r) // 2
            g = guess(m)
            if g == 0:
                return m
            elif g < 0:
                r = m - 1
            else:
                l = m + 1
        return -1
