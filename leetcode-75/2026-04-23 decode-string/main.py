# Approach: Stack to handle nested patterns with counts
# Time Complexity: O(n)
# Space Complexity: O(n)
# Edge Cases: Nested patterns, multi-digit counts

class Solution:
    def decodeString(self, s: str) -> str:
        out = ""
        st = []
        n = 0

        for c in s:
            if c.isdigit():
                n = n * 10 + int(c)
            
            elif c == '[':
                st.append((out, n))
                out = ""
                n = 0
            
            elif c == ']':
                pre, num = st.pop()
                out = pre + out * num

            else:
                out += c
            
        return out
