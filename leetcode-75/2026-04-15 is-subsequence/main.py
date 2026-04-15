# Approach: Two pointers scanning t to match s
# Time Complexity: O(n)
# Space Complexity: O(1)
# Edge Cases: Empty s, s longer than t

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for c in t:
            if i < len(s) and s[i] == c:
                i += 1
        return i == len(s)
