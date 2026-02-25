from main import Solution

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def test():
    s = Solution()

    t1 = TreeNode(3,
                  TreeNode(1, TreeNode(3)),
                  TreeNode(4, TreeNode(1), TreeNode(5)))
    assert s.goodNodes(t1) == 4

    assert s.goodNodes(TreeNode(1)) == 1

    t2 = TreeNode(5,
                  TreeNode(4, TreeNode(3)))
    assert s.goodNodes(t2) == 1

    print("All tests passed!")

if __name__ == "__main__":
    test()
