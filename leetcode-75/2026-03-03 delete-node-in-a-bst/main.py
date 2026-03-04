from __future__ import annotations
from typing import Optional

# Approach: Recursive BST deletion. Traverse to find node. 
# If node has 0 or 1 child, return that child.
# If node has 2 children, replace value with inorder successor (smallest in right subtree),
# then delete the successor from the right subtree.
# Time Complexity: O(h) where h = height of tree
# Space Complexity: O(h) recursion stack
# Edge Cases: empty tree, deleting root, deleting leaf, deleting node with 1 or 2 children

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            
            successor = root.right
            while successor.left is not None:
                successor = successor.left
            
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)

        return root
