from collections import deque

# Approach: Two queues simulating banning process by indices
# Time Complexity: O(n)
# Space Complexity: O(n)
# Edge Cases: All same party, alternating pattern

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_queue = deque()
        d_queue = deque()
        n = len(senate)

        for i, c in enumerate(senate):
            if c == 'R':
                r_queue.append(i)
            else:
                d_queue.append(i)

        while r_queue and d_queue:
            r = r_queue.popleft()
            d = d_queue.popleft()

            if r < d:
                r_queue.append(r + n)
            else:
                d_queue.append(d + n)

        return "Radiant" if r_queue else "Dire"
