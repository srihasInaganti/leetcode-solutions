from typing import List
from collections import defaultdict

# Approach: DFS with directed edges tracking reversals needed
# Time Complexity: O(n)
# Space Complexity: O(n)
# Edge Cases: Single node, all edges already correct

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for u, v in connections:
            graph[u].append((v, 1))
            graph[v].append((u, 0))
        
        visited = set()
        
        def dfs(node):
            visited.add(node)
            changes = 0
            
            for n, cost in graph[node]:
                if n not in visited:
                    changes += cost + dfs(n)
            
            return changes
        
        return dfs(0)
