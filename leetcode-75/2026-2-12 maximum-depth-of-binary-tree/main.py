# Approach: Use recursive DFS to compute the depth of left and right subtrees and return the larger depth plus one.
# Time Complexity: O(n), where n is the number of nodes (each node visited once).
# Space Complexity: O(h), where h is the tree height due to recursion stack.
# Edge Cases: empty tree, single-node tree, completely skewed tree.
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional['TreeNode']) -> int:
        if root is None:
            return 0
        left = 1 + self.maxDepth(root.left)
        right = 1 + self.maxDepth(root.right)
        return left if left > right else right
