from typing import List
from collections import deque

# Approach: BFS from entrance to find nearest boundary exit
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
# Edge Cases: No exit reachable, entrance on boundary

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        queue = deque([(entrance[0], entrance[1], 0)])
        visited = set([(entrance[0], entrance[1])])

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while queue:
            r, c, dist = queue.popleft()

            if (r, c) != (entrance[0], entrance[1]) and (
                r == 0 or r == rows - 1 or c == 0 or c == cols - 1
            ):
                return dist

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if maze[nr][nc] == '.' and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc, dist + 1))

        return -1
