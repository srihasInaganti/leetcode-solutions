from collections import Counter

# Approach: Compare character sets and frequency distributions
# Time Complexity: O(n log n)
# Space Complexity: O(1)
# Edge Cases: Different lengths, different char sets, same chars diff freq

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        
        if set(c1.keys()) != set(c2.keys()):
            return False
        
        return sorted(c1.values()) == sorted(c2.values())
