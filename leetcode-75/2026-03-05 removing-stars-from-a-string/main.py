# Approach: Use a stack; push characters and pop the last one whenever a '*' is encountered.
# Time Complexity: O(n)
# Space Complexity: O(n)
# Edge Cases: no stars, stars removing entire string, consecutive stars

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in s:
            if i != "*":
                stack.append(i)
            else:
                stack.pop()
        return "".join(stack)
