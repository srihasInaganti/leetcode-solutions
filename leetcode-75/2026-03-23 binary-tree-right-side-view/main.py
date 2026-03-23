from __future__ import annotations
from typing import Optional, List

# Approach: DFS prioritizing right subtree; first node seen at each depth is the rightmost.
# Time Complexity: O(n)
# Space Complexity: O(h)
# Edge Cases: empty tree, single node, skewed tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        
        def dfs(node, depth):
            if node is None:
                return
            
            if depth == len(out):
                out.append(node.val)
            
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        
        dfs(root, 0)
        return out
