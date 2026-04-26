from typing import Optional

# Approach: DFS from each node accumulating path sums
# Time Complexity: O(n^2)
# Space Complexity: O(h)
# Edge Cases: Empty tree, single node equals target

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def dfs(root, curr):
            if not root:
                return 0
            
            curr += root.val
            count = 1 if curr == targetSum else 0

            count += dfs(root.left, curr)
            count += dfs(root.right, curr)

            return count

        if not root:
            return 0

        return (dfs(root, 0) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum))
