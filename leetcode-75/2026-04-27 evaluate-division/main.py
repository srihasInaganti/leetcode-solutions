from typing import List
from collections import defaultdict

# Approach: Build graph and DFS to compute path product
# Time Complexity: O(E + Q * E)
# Space Complexity: O(E)
# Edge Cases: Variable not present, query same variable

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        
        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1 / val
        
        def dfs(start, end, visited):
            if start not in graph:
                return -1.0
            if end in graph[start]:
                return graph[start][end]
            
            visited.add(start)
            
            for neighbor, val in graph[start].items():
                if neighbor not in visited:
                    res = dfs(neighbor, end, visited)
                    if res != -1.0:
                        return val * res
            
            return -1.0
        
        results = []
        for a, b in queries:
            if a == b and a in graph:
                results.append(1.0)
            else:
                results.append(dfs(a, b, set()))
        
        return results
