# Approach: Store ping timestamps in a queue-like list and remove any that fall outside the [t-3000, t] window.
# Time Complexity: O(n) worst-case due to pop(0)
# Space Complexity: O(n)
# Edge Cases: first ping, multiple pings at same timestamp, large gaps between pings

class RecentCounter:
    def __init__(self):
        self.pings = []

    def ping(self, t: int) -> int:
        self.pings.append(t)
        floor = t - 3000

        while self.pings[0] < floor:
            self.pings.pop(0)
            
        return len(self.pings)
