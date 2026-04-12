from typing import List

# Approach: Backtracking generating combinations from 1-9
# Time Complexity: O(C(n,k))
# Space Complexity: O(k)
# Edge Cases: No valid combination, k > 9, n too small

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrack(start, path, total):
            if len(path) == k and total == n:
                res.append(path[:])
                return
            
            if len(path) > k or total > n:
                return
            
            for i in range(start, 10):
                path.append(i)
                backtrack(i + 1, path, total + i)
                path.pop()

        backtrack(1, [], 0)
        return res
