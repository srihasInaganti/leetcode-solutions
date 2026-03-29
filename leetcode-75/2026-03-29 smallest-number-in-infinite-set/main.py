import heapq

# Approach: Min-heap for added-back numbers with pointer for next smallest
# Time Complexity: O(log n) per operation
# Space Complexity: O(n)
# Edge Cases: Re-adding existing numbers, sequential pops

class SmallestInfiniteSet:

    def __init__(self):
        self.curr = 1
        self.heap = []
        self.set = set()

    def popSmallest(self) -> int:
        if len(self.heap) > 0:
            val = heapq.heappop(self.heap)
            self.set.remove(val)
            return val
        
        val = self.curr
        self.curr += 1
        return val

    def addBack(self, num: int) -> None:
        if num < self.curr and num not in self.set:
            heapq.heappush(self.heap, num)
            self.set.add(num)
