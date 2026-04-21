from typing import List

# Approach: Two pointers to compress in-place with counts
# Time Complexity: O(n)
# Space Complexity: O(1)
# Edge Cases: Single char, all unique chars

class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        w = 0

        while i < len(chars):
            j = i
            while j < len(chars) and chars[j] == chars[i]:
                j += 1

            chars[w] = chars[i]
            w += 1

            cnt = j - i
            if cnt > 1:
                for c in str(cnt):
                    chars[w] = c
                    w += 1

            i = j

        return w
