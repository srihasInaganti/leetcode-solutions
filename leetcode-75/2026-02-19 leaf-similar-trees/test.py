from main import Solution

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def test():
    s = Solution()

    t1 = TreeNode(3,
                  TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
                  TreeNode(1, TreeNode(9), TreeNode(8)))

    t2 = TreeNode(3,
                  TreeNode(5, TreeNode(6), TreeNode(7)),
                  TreeNode(1, TreeNode(4), TreeNode(2, TreeNode(9), TreeNode(8))))

    assert s.leafSimilar(t1, t2) is True
    assert s.leafSimilar(TreeNode(1), TreeNode(1)) is True
    assert s.leafSimilar(TreeNode(1), TreeNode(2)) is False
    assert s.leafSimilar(None, None) is True

    print("All tests passed!")

if __name__ == "__main__":
    test()
