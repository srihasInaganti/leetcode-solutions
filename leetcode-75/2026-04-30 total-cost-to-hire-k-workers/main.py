import heapq
from typing import List

# Approach: Two min-heaps from both ends selecting smallest each step
# Time Complexity: O((k + candidates) log candidates)
# Space Complexity: O(candidates)
# Edge Cases: candidates > n/2, k = 1

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)

        lHeap = []
        rHeap = []

        left = 0
        right = n - 1

        for _ in range(candidates):
            if left <= right:
                heapq.heappush(lHeap, costs[left])
                left += 1

        for _ in range(candidates):
            if left <= right:
                heapq.heappush(rHeap, costs[right])
                right -= 1

        total = 0

        for _ in range(k):
            leftMin = lHeap[0] if lHeap else float('inf')
            rightMin = rHeap[0] if rHeap else float('inf')

            if leftMin <= rightMin:
                total += heapq.heappop(lHeap)

                if left <= right:
                    heapq.heappush(lHeap, costs[left])
                    left += 1
            else:
                total += heapq.heappop(rHeap)

                if left <= right:
                    heapq.heappush(rHeap, costs[right])
                    right -= 1

        return total
