from typing import List

# Approach: Greedy sorting by end time to minimize overlaps
# Time Complexity: O(n log n)
# Space Complexity: O(1)
# Edge Cases: No overlaps, all overlapping

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        end = intervals[0][1]
        removals = 0

        for start, finish in intervals[1:]:
            if start < end:
                removals += 1
            else:
                end = finish

        return removals
