# Approach: Recursively traverse left or right based on BST property until the value is found or a null node is reached.
# Time Complexity: O(h), where h is the height of the tree.
# Space Complexity: O(h), due to recursion stack.
# Edge Cases: empty tree, value not present, value at root, single-node tree.
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root: Optional['TreeNode'], val: int) -> Optional['TreeNode']:
        if root is None:
            return None
        if root.val == val:
            return root
        if val < root.val:
            return self.searchBST(root.left, val)
        return self.searchBST(root.right, val)
