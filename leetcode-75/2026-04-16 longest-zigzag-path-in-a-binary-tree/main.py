from typing import Optional

# Approach: DFS returning left/right zigzag lengths and global max
# Time Complexity: O(n)
# Space Complexity: O(h)
# Edge Cases: Single node tree, skewed tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return (-1, -1, -1)
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            left_len = left[1] + 1
            right_len = right[0] + 1
            
            max_len = max(left_len, right_len, left[2], right[2])
            
            return (left_len, right_len, max_len)
        
        return dfs(root)[2]
