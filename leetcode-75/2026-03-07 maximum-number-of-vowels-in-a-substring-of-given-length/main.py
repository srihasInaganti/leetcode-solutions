# Approach: Use a sliding window of size k and track the number of vowels. 
# Add the entering character and remove the leaving one as the window moves.
# Time Complexity: O(n)
# Space Complexity: O(1)
# Edge Cases: k = 1, k = len(s), no vowels

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        out = 0
        s = s.strip()
        for i in range(k):
            if s[i] in vowels:
                out += 1
        curr = out
        for i in range(len(s) - k):
            if s[i] in vowels:
                curr -= 1
            if s[i + k] in vowels:
                curr += 1
            out = max(curr, out)
        
        return out
