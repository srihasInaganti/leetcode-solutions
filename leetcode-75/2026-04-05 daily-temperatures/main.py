from typing import List

# Approach: Monotonic decreasing stack storing indices
# Time Complexity: O(n)
# Space Complexity: O(n)
# Edge Cases: All decreasing, all same temperature

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        out = [0] * n
        stack = []
        
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                prev = stack.pop()
                out[prev] = i - prev
            stack.append(i)
        
        return out
