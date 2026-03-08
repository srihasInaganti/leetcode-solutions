from typing import List
import heapq

# Approach: Maintain a min-heap of size k. Push elements and pop when size exceeds k so the heap keeps the k largest elements.
# Time Complexity: O(n log k)
# Space Complexity: O(k)
# Edge Cases: k = 1, k = len(nums), duplicate values

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for i in nums:
            heapq.heappush(heap, i)

            if len(heap) > k:
                heapq.heappop(heap)
            
        return heap[0]
