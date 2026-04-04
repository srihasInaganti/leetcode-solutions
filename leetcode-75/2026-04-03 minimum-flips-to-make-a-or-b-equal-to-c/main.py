# Approach: Bit manipulation checking each bit position
# Time Complexity: O(1)
# Space Complexity: O(1)
# Edge Cases: All zeros, large integers, already equal

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        for i in range(32):
            abit = (a >> i) & 1
            bbit = (b >> i) & 1
            cbit = (c >> i) & 1
            
            if cbit == 0:
                flips += abit + bbit
            else:
                if abit == 0 and bbit == 0:
                    flips += 1
        
        return flips
