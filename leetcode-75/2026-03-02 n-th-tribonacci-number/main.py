# Approach: Iterative DP keeping only last three values (rolling variables).
# Time Complexity: O(n)
# Space Complexity: O(1)
# Edge Cases: n = 0, n = 1, n = 2
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        f = 1
        s = 1
        t = 0
        c = 0
        for i in range(3, n + 1):
            c = f + s + t
            t = s
            s = f
            f = c
        return c
