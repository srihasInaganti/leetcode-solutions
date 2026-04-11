from typing import List

# Approach: Sort potions and binary search for each spell threshold
# Time Complexity: O(n log n + m log n)
# Space Complexity: O(1)
# Edge Cases: No valid pairs, all valid pairs, large success

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        out = []
        potions.sort()

        for spell in spells:
            l, r = 0, len(potions) - 1
            first_valid = len(potions)

            target = (success + spell - 1) // spell

            while l <= r:
                m = (l + r) // 2

                if potions[m] >= target:
                    first_valid = m
                    r = m - 1
                else:
                    l = m + 1

            out.append(len(potions) - first_valid)
        return out
