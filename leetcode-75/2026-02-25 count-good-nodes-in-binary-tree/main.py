# Approach: Perform DFS while carrying the maximum value seen so far and count nodes that are >= that maximum.
# Time Complexity: O(n), each node is visited once.
# Space Complexity: O(h), recursion stack where h is tree height.
# Edge Cases: single-node tree, strictly increasing path, strictly decreasing path, negative values.
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: Optional['TreeNode']) -> int:
        maxNum = root.val
        def dfs(maximum, root):
            count = 0
            if root is None:
                return 0
            if root.val >= maximum:
                count += 1
                maximum = root.val
            return count + dfs(maximum, root.left) + dfs(maximum, root.right)

        left = dfs(maxNum, root.left)
        right = dfs(maxNum, root.right)
        return 1 + left + right
