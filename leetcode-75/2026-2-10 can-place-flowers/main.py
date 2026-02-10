# Approach: Greedily scan the flowerbed and place a flower whenever the previous and next plots are empty, decrementing n.
# Time Complexity: O(n), n = length of the flowerbed.
# Space Complexity: O(1), modifies the flowerbed in place.
# Edge Cases: n = 0, single-plot flowerbed, consecutive 1s blocking placement, all-zero flowerbed.

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev = 0

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                next_val = 0 if i == len(flowerbed) - 1 else flowerbed[i + 1]
                if prev == 0 and next_val == 0:
                    flowerbed[i] = 1
                    n -= 1
                    if n <= 0:
                        return True
            prev = flowerbed[i]

        return n <= 0
