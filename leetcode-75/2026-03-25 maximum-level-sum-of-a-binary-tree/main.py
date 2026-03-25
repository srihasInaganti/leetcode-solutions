from typing import Optional

# Approach: Level order traversal (BFS) tracking sum per level
# Time Complexity: O(n)
# Space Complexity: O(n)
# Edge Cases: Single node, negative values, empty tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = [root]
        maxSum = float('-inf')
        best_level = 1
        lvl = 1
        
        while queue:
            levelSize = len(queue)
            currSum = 0
            
            for _ in range(levelSize):
                node = queue.pop(0)
                currSum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if currSum > maxSum:
                maxSum = currSum
                best_level = lvl
            
            lvl += 1
        
        return best_level
