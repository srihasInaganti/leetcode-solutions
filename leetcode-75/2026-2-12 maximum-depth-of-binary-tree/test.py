from main import Solution

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def test():
    s = Solution()

    assert s.maxDepth(None) == 0

    root1 = TreeNode(1)
    assert s.maxDepth(root1) == 1

    root2 = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert s.maxDepth(root2) == 3

    root3 = TreeNode(1, TreeNode(2), TreeNode(3))
    assert s.maxDepth(root3) == 2

    print("All tests passed!")

if __name__ == "__main__":
    test()
