# Approach: Convert both lists to sets and return elements unique to each using set difference.
# Time Complexity: O(n + m), where n and m are lengths of nums1 and nums2.
# Space Complexity: O(n + m), for storing the two sets.
# Edge Cases: empty lists, identical arrays, one array fully contained in the other, duplicates in input.
from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1, set2 = set(nums1), set(nums2)
        return [list(set1 - set2), list(set2 - set1)]