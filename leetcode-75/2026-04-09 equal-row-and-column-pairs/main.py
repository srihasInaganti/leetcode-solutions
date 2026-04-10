from typing import List
from collections import defaultdict

# Approach: Count rows with hashmap and match with columns
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
# Edge Cases: All same rows, no matches, single element grid

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        out = 0
        rows = defaultdict(int)

        for row in grid:
            rows[tuple(row)] += 1 

        for col in zip(*grid):
            if col in rows:
                out += rows[col]
        return out
