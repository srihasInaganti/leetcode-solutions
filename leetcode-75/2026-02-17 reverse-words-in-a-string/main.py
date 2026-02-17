# Approach: Split the string into words, then pop from the end to rebuild the sentence in reverse order.
# Time Complexity: O(n), n = length of the string.
# Space Complexity: O(n), for storing split words and output string.
# Edge Cases: leading/trailing spaces, multiple spaces between words, single word, empty string.
class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        out = ""
        while len(arr) > 0:
            out += arr.pop()
            if len(arr) >= 1:
                out += " "
        return out
