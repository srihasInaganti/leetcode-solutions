import math

# Approach: If str1+str2 != str2+str1 no valid divisor exists; otherwise the GCD length of the strings gives the repeating base.
# Time Complexity: O(n)
# Space Complexity: O(1)
# Edge Cases: no common divisor, identical strings, one string multiple of the other

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        
        length = math.gcd(len(str1), len(str2))
        return str1[:length]
