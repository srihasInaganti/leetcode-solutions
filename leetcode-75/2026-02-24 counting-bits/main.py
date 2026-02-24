# Approach: For each number from 0 to n, convert to binary and count the number of '1' bits.
# Time Complexity: O(n log n), since each binary conversion takes O(log n).
# Space Complexity: O(n), for storing the output list.
# Edge Cases: n = 0, n = 1, large n, sequential powers of two.
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        out = []
        for i in range(0, n + 1):
            binary = bin(i)[2:].count("1")
            out.append(binary)
        return out
