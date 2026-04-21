from typing import List

# Approach: Sliding window allowing at most one zero
# Time Complexity: O(n)
# Space Complexity: O(1)
# Edge Cases: All ones, single element

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=z=0
        r=0
        n=len(nums)
        res=0
        for r in range(n):
            if nums[r]==0: z+=1
            while z>1:
                if nums[l]==0: z-=1
                l+=1
            res=max(res,r-l+1)
        return res-1
