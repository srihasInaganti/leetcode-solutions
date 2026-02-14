# Approach: Alternate characters from both strings until the longer one is used.
# Time Complexity: O(n + m), where n and m are the lengths of word1 and word2.
# Space Complexity: O(n + m) for the result list.
# Edge Cases: One string empty, strings of unequal length, both strings empty.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        for i in range(max(len(word1), len(word2))):
            if i < len(word1): res.append(word1[i])
            if i < len(word2): res.append(word2[i])
        return "".join(res)
