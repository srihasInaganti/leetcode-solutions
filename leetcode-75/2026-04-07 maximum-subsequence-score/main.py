from typing import List
import heapq

# Approach: Sort by nums2 desc, maintain top k nums1 with min-heap
# Time Complexity: O(n log n)
# Space Complexity: O(k)
# Edge Cases: k = 1, all equal values, large inputs

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = sorted(zip(nums2, nums1), reverse=True)
        
        heap = []
        curr_sum = 0
        max_score = 0
        
        for n2, n1 in pairs:
            heapq.heappush(heap, n1)
            curr_sum += n1
            
            if len(heap) > k:
                curr_sum -= heapq.heappop(heap)
            
            if len(heap) == k:
                max_score = max(max_score, curr_sum * n2)
        
        return max_score
