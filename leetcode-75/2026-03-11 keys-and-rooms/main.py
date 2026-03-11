from typing import List

# Approach: Use DFS starting from room 0, visiting rooms through keys and tracking visited rooms in a set.
# Time Complexity: O(n + k)
# Space Complexity: O(n)
# Edge Cases: single room, unreachable rooms, cyclic keys

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def dfs(room):
            if room in visited:
                return
            visited.add(room)

            for key in rooms[room]:
                dfs(key)

        dfs(0)
        return len(visited) == len(rooms)
