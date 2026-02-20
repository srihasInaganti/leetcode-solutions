# Approach: Use two pointers from both ends and swap characters when both are vowels, moving inward.
# Time Complexity: O(n), n = length of the string.
# Space Complexity: O(n), due to converting string to list.
# Edge Cases: empty string, no vowels, all vowels, mixed case vowels.
class Solution:
    def reverseVowels(self, s: str) -> str:
        v = set('aeiouAEIOU')
        s = list(s)
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] in v and s[r] in v:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif s[l] not in v:
                l += 1
            else:
                r -= 1
        return "".join(s)

