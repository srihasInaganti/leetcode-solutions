# Approach: Perform DFS on both trees to collect leaf values in order, then compare the resulting lists.
# Time Complexity: O(n + m), where n and m are the number of nodes in each tree.
# Space Complexity: O(n + m), for storing leaf sequences and recursion stack.
# Edge Cases: one or both trees empty, single-node trees, different structures but same leaf sequence.
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: Optional['TreeNode'], root2: Optional['TreeNode']) -> bool:
        def getLeaves(root, leaves):
            if root is None:
                return
            if root.left is None and root.right is None:
                leaves.append(root.val)
                return
            getLeaves(root.left, leaves)
            getLeaves(root.right, leaves)

        r1 = []
        getLeaves(root1, r1)
        r2 = []
        getLeaves(root2, r2)

        return r1 == r2
