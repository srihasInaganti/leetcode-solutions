# Approach: Count frequencies using a dictionary and verify that the number of unique counts equals the number of distinct elements.
# Time Complexity: O(n), n = length of arr.
# Space Complexity: O(n), for storing frequency counts.
# Edge Cases: empty array, all elements same, all elements unique, negative numbers.
from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for i in arr:
            d[i] = d.get(i, 0) + 1
        valSet = set(d.values())
        if len(d.values()) == len(valSet):
            return True
        return False

